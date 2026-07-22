# 糖类 · 单糖二糖多糖

## 1. 需求
动画展示单糖、二糖、多糖三类糖类及其特征检验。

## 2. 专业思考
糖类（化学视角，区别于生物的物质功能）。动画三屏：单糖葡萄糖(醛基、银镜反应)、二糖蔗糖(水解)、多糖淀粉(遇碘变蓝)。强调糖类通式 Cm(H₂O)n（并非真正水合物）、醛基的还原性检验、淀粉的碘显色。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>糖类 · 单糖二糖多糖</title>
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
  <span class="title">糖类 · 单糖二糖多糖</span>
  <span class="subtitle">葡萄糖/蔗糖/淀粉</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>单糖</h4><div class="v">葡萄糖(醛糖)</div></div><div class="card s3"><div class="num">2</div><h4>二糖</h4><div class="v">蔗糖/麦芽糖</div></div><div class="card s4"><div class="num">3</div><h4>多糖</h4><div class="v">淀粉/纤维素</div></div><div class="card "><div class="num">4</div><h4>检验</h4><div class="v">银镜/碘色</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">糖类 · 单糖二糖多糖</span></h2>
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
  <span id="status" class="status">点击播放切换类别</span>
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
const STEPS=[{"tag": "基础", "name": "糖的分类", "body": "糖类按水解分为<strong>单糖、二糖、多糖</strong>。单糖不能水解，如葡萄糖。", "points": {"title": "分类", "items": ["<strong>单糖</strong>：不水解", "<strong>二糖</strong>：水解2单", "<strong>多糖</strong>：多聚", "<strong>通式</strong>：Cm(H2O)n"]}}, {"tag": "单糖", "name": "葡萄糖", "body": "葡萄糖是<strong>醛糖(含醛基)</strong>，能发生银镜反应；是主要供能物质。", "points": {"title": "葡萄糖", "items": ["<strong>醛基</strong>：−CHO", "<strong>银镜</strong>反应", "<strong>供能</strong>", "<strong>C₆H₁₂O₆</strong>"]}}, {"tag": "二糖", "name": "二糖", "body": "蔗糖、麦芽糖等二糖<strong>水解为两分子单糖</strong>。", "points": {"title": "二糖", "items": ["<strong>蔗糖</strong>：葡萄糖+果糖", "<strong>麦芽糖</strong>：两葡萄糖", "<strong>水解</strong>：得单糖", "<strong>甜</strong>：味"]}}, {"tag": "多糖", "name": "多糖", "body": "淀粉、纤维素等多糖由许多单糖聚合；<strong>淀粉遇碘变蓝</strong>。", "points": {"title": "多糖", "items": ["<strong>淀粉</strong>：遇碘蓝", "<strong>纤维素</strong>：结构", "<strong>储能</strong>：淀粉/糖原", "<strong>聚合</strong>：高分子"]}}];
let stepIdx=0;
const SUGAR={t:0};
function sceneInit(){SUGAR.t=0;}
function sceneReset(){SUGAR.t=0;}
function sceneUpdate(dt){SUGAR.t+=dt*speed;if(SUGAR.t>6)SUGAR.t=0;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 const s=Math.floor(SUGAR.t/2)%3;
 const names=['单糖：葡萄糖(醛糖,银镜反应)','二糖：蔗糖(遇酸水解)','多糖：淀粉(遇碘变蓝)'];
 drawText('糖类：'+names[s],W/2,22,'#74b9ff',13);
 const cx=W/2,cy=H/2;
 if(s===0){ctx.fillStyle='#34d399';ctx.beginPath();ctx.arc(cx,cy,30,0,7);ctx.fill();drawText('C₆H₁₂O₆',cx,cy,'#06281c',11);drawText('醛基→银镜反应',cx,cy+50,'#9ab0d0',11);}
 else if(s===1){ctx.fillStyle='#1e3a5f';roundRect(cx-50,cy-15,100,30,6);ctx.fill();ctx.strokeStyle='#74b9ff';ctx.stroke();drawText('葡萄糖+果糖',cx,cy,'#fbbf24',11);drawText('水解为单糖',cx,cy+50,'#9ab0d0',11);}
 else {ctx.fillStyle='#cbd5e1';for(let i=0;i<6;i++){ctx.beginPath();ctx.arc(cx-60+i*22,cy,9,0,7);ctx.fill();}drawText('淀粉+碘→蓝色',cx,cy+50,'#9ab0d0',11);}
 drawText('糖是主要能源物质；多糖可储能(淀粉/糖原)',W/2,H-22,'#9ab0d0',11);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
