# 酸的共性 · 电离出 H⁺

## 1. 需求
动画展示酸的四类通性：与活泼金属、与碱中和、与碳酸盐、使石蕊变红，以及电离本质。

## 2. 专业思考
酸的通性统一源于电离出 H⁺。动画用 5 个相位循环：活泼金属放 H₂、碱中和生成水、碳酸盐放 CO₂（检验碳酸盐）、石蕊变红、电离式。强调这是“通性”而非个别酸的性质；同时提醒浓硫酸、硝酸有强氧化性，与金属不放 H₂，是例外，避免绝对化。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>酸的共性 · 电离出 H⁺</title>
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
  <span class="title">酸的共性 · 电离出 H⁺</span>
  <span class="subtitle">酸 = H⁺ + 酸根离子</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>电离</h4><div class="v">酸 → H⁺ + A⁻</div></div><div class="card s3"><div class="num">2</div><h4>与金属</h4><div class="v">→ 盐 + H₂</div></div><div class="card s4"><div class="num">3</div><h4>与碱</h4><div class="v">→ 盐 + 水</div></div><div class="card "><div class="num">4</div><h4>与碳酸盐</h4><div class="v">→ 盐 + H₂O + CO₂</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">酸的共性 · 电离出 H⁺</span></h2>
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
const STEPS=[{"tag": "基础", "name": "酸的电离", "body": "酸在水溶液中都能电离出<strong>氢离子 H⁺</strong>，这是酸具有通性的根本原因。如 HCl → H⁺ + Cl⁻。", "points": {"title": "本质", "items": ["<strong>共性来源</strong>：H⁺", "<strong>HCl</strong>→H⁺+Cl⁻", "<strong>H₂SO₄</strong>→2H⁺+SO₄²⁻", "<strong>pH</strong>：酸 < 7"]}, "code": "HCl → H⁺ + Cl⁻\nH₂SO₄ → 2H⁺ + SO₄²⁻"}, {"tag": "与金属", "name": "与活泼金属", "body": "酸与<strong>活泼金属</strong>反应放出氢气：如 Zn + 2HCl → ZnCl₂ + H₂↑。", "points": {"title": "条件", "items": ["<strong>金属</strong>在 H 之前", "<strong>生成</strong>：盐 + H₂", "<strong>现象</strong>：冒气泡", "<strong>示例</strong>：Zn/Fe"]}}, {"tag": "与碱", "name": "与碱中和", "body": "酸与<strong>碱</strong>发生中和反应生成盐和水：如 HCl + NaOH → NaCl + H₂O。", "points": {"title": "中和", "items": ["<strong>酸+碱</strong>→盐+水", "<strong>放热</strong>", "<strong>pH</strong>→7", "<strong>应用</strong>：改良土壤"]}}, {"tag": "与碳酸盐", "name": "与碳酸盐", "body": "酸与<strong>碳酸盐</strong>反应放出 CO₂：如 CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂↑，用于检验碳酸盐。", "points": {"title": "检验", "items": ["<strong>生成</strong>：盐+水+CO₂", "<strong>现象</strong>：无色气泡", "<strong>石灰水</strong>变浑浊", "<strong>示例</strong>：CaCO₃"]}}, {"tag": "指示剂", "name": "使石蕊变红", "body": "酸能使<strong>紫色石蕊试液变红</strong>，这是酸的简便检验方法（酚酞遇酸不变色）。", "points": {"title": "指示", "items": ["<strong>石蕊</strong>：紫→红", "<strong>酚酞</strong>：不变", "<strong>pH试纸</strong>：变红", "<strong>注意</strong>：浓酸腐蚀"]}}];
let stepIdx=0;
const ACID={t:0};
function sceneInit(){ACID.t=0;}
function sceneReset(){ACID.t=0;}
function sceneUpdate(dt){ACID.t+=dt*speed;if(ACID.t>10)ACID.t=0;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 const r=Math.floor(ACID.t/2)%5;
 const titles=['① 与活泼金属 → 盐 + H₂','② 与碱 → 盐 + 水（中和）','③ 与碳酸盐 → 盐 + H₂O + CO₂','④ 使紫色石蕊变红','⑤ 电离：酸 → H⁺ + A⁻'];
 drawText('酸的共性（电离出 H⁺）：'+titles[r],W/2,24,'#74b9ff',13);
 const bx=W/2-90,by=H-70,bw=180,bh=180;
 ctx.fillStyle='rgba(248,113,113,0.22)';roundRect(bx,by-bh,bw,bh,8);ctx.fill();
 ctx.strokeStyle='#f87171';ctx.lineWidth=2;roundRect(bx,by-bh,bw,bh,8);ctx.stroke();
 drawText('H⁺ + A⁻',W/2,by-bh-18,'#f87171',13);
 let msg='';
 if(r===0){ctx.fillStyle='#cbd5e1';ctx.fillRect(bx+30,by-60,20,52);drawText('Zn',bx+40,by-34,'#0a1628',11);ctx.fillStyle='#34d399';drawText('↑H₂',bx+bw-28,by-92,'#34d399',12);msg='活泼金属 + 酸 → 盐 + 氢气';}
 else if(r===1){ctx.fillStyle='#34d399';ctx.fillRect(bx+30,by-60,42,52);drawText('OH⁻',bx+51,by-34,'#06281c',11);msg='酸 + 碱 → 盐 + 水（中和）';}
 else if(r===2){ctx.fillStyle='#fbbf24';ctx.fillRect(bx+30,by-60,42,52);drawText('CO₃²⁻',bx+51,by-34,'#06281c',11);ctx.fillStyle='#9ab0d0';drawText('↑CO₂',bx+bw-30,by-92,'#9ab0d0',12);msg='碳酸盐 + 酸 → 盐 + 水 + CO₂';}
 else if(r===3){ctx.fillStyle='#a855f7';ctx.fillRect(bx+30,by-60,42,52);drawText('石蕊',bx+51,by-34,'#fff',11);msg='酸使紫色石蕊试液变红';}
 else {ctx.fillStyle='#1e3a5f';ctx.fillRect(bx+30,by-60,60,52);ctx.strokeStyle='#74b9ff';ctx.strokeRect(bx+30,by-60,60,52);drawText('H⁺  A⁻',bx+60,by-34,'#fbbf24',11);msg='酸在水溶液中电离出 H⁺';}
 drawText(msg,W/2,by+24,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
