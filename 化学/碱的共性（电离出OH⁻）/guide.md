# 碱的共性 · 电离出 OH⁻

## 1. 需求
动画展示碱的四类通性：电离出OH⁻、与酸中和、使指示剂变色、与氧化物/盐反应。

## 2. 专业思考
碱的通性源于电离出 OH⁻。动画四相位循环：电离式、与酸中和生成水、酚酞变红、与 CO₂/盐反应。强调‘通性’而非个别碱；难溶碱(如 Cu(OH)₂、Fe(OH)₃)虽不溶性仍属碱但有局限。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>碱的共性 · 电离出 OH⁻</title>
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
  <a class="back" href="../化学/index.html">← 返回化学目录</a>
  <span class="title">碱的共性 · 电离出 OH⁻</span>
  <span class="subtitle">碱 = M⁺ + OH⁻</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>电离</h4><div class="v">碱→M⁺+OH⁻</div></div><div class="card s3"><div class="num">2</div><h4>中和</h4><div class="v">+酸→盐+水</div></div><div class="card s4"><div class="num">3</div><h4>指示</h4><div class="v">酚酞变红</div></div><div class="card "><div class="num">4</div><h4>反应</h4><div class="v">+非金属氧化物/盐</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">碱的共性 · 电离出 OH⁻</span></h2>
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
  <span id="status" class="status">点击播放观察四类反应</span>
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
const STEPS=[{"tag": "基础", "name": "碱的电离", "body": "碱在水溶液中都能电离出<strong>氢氧根离子 OH⁻</strong>，这是碱具通性的原因。如 NaOH → Na⁺ + OH⁻。", "points": {"title": "本质", "items": ["<strong>共性源</strong>：OH⁻", "<strong>NaOH</strong>→Na⁺+OH⁻", "<strong>Ca(OH)₂</strong>：可溶", "<strong>pH</strong>：>7"]}, "code": "NaOH → Na⁺ + OH⁻"}, {"tag": "中和", "name": "与酸中和", "body": "碱与酸发生中和：<strong>碱 + 酸 → 盐 + 水</strong>。", "points": {"title": "中和", "items": ["<strong>OH⁻+H⁺</strong>→H₂O", "<strong>生成</strong>：盐+水", "<strong>放热</strong>", "<strong>应用</strong>：改良土"]}}, {"tag": "指示", "name": "指示剂", "body": "碱使<strong>紫色石蕊变蓝、无色酚酞变红</strong>。", "points": {"title": "指示", "items": ["<strong>石蕊</strong>：紫→蓝", "<strong>酚酞</strong>：无→红", "<strong>pH试纸</strong>：蓝", "<strong>注意</strong>：腐蚀"]}}, {"tag": "反应", "name": "其他反应", "body": "碱还能与<strong>非金属氧化物</strong>(CO₂+2NaOH→Na₂CO₃+H₂O)、某些<strong>盐</strong>反应。", "points": {"title": "通性", "items": ["<strong>+CO₂</strong>→碳酸盐", "<strong>+盐</strong>→新盐", "<strong>通性</strong>：源于OH⁻", "<strong>难溶</strong>：Cu(OH)₂"]}}];
let stepIdx=0;
const BASE={t:0};
function sceneInit(){BASE.t=0;}
function sceneReset(){BASE.t=0;}
function sceneUpdate(dt){BASE.t+=dt*speed;if(BASE.t>10)BASE.t=0;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 const r=Math.floor(BASE.t/2)%4;
 const names=['① 电离出 OH⁻：碱 → M⁺ + OH⁻','② 与酸中和 → 盐+水','③ 使酚酞变红、石蕊变蓝','④ 与非金属氧化物/盐反应'];
 drawText('碱的共性（电离出 OH⁻）：'+names[r],W/2,22,'#74b9ff',12);
 const bx=W/2-90,by=H-70,bw=180,bh=180;
 ctx.fillStyle='rgba(167,139,250,0.22)';roundRect(bx,by-bh,bw,bh,8);ctx.fill();ctx.strokeStyle='#a855f7';ctx.lineWidth=2;roundRect(bx,by-bh,bw,bh,8);ctx.stroke();
 drawText('OH⁻',W/2,by-bh-18,'#a855f7',13);
 let msg='';
 if(r===0){ctx.fillStyle='#a855f7';drawText('M⁺  OH⁻',W/2,by-60,'#fff',12);msg='碱在水溶液电离出 OH⁻';}
 else if(r===1){ctx.fillStyle='#34d399';drawText('H⁺+OH⁻→H₂O',W/2,by-60,'#06281c',12);msg='碱+酸→盐+水（中和）';}
 else if(r===2){ctx.fillStyle='#f87171';drawText('酚酞→红',W/2,by-60,'#fff',12);msg='碱使酚酞变红、石蕊变蓝';}
 else {ctx.fillStyle='#fbbf24';drawText('CO₂+2NaOH→Na₂CO₃+H₂O',W/2,by-60,'#06281c',10);msg='碱+非金属氧化物/某些盐反应';}
 drawText(msg,W/2,by+24,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
