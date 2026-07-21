import os, re

def check_subject(base_path, name):
    critical = []
    all_issues = []
    
    for folder in sorted(os.listdir(base_path)):
        fp = os.path.join(base_path, folder, 'index.html')
        if not os.path.isfile(fp): continue
        
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
        js = '\n'.join(scripts)
        lines_count = content.count('\n') + 1
        
        issues = []
        
        # 1. Timing risk
        has_getBBox = 'getBoundingClientRect' in js
        has_direct = bool(re.search(r'^(draw|init|fit|animate|loop|render)\s*\(', js, re.MULTILINE))
        has_raf_double = 'requestAnimationFrame(function(){requestAnimationFrame' in js
        if has_getBBox and has_direct and not has_raf_double:
            issues.append('TIMING_RISK')
        
        # 2. No animation loop
        has_raf = 'requestAnimationFrame' in js
        has_interval = 'setInterval' in js
        has_click_loop = 'addEventListener' in js and ('click' in js or 'input' in js)
        if not has_raf and not has_interval and not has_click_loop:
            issues.append('NO_ANIMATION_LOOP')
        
        # 3. Very small files
        if lines_count < 50:
            issues.append(f'TOO_SMALL({lines_count}L)')
        
        # 4. Canvas missing
        if '<canvas' not in content:
            issues.append('NO_CANVAS')
        
        # 5. getContext missing
        if 'getContext' not in js:
            issues.append('NO_CONTEXT')
        
        # 6. Bracket imbalance
        js_clean = re.sub(r'"[^"]*"', '""', js)
        js_clean = re.sub(r"'[^']*'", "''", js_clean)
        js_clean = re.sub(r'`[^`]*`', '``', js_clean, flags=re.DOTALL)
        js_clean = re.sub(r'//.*', '', js_clean)
        js_clean = re.sub(r'/\*.*?\*/', '', js_clean, flags=re.DOTALL)
        p_diff = js_clean.count('(') - js_clean.count(')')
        b_diff = js_clean.count('{') - js_clean.count('}')
        if abs(p_diff) > 3: issues.append(f'PAREN({p_diff:+d})')
        if abs(b_diff) > 3: issues.append(f'BRACE({b_diff:+d})')
        
        if issues:
            all_issues.append((folder, issues, lines_count))
            if any(k in i for i in issues for k in ['TIMING_RISK','NO_ANIMATION_LOOP','NO_CANVAS','NO_CONTEXT','PAREN','BRACE']):
                critical.append(folder)
    
    print(f"\n{'='*70}")
    print(f"{name} ANIMATION CHECK")
    print(f"{'='*70}")
    
    print(f"\n--- CRITICAL ({len(critical)}) ---")
    for f in critical:
        for folder, issues, lc in all_issues:
            if folder == f:
                print(f"  {f} ({lc}L): {', '.join(issues)}")
                break
    
    other = [(f,i,l) for f,i,l in all_issues if f not in critical]
    if other:
        print(f"\n--- OTHER ISSUES ({len(other)}) ---")
        for folder, issues, lc in other:
            print(f"  {folder} ({lc}L): {', '.join(issues)}")
    
    total = len([f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f, 'index.html'))])
    ok = total - len(all_issues)
    print(f"\nTotal: {total} | Critical: {len(critical)} | Other: {len(other)} | OK: {ok}")
    
    return critical

it_critical = check_subject(r'd:\K12-Teaching-Animation\信息技术', 'IT (信息技术)')
bio_critical = check_subject(r'd:\K12-Teaching-Animation\生物', 'BIOLOGY (生物)')

print(f"\n\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"IT Critical: {len(it_critical)}")
for f in it_critical: print(f"  {f}")
print(f"\nBio Critical: {len(bio_critical)}")
for f in bio_critical: print(f"  {f}")
