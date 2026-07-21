import os, re

base = r'd:\K12-Teaching-Animation\物理'
critical = []

for folder in sorted(os.listdir(base)):
    fp = os.path.join(base, folder, 'index.html')
    if not os.path.isfile(fp): continue
    
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    js = '\n'.join(scripts)
    
    # Check for getBoundingClientRect usage (layout-dependent)
    has_getBBox = 'getBoundingClientRect' in js
    
    # Check for direct init/draw calls
    has_direct = bool(re.search(r'^(draw|init|fit|animate)\s*\(', js, re.MULTILINE))
    
    # Check if already using proper timing
    has_raf_double = 'requestAnimationFrame(function(){requestAnimationFrame' in js
    has_load_check = "document.readyState" in js
    
    if has_getBBox and has_direct and not has_raf_double:
        critical.append(folder)

print(f"Critical files (use getBoundingClientRect + direct init, no RAF double-buffer):")
print(f"{'='*60}")
for f in critical:
    print(f"  {f}")
print(f"\nTotal: {len(critical)} files need fix")
