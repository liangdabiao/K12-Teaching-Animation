# 比热容 · 相同加热下升温快慢

## 1. 需求
用动画对比水和油在相同加热功率下的升温快慢，直观说明比热容概念与公式 c=Q/(m·ΔT)。

## 2. 专业思考
比热容是热学核心概念。设计要点：固定加热功率 P 与质量 m，令 ΔT=Q/(mc)=P·t/(m·c)，则温度随时间线性上升、斜率反比于 c。水的 c≈4.2 J/(g·℃)，食用油 c≈2.0，故相同条件下油升温约为水的 2 倍。动画用两个烧杯 + 温度计柱 + 实时温度数值，并标注公式，避免抽象。可延伸：沿海地区昼夜温差小、汽车水箱用水作冷却液，都源于水的大比热容。

## 3. HTML_CODE
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>比热容 · 相同加热下升温快慢</title>
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
  <span class="title">比热容 · 相同加热下升温快慢</span>
  <span class="subtitle">c = Q /(m·ΔT)</span>
</header>
<div class="cards"><div class="card s2"><div class="num">1</div><h4>概念</h4><div class="v">比热容 c 是物质升温 1℃ 所需热量</div></div><div class="card s3"><div class="num">2</div><h4>公式</h4><div class="v">c = Q /(m·ΔT)</div></div><div class="card s4"><div class="num">3</div><h4>对比</h4><div class="v">同 Q、同 m：c 大 → 升温慢</div></div><div class="card "><div class="num">4</div><h4>单位</h4><div class="v">J/(kg·℃)</div></div></div>
<main>
  <div class="stage"><canvas id="cv"></canvas></div>
  <aside class="panel">
    <h2><span class="badge" id="stepBadge">基础</span><span id="stepTitle">比热容 · 相同加热下升温快慢</span></h2>
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
  <span id="status" class="status">点击播放观察水与油升温差异</span>
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
const STEPS=[{"tag": "基础", "name": "什么是比热容", "body": "<strong>比热容 c</strong> 表示单位质量的物质升高 1℃ 所吸收的热量，单位 J/(kg·℃)。它反映物质“怕冷怕热”的程度。", "points": {"title": "要点", "items": ["<strong>定义</strong>：1kg 物质升温 1℃ 吸热", "<strong>单位</strong>：J/(kg·℃)", "<strong>水</strong>：c≈4.2×10³，常见最大", "<strong>沙/金属</strong>：c 小，易升易降"]}, "code": "c = Q / (m · ΔT)\n// 水的 c 很大 → 升温慢、降温也慢"}, {"tag": "公式", "name": "升温公式", "body": "吸收相同热量 Q、质量相同 m 时，<strong>ΔT = Q/(m·c)</strong>。因此 <strong>c 越大，升温越慢</strong>。", "points": {"title": "推导", "items": ["<strong>Q</strong> 相同、<strong>m</strong> 相同", "<strong>ΔT</strong> 与 <strong>c</strong> 成反比", "<strong>水</strong> c 大 → ΔT 小", "<strong>油</strong> c 小 → ΔT 大"]}}, {"tag": "演示", "name": "水 vs 油", "body": "用<strong>相同功率</strong>给等质量的水和油加热。观察：油升温明显更快，水升温更慢——正是比热容不同。", "points": {"title": "观察", "items": ["<strong>黄色</strong>：油（c≈2.0）", "<strong>蓝色</strong>：水（c≈4.2）", "相同时间油温度更高", "海边昼夜温差小因水 c 大"]}}, {"tag": "应用", "name": "生活与工程", "body": "水的比热容大，常用作<strong>冷却剂、取暖介质</strong>；沙漠昼夜温差大因砂石 c 小；海陆风也源于此。", "points": {"title": "实例", "items": ["<strong>汽车水箱</strong>：水循环散热", "<strong>暖气</strong>：热水储热", "<strong>气候</strong>：沿海温和", "<strong>农业</strong>：夜间灌水防霜"]}}];
let stepIdx=0;
const BC={t:0,m:1,P:60,cW:4.2,cO:2.0};
function sceneInit(){BC.t=0;}
function sceneReset(){BC.t=0;}
function sceneUpdate(dt){BC.t+=dt*speed;if(BC.t>14)BC.t=0;}
function tempW(){return Math.min(95,BC.P*BC.t/(BC.m*BC.cW));}
function tempO(){return Math.min(95,BC.P*BC.t/(BC.m*BC.cO));}
function sceneDraw(){const W=cv.width,H=cv.height;ctx.clearRect(0,0,W,H);
 drawText('比热容 c：相同质量、相同加热功率，c 越大升温越慢',W/2,26,'#74b9ff',14);
 const bx1=W*0.30, bx2=W*0.70, by=H-90, bh=200, bw=120;
 ctx.fillStyle='#11203a';ctx.strokeStyle='#3b82f6';ctx.lineWidth=2;roundRect(bx1-bw/2,by-bh,bw,bh,8);ctx.fill();ctx.stroke();
 const fW=tempW()/95;ctx.fillStyle='#38bdf8';roundRect(bx1-bw/2+4,by-4-(bh-8)*fW,bw-8,(bh-8)*fW,6);ctx.fill();
 drawText('水 c=4.2',bx1,by-bh-26,'#9ab0d0',13);drawText(tempW().toFixed(0)+'°C',bx1,by+24,'#74b9ff',15);
 ctx.fillStyle='#11203a';ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;roundRect(bx2-bw/2,by-bh,bw,bh,8);ctx.fill();ctx.stroke();
 const fO=tempO()/95;ctx.fillStyle='#f59e0b';roundRect(bx2-bw/2+4,by-4-(bh-8)*fO,bw-8,(bh-8)*fO,6);ctx.fill();
 drawText('油 c=2.0',bx2,by-bh-26,'#9ab0d0',13);drawText(tempO().toFixed(0)+'°C',bx2,by+24,'#fbbf24',15);
 drawText('🔥 相同加热功率 P',W/2,by+50,'#f87171',12);
 drawText('公式 c = Q/(m·ΔT) → 同 Q、同 m 时，c↑ 则 ΔT↓',W/2,H-18,'#9ab0d0',12);}
sceneInit(); buildStepbar(); loadStep(); requestAnimationFrame(loop);
</script>
</body>
</html>
```
