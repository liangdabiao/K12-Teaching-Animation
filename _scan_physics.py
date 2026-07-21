import os, re, glob

base = r'd:\K12-Teaching-Animation\物理'
results = []

for folder in sorted(os.listdir(base)):
    fp = os.path.join(base, folder, 'index.html')
    if not os.path.isfile(fp):
        results.append((folder, 'MISSING', 'index.html not found'))
        continue
    
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.count('\n') + 1
    issues = []
    
    # Extract JS from <script> tags
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    js = '\n'.join(scripts)
    
    # 1. Check canvas setup
    if 'getContext' not in js:
        issues.append('NO_CANVAS: no getContext found')
    if "getElementById('cv')" not in js and 'getElementById("cv")' not in js:
        if 'canvas' not in content.lower() or 'getContext' not in js:
            issues.append('NO_CANVAS_ID: canvas element may not exist')
    
    # 2. Check animation loop
    has_raf = 'requestAnimationFrame' in js
    has_interval = 'setInterval' in js
    has_timer = 'setTimeout' in js
    has_event_loop = 'addEventListener' in js and ('mousemove' in js or 'click' in js or 'input' in js)
    if not has_raf and not has_interval and not has_timer:
        if not has_event_loop:
            issues.append('NO_ANIMATION: no RAF/setInterval/timeout/event loop')
    
    # 3. Check for drawing operations
    draw_ops = ['fillRect', 'strokeRect', 'fillText', 'strokeText', 'beginPath', 'arc(', 'moveTo', 'lineTo', 'fill()', 'stroke()', 'drawImage', 'clearRect']
    found_draw = [op for op in draw_ops if op in js]
    if len(found_draw) < 3:
        issues.append(f'MINIMAL_DRAWING: only {len(found_draw)} draw operations found')
    
    # 4. Check bracket balance (rough)
    open_paren = js.count('(') - js.count(')')
    open_brace = js.count('{') - js.count('}')
    open_bracket = js.count('[') - js.count(']')
    if abs(open_paren) > 2:
        issues.append(f'PAREN_IMBALANCE: ( vs ) diff = {open_paren}')
    if abs(open_brace) > 2:
        issues.append(f'BRACE_IMBALANCE: {{ vs }} diff = {open_brace}')
    if abs(open_bracket) > 2:
        issues.append(f'BRACKET_IMBALANCE: [ vs ] diff = {open_bracket}')
    
    # 5. Check for common errors
    # Unclosed string literals
    if re.search(r"[^\\]'[^'\n]*$", js, re.MULTILINE):
        issues.append('UNCLOSED_STRING: possible unclosed string literal')
    
    # 6. Check control buttons exist in HTML but not connected in JS
    btn_ids = re.findall(r'id=["\']([^"\']*(?:btn|Btn|button|Button)[^"\']*)["\']', content)
    for bid in btn_ids:
        if bid not in js:
            issues.append(f'BTN_DISCONNECTED: #{bid} in HTML but not referenced in JS')
    
    # 7. Check for undefined function calls
    # Find function calls
    func_calls = set(re.findall(r'\b([a-zA-Z_]\w*)\s*\(', js))
    # Find function definitions
    func_defs = set(re.findall(r'function\s+([a-zA-Z_]\w*)', js))
    # Also check for var/let/const func = function
    func_defs.update(re.findall(r'(?:var|let|const)\s+([a-zA-Z_]\w*)\s*=\s*function', js))
    # Also check for obj.method = function
    func_defs.update(re.findall(r'\.([a-zA-Z_]\w*)\s*=\s*function', js))
    # Built-in and DOM methods to exclude
    builtins = {'getElementById','querySelector','querySelectorAll','addEventListener','removeEventListener',
                'getContext','fillRect','strokeRect','clearRect','beginPath','arc','moveTo','lineTo','closePath',
                'fill','stroke','fillText','strokeText','measureText','save','restore','translate','rotate',
                'scale','setTransform','createLinearGradient','createRadialGradient','addColorStop',
                'drawImage','createPattern','clip','isPointInPath','getImageData','putImageData',
                'requestAnimationFrame','cancelAnimationFrame','setInterval','clearInterval','setTimeout','clearTimeout',
                'Math','parseInt','parseFloat','isNaN','isFinite','encodeURIComponent','decodeURIComponent',
                'push','pop','shift','unshift','splice','slice','concat','join','reverse','sort','indexOf',
                'forEach','map','filter','reduce','some','every','find','includes','indexOf',
                'toFixed','toString','valueOf','hasOwnProperty','keys','values','entries','assign',
                'getBoundingClientRect','preventDefault','stopPropagation',
                'log','warn','error','alert','confirm','prompt',
                'textContent','classList','style','checked','value','target',
                'sin','cos','tan','sqrt','abs','floor','ceil','round','random','min','max','PI','pow','atan2',
                'replace','match','test','search','split','substring','charAt','charCodeAt',
                'addEventListener','removeEventListener','dispatchEvent',
                'width','height','clientWidth','clientHeight','getBoundingClientRect',
                'close','fill','stroke','moveTo','lineTo','arc','rect','ellipse','bezierCurveTo','quadraticCurveTo',
                'setLineDash','getLineDash','createImageData','readPixels',
                'then','catch','finally','Promise','fetch','XMLHttpRequest',
                'Date','Array','Object','String','Number','Boolean','RegExp','Error','Map','Set','WeakMap','WeakSet',
                'JSON','console','window','document','navigator','location','history','screen',
                'setTimeout','clearTimeout','setInterval','clearInterval','requestAnimationFrame',
                'btoa','atob','encodeURIComponent','decodeURIComponent','encodeURI','decodeURI',
                'isNaN','isFinite','parseFloat','parseInt','Infinity','NaN','undefined',
                }
    
    # 8. Check for very small files (likely broken)
    if lines < 30:
        issues.append(f'TOO_SMALL: only {lines} lines, likely incomplete')
    
    # 9. Check if JS has obvious syntax errors
    # Check for common patterns like ,, ;;  etc
    if re.search(r'[;,]\s*[;,]\s*[;,]', js):
        issues.append('SYNTAX_SUSPICIOUS: multiple consecutive semicolons/commas')
    
    # 10. Check for template literal issues
    if '${' not in js and '`' in js:
        # Backtick without template literal might be an issue
        pass
    
    severity = 'OK' if not issues else ('SEVERE' if any(x.startswith('NO_CANVAS') or x.startswith('NO_ANIMATION') or x.startswith('BRACE_IMBALANCE') or x.startswith('PAREN_IMBALANCE') or x.startswith('TOO_SMALL') for x in issues) else 'MODERATE')
    
    if issues:
        results.append((folder, severity, '; '.join(issues)))
    else:
        results.append((folder, 'OK', f'{lines} lines'))

# Print summary
print(f"{'='*80}")
print(f"PHYSICS ANIMATION FUNCTIONAL CHECK")
print(f"{'='*80}")

severe = [(f,s,i) for f,s,i in results if s == 'SEVERE']
moderate = [(f,s,i) for f,s,i in results if s == 'MODERATE']
ok = [(f,s,i) for f,s,i in results if s == 'OK']

print(f"\n--- SEVERE ({len(severe)}) ---")
for f,s,i in severe:
    print(f"  {f}: {i}")

print(f"\n--- MODERATE ({len(moderate)}) ---")
for f,s,i in moderate:
    print(f"  {f}: {i}")

print(f"\n--- OK ({len(ok)}) ---")
for f,s,i in ok:
    print(f"  {f}: {i}")

print(f"\nTotal: {len(results)} | Severe: {len(severe)} | Moderate: {len(moderate)} | OK: {len(ok)}")
