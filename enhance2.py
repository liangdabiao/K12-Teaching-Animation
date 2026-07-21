#!/usr/bin/env python3
"""增强剩余简陋模板文件 - 紧凑版"""
import os, re
BASE = r'd:\K12-Teaching-Animation'

# 通用增强模板 - 每个文件用不同的sceneDraw
COMMON_HEAD = '''const cv=document.getElementById('cv');const ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(360,Math.min(980,r.width-8));cv.height=Math.max(360,Math.min(560,r.height-8));}
window.addEventListener('resize',()=>{fit();draw();});fit();
'''
COMMON_TAIL = '''
let playing=false,lastT=0,speed=1,t=0;
const playBtn=document.getElementById('playBtn'),resetBtn=document.getElementById('resetBtn');
const stepBackBtn=document.getElementById('stepBackBtn'),stepFwdBtn=document.getElementById('stepFwdBtn');
const speedEl=document.getElementById('speed');
function loop(ts){if(!lastT)lastT=ts;const dt=(ts-lastT)/1000;lastT=ts;if(playing){t+=dt*speed;if(window.sceneUpdate)sceneUpdate(dt*speed);}draw();requestAnimationFrame(loop);}
requestAnimationFrame(loop);
playBtn.onclick=()=>{playing=!playing;playBtn.textContent=playing?'⏸ 暂停':'▶ 播放';};
resetBtn.onclick=()=>{if(window.sceneReset)sceneReset();t=0;playing=false;playBtn.textContent='▶ 播放';draw();};
stepFwdBtn.onclick=()=>{if(window.sceneStep)sceneStep(1);draw();};
stepBackBtn.onclick=()=>{if(window.sceneStep)sceneStep(-1);draw();};
speedEl.oninput=()=>{speed=parseFloat(speedEl.value);};
function draw(){if(window.sceneDraw)sceneDraw();}
if(window.sceneInit)sceneInit();
draw();
'''

# key: 目录名关键字, value: (initCode, updateCode, drawCode, statusText)
ANIMS = {
    '实验室制取二氧化碳': (
        'const R={t:0,bubbles:[]};',
        'R.t+=dt;for(let i=0;i<2;i++)R.bubbles.push({x:cv.width*0.4+(Math.random()-0.5)*40,y:cv.height*0.6,vy:-40-Math.random()*30,vx:(Math.random()-0.5)*10,life:2,r:3+Math.random()*3});R.bubbles.forEach(b=>{b.x+=b.vx*dt;b.y+=b.vy*dt;b.life-=dt;b.r+=dt;});R.bubbles=R.bubbles.filter(b=>b.life>0);',
        '''ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('实验室制取CO₂：CaCO₃+2HCl→CaCl₂+H₂O+CO₂↑',W/2,25);
ctx.fillStyle='rgba(9,132,227,0.15)';ctx.fillRect(W*0.2,H*0.5,W*0.6,H*0.35);ctx.strokeStyle='#0984e3';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(W*0.2,H*0.5);ctx.lineTo(W*0.8,H*0.5);ctx.stroke();
ctx.fillStyle='#aaa';ctx.font='11px sans-serif';ctx.fillText('稀盐酸',W*0.15,H*0.5-5);
ctx.fillStyle='#636e72';for(let i=0;i<5;i++){ctx.beginPath();ctx.arc(W*0.35+i*12,H*0.75,6,0,Math.PI*2);ctx.fill();}ctx.fillStyle='#fff';ctx.font='10px sans-serif';ctx.fillText('CaCO₃(大理石)',W*0.4,H*0.75+20);
R.bubbles.forEach(b=>{ctx.strokeStyle='rgba(99,110,114,0.7)';ctx.lineWidth=1;ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,Math.PI*2);ctx.stroke();ctx.fillStyle='rgba(99,110,114,0.2)';ctx.fill();});
ctx.fillStyle='#636e72';ctx.font='bold 12px sans-serif';ctx.fillText('CO₂↑',W*0.4,H*0.3);
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('H⁺攻击CaCO₃晶格→CO₃²⁻分解→CO₂分子从液面逸出',W/2,H-15);''',
        'CaCO₃+2HCl→CaCl₂+H₂O+CO₂↑：H⁺攻击晶格→CO₂逸出'
    ),
    '浓硫酸稀释': (
        'const A={t:0,heat:0,mols:[]};for(let i=0;i<20;i++)A.mols.push({x:Math.random(),y:0.7,vx:(Math.random()-0.5)*2,vy:(Math.random()-0.5)*2});',
        'A.t+=dt;A.heat=Math.min(1,A.t*0.2);A.mols.forEach(p=>{p.x+=p.vx*dt*(1+A.heat*3)*0.3;p.y+=p.vy*dt*(1+A.heat*3)*0.3;if(p.x<0||p.x>1)p.vx*=-1;if(p.y<0.3||p.y>1)p.vy*=-1;p.x=Math.max(0,Math.min(1,p.x));p.y=Math.max(0.3,Math.min(1,p.y));});',
        '''ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('浓硫酸稀释：大量放热，必须酸入水！',W/2,25);
ctx.fillStyle='rgba(9,132,227,0.2)';ctx.fillRect(W*0.2,H*0.3,W*0.6,H*0.6);ctx.strokeStyle='#0984e3';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(W*0.2,H*0.3);ctx.lineTo(W*0.8,H*0.3);ctx.stroke();
ctx.fillStyle='#0984e3';ctx.font='11px sans-serif';ctx.fillText('水',W*0.15,H*0.3-5);
const glow=ctx.createRadialGradient(W/2,H*0.5,10,W/2,H*0.5,100);glow.addColorStop(0,`rgba(225,69,83,${A.heat*0.3})`);glow.addColorStop(1,'rgba(225,69,83,0)');ctx.fillStyle=glow;ctx.fillRect(W*0.2,H*0.3,W*0.6,H*0.6);
A.mols.forEach(p=>{ctx.fillStyle='#74b9ff';ctx.beginPath();ctx.arc(W*0.2+p.x*W*0.6,H*0.3+p.y*H*0.6,3,0,Math.PI*2);ctx.fill();});
if(A.heat>0.3){ctx.fillStyle='#e17055';ctx.font='16px sans-serif';ctx.fillText('⚠ 放热!',W/2,H*0.25);}
ctx.fillStyle='#fdcb6e';ctx.font='bold 13px sans-serif';ctx.fillText('✓ 正确：酸沿壁注入水+搅拌  ✗ 错误：水倒入酸→喷溅!',W/2,H-30);
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('浓硫酸溶于水释放大量热，水浮在酸面上剧烈沸腾喷溅',W/2,H-10);''',
        '浓硫酸稀释：大量放热，必须酸入水、沿壁慢倒、不断搅拌'
    ),
    '电解池': (
        'const EL={t:0,ions:[]};for(let i=0;i<8;i++){EL.ions.push({x:0.4+Math.random()*0.2,y:0.3+Math.random()*0.4,type:i<4?\"Na\":\"Cl\"});}',
        'EL.t+=dt;EL.ions.forEach(p=>{if(p.type===\"Na\")p.x-=dt*0.03;else p.x+=dt*0.03;if(p.x<0.15)p.x=0.85;if(p.x>0.85)p.x=0.15;p.y+=Math.sin(EL.t*2)*0.005;p.y=Math.max(0.2,Math.min(0.8,p.y));});',
        '''ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,cx=W/2,cy=H/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('电解饱和食盐水：离子定向移动+电极反应',W/2,25);
ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.strokeRect(cx-W*0.3,cy-H*0.25,W*0.6,H*0.5);ctx.fillStyle='rgba(9,132,227,0.1)';ctx.fillRect(cx-W*0.3,cy-H*0.25,W*0.6,H*0.5);
ctx.fillStyle='#e17055';ctx.fillRect(cx-W*0.28,cy-H*0.22,8,H*0.44);ctx.fillStyle='#0984e3';ctx.fillRect(cx+W*0.27,cy-H*0.22,8,H*0.44);
ctx.fillStyle='#e17055';ctx.font='11px sans-serif';ctx.fillText('阳极(+)',cx-W*0.28,cy-H*0.28);ctx.fillStyle='#0984e3';ctx.fillText('阴极(-)',cx+W*0.28,cy-H*0.28);
EL.ions.forEach(p=>{const x=cx-W*0.3+p.x*W*0.6,y=cy-H*0.25+p.y*H*0.5;ctx.fillStyle=p.type===\"Na\"?'#00b894':'#e84393';ctx.beginPath();ctx.arc(x,y,6,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='8px sans-serif';ctx.fillText(p.type===\"Na\"?'+':'−',x,y+3);});
ctx.fillStyle='#e17055';ctx.font='11px sans-serif';ctx.fillText('2Cl⁻→Cl₂↑',cx-W*0.28,cy+H*0.3);
ctx.fillStyle='#0984e3';ctx.fillText('2H₂O+2e⁻→H₂↑+2OH⁻',cx+W*0.15,cy+H*0.3);
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('阳极：Cl⁻失电子→Cl₂↑  阴极：H₂O得电子→H₂↑+NaOH',W/2,H-15);''',
        '电解饱和食盐水：阳极Cl₂↑ 阴极H₂↑+NaOH'
    ),
    '神经元动作电位': (
        'const N={t:0,signal:0,voltage:[]};for(let i=0;i<100;i++)N.voltage.push(-70);',
        'N.t+=dt;N.signal=Math.min(1,N.signal+dt*0.3);N.voltage.push(-70+Math.sin(N.t*5)*80*Math.exp(-((N.t*5%6)-1)*((N.t*5%6)-1)*0.5));if(N.voltage.length>200)N.voltage.shift();',
        '''ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('神经元动作电位与突触传递',W/2,25);
const ax=W*0.1,ay=H*0.35,aw=W*0.5,ah=H*0.3;
ctx.strokeStyle='#7f93b5';ctx.lineWidth=1;ctx.strokeRect(ax,ay,aw,ah);
ctx.fillStyle='#aaa';ctx.font='10px sans-serif';ctx.textAlign='right';ctx.fillText('+40mV',ax-5,ay+10);ctx.fillText('-70mV',ax-5,ay+ah);ctx.textAlign='center';ctx.fillText('时间→',ax+aw/2,ay+ah+15);
ctx.strokeStyle='#00b894';ctx.lineWidth=2;ctx.beginPath();
N.voltage.forEach((v,i)=>{const x=ax+i/200*aw;const y=ay+ah-(v+80)/120*ah;i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);});ctx.stroke();
ctx.strokeStyle='rgba(255,255,255,0.2)';ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(ax,ay+ah-(-70+80)/120*ah);ctx.lineTo(ax+aw,ay+ah-(-70+80)/120*ah);ctx.stroke();ctx.setLineDash([]);
ctx.fillStyle='#fdcb6e';ctx.font='11px sans-serif';ctx.fillText('去极化→反极化→复极化',ax+aw/2,ay-10);
const sx=W*0.65,sy=H*0.4;ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(sx,sy,30,0,Math.PI*2);ctx.stroke();ctx.beginPath();ctx.arc(sx+60,sy,30,0,Math.PI*2);ctx.stroke();
ctx.fillStyle='#7f93b5';ctx.font='10px sans-serif';ctx.fillText('突触前',sx,sy+4);ctx.fillText('突触后',sx+60,sy+4);
for(let i=0;i<3;i++){const vx=sx+25+Math.sin(N.t*3+i)*5;const vy=sy-5+i*5;ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(vx,vy,3,0,Math.PI*2);ctx.fill();}
ctx.fillStyle='#fbbf24';ctx.font='10px sans-serif';ctx.fillText('神经递质',sx+30,sy-20);
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('电信号沿轴突传导→突触处化学传递(神经递质)→突触延搁',W/2,H-15);''',
        '动作电位：Na⁺内流→去极化→K⁺外流→复极化，突触处化学传递'
    ),
}

def get_dirname(fp):
    return os.path.basename(os.path.dirname(fp))

def enhance_file(filepath, key, anim_data):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    init_code, update_code, draw_code, status_text = anim_data
    
    new_script = COMMON_HEAD + init_code + '\n'
    new_script += 'function sceneInit(){sceneReset();}\n'
    new_script += 'function sceneReset(){' + init_code.split('=',1)[-1].rstrip(';') + ';}\n' if '=' in init_code else ''
    new_script += 'function sceneUpdate(dt){' + update_code + '}\n'
    new_script += 'function sceneDraw(){\n' + draw_code + '\nstatusEl.textContent="' + status_text + '";\n}\n'
    new_script += COMMON_TAIL
    
    script_match = re.search(r'(<script>\n)(.*?)(\n</script>)', content, re.DOTALL)
    if not script_match:
        return False
    
    content = content[:script_match.start(2)] + new_script + content[script_match.end(2):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def main():
    count = 0
    for root, dirs, files in os.walk(BASE):
        if '.workbuddy' in root:
            continue
        for fname in files:
            if fname == 'index.html':
                fpath = os.path.join(root, fname)
                dirname = get_dirname(fpath)
                with open(fpath, 'r', encoding='utf-8') as f:
                    lines = sum(1 for _ in f)
                if lines >= 200:
                    continue
                for key, anim_data in ANIMS.items():
                    if key in dirname:
                        if enhance_file(fpath, key, anim_data):
                            print(f'  OK: {dirname} ({lines} lines)')
                            count += 1
                        break
    print(f'\n共增强 {count} 个文件')

if __name__ == '__main__':
    main()
