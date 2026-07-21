import os, re

base = r'd:\K12-Teaching-Animation\物理'

for folder in sorted(os.listdir(base)):
    fp = os.path.join(base, folder, 'index.html')
    if not os.path.isfile(fp): continue
    
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    js = '\n'.join(scripts)
    lines = content.count('\n') + 1
    
    issues = []
    
    # 1. Paren/brace balance (real check - ignore strings)
    # Remove string contents first for accurate counting
    js_clean = re.sub(r'"[^"]*"', '""', js)
    js_clean = re.sub(r"'[^']*'", "''", js_clean)
    js_clean = re.sub(r'`[^`]*`', '``', js_clean, flags=re.DOTALL)
    # Remove comments
    js_clean = re.sub(r'//.*', '', js_clean)
    js_clean = re.sub(r'/\*.*?\*/', '', js_clean, flags=re.DOTALL)
    
    p_diff = js_clean.count('(') - js_clean.count(')')
    b_diff = js_clean.count('{') - js_clean.count('}')
    k_diff = js_clean.count('[') - js_clean.count(']')
    
    if abs(p_diff) > 3: issues.append(f'PAREN({p_diff:+d})')
    if abs(b_diff) > 3: issues.append(f'BRACE({b_diff:+d})')
    if abs(k_diff) > 3: issues.append(f'BRACKET({k_diff:+d})')
    
    # 2. Check for function calls that are never defined
    # Get all called functions (name followed by open paren)
    called = set(re.findall(r'\b([a-z][a-zA-Z0-9_]*)\s*\(', js_clean))
    # Get defined functions
    defined = set(re.findall(r'function\s+([a-zA-Z_]\w*)', js_clean))
    defined.update(re.findall(r'(?:var|let|const)\s+([a-zA-Z_]\w*)\s*=\s*(?:function|\()', js_clean))
    defined.update(re.findall(r'\.([a-zA-Z_]\w*)\s*=\s*function', js_clean))
    # Known built-ins
    builtins = {'getElementById','querySelector','querySelectorAll','addEventListener','getContext',
        'fillRect','strokeRect','clearRect','beginPath','arc','moveTo','lineTo','closePath','fill','stroke',
        'fillText','strokeText','measureText','save','restore','translate','rotate','scale','setTransform',
        'createLinearGradient','createRadialGradient','addColorStop','drawImage','clip','rect','ellipse',
        'requestAnimationFrame','cancelAnimationFrame','setInterval','clearInterval','setTimeout','clearTimeout',
        'push','pop','shift','splice','slice','concat','join','reverse','sort','indexOf','forEach','map',
        'filter','reduce','some','every','find','includes','toFixed','toString','replace','match','test',
        'search','split','substring','charAt','preventDefault','log','warn','error','sin','cos','tan',
        'sqrt','abs','floor','ceil','round','random','min','max','pow','atan2','keys','values','entries',
        'assign','getBoundingClientRect','createImageData','putImageData','getImageData','setLineDash',
        'bezierCurveTo','quadraticCurveTo','createPattern','isPointInPath','readPixels','then','catch',
        'parseInt','parseFloat','isNaN','encodeURIComponent','decodeURIComponent','btoa','atob',
        'stopPropagation','dispatchEvent','removeEventListener','focus','blur','click','submit','reset',
        'add','remove','toggle','contains','getComputedStyle','matchMedia','scrollTo','scrollIntoView',
        'createElement','appendChild','insertBefore','removeChild','replaceChild','cloneNode',
        'setInterval','clearInterval','setTimeout','clearTimeout','alert','confirm','prompt',
        'stopImmediatePropagation','preventDefault'}
    
    user_called = called - defined - builtins
    # Filter out common false positives
    user_called = {f for f in user_called if f not in {'if','for','while','switch','catch','return','new','typeof','void','delete','throw','case'}}
    
    if user_called:
        issues.append(f'UNDEF_FUNC({",".join(list(user_called)[:3])})')
    
    # 3. Check buttons in HTML not referenced in JS
    html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
    btn_ids = {i for i in html_ids if any(k in i.lower() for k in ['btn','button','play','pause','reset','start','stop','toggle','switch'])}
    for bid in btn_ids:
        if bid not in js:
            issues.append(f'BTN_UNREF(#{bid})')
    
    # 4. Check if animation actually starts (init/draw/loop called at top level)
    # Look for function calls outside of function definitions
    has_init_call = bool(re.search(r'^(?:init|draw|animate|start|setup|main|loop|render)\s*\(', js, re.MULTILINE))
    has_raf_call = 'requestAnimationFrame' in js
    has_interval_call = 'setInterval' in js
    
    if not has_init_call and not has_raf_call and not has_interval_call:
        issues.append('NO_ENTRY_POINT')
    
    # 5. Check for very short files
    if lines < 50:
        issues.append(f'SHORT({lines}L)')
    
    # 6. Check canvas element exists
    if '<canvas' not in content:
        issues.append('NO_CANVAS_ELEM')
    
    if issues:
        print(f"[ISSUE] {folder}")
        for iss in issues:
            print(f"    -> {iss}")
    else:
        print(f"[OK] {folder} ({lines}L)")
