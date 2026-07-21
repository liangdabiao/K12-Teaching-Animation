#!/usr/bin/env python3
import os,re
BASE=r'd:\K12-Teaching-Animation'
H='const cv=document.getElementById(\'cv\');const ctx=cv.getContext(\'2d\');\nconst statusEl=document.getElementById(\'status\');\nfunction fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(360,Math.min(980,r.width-8));cv.height=Math.max(360,Math.min(560,r.height-8));}\nwindow.addEventListener(\'resize\',()=>{fit();draw();});fit();\n'
T='\nlet playing=false,lastT=0,speed=1,t=0;\nconst playBtn=document.getElementById(\'playBtn\'),resetBtn=document.getElementById(\'resetBtn\');\nconst stepBackBtn=document.getElementById(\'stepBackBtn\'),stepFwdBtn=document.getElementById(\'stepFwdBtn\');\nconst speedEl=document.getElementById(\'speed\');\nfunction loop(ts){if(!lastT)lastT=ts;const dt=(ts-lastT)/1000;lastT=ts;if(playing){t+=dt*speed;if(window.sceneUpdate)sceneUpdate(dt*speed);}draw();requestAnimationFrame(loop);}\nrequestAnimationFrame(loop);\nplayBtn.onclick=()=>{playing=!playing;playBtn.textContent=playing?\'⏸ 暂停\':\'▶ 播放\';};\nresetBtn.onclick=()=>{if(window.sceneReset)sceneReset();t=0;playing=false;playBtn.textContent=\'▶ 播放\';draw();};\nstepFwdBtn.onclick=()=>{if(window.sceneStep)sceneStep(1);draw();};\nstepBackBtn.onclick=()=>{if(window.sceneStep)sceneStep(-1);draw();};\nspeedEl.oninput=()=>{speed=parseFloat(speedEl.value);};\nfunction draw(){if(window.sceneDraw)sceneDraw();}\nif(window.sceneInit)sceneInit();\ndraw();\n'

def rep(fp,key,code):
    dn=os.path.basename(os.path.dirname(fp))
    if key not in dn:return False
    with open(fp,'r',encoding='utf-8') as f:c=f.read()
    m=re.search(r'(<script>\n)(.*?)(\n</script>)',c,re.DOTALL)
    if not m:return False
    ns=H+code+T
    c=c[:m.start(2)]+ns+c[m.end(2):]
    with open(fp,'w',encoding='utf-8') as f:f.write(c)
    return True

def walk(anims):
    n=0
    for r,d,fs in os.walk(BASE):
        if '.workbuddy' in r:continue
        for fn in fs:
            if fn=='index.html':
                fp=os.path.join(r,fn)
                with open(fp,'r',encoding='utf-8') as f:lc=sum(1 for _ in f)
                if lc>=200:continue
                for k,v in anims.items():
                    if rep(fp,k,v):print(f'  OK: {os.path.basename(os.path.dirname(fp))}');n+=1;break
    return n
