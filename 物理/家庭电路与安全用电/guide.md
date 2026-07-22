# 家庭电路与安全用电

## 1. 需求
动画展示家庭电路火线/零线/地线及漏电保护器的工作原理。

## 2. 专业思考
安全用电教育重点。动画上方三线（火红、零蓝、地黄绿虚线），右侧插座+用电器，下方正常/漏电两态：漏电时保护器变红并提示跳闸。强调‘左零右火上地’、金属外壳接地、漏保每月试按、先断电后救护。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>家庭电路与安全用电</title>
<style>:root{
  --bg:#0a1628;--panel:#11203a;--card:#172a4a;--ink:#e8eef8;--muted:#9ab0d0;
  --accent:#3b82f6;--accent2:#74b9ff;--line:#243a5e;
  --good:#34d399;--warn:#fbbf24;--bad:#f87171;--info:#38bdf8;
}
*{box-sizing:border-box}html,body{margin:0;height:100%;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
body{background:var(--bg);color:var(--ink);display:flex;flex-direction:column;height:100vh;overflow:hidden}
.topbar{display:flex;align-items:center;gap:14px;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line);flex-wrap:wrap}
.back{color:var(--accent2);text-decoration:none;font-size:13px;padding:6px 12px;border:1px solid var(--line);border-radius:8px;white-space:nowrap;background:rgba(116,185,255,.06)}
.back:hover{background:rgba(116,185,255,.14)}
.title{font-size:15px;font-weight:600}
.subtitle{font-size:12px;color:var(--muted)}
.cards{display:flex;gap:10px;padding:10px 16px;flex-wrap:wrap;background:linear-gradient(180deg,rgba(59,130,246,.06),transparent)}
.card{flex:1;min-width:160px;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;position:relative;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--accent)}
.card.s2::before{background:var(--good)}
.card.s3::before{background:var(--bad)}
.card.s4::before{background:var(--warn)}
.card h4{margin:0 0 4px;font-size:13px;color:var(--ink)}
.card .v{font-size:11px;color:var(--muted);line-height:1.5}
.card .num{position:absolute;right:8px;top:6px;font-size:24px;font-weight:700;color:rgba(255,255,255,.07)}
main{flex:1;display:flex;min-height:0}
.stage{flex:1;display:flex;align-items:center;justify-content:center;padding:10px;min-width:0}
canvas{background:#06101f;border:1px solid var(--line);border-radius:12px;max-width:100%;max-height:100%;display:block}
.panel{width:340px;flex:none;padding:14px;overflow:auto;border-left:1px solid var(--line);background:var(--panel);font-size:13px;line-height:1.7}
.panel h2{font-size:14px;margin:0 0 8px;display:flex;align-items:center;gap:8px}
.badge{display:inline-block;padding:2px 8px;border-radius:6px;background:var(--accent);color:#fff;font-size:11px;font-weight:600}
.body{color:var(--muted);margin:0 0 10px}
.body strong{color:var(--ink)}
.body code{background:rgba(59,130,246,.2);color:#bfdbfe;padding:1px 5px;border-radius:4px;font-family:Consolas,Monaco,monospace;font-size:12px}
.points{background:rgba(255,255,255,.04);border-radius:8px;padding:10px;margin-top:8px;border-left:3px solid var(--accent2)}
.points h4{margin:0 0 6px;font-size:13px;color:var(--ink)}
.points ul{margin:0;padding-left:18px;color:var(--muted)}
.points li{margin-bottom:3px}
.points li strong{color:var(--accent)}
.code{background:#0d1117;border:1px solid var(--line);border-radius:6px;padding:8px 10px;margin-top:8px;font-family:Consolas,Monaco,monospace;font-size:11px;line-height:1.6;color:#c9d1d9;white-space:pre-wrap}
.code .kw{color:#ff7b72}.code .ty{color:#79c0ff}.code .cm{color:#8b949e}
.stepbar{display:flex;gap:6px;padding:8px 16px;background:var(--panel);border-top:1px solid var(--line);overflow-x:auto}
.step{flex:1;min-width:100px;padding:8px 10px;background:var(--card);border:1px solid var(--line);border-radius:8px;cursor:pointer;font-size:12px;text-align:center;transition:all .15s}
.step:hover{background:#1e345a;border-color:var(--accent2)}
.step.active{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:600;border-color:transparent}
.controls{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--panel);border-top:1px solid var(--line);flex-wrap:wrap}
button{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);padding:7px 14px;border-radius:8px;cursor:pointer;font-size:13px}
button:hover{background:#1e345a}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
button.primary:hover{background:#4b91f8}
.controls label{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px}
input[type=range],input[type=number]{accent-color:var(--accent);background:var(--card);color:var(--ink);border:1px solid var(--line);padding:4px 6px;border-radius:4px;width:60px}
.status{font-size:12px;color:var(--muted);margin-left:auto}
@media(max-width:960px){main{flex-direction:column}.panel{width:auto;border-left:none;border-top:1px solid var(--line);max-height:240px}}
</style>
</head>
<body>
<header class="topbar">
  <a class="back" href="../物理/index.html">← 返回物理目录</a>
  <span class="title">家庭电路与安全用电</span>
  <span class="subtitle">火线/零线/地线 · 漏保</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>三线</h4><div class="v">火/零/地三线</div></div><div class="card s3"><div class="num">2</div><h4>插座</h4><div class="v">左零右火上地</div></div><div class="card s4"><div class="num">3</div><h4>漏保</h4><div class="v">漏电即跳闸</div></div><div class="card "><div class="num">4</div><h4>原则</h4><div class="v">不接触带电体</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">家庭电路与安全用电</span></h2>
    <p class="body" id="stepBody"></p>
    <div class="points" id="stepPoints"></div>
    <div class="code" id="stepCode"></div>
  </aside>
</main>
<div class="stepbar" id="stepbar"></div>
<div class="controls">
  <button id="playBtn" class="primary">▶ 播放</button>
  <button id="resetBtn">↺ 重置</button>
  <button id="stepBackBtn">◀ 上一步</button>
  <button id="stepFwdBtn">下一步 ▶</button>
  
  <label>速度 <input id="speed" type="range" min="0.3" max="3" step="0.1" value="1"></label>
  <span id="status" class="status">点击播放观察漏电保护</span>
</div>
<script>
const cv=document.getElementById('cv'),ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(560,Math.min(1100,r.width-12));cv.height=Math.max(420,Math.min(560,r.height-12));}
window.addEventListener('resize',()=>{fit();sceneDraw();});fit();
function roundRect(x,y,w,h,r){ctx.beginPath();ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath();}
function drawText(t,x,y,c,fs,align,baseline){ctx.fillStyle=c||'#9ab0d0';ctx.font=(fs||12)+'px sans-serif';ctx.textAlign=align||'center';ctx.textBaseline=baseline||'middle';ctx.fillText(t,x,y);}
window.showTip=function(m){if(statusEl)statusEl.textContent=m;};
let playing=false,lastT=0,speed=1;
function loop(ts){if(!lastT)lastT=ts;const dt=(ts-lastT)/1000;lastT=ts;if(playing)sceneUpdate(dt);sceneDraw();requestAnimationFrame(loop);}
const playBtn=document.getElementById('playBtn'),resetBtn=document.getElementById('resetBtn'),stepBackBtn=document.getElementById('stepBackBtn'),stepFwdBtn=document.getElementById('stepFwdBtn'),speedEl=document.getElementById('speed');
playBtn.onclick=()=>{playing=!playing;playBtn.textContent=playing?'⏸ 暂停':'▶ 播放';};
resetBtn.onclick=()=>{sceneReset();sceneDraw();statusEl.textContent='已重置';};
stepFwdBtn.onclick=()=>{stepIdx=(stepIdx+1)%STEPS.length;loadStep();};
stepBackBtn.onclick=()=>{stepIdx=(stepIdx-1+STEPS.length)%STEPS.length;loadStep();};
speedEl.oninput=()=>{speed=parseFloat(speedEl.value);};
function loadStep(){const s=STEPS[stepIdx];if(!s)return;document.getElementById('stepBadge').textContent=s.tag;document.getElementById('stepTitle').textContent=s.name;document.getElementById('stepBody').innerHTML=s.body;document.getElementById('stepPoints').innerHTML='<h4>'+(s.points?s.points.title:'')+'</h4><ul>'+((s.points?s.points.items:[]).map(x=>'<li>'+x+'</li>').join(''))+'</ul>';document.getElementById('stepCode').innerHTML=s.code||'';document.querySelectorAll('.step').forEach((el,i)=>el.classList.toggle('active',i===stepIdx));statusEl.textContent='步骤 '+(stepIdx+1)+' / '+STEPS.length+' · '+s.name;}
function buildStepbar(){const bar=document.getElementById('stepbar');bar.innerHTML='';STEPS.forEach((s,i)=>{const el=document.createElement('div');el.className='step'+(i===stepIdx?' active':'');el.innerHTML='<div>'+s.tag+'</div><div>'+(s.name.length>8?s.name.slice(0,7)+'…':s.name)+'</div>';el.onclick=()=>{stepIdx=i;loadStep();};bar.appendChild(el);});}
const STEPS=[{"tag": "基础", "name": "家庭电路组成", "body": "家庭电路由<strong>火线(L,带电)、零线(N,回路)、地线(PE,保护)</strong>及电能表、开关、插座、用电器组成。", "points": {"title": "三线", "items": ["<strong>火线L</strong>：带电(红)", "<strong>零线N</strong>：回路(蓝)", "<strong>地线PE</strong>：保护(黄绿)", "<strong>插座</strong>：左零右火上地"]}}, {"tag": "触电", "name": "触电原理", "body": "人体接触<strong>火线且与大地连通</strong>时形成电流回路即触电；站在绝缘物上单手操作可减小危险。", "points": {"title": "危险", "items": ["<strong>火+地</strong>：触电", "<strong>湿手</strong>：更危险", "<strong>绝缘</strong>：防护", "<strong>断</strong>：先断电"]}}, {"tag": "漏保", "name": "漏电保护器", "body": "<strong>漏电保护器</strong>检测火零线电流差，一旦漏电立即跳闸切断电源，是重要保命装置。", "points": {"title": "原理", "items": ["<strong>火≠零</strong>：漏电", "<strong>毫秒级</strong>：跳闸", "<strong>浴室</strong>：必装", "<strong>每月</strong>：试按"]}}, {"tag": "规则", "name": "安全用电", "body": "不接触低压带电体、不靠近高压；电器金属壳<strong>接地</strong>；雷雨天远离天线与水体。", "points": {"title": "守则", "items": ["<strong>不接触</strong>：带电体", "<strong>外壳</strong>：接地", "<strong>破损</strong>：停用", "<strong>救护</strong>：先断电"]}}];
let stepIdx=0;
const HOME={t:0,phase:0};
function sceneInit(){HOME.t=0;}
function sceneReset(){HOME.t=0;}
function sceneUpdate(dt){HOME.t+=dt*speed;if(HOME.t>8)HOME.t=0;HOME.phase=Math.floor(HOME.t/4)%2;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('家庭电路：火线(红)/零线(蓝)/地线(黄绿) · 漏电保护器',W/2,20,'#74b9ff',12);
 const fault=HOME.phase===1;
 ctx.strokeStyle='#f87171';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(40,80);ctx.lineTo(W-200,80);ctx.stroke();drawText('火线 L',50,68,'#f87171',11);
 ctx.strokeStyle='#38bdf8';ctx.beginPath();ctx.moveTo(40,110);ctx.lineTo(W-200,110);ctx.stroke();drawText('零线 N',50,128,'#38bdf8',11);
 ctx.strokeStyle='#34d399';ctx.setLineDash([6,4]);ctx.beginPath();ctx.moveTo(40,140);ctx.lineTo(W-200,140);ctx.stroke();ctx.setLineDash([]);drawText('地线 PE',50,158,'#34d399',11);
 const sx=W-150,sy=110;ctx.fillStyle='#1e3a5f';ctx.strokeStyle='#74b9ff';ctx.strokeRect(sx,sy-30,60,60);
 ctx.fillStyle=fault?'#f87171':'#34d399';ctx.beginPath();ctx.arc(sx+30,sy,16,0,7);ctx.fill();drawText(fault?'⚠ 漏电':'保护',sx+30,sy-26,'#9ab0d0',10);
 drawText(fault?'漏电→保护器跳闸切断电源(安全)':'正常：地线保命，触电即断',W/2,H-26,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
