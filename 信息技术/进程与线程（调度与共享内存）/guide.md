# 进程与线程 · 调度与共享

## 1. 需求
动画展示进程包含多个线程、线程共享进程内存、调度器时间片轮转分配 CPU。

## 2. 专业思考
进程/线程是操作系统基础。动画用外框表示进程（独立内存），内部多个线程块，下方“共享内存”条，CPU 时间片轮流点亮当前运行线程。强调：进程是资源容器、线程是执行流；线程共享内存故通信快但需同步（锁/信号量）防竞态；单核并发靠切换、多核可真并行。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>进程与线程 · 调度与共享</title>
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
  <span class="title">进程与线程 · 调度与共享</span>
  <span class="subtitle">时间片轮转 · 共享内存</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>进程</h4><div class="v">资源分配基本单位</div></div><div class="card s3"><div class="num">2</div><h4>线程</h4><div class="v">CPU调度基本单位</div></div><div class="card s4"><div class="num">3</div><h4>共享</h4><div class="v">同进程线程共享内存</div></div><div class="card "><div class="num">4</div><h4>调度</h4><div class="v">时间片轮转</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">进程与线程 · 调度与共享</span></h2>
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
  <span id="status" class="status">点击播放观察调度</span>
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
const STEPS=[{"tag": "基础", "name": "进程 vs 线程", "body": "<strong>进程</strong>是资源分配的基本单位，拥有独立内存空间；<strong>线程</strong>是 CPU 调度的基本单位，一个进程可含多个线程。", "points": {"title": "区别", "items": ["<strong>进程</strong>：独立内存", "<strong>线程</strong>：轻量、共享", "<strong>开销</strong>：进程大", "<strong>通信</strong>：线程易"]}, "code": "进程 = 资源容器\n线程 = 执行流"}, {"tag": "共享", "name": "共享内存", "body": "同一进程的<strong>线程共享</strong>其内存与资源（代码、数据、文件），因此线程间通信高效，但需同步避免竞态。", "points": {"title": "共享", "items": ["<strong>共享</strong>：内存/文件", "<strong>私有</strong>：栈/寄存器", "<strong>高效</strong>：免拷贝", "<strong>风险</strong>：竞态"]}}, {"tag": "调度", "name": "CPU 调度", "body": "操作系统用<strong>时间片轮转</strong>等策略，让多个线程轮流占用 CPU，造成“并发”执行的假象（单核）或真并行（多核）。", "points": {"title": "调度", "items": ["<strong>时间片</strong>：轮流", "<strong>并发</strong>：单核交替", "<strong>并行</strong>：多核同时", "<strong>切换</strong>：上下文"]}}, {"tag": "应用", "name": "应用", "body": "多线程用于<strong>并发服务器、GUI 不卡顿、并行计算</strong>；需注意锁与同步（如互斥量）防止数据错乱。", "points": {"title": "场景", "items": ["<strong>服务器</strong>：并发处理", "<strong>GUI</strong>：后台任务", "<strong>并行</strong>：多核计算", "<strong>同步</strong>：锁"]}}];
let stepIdx=0;
const PT={t:0,threads:3};
function sceneInit(){PT.t=0;}
function sceneReset(){PT.t=0;}
function sceneUpdate(dt){PT.t+=dt*speed;}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('进程与线程：一进程含多线程，线程共享内存，调度器分时占用 CPU',W/2,20,'#74b9ff',12);
 ctx.strokeStyle='#34d399';ctx.lineWidth=2;ctx.strokeRect(40,56,W-80,H-160);
 drawText('进程 Process（独立内存空间）',W/2,74,'#34d399',12);
 ctx.fillStyle='#1e3a5f';ctx.strokeStyle='#74b9ff';ctx.fillRect(W/2-120,H-130,240,30);ctx.strokeRect(W/2-120,H-130,240,30);drawText('共享内存 / 资源',W/2,H-115,'#fbbf24',12);
 const cur=Math.floor(PT.t*1.2)%PT.threads;
 for(let i=0;i<PT.threads;i++){const x=80+i*(W-160)/PT.threads,y=104+i*44;ctx.fillStyle=i===cur?'#34d399':'#1e3a5f';ctx.strokeStyle='#3b82f6';ctx.fillRect(x,y,130,30);ctx.strokeRect(x,y,130,30);drawText('线程 T'+(i+1)+(i===cur?' ◀运行中':''),x+65,y+15,'#fbbf24',11);
  ctx.strokeStyle='#243a5e';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x+65,y+30);ctx.lineTo(W/2,H-130);ctx.stroke();}
 ctx.fillStyle='#fbbf24';roundRect(W/2-60,H-70,120,30,6);ctx.fill();drawText('CPU 时间片轮转',W/2,H-55,'#06281c',11);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
