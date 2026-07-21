import os, re

base = r'd:\K12-Teaching-Animation\物理'
issues = []

for folder in sorted(os.listdir(base)):
    fp = os.path.join(base, folder, 'index.html')
    if not os.path.isfile(fp): continue
    
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    js = '\n'.join(scripts)
    
    # Check for direct calls to init/draw/fit/loop at the end of script (not inside functions)
    # Look for patterns like: draw(); or init(); or fit(); at the end
    lines = js.split('\n')
    
    has_direct_call = False
    has_raf_init = False
    has_load_init = False
    has_domcontent_init = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Check for direct function calls at top level (not inside function definitions)
        if re.match(r'^(draw|init|fit|loop|animate|render)\s*\(', stripped):
            # Check if this is inside a function definition
            # Simple heuristic: check if we're inside a function by counting braces
            before = '\n'.join(lines[:i])
            open_braces = before.count('{') - before.count('}')
            if open_braces == 0:  # Top-level call
                has_direct_call = True
                issues.append((folder, 'DIRECT_CALL', stripped, i+1))
        
        if 'requestAnimationFrame' in stripped and ('init' in stripped or 'draw' in stripped):
            has_raf_init = True
        if "addEventListener('load'" in stripped or 'addEventListener("load"' in stripped:
            has_load_init = True
        if "addEventListener('DOMContentLoaded'" in stripped:
            has_domcontent_init = True
    
    # Check for fit() called directly
    if re.search(r'^fit\(\)', js, re.MULTILINE):
        has_direct_call = True
        issues.append((folder, 'FIT_DIRECT', 'fit() called directly', 0))

print(f"Files with potential initialization timing issues:")
print(f"{'='*60}")
for folder, issue_type, detail, line_num in issues:
    print(f"  {folder}")
    print(f"    -> {issue_type}: {detail} (line {line_num})")

print(f"\nTotal: {len(issues)} files")
