#!/usr/bin/env python3
"""创建物理高优先级动画：牛顿第二定律、电场/电势、库仑定律"""
import os
BASE = r'd:\K12-Teaching-Animation\物理'

ANIMS = {}

# ============ 1. 牛顿第二定律 F=ma ============
ANIMS['牛顿第二定律（F=ma：力、质量与加速度的定量关系）'] = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>牛顿第二定律 F=ma</title>
<style>
:root{--bg:#0a1628;--panel:#111d33;--ink:#e8edf6;--muted:#8b9dc3;--accent:#0984e3;--line:#1e3050;--good:#00b894;--warn:#fdcb6e;--bad:#d63031;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--ink);min-height:100vh;display:flex;flex-direction:column}
.topbar{display:flex;align-items:center;gap:14px;padding:12px 18px;background:var(--panel);border-bottom:1px solid var(--line)}
.back{color:var(--accent);text-decoration:none;font-size:14px;padding:6px 12px;border:1px solid var(--line);border-radius:8px}
.back:hover{background:#1a2d4a}
main{flex:1;display:flex;min-height:0}
.stage{flex:1;display:flex;align-items:center;justify-content:center;padding:16px}
canvas{background:#060e1a;border:1px solid var(--line);border-radius:12px;max-width:100%}
.panel{width:340px;flex:none;padding:16px;overflow:auto;border-left:1px solid var(--line);background:var(--panel)}
.panel h2{font-size:15px;margin-bottom:10px;color:var(--accent)}
.panel p{font-size:13px;line-height:1.8;color:var(--muted);margin-bottom:12px}
.key-points{margin-top:12px;padding:12px;background:rgba(9,132,227,0.08);border-radius:8px;font-size:13px;line-height:1.8}
.key-points h3{font-size:14px;margin-bottom:8px;color:var(--warn)}
.key-points ul{padding-left:18px}
.key-points li{margin-bottom:4px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.legend span{font-size:12px;display:flex;align-items:center;gap:5px;color:var(--muted)}
.dot{width:12px;height:12px;border-radius:50%;display:inline-block}
.controls{display:flex;align-items:center;gap:10px;padding:12px 18px;background:var(--panel);border-top:1px solid var(--line);flex-wrap:wrap}
button{font:inherit;color:var(--ink);background:#1a2d4a;border:1px solid var(--line);padding:8px 14px;border-radius:8px;cursor:pointer}
button:hover{background:#243d5e}button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.controls label{font-size:13px;color:var(--muted)}
input[type=range]{accent-color:var(--accent)}
.status{font-size:12px;color:var(--muted);margin-left:auto}
.slider-group{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.slider-group label{font-size:12px;color:var(--muted);display:flex;justify-content:space-between}
.slider-group input{width:100%}
@media(max-width:860px){main{flex-direction:column}.panel{width:auto;border-left:none;border-top:1px solid var(--line)}}
</style>
</head>
<body>
<header class="topbar">
  <a class="back" href="../index.html">← 返回物理</a>
  <span>牛顿第二定律 F = ma</span>
</header>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2>原理说明</h2>
    <p>牛顿第二定律：物体的加速度a与所受合外力F成正比，与质量m成反比。公式：<b>F = ma</b>。力的方向与加速度方向相同。这是连接力和运动的桥梁——已知力求运动，或已知运动求力。</p>
    <div class="legend">
      <span><span class="dot" style="background:#0984e3"></span>物体(质量m)</span>
      <span><span class="dot" style="background:#d63031"></span>力F(红色箭头)</span>
      <span><span class="dot" style="background:#00b894"></span>加速度a</span>
      <span><span class="dot" style="background:#fdcb6e"></span>速度v</span>
    </div>
    <div class="slider-group">
      <label>力 F = <span id="fVal">10</span> N <input type="range" id="fSlider" min="1" max="30" value="10"></label>
      <label>质量 m = <span id="mVal">2</span> kg <input type="range" id="mSlider" min="1" max="10" value="2"></label>
    </div>
    <div class="key-points">
      <h3>核心公式</h3>
      <ul>
        <li><b>F = ma</b>（核心公式）</li>
        <li>a = F/m（加速度与力成正比，与质量成反比）</li>
        <li>1N = 1kg·m/s²</li>
        <li>力的方向 = 加速度方向</li>
        <li>适用于惯性参考系</li>
        <li>瞬时性：力变→a立即变</li>
      </ul>
    </div>
  </aside>
</main>
<div class="controls">
  <button id="playBtn" class="primary">▶ 播放</button>
  <button id="resetBtn">↺ 重置</button>
  <label>速度 <input id="speed" type="range" min="0.3" max="3" step="0.1" value="1"></label>
  <span id="status" class="status"></span>
</div>
<script>
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
const fSlider=document.getElementById('fSlider'),mSlider=document.getElementById('mSlider');
const fVal=document.getElementById('fVal'),mVal=document.getElementById('mVal');
let playing=false,t=0,speed=1;
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(400,Math.min(900,r.width-8));cv.height=Math.max(350,Math.min(550,r.height-8));}
window.addEventListener('resize',()=>{fit();});fit();

let F=10,M=2;
fSlider.oninput=()=>{F=+fSlider.value;fVal.textContent=F;};
mSlider.oninput=()=>{M=+mSlider.value;mVal.textContent=M;};

function draw(){
  const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  const a=F/M;
  const groundY=H*0.7;
  
  // 地面
  ctx.strokeStyle='#1e3050';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(40,groundY);ctx.lineTo(W-40,groundY);ctx.stroke();
  // 地面刻度
  for(let x=60;x<W-40;x+=40){
    ctx.beginPath();ctx.moveTo(x,groundY);ctx.lineTo(x,groundY+8);ctx.stroke();
  }
  
  // 物体位置
  const blockSize=30+M*4;
  const bx=80+t*t*a*0.3;
  const by=groundY-blockSize;
  
  if(bx<W-60){
    // 物体
    ctx.fillStyle='#0984e3';
    ctx.fillRect(bx,by,blockSize,blockSize);
    ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
    ctx.fillText(M+'kg',bx+blockSize/2,by+blockSize/2+5);
    
    // 力箭头
    const arrowLen=F*4;
    ctx.strokeStyle='#d63031';ctx.lineWidth=3;ctx.fillStyle='#d63031';
    ctx.beginPath();ctx.moveTo(bx+blockSize,by+blockSize/2);
    ctx.lineTo(bx+blockSize+arrowLen,by+blockSize/2);ctx.stroke();
    // 箭头头
    ctx.beginPath();
    ctx.moveTo(bx+blockSize+arrowLen,by+blockSize/2);
    ctx.lineTo(bx+blockSize+arrowLen-10,by+blockSize/2-6);
    ctx.lineTo(bx+blockSize+arrowLen-10,by+blockSize/2+6);
    ctx.fill();
    ctx.fillStyle='#d63031';ctx.font='bold 13px sans-serif';
    ctx.fillText('F='+F+'N',bx+blockSize+arrowLen/2,by+blockSize/2-12);
    
    // 加速度标注
    ctx.fillStyle='#00b894';ctx.font='13px sans-serif';
    ctx.fillText('a='+a.toFixed(1)+'m/s²',bx+blockSize/2,by-20);
    
    // 速度
    const v=a*t*0.5;
    ctx.fillStyle='#fdcb6e';
    ctx.fillText('v='+v.toFixed(1)+'m/s',bx+blockSize/2,by-40);
  }
  
  // 信息面板
  ctx.fillStyle='rgba(17,29,51,0.9)';
  ctx.fillRect(W-220,20,200,120);
  ctx.strokeStyle='#1e3050';ctx.strokeRect(W-220,20,200,120);
  ctx.fillStyle='#e8edf6';ctx.font='bold 14px sans-serif';ctx.textAlign='left';
  ctx.fillText('F = ma',W-200,45);
  ctx.font='13px sans-serif';ctx.fillStyle='#8b9dc3';
  ctx.fillText('F = '+F+' N',W-200,70);
  ctx.fillText('m = '+M+' kg',W-200,90);
  ctx.fillStyle='#00b894';
  ctx.fillText('a = F/m = '+a.toFixed(2)+' m/s²',W-200,115);
  ctx.fillStyle='#fdcb6e';
  ctx.fillText('t = '+t.toFixed(1)+' s',W-200,135);
  
  statusEl.textContent='F='+F+'N  m='+M+'kg  a='+a.toFixed(1)+'m/s²';
}

let lastTime=0;
function loop(ts){
  if(!lastTime)lastTime=ts;
  const dt=(ts-lastTime)/1000*speed;
  lastTime=ts;
  if(playing){t+=dt;draw();}
  requestAnimationFrame(loop);
}

document.getElementById('playBtn').onclick=function(){
  playing=!playing;
  this.textContent=playing?'⏸ 暂停':'▶ 播放';
};
document.getElementById('resetBtn').onclick=function(){t=0;draw();};
document.getElementById('speed').oninput=function(){speed=+this.value;};

draw();
requestAnimationFrame(loop);
</script>
</body>
</html>'''

# ============ 2. 电场/电场线/电势 ============
ANIMS['电场与电场线（点电荷电场分布+电势等高线）'] = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>电场与电场线</title>
<style>
:root{--bg:#0a1628;--panel:#111d33;--ink:#e8edf6;--muted:#8b9dc3;--accent:#0984e3;--line:#1e3050;--good:#00b894;--warn:#fdcb6e;--bad:#d63031;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--ink);min-height:100vh;display:flex;flex-direction:column}
.topbar{display:flex;align-items:center;gap:14px;padding:12px 18px;background:var(--panel);border-bottom:1px solid var(--line)}
.back{color:var(--accent);text-decoration:none;font-size:14px;padding:6px 12px;border:1px solid var(--line);border-radius:8px}
main{flex:1;display:flex;min-height:0}
.stage{flex:1;display:flex;align-items:center;justify-content:center;padding:16px}
canvas{background:#060e1a;border:1px solid var(--line);border-radius:12px}
.panel{width:340px;flex:none;padding:16px;overflow:auto;border-left:1px solid var(--line);background:var(--panel)}
.panel h2{font-size:15px;margin-bottom:10px;color:var(--accent)}
.panel p{font-size:13px;line-height:1.8;color:var(--muted);margin-bottom:12px}
.key-points{margin-top:12px;padding:12px;background:rgba(9,132,227,0.08);border-radius:8px;font-size:13px;line-height:1.8}
.key-points h3{font-size:14px;margin-bottom:8px;color:var(--warn)}
.key-points ul{padding-left:18px}.key-points li{margin-bottom:4px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.legend span{font-size:12px;display:flex;align-items:center;gap:5px;color:var(--muted)}
.dot{width:12px;height:12px;border-radius:50%;display:inline-block}
.controls{display:flex;align-items:center;gap:10px;padding:12px 18px;background:var(--panel);border-top:1px solid var(--line);flex-wrap:wrap}
button{font:inherit;color:var(--ink);background:#1a2d4a;border:1px solid var(--line);padding:8px 14px;border-radius:8px;cursor:pointer}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.controls label{font-size:13px;color:var(--muted)}
input[type=range]{accent-color:var(--accent)}
.status{font-size:12px;color:var(--muted);margin-left:auto}
.charge-btns{display:flex;gap:8px;margin:10px 0}
.charge-btns button{font-size:12px;padding:6px 12px}
.charge-btns button.active{background:var(--accent);border-color:var(--accent)}
@media(max-width:860px){main{flex-direction:column}.panel{width:auto;border-left:none;border-top:1px solid var(--line)}}
</style>
</head>
<body>
<header class="topbar">
  <a class="back" href="../index.html">← 返回物理</a>
  <span>电场与电场线</span>
</header>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2>原理说明</h2>
    <p>电场是电荷周围空间存在的一种特殊物质。正电荷电场线向外辐射，负电荷电场线向内汇聚。电场线越密→电场越强。沿电场线方向电势降低。等势面与电场线垂直。</p>
    <div class="legend">
      <span><span class="dot" style="background:#d63031"></span>正电荷+</span>
      <span><span class="dot" style="background:#0984e3"></span>负电荷-</span>
      <span><span class="dot" style="background:#fdcb6e"></span>电场线</span>
      <span><span class="dot" style="background:#00b894"></span>等势面</span>
    </div>
    <div class="charge-btns">
      <button id="btnPos" class="active" onclick="setCharge('pos')">正电荷</button>
      <button id="btnNeg" onclick="setCharge('neg')">负电荷</button>
      <button id="btnDipole" onclick="setCharge('dipole')">等量异种</button>
      <button id="btnSame" onclick="setCharge('same')">等量同种</button>
    </div>
    <div class="key-points">
      <h3>核心公式</h3>
      <ul>
        <li>电场强度：E = F/q（定义式）</li>
        <li>点电荷电场：E = kQ/r²</li>
        <li>匀强电场：E = U/d</li>
        <li>电场力：F = qE</li>
        <li>电势差：U_AB = φ_A - φ_B</li>
        <li>电场力做功：W = qU = qEd</li>
        <li>沿电场线方向电势降低</li>
        <li>等势面⊥电场线</li>
      </ul>
    </div>
  </aside>
</main>
<div class="controls">
  <button id="playBtn" class="primary">▶ 播放</button>
  <button id="resetBtn">↺ 重置</button>
  <label>速度 <input id="speed" type="range" min="0.3" max="3" step="0.1" value="1"></label>
  <span id="status" class="status"></span>
</div>
<script>
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
let playing=false,t=0,speed=1,chargeType='pos';
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(400,Math.min(700,r.width-8));cv.height=Math.max(400,Math.min(600,r.height-8));}
window.addEventListener('resize',()=>{fit();});fit();

function setCharge(type){
  chargeType=type;
  document.querySelectorAll('.charge-btns button').forEach(b=>b.classList.remove('active'));
  document.getElementById({pos:'btnPos',neg:'btnNeg',dipole:'btnDipole',same:'btnSame'}[type]).classList.add('active');
  t=0;draw();
}

function getCharges(){
  const cx=cv.width/2,cy=cv.height/2;
  switch(chargeType){
    case 'pos': return [{x:cx,y:cy,q:1}];
    case 'neg': return [{x:cx,y:cy,q:-1}];
    case 'dipole': return [{x:cx-80,y:cy,q:1},{x:cx+80,y:cy,q:-1}];
    case 'same': return [{x:cx-80,y:cy,q:1},{x:cx+80,y:cy,q:1}];
  }
}

function fieldAt(x,y,charges){
  let Ex=0,Ey=0;
  for(const c of charges){
    const dx=x-c.x,dy=y-c.y;
    const r2=dx*dx+dy*dy;
    if(r2<100)continue;
    const r=Math.sqrt(r2);
    const E=c.q/r2*5000;
    Ex+=E*dx/r;Ey+=E*dy/r;
  }
  return {Ex,Ey};
}

function draw(){
  const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  const charges=getCharges();
  
  // 画等势面
  ctx.globalAlpha=0.15;
  for(const c of charges){
    for(let r=30;r<200;r+=30){
      ctx.strokeStyle=c.q>0?'#d63031':'#0984e3';
      ctx.lineWidth=1;
      ctx.beginPath();ctx.arc(c.x,c.y,r,0,Math.PI*2);ctx.stroke();
    }
  }
  ctx.globalAlpha=1;
  
  // 画电场线
  const nLines=chargeType==='pos'||chargeType==='neg'?16:12;
  for(let i=0;i<nLines;i++){
    const angle=i/nLines*Math.PI*2;
    let px,py;
    if(chargeType==='neg'){
      px=charges[0].x+Math.cos(angle)*180;
      py=charges[0].y+Math.sin(angle)*180;
    } else {
      px=charges[0].x+Math.cos(angle)*15;
      py=charges[0].y+Math.sin(angle)*15;
    }
    
    ctx.strokeStyle='rgba(253,203,110,0.5)';ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(px,py);
    
    for(let step=0;step<200;step++){
      const {Ex,Ey}=fieldAt(px,py,charges);
      const Em=Math.sqrt(Ex*Ex+Ey*Ey);
      if(Em<0.001)break;
      const ds=3;
      const dir=charges[0].q>0&&chargeType!=='neg'?1:(chargeType==='neg'?-1:1);
      px+=dir*Ex/Em*ds;py+=dir*Ey/Em*ds;
      if(px<0||px>W||py<0||py>H)break;
      ctx.lineTo(px,py);
      
      // 检查是否接近负电荷
      let tooClose=false;
      for(const c of charges){
        if(c.q<0){const dx=px-c.x,dy=py-c.y;if(dx*dx+dy*dy<200)tooClose=true;}
      }
      if(tooClose)break;
    }
    ctx.stroke();
  }
  
  // 动画：运动的试探电荷
  if(playing){
    const testAngle=t*0.5%(Math.PI*2);
    const testR=40+((t*20)%150);
    const tx=charges[0].x+Math.cos(testAngle)*testR;
    const ty=charges[0].y+Math.sin(testAngle)*testR;
    const {Ex,Ey}=fieldAt(tx,ty,charges);
    const Em=Math.sqrt(Ex*Ex+Ey*Ey);
    
    if(Em>0.01){
      // 试探电荷
      ctx.fillStyle='#fdcb6e';
      ctx.beginPath();ctx.arc(tx,ty,5,0,Math.PI*2);ctx.fill();
      // 力的方向
      ctx.strokeStyle='#fdcb6e';ctx.lineWidth=2;
      const fLen=Math.min(Em*300,30);
      ctx.beginPath();ctx.moveTo(tx,ty);
      ctx.lineTo(tx+Ex/Em*fLen,ty+Ey/Em*fLen);ctx.stroke();
    }
  }
  
  // 画电荷
  for(const c of charges){
    ctx.fillStyle=c.q>0?'#d63031':'#0984e3';
    ctx.beginPath();ctx.arc(c.x,c.y,14,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#fff';ctx.font='bold 18px sans-serif';ctx.textAlign='center';
    ctx.fillText(c.q>0?'+':'−',c.x,c.y+6);
  }
  
  // 标注
  ctx.fillStyle='#8b9dc3';ctx.font='12px sans-serif';ctx.textAlign='left';
  ctx.fillText('E = kQ/r²',10,20);
  ctx.fillText('沿电场线方向电势降低',10,38);
  
  statusEl.textContent='电场线分布 | '+{pos:'正点电荷',neg:'负点电荷',dipole:'等量异种电荷',same:'等量同种电荷'}[chargeType];
}

let lastTime=0;
function loop(ts){
  if(!lastTime)lastTime=ts;
  const dt=(ts-lastTime)/1000*speed;
  lastTime=ts;
  if(playing){t+=dt;}
  draw();
  requestAnimationFrame(loop);
}

document.getElementById('playBtn').onclick=function(){playing=!playing;this.textContent=playing?'⏸ 暂停':'▶ 播放';};
document.getElementById('resetBtn').onclick=function(){t=0;draw();};
document.getElementById('speed').oninput=function(){speed=+this.value;};

draw();
requestAnimationFrame(loop);
</script>
</body>
</html>'''

# ============ 3. 库仑定律 ============
ANIMS['库仑定律（点电荷间作用力F=kQ₁Q₂/r²）'] = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>库仑定律</title>
<style>
:root{--bg:#0a1628;--panel:#111d33;--ink:#e8edf6;--muted:#8b9dc3;--accent:#0984e3;--line:#1e3050;--good:#00b894;--warn:#fdcb6e;--bad:#d63031;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--ink);min-height:100vh;display:flex;flex-direction:column}
.topbar{display:flex;align-items:center;gap:14px;padding:12px 18px;background:var(--panel);border-bottom:1px solid var(--line)}
.back{color:var(--accent);text-decoration:none;font-size:14px;padding:6px 12px;border:1px solid var(--line);border-radius:8px}
main{flex:1;display:flex;min-height:0}
.stage{flex:1;display:flex;align-items:center;justify-content:center;padding:16px}
canvas{background:#060e1a;border:1px solid var(--line);border-radius:12px}
.panel{width:340px;flex:none;padding:16px;overflow:auto;border-left:1px solid var(--line);background:var(--panel)}
.panel h2{font-size:15px;margin-bottom:10px;color:var(--accent)}
.panel p{font-size:13px;line-height:1.8;color:var(--muted);margin-bottom:12px}
.key-points{margin-top:12px;padding:12px;background:rgba(9,132,227,0.08);border-radius:8px;font-size:13px;line-height:1.8}
.key-points h3{font-size:14px;margin-bottom:8px;color:var(--warn)}
.key-points ul{padding-left:18px}.key-points li{margin-bottom:4px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.legend span{font-size:12px;display:flex;align-items:center;gap:5px;color:var(--muted)}
.dot{width:12px;height:12px;border-radius:50%;display:inline-block}
.controls{display:flex;align-items:center;gap:10px;padding:12px 18px;background:var(--panel);border-top:1px solid var(--line);flex-wrap:wrap}
button{font:inherit;color:var(--ink);background:#1a2d4a;border:1px solid var(--line);padding:8px 14px;border-radius:8px;cursor:pointer}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.controls label{font-size:13px;color:var(--muted)}
input[type=range]{accent-color:var(--accent);width:100%}
.status{font-size:12px;color:var(--muted);margin-left:auto}
.slider-group{display:flex;flex-direction:column;gap:10px;margin:10px 0}
.slider-group label{font-size:12px;color:var(--muted);display:flex;flex-direction:column;gap:4px}
@media(max-width:860px){main{flex-direction:column}.panel{width:auto;border-left:none;border-top:1px solid var(--line)}}
</style>
</head>
<body>
<header class="topbar">
  <a class="back" href="../index.html">← 返回物理</a>
  <span>库仑定律 F = kQ₁Q₂/r²</span>
</header>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2>原理说明</h2>
    <p>库仑定律：真空中两个静止点电荷之间的作用力F与它们的电荷量Q₁、Q₂的乘积成正比，与它们距离r的平方成反比。公式：<b>F = kQ₁Q₂/r²</b>，其中k = 9×10⁹ N·m²/C²。同种电荷相斥，异种电荷相吸。</p>
    <div class="legend">
      <span><span class="dot" style="background:#d63031"></span>正电荷</span>
      <span><span class="dot" style="background:#0984e3"></span>负电荷</span>
      <span><span class="dot" style="background:#fdcb6e"></span>库仑力</span>
    </div>
    <div class="slider-group">
      <label>Q₁ = <span id="q1Val">3</span> μC <input type="range" id="q1" min="-5" max="5" value="3"></label>
      <label>Q₂ = <span id="q2Val">2</span> μC <input type="range" id="q2" min="-5" max="5" value="2"></label>
      <label>距离 r = <span id="rVal">10</span> cm <input type="range" id="rSlider" min="3" max="20" value="10"></label>
    </div>
    <div class="key-points">
      <h3>核心公式</h3>
      <ul>
        <li><b>F = kQ₁Q₂/r²</b></li>
        <li>k = 9×10⁹ N·m²/C²（静电力常量）</li>
        <li>适用条件：真空、点电荷</li>
        <li>同种电荷→斥力；异种电荷→引力</li>
        <li>库仑力是矢量，沿连线方向</li>
        <li>满足牛顿第三定律（作用力=反作用力）</li>
        <li>r加倍→F变为1/4（平方反比）</li>
      </ul>
    </div>
  </aside>
</main>
<div class="controls">
  <button id="playBtn" class="primary">▶ 播放</button>
  <button id="resetBtn">↺ 重置</button>
  <label>速度 <input id="speed" type="range" min="0.3" max="3" step="0.1" value="1"></label>
  <span id="status" class="status"></span>
</div>
<script>
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
let playing=false,t=0,speed=1;
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(400,Math.min(800,r.width-8));cv.height=Math.max(350,Math.min(550,r.height-8));}
window.addEventListener('resize',()=>{fit();});fit();

const q1S=document.getElementById('q1'),q2S=document.getElementById('q2'),rS=document.getElementById('rSlider');
const q1V=document.getElementById('q1Val'),q2V=document.getElementById('q2Val'),rV=document.getElementById('rVal');
let Q1=3,Q2=2,R=10;
q1S.oninput=()=>{Q1=+q1S.value;q1V.textContent=Q1;};
q2S.oninput=()=>{Q2=+q2S.value;q2V.textContent=Q2;};
rS.oninput=()=>{R=+rS.value;rV.textContent=R;};

function draw(){
  const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  const cy=H/2;
  const cx=W/2;
  const scale=R*8;
  const x1=cx-scale/2,x2=cx+scale/2;
  
  // F = kQ1Q2/r^2 (简化计算)
  const F=Math.abs(Q1*Q2)/(R*R)*9;
  const isRepel=(Q1*Q2>0);
  
  // 距离标尺
  ctx.strokeStyle='#1e3050';ctx.lineWidth=1;
  ctx.beginPath();ctx.moveTo(x1,cy+50);ctx.lineTo(x2,cy+50);ctx.stroke();
  ctx.beginPath();ctx.moveTo(x1,cy+45);ctx.lineTo(x1,cy+55);ctx.stroke();
  ctx.beginPath();ctx.moveTo(x2,cy+45);ctx.lineTo(x2,cy+55);ctx.stroke();
  ctx.fillStyle='#8b9dc3';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('r = '+R+' cm',cx,cy+68);
  
  // 电荷1
  const c1Color=Q1>=0?'#d63031':'#0984e3';
  const c1Size=14+Math.abs(Q1)*2;
  ctx.fillStyle=c1Color;ctx.beginPath();ctx.arc(x1,cy,c1Size,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';
  ctx.fillText(Q1>=0?'+':'−',x1,cy+5);
  ctx.fillStyle='#8b9dc3';ctx.font='12px sans-serif';
  ctx.fillText('Q₁='+Q1+'μC',x1,cy-c1Size-10);
  
  // 电荷2
  const c2Color=Q2>=0?'#d63031':'#0984e3';
  const c2Size=14+Math.abs(Q2)*2;
  ctx.fillStyle=c2Color;ctx.beginPath();ctx.arc(x2,cy,c2Size,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';
  ctx.fillText(Q2>=0?'+':'−',x2,cy+5);
  ctx.fillStyle='#8b9dc3';ctx.font='12px sans-serif';
  ctx.fillText('Q₂='+Q2+'μC',x2,cy-c2Size-10);
  
  // 库仑力箭头
  if(Q1!==0&&Q2!==0){
    const arrowLen=Math.min(F*5,80);
    ctx.strokeStyle='#fdcb6e';ctx.lineWidth=3;ctx.fillStyle='#fdcb6e';
    
    // 力在Q1上
    const dir1=isRepel?-1:1;
    ctx.beginPath();ctx.moveTo(x1,cy);ctx.lineTo(x1+dir1*arrowLen,cy);ctx.stroke();
    ctx.beginPath();ctx.moveTo(x1+dir1*arrowLen,cy);
    ctx.lineTo(x1+dir1*arrowLen-dir1*8,cy-5);ctx.lineTo(x1+dir1*arrowLen-dir1*8,cy+5);ctx.fill();
    
    // 力在Q2上
    const dir2=isRepel?1:-1;
    ctx.beginPath();ctx.moveTo(x2,cy);ctx.lineTo(x2+dir2*arrowLen,cy);ctx.stroke();
    ctx.beginPath();ctx.moveTo(x2+dir2*arrowLen,cy);
    ctx.lineTo(x2+dir2*arrowLen-dir2*8,cy-5);ctx.lineTo(x2+dir2*arrowLen-dir2*8,cy+5);ctx.fill();
    
    ctx.fillStyle='#fdcb6e';ctx.font='bold 13px sans-serif';
    ctx.fillText('F='+F.toFixed(1)+'N',x1+dir1*arrowLen/2,cy-15);
    ctx.fillText('F='+F.toFixed(1)+'N',x2+dir2*arrowLen/2,cy-15);
  }
  
  // 力的类型标注
  ctx.fillStyle=isRepel?'#d63031':'#00b894';ctx.font='bold 14px sans-serif';
  ctx.fillText(isRepel?'斥力 ←→':'引力 →←',cx,cy-60);
  
  // F-r关系图
  const gx=W-180,gy=30,gw=160,gh=120;
  ctx.fillStyle='rgba(17,29,51,0.9)';ctx.fillRect(gx,gy,gw,gh);
  ctx.strokeStyle='#1e3050';ctx.strokeRect(gx,gy,gw,gh);
  ctx.fillStyle='#e8edf6';ctx.font='bold 12px sans-serif';ctx.textAlign='left';
  ctx.fillText('F ∝ 1/r² 关系',gx+10,gy+18);
  
  // 画曲线
  ctx.strokeStyle='#fdcb6e';ctx.lineWidth=1.5;ctx.beginPath();
  for(let i=0;i<gw-20;i++){
    const rr=1+i/(gw-20)*4;
    const ff=1/(rr*rr);
    const px=gx+10+i;
    const py=gy+gh-15-ff*(gh-40);
    if(i===0)ctx.moveTo(px,py);else ctx.lineTo(px,py);
  }
  ctx.stroke();
  
  // 当前点
  const curR=R/5;const curF=1/(curR*curR);
  const cpx=gx+10+(curR-1)/4*(gw-20);
  const cpy=gy+gh-15-Math.min(curF,1)*(gh-40);
  ctx.fillStyle='#d63031';ctx.beginPath();ctx.arc(cpx,cpy,4,0,Math.PI*2);ctx.fill();
  
  ctx.fillStyle='#8b9dc3';ctx.font='10px sans-serif';
  ctx.fillText('r →',gx+gw-25,gy+gh-5);
  ctx.fillText('F ↑',gx+2,gy+28);
  
  statusEl.textContent='F = kQ₁Q₂/r² = '+F.toFixed(1)+'N | '+(isRepel?'斥力':'引力');
}

let lastTime=0;
function loop(ts){
  if(!lastTime)lastTime=ts;
  lastTime=ts;
  if(playing){t+=0.016*speed;}
  draw();
  requestAnimationFrame(loop);
}

document.getElementById('playBtn').onclick=function(){playing=!playing;this.textContent=playing?'⏸ 暂停':'▶ 播放';};
document.getElementById('resetBtn').onclick=function(){Q1=3;Q2=2;R=10;q1S.value=3;q2S.value=2;rS.value=10;q1V.textContent=3;q2V.textContent=2;rV.textContent=10;draw();};
document.getElementById('speed').oninput=function(){speed=+this.value;};

draw();
requestAnimationFrame(loop);
</script>
</body>
</html>'''

# 创建文件
for name, html in ANIMS.items():
    d = os.path.join(BASE, name)
    os.makedirs(d, exist_ok=True)
    fp = os.path.join(d, 'index.html')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✓ 创建: {name}')

print(f'\n共创建 {len(ANIMS)} 个物理动画')
