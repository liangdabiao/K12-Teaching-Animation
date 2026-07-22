# Prim 算法 · 最小生成树

## 1. 需求
动画展示 Prim 算法从起点贪心扩展、逐步加入最近点构建最小生成树。

## 2. 专业思考
Prim 是 MST 算法，以点为中心贪心扩展。动画随时间把离生成树最近的点加入（绿边），实时显示权值和。强调与 Kruskal 区别：Prim 维护点集、适合稠密图；Kruskal 排序边、适合稀疏图。应用：网络布线最小成本。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prim 算法 · 最小生成树</title>
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
  <a class="back" href="../信息技术/index.html">← 返回信息技术目录</a>
  <span class="title">Prim 算法 · 最小生成树</span>
  <span class="subtitle">点扩展 · 贪心</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>目标</h4><div class="v">最小生成树</div></div><div class="card s3"><div class="num">2</div><h4>策略</h4><div class="v">每次加最近点</div></div><div class="card s4"><div class="num">3</div><h4>结构</h4><div class="v">点集扩展</div></div><div class="card "><div class="num">4</div><h4>复杂</h4><div class="v">O(E log V)</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">Prim 算法 · 最小生成树</span></h2>
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
  <span id="status" class="status">点击播放观察生长</span>
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
const STEPS=[{"tag": "基础", "name": "最小生成树", "body": "<strong>最小生成树(MST)</strong>：在连通加权图中选 V-1 条边连通所有点且总权最小。", "points": {"title": "概念", "items": ["<strong>连通</strong>", "<strong>无环</strong>", "<strong>V-1边</strong>", "<strong>权最小</strong>"]}}, {"tag": "策略", "name": "Prim 策略", "body": "Prim 从一点出发，每步把<strong>离当前生成树最近的未入树点</strong>加入（贪心）。", "points": {"title": "策略", "items": ["<strong>起点</strong>", "<strong>最近</strong>未入树", "<strong>贪心</strong>加", "<strong>点扩展</strong>"]}, "code": "每次：选 min{w(u,v)|u∈树,v∉树}"}, {"tag": "对比", "name": "与 Kruskal", "body": "Prim <strong>以点为中心</strong>扩展，适合<strong>稠密图</strong>；Kruskal 以边排序、适合稀疏图。", "points": {"title": "对比", "items": ["<strong>Prim</strong>：点扩", "<strong>Kruskal</strong>：边排", "<strong>稠密</strong>：Prim优", "<strong>稀疏</strong>：Krus优"]}}, {"tag": "应用", "name": "应用", "body": "MST 用于<strong>网络布线、聚类、电路设计</strong>等最小成本连通。", "points": {"title": "用途", "items": ["<strong>布线</strong>", "<strong>聚类</strong>", "<strong>电路</strong>", "<strong>成本</strong>最小"]}}];
let stepIdx=0;
const PRIM={t:0,n:6,edges:[[0,1,7],[0,2,9],[0,5,14],[1,2,10],[1,3,15],[2,3,11],[2,4,2],[3,4,6],[4,5,9]],vis:[],mst:0};
function sceneInit(){PRIM.vis=[true,false,false,false,false,false];PRIM.mst=0;PRIM.t=0;}
function sceneReset(){PRIM.vis=[true,false,false,false,false,false];PRIM.mst=0;PRIM.t=0;}
function sceneUpdate(dt){PRIM.t+=dt*speed;if(PRIM.t>6)PRIM.t=0;const steps=Math.floor(PRIM.t/1.5);let v=[true].concat(new Array(5).fill(false));let cost=0;let used=0;for(let s=0;s<steps&&used<PRIM.n-1;s++){let bi=-1,bj=-1,bw=1e9;for(const e of PRIM.edges){if(v[e[0]]!==v[e[1]]&&e[2]<bw){bw=e[2];bi=e[0];bj=e[1];}}if(bi<0)break;v[bi]=v[bj]=true;cost+=bw;used++;}PRIM.mst=cost;PRIM.vis=v;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('Prim 算法：每次加入离生成树最近的点',W/2,20,'#74b9ff',12);
 const pos=[[W*0.2,H*0.4],[W*0.4,H*0.3],[W*0.5,H*0.6],[W*0.7,H*0.35],[W*0.8,H*0.6],[W*0.6,H*0.25]];
 for(const e of PRIM.edges){ctx.strokeStyle='#243a5e';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(pos[e[0]][0],pos[e[0]][1]);ctx.lineTo(pos[e[1]][0],pos[e[1]][1]);ctx.stroke();}
 let v=[true].concat(new Array(5).fill(false));let used=0;const steps=Math.floor(PRIM.t/1.5);for(let s=0;s<steps&&used<PRIM.n-1;s++){let bi=-1,bj=-1,bw=1e9;for(const e of PRIM.edges){if(v[e[0]]!==v[e[1]]&&e[2]<bw){bw=e[2];bi=e[0];bj=e[1];}}if(bi<0)break;v[bi]=v[bj]=true;used++;ctx.strokeStyle='#34d399';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(pos[bi][0],pos[bi][1]);ctx.lineTo(pos[bj][0],pos[bj][1]);ctx.stroke();}
 for(let i=0;i<PRIM.n;i++){ctx.fillStyle=PRIM.vis[i]?'#34d399':'#1e3a5f';ctx.beginPath();ctx.arc(pos[i][0],pos[i][1],16,0,7);ctx.fill();ctx.strokeStyle='#3b82f6';ctx.stroke();drawText('v'+i,pos[i][0],pos[i][1],'#fbf4d0',10);}
 drawText('当前 MST 权值和 = '+PRIM.mst,W/2,H-22,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
