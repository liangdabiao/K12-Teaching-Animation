# 变压器 · 互感变压

## 1. 需求
动画展示变压器结构、互感原理及电压与匝数关系 U₂/U₁=N₂/N₁。

## 2. 专业思考
变压器是交流电专属设备。动画左侧少匝原线圈接 220V，右侧多匝副线圈感应出更高电压，中间铁芯导磁。强调：只用于交流（变化磁通才感应）、U₂/U₁=N₂/N₁、电流与匝数反比。应用：输电升压降损、配电降压、充电器。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>变压器 · 互感变压</title>
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
  <span class="title">变压器 · 互感变压</span>
  <span class="subtitle">U₂/U₁ = N₂/N₁</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>结构</h4><div class="v">铁芯+原副线圈</div></div><div class="card s3"><div class="num">2</div><h4>原理</h4><div class="v">互感生电动势</div></div><div class="card s4"><div class="num">3</div><h4>匝比</h4><div class="v">U₂/U₁=N₂/N₁</div></div><div class="card "><div class="num">4</div><h4>类型</h4><div class="v">升压/降压</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">变压器 · 互感变压</span></h2>
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
  <span id="status" class="status">点击播放观察磁通与感应</span>
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
const STEPS=[{"tag": "基础", "name": "变压器结构", "body": "变压器由<strong>闭合铁芯</strong>与绕在其上的<strong>原线圈(初级)、副线圈(次级)</strong>组成，只能用于交流电。", "points": {"title": "组成", "items": ["<strong>铁芯</strong>：导磁", "<strong>原线圈</strong>：接电源", "<strong>副线圈</strong>：接负载", "<strong>交流</strong>：才可变压"]}}, {"tag": "原理", "name": "互感原理", "body": "原线圈交变电流产生<strong>变化磁通</strong>，经铁芯耦合到副线圈，感应出电动势——这就是互感。", "points": {"title": "过程", "items": ["<strong>电→磁</strong>：原线圈", "<strong>磁→电</strong>：副线圈", "<strong>铁芯</strong>：导磁路", "<strong>变化</strong>：关键"]}, "code": "Φ 变化 → 副线圈感应 E"}, {"tag": "匝比", "name": "电压关系", "body": "忽略损耗时，<strong>U₂ / U₁ = N₂ / N₁</strong>：匝数多的线圈电压高。", "points": {"title": "公式", "items": ["<strong>U₂/U₁</strong>=N₂/N₁", "<strong>升压</strong>：N₂>N₁", "<strong>降压</strong>：N₂<N₁", "<strong>电流反</strong>：I₁N₁=I₂N₂"]}, "code": "U2/U1 = N2/N1"}, {"tag": "应用", "name": "应用", "body": "输电先<strong>升压</strong>减小电流降损，入户前<strong>降压</strong>到 220V；手机充电器内含小型变压器。", "points": {"title": "用途", "items": ["<strong>远距离</strong>：升压", "<strong>配电</strong>：降压", "<strong>充电器</strong>：小型", "<strong>隔离</strong>：安全"]}}];
let stepIdx=0;
const TRA={t:0};
function sceneInit(){TRA.t=0;}
function sceneReset(){TRA.t=0;}
function sceneUpdate(dt){TRA.t+=dt*speed;}
function coil(x,y,n,color,amp,ph){ctx.strokeStyle=color;ctx.lineWidth=3;for(let i=0;i<n;i++){const yy=y-30+i*6;ctx.beginPath();ctx.moveTo(x,yy+Math.sin(ph+i*0.3)*amp);ctx.lineTo(x+14,yy+Math.sin(ph+i*0.3)*amp);ctx.stroke();}}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('变压器：U₂/U₁ = N₂/N₁（互感变压）',W/2,22,'#74b9ff',14);
 const cy=H/2;
 coil(W*0.22,cy,8,'#fbbf24',6,TRA.t*4);drawText('N₁(少) 初级',W*0.22,cy-50,'#fbbf24',12);
 drawText('U₁=220V',W*0.22,cy+60,'#9ab0d0',12);
 ctx.fillStyle='#243a5e';ctx.fillRect(W*0.42,cy-50,16,100);ctx.fillRect(W*0.55,cy-50,16,100);
 coil(W*0.78,cy,14,'#34d399',6,TRA.t*4);drawText('N₂(多) 次级',W*0.78,cy-50,'#34d399',12);
 drawText('U₂=220×14/8≈385V',W*0.78,cy+60,'#9ab0d0',12);
 drawText('交流电→铁芯磁通变化→次级感应电动势',W/2,H-24,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
