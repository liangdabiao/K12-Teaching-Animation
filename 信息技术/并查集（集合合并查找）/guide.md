# 并查集 · 合并集合 / 路径压缩

## 1. 需求
动画展示并查集的初始化、逐步 union 合并集合，以及根节点代表的集合结构。

## 2. 专业思考
并查集用森林表示集合：每个节点 parent 指向父，根为自身。动画随时间依次执行 5 次 union，绿色节点为各集合根，合并后同集合节点最终连到同一根。强调两大优化：按秩（小树挂大树）与路径压缩（find 时扁平化），使均摊接近 O(1)。应用：Kruskal 判环、连通分量。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>并查集 · 合并集合 / 路径压缩</title>
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
  <span class="title">并查集 · 合并集合 / 路径压缩</span>
  <span class="subtitle">Union-Find</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>操作</h4><div class="v">find / union</div></div><div class="card s3"><div class="num">2</div><h4>优化</h4><div class="v">按秩合并</div></div><div class="card s4"><div class="num">3</div><h4>优化</h4><div class="v">路径压缩</div></div><div class="card "><div class="num">4</div><h4>应用</h4><div class="v">连通分量/Kruskal</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">并查集 · 合并集合 / 路径压缩</span></h2>
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
  <span id="status" class="status">点击播放观察合并过程</span>
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
const STEPS=[{"tag": "基础", "name": "并查集用途", "body": "<strong>并查集（Union-Find）</strong>维护若干<strong>不相交集合</strong>，支持：<strong>find</strong>（查根/代表）与 <strong>union</strong>（合并两集合）。", "points": {"title": "操作", "items": ["<strong>find(x)</strong>：找代表", "<strong>union(a,b)</strong>：合并", "<strong>动态</strong>：边加边查", "<strong>用途</strong>：连通性"]}, "code": "find(x): 沿 parent 找根\nunion(a,b): 两树合并"}, {"tag": "合并", "name": "合并集合", "body": "union 把两棵树合并：让一棵树的根指向另一棵树的根。为避免退化，常配合<strong>按秩/大小合并</strong>。", "points": {"title": "合并", "items": ["<strong>找两代表</strong>", "<strong>小树挂大树</strong>", "<strong>按秩</strong>：降高度", "<strong>初态</strong>：各自独立"]}}, {"tag": "压缩", "name": "路径压缩", "body": "find 时把路径上所有节点<strong>直接指向根</strong>，称路径压缩，使后续查询接近 O(1)（均摊）。", "points": {"title": "压缩", "items": ["<strong>递归</strong>：parent=find(parent)", "<strong>扁平化</strong>树", "<strong>均摊</strong>：≈O(1)", "<strong>配合</strong>：按秩更佳"]}, "code": "find(x):\n  if parent[x]!=x:\n    parent[x]=find(parent[x])\n  return parent[x]"}, {"tag": "应用", "name": "应用", "body": "并查集用于<strong>连通分量计数、Kruskal 最小生成树、社交网络圈子</strong>等需要动态连通性判断的场景。", "points": {"title": "实例", "items": ["<strong>Kruskal</strong>：判环", "<strong>连通块</strong>计数", "<strong>朋友圈</strong>", "<strong>迷宫</strong>连通"]}}];
let stepIdx=0;
const UF={t:0,parent:[],unions:[[0,1],[1,2],[3,4],[4,5],[5,6]]};
function applyUnions(k){UF.parent=[0,1,2,3,4,5,6];for(let s=0;s<k;s++){const a=UF.unions[s][0],b=UF.unions[s][1];let ra=a,rb=b;while(UF.parent[ra]!==ra)ra=UF.parent[ra];while(UF.parent[rb]!==rb)rb=UF.parent[rb];if(ra!==rb)UF.parent[rb]=ra;}}
function sceneInit(){applyUnions(0);UF.t=0;}
function sceneReset(){applyUnions(0);UF.t=0;}
function sceneUpdate(dt){UF.t+=dt*speed;if(UF.t>5)UF.t=0;applyUnions(Math.min(UF.unions.length,Math.floor(UF.t)));}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('并查集 Union-Find：合并集合 / 查找根（绿色=根）',W/2,22,'#74b9ff',13);
 const pos=[];for(let i=0;i<7;i++)pos[i]={x:W*(i+0.5)/7,y:H/2};
 for(let i=0;i<7;i++){if(UF.parent[i]!==i){const p=pos[i],pp=pos[UF.parent[i]];ctx.strokeStyle='#74b9ff';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(pp.x,pp.y);ctx.stroke();drawText(String(UF.parent[i]),(p.x+pp.x)/2,(p.y+pp.y)/2-6,'#9ab0d0',10);}}
 for(let i=0;i<7;i++){const p=pos[i];ctx.fillStyle=UF.parent[i]===i?'#34d399':'#1e3a5f';ctx.beginPath();ctx.arc(p.x,p.y,18,0,7);ctx.fill();ctx.strokeStyle='#3b82f6';ctx.lineWidth=2;ctx.stroke();drawText('n'+i,p.x,p.y,'#fbbf24',11);}
 drawText('随时间依次 union：根(绿)代表一个集合；同一集合节点最终连到同根',W/2,H-22,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
