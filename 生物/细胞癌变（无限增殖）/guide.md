# 细胞癌变 · 失控增殖

## 1. 需求
动画对比正常细胞（接触抑制）与癌细胞（无限增殖、失去接触抑制），解释癌变机制。

## 2. 专业思考
癌变是细胞生物学重点。动画左右分屏：左侧正常细胞受接触抑制呈单层排列，右侧癌细胞持续分裂堆叠。机制层面点出原癌基因（促进增殖）被激活、抑癌基因（如 p53）失活，细胞周期检查点失效。特征：无限增殖、糖蛋白减少易转移、形态改变。诱因分物理/化学/病毒三类，预防靠远离因子与免疫监视。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>细胞癌变 · 失控增殖</title>
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
  <a class="back" href="../生物/index.html">← 返回生物目录</a>
  <span class="title">细胞癌变 · 失控增殖</span>
  <span class="subtitle">原癌基因/抑癌基因失衡</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>诱因</h4><div class="v">基因突变/致癌因子</div></div><div class="card s3"><div class="num">2</div><h4>机制</h4><div class="v">原癌基因激活·抑癌失活</div></div><div class="card s4"><div class="num">3</div><h4>特征</h4><div class="v">无限增殖·转移</div></div><div class="card "><div class="num">4</div><h4>预防</h4><div class="v">远离致癌因子</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">细胞癌变 · 失控增殖</span></h2>
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
  <span id="status" class="status">点击播放观察增殖失控</span>
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
const STEPS=[{"tag": "基础", "name": "癌变的本质", "body": "细胞癌变是<strong>原癌基因被激活、抑癌基因失活</strong>，导致<strong>细胞周期失控</strong>、正常分化丧失的变异。", "points": {"title": "基因层面", "items": ["<strong>原癌基因</strong>：促增殖", "<strong>抑癌基因</strong>：抑增殖", "<strong>突变</strong>：二者失衡", "<strong>结果</strong>：失控分裂"]}, "code": "原癌基因(激活) + 抑癌基因(失活)\n   → 细胞周期失控 → 癌"}, {"tag": "诱因", "name": "致癌因子", "body": "物理（紫外线、射线）、化学（亚硝胺、苯）、病毒（如 HPV）等<strong>致癌因子</strong>可诱发基因突变。", "points": {"title": "三类", "items": ["<strong>物理</strong>：UV/射线", "<strong>化学</strong>：亚硝胺", "<strong>病毒</strong>：HPV等", "<strong>累积</strong>：多突变"]}}, {"tag": "特征", "name": "癌细胞特征", "body": "癌细胞具有<strong>无限增殖、形态结构改变、表面糖蛋白减少（易转移）、失去接触抑制</strong>等特征。", "points": {"title": "特征", "items": ["<strong>无限增殖</strong>", "<strong>接触抑制丧失</strong>", "<strong>糖蛋白↓</strong>→易扩散", "<strong>形态</strong>：畸形"]}}, {"tag": "预防", "name": "预防", "body": "远离致癌因子、健康生活方式、定期筛查可降低风险；<strong>免疫系统</strong>可清除多数突变细胞。", "points": {"title": "措施", "items": ["<strong>戒烟</strong>限酒", "<strong>防晒</strong>", "<strong>筛查</strong>早诊", "<strong>免疫</strong>监视"]}}];
let stepIdx=0;
const CAN={t:0};
function sceneInit(){CAN.t=0;}
function sceneReset(){CAN.t=0;}
function sceneUpdate(dt){CAN.t+=dt*speed;}
function cell(x,y,r,color){ctx.fillStyle=color;ctx.beginPath();ctx.arc(x,y,r,0,7);ctx.fill();ctx.strokeStyle='#74b9ff';ctx.lineWidth=2;ctx.stroke();ctx.fillStyle='#34d399';ctx.beginPath();ctx.arc(x,y,r*0.4,0,7);ctx.fill();}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('细胞癌变：原癌基因激活 / 抑癌基因失活 → 失去接触抑制，无限增殖',W/2,22,'#74b9ff',12);
 drawText('正常细胞（有接触抑制）',W*0.28,64,'#34d399',13);
 let n=0;for(let i=0;i<5&&n<8;i++){for(let j=0;j<2;j++){const x=W*0.12+i*42,y=104+j*42;cell(x,y,16,'#1e3a5f');n++;}}
 drawText('癌细胞（失控增殖）',W*0.75,64,'#f87171',13);
 const cnt=Math.floor((CAN.t*3)%9)+4;let k=0;for(let i=0;i<4&&k<cnt;i++){for(let j=0;j<3;j++){const x=W*0.62+i*34,y=104+j*34;if(k<cnt){cell(x,y,14,'#3a1e2a');k++;}}}
 drawText('DNA 损伤 → 细胞周期检查点失效 → 异常分裂、可转移',W/2,H-22,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
