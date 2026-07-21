#!/usr/bin/env python3
"""批量增强简陋的模板动画文件，添加更丰富的Canvas动画逻辑"""
import os, re

BASE = r'd:\K12-Teaching-Animation'

# 每个文件的增强版JS代码
ENHANCED = {}

# ===== 物理 =====
ENHANCED['分子运动论'] = '''
const M={t:0,molecules:[],temp:300,brownianTrail:[],diffusionDrops:[]};
function sceneInit(){sceneReset();for(let i=0;i<60;i++)M.molecules.push({x:Math.random(),y:Math.random(),vx:(Math.random()*2-1)*2,vy:(Math.random()*2-1)*2,r:3+Math.random()*2});}
function sceneReset(){M.t=0;M.brownianTrail=[];M.diffusionDrops=[];for(let i=0;i<5;i++)M.diffusionDrops.push({x:0.8,y:0.3+Math.random()*0.1,spread:0});}
function sceneUpdate(dt){
  M.t+=dt;
  const speed=Math.sqrt(M.temp/300);
  M.molecules.forEach(p=>{
    p.x+=p.vx*dt*0.3*speed;p.y+=p.vy*dt*0.3*speed;
    if(p.x<0||p.x>1){p.vx*=-1;p.x=Math.max(0,Math.min(1,p.x));}
    if(p.y<0||p.y>1){p.vy*=-1;p.y=Math.max(0,Math.min(1,p.y));}
    // 分子间碰撞
    M.molecules.forEach(q=>{if(p!==q){const dx=p.x-q.x,dy=p.y-q.y,d=Math.sqrt(dx*dx+dy*dy);if(d<0.03){p.vx+=dx*2*dt;p.vy+=dy*2*dt;}}});
  });
  // 布朗运动粒子(大颗粒)
  if(M.brownianTrail.length===0)M.brownianTrail.push({x:0.3,y:0.5});
  const bp=M.brownianTrail[M.brownianTrail.length-1];
  bp.x+=((Math.random()-0.5)*0.01);bp.y+=((Math.random()-0.5)*0.01);
  bp.x=Math.max(0.05,Math.min(0.45,bp.x));bp.y=Math.max(0.1,Math.min(0.9,bp.y));
  if(M.brownianTrail.length>200)M.brownianTrail.shift();
  // 扩散
  M.diffusionDrops.forEach(d=>{d.spread=Math.min(1,d.spread+dt*0.1);});
}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H=cv.height;
  // 容器
  ctx.strokeStyle='#7f93b5';ctx.lineWidth=3;ctx.strokeRect(30,60,W*0.5-20,H-100);
  ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('气体分子热运动',W*0.25,55);
  // 分子
  M.molecules.forEach(p=>{
    const x=30+(W*0.5-50)*p.x,y=60+(H-110)*p.y;
    const speed=Math.sqrt(p.vx*p.vx+p.vy*p.vy);
    ctx.fillStyle=speed>2?'#f87171':'#7dd3fc';
    ctx.beginPath();ctx.arc(x,y,p.r,0,Math.PI*2);ctx.fill();
    // 速度矢量
    ctx.strokeStyle='rgba(255,255,255,0.2)';ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+p.vx*5,y+p.vy*5);ctx.stroke();
  });
  // 布朗运动区域
  ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.strokeRect(W*0.55,60,W*0.2,H-100);
  ctx.fillStyle='#aaa';ctx.fillText('布朗运动',W*0.65,55);
  // 布朗粒子
  if(M.brownianTrail.length>1){
    ctx.strokeStyle='#fbbf24';ctx.lineWidth=1.5;ctx.beginPath();
    M.brownianTrail.forEach((p,i)=>{const x=W*0.55+W*0.2*p.x,y=60+(H-100)*p.y;i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);});
    ctx.stroke();
    const last=M.brownianTrail[M.brownianTrail.length-1];
    ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(W*0.55+W*0.2*last.x,60+(H-100)*last.y,6,0,Math.PI*2);ctx.fill();
  }
  // 扩散区域
  ctx.strokeStyle='#7f93b5';ctx.strokeRect(W*0.8,60,W*0.18,H-100);
  ctx.fillStyle='#aaa';ctx.fillText('扩散',W*0.89,55);
  M.diffusionDrops.forEach(d=>{
    const cx2=W*0.89,cy2=60+(H-100)*d.y;
    const r=d.spread*40;
    const grad=ctx.createRadialGradient(cx2,cy2,0,cx2,cy2,r);
    grad.addColorStop(0,'rgba(59,130,246,0.8)');grad.addColorStop(1,'rgba(59,130,246,0)');
    ctx.fillStyle=grad;ctx.fillRect(W*0.8,60,W*0.18,H-100);
  });
  // 温度控制
  ctx.fillStyle='#cdd7ea';ctx.font='12px sans-serif';ctx.textAlign='left';
  ctx.fillText('温度: '+Math.round(M.temp)+'K',30,H-15);
  ctx.fillText('温度越高，分子运动越剧烈',30,H-35);
  statusEl.textContent='分子动理论：分子永不停息做无规则运动，温度是分子平均动能的标志';
}
'''

ENHANCED['减数分裂'] = '''
const M={t:0,step:0,chromosomes:[],cellY:0};
const STAGES=['间期：DNA复制','减Ⅰ前期：联会→四分体→交叉互换','减Ⅰ中期：同源排列赤道板','减Ⅰ后期：同源分离','减Ⅱ后期：姐妹单体分离','形成4个单倍体细胞'];
function sceneInit(){sceneReset();initChromosomes();}
function sceneReset(){M.t=0;M.step=0;initChromosomes();}
function sceneStep(d){M.step=Math.max(0,Math.min(5,M.step+d));M.t=0;}
function initChromosomes(){
  M.chromosomes=[
    {type:'A',x:0,col1:'#f87171',col2:'#34d399',separated:false},
    {type:'B',x:1,col1:'#60a5fa',col2:'#fbbf24',separated:false}
  ];
}
function sceneUpdate(dt){M.t+=dt;}
function drawChromosomePair(cx,cy,sep,phase){
  const armLen=25;
  // 着丝粒
  ctx.fillStyle='#cdd7ea';ctx.beginPath();ctx.arc(cx,cy,4,0,Math.PI*2);ctx.fill();
  if(sep<0.5){
    // 未分离：两条姐妹染色单体
    const gap=sep*20;
    ctx.strokeStyle='#f87171';ctx.lineWidth=3;
    ctx.beginPath();ctx.moveTo(cx-gap,cy-armLen);ctx.lineTo(cx-gap,cy);ctx.lineTo(cx-gap,cy+armLen);ctx.stroke();
    ctx.strokeStyle='#34d399';
    ctx.beginPath();ctx.moveTo(cx+gap,cy-armLen);ctx.lineTo(cx+gap,cy);ctx.lineTo(cx+gap,cy+armLen);ctx.stroke();
  }else{
    // 已分离
    const d=(sep-0.5)*2*40;
    ctx.strokeStyle='#f87171';ctx.lineWidth=3;
    ctx.beginPath();ctx.moveTo(cx-d,cy-armLen);ctx.lineTo(cx-d,cy);ctx.lineTo(cx-d,cy+armLen);ctx.stroke();
    ctx.strokeStyle='#34d399';
    ctx.beginPath();ctx.moveTo(cx+d,cy-armLen);ctx.lineTo(cx+d,cy);ctx.lineTo(cx+d,cy+armLen);ctx.stroke();
  }
}
function drawCrossOver(cx,cy,progress){
  // 交叉互换
  ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;ctx.setLineDash([3,3]);
  ctx.beginPath();ctx.moveTo(cx-15,cy-10);ctx.lineTo(cx+15,cy+10);ctx.stroke();
  ctx.beginPath();ctx.moveTo(cx+15,cy-10);ctx.lineTo(cx-15,cy+10);ctx.stroke();
  ctx.setLineDash([]);
  if(progress>0.5){
    ctx.fillStyle='#fbbf24';ctx.font='10px sans-serif';ctx.textAlign='center';
    ctx.fillText('交叉互换',cx,cy-30);
  }
}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H=cv.height,cx=W/2,cy=H/2;
  // 标题
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
  ctx.fillText('减数分裂 — '+STAGES[M.step],cx,30);
  // 步骤指示
  for(let i=0;i<6;i++){ctx.fillStyle=i<=M.step?'#00b894':'rgba(255,255,255,0.2)';ctx.fillRect(cx-150+i*52,42,48,4);}
  const p=Math.min(1,M.t*0.4);
  switch(M.step){
    case 0:{ // 间期复制
      ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(cx,cy,80,0,Math.PI*2);ctx.stroke();
      ctx.fillStyle='rgba(255,255,255,0.05)';ctx.fill();
      // 复制前→复制后
      if(p<0.5){
        drawChromosomePair(cx-30,cy,0,0);drawChromosomePair(cx+30,cy,0,0);
        ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('2n=4 (复制前)',cx,cy+100);
      }else{
        drawChromosomePair(cx-30,cy,0,0);drawChromosomePair(cx+30,cy,0,0);
        ctx.fillStyle='#00b894';ctx.font='12px sans-serif';ctx.fillText('DNA复制完成，每条染色体含2条姐妹单体',cx,cy+100);
      }
      break;
    }
    case 1:{ // 联会→四分体→交叉互换
      ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(cx,cy,80,0,Math.PI*2);ctx.stroke();
      // 同源染色体配对
      const close=p*15;
      drawChromosomePair(cx-close,cy-20,0,0);drawChromosomePair(cx+close,cy-20,0,0);
      drawChromosomePair(cx-close,cy+20,0,0);drawChromosomePair(cx+close,cy+20,0,0);
      if(p>0.5)drawCrossOver(cx,cy-20,p);
      ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('同源染色体联会，形成四分体',cx,cy+100);
      break;
    }
    case 2:{ // 中期I
      ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(cx,cy,80,0,Math.PI*2);ctx.stroke();
      // 赤道板
      ctx.strokeStyle='#fbbf24';ctx.setLineDash([4,4]);ctx.beginPath();ctx.moveTo(cx-60,cy);ctx.lineTo(cx+60,cy);ctx.stroke();ctx.setLineDash([]);
      drawChromosomePair(cx-25,cy,0,0);drawChromosomePair(cx+25,cy,0,0);
      ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('同源染色体排列在赤道板上',cx,cy+100);
      break;
    }
    case 3:{ // 后期I：同源分离
      ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(cx,cy,80,0,Math.PI*2);ctx.stroke();
      const sep=p*50;
      drawChromosomePair(cx-30-sep,cy-20,0,0);drawChromosomePair(cx-30-sep,cy+20,0,0);
      drawChromosomePair(cx+30+sep,cy-20,0,0);drawChromosomePair(cx+30+sep,cy+20,0,0);
      ctx.fillStyle='#fbbf24';ctx.font='12px sans-serif';ctx.fillText('同源染色体分离→非同源自由组合',cx,cy+100);
      break;
    }
    case 4:{ // 减II
      // 两个细胞
      const c1x=cx-100,c2x=cx+100;
      ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;
      ctx.beginPath();ctx.arc(c1x,cy,55,0,Math.PI*2);ctx.stroke();
      ctx.beginPath();ctx.arc(c2x,cy,55,0,Math.PI*2);ctx.stroke();
      const sep2=p*20;
      drawChromosomePair(c1x-sep2,cy-10,0.5+p*0.5,0);drawChromosomePair(c1x+sep2,cy+10,0.5+p*0.5,0);
      drawChromosomePair(c2x-sep2,cy-10,0.5+p*0.5,0);drawChromosomePair(c2x+sep2,cy+10,0.5+p*0.5,0);
      ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('减Ⅱ：姐妹染色单体分离（类似有丝分裂）',cx,cy+100);
      break;
    }
    case 5:{ // 完成
      const positions=[[cx-150,cy-40],[cx-50,cy-40],[cx+50,cy-40],[cx+150,cy-40]];
      positions.forEach((pos,i)=>{
        ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(pos[0],pos[1],35,0,Math.PI*2);ctx.stroke();
        drawChromosomePair(pos[0],pos[1],1,0);
        ctx.fillStyle='#00b894';ctx.font='10px sans-serif';ctx.fillText('n=2',pos[0],pos[1]+50);
      });
      ctx.fillStyle='#00b894';ctx.font='bold 13px sans-serif';ctx.fillText('✓ 形成4个单倍体精细胞，染色体数目减半',cx,cy+60);
      break;
    }
  }
  statusEl.textContent='减数分裂：染色体复制一次，细胞分裂两次，子细胞染色体数目减半';
}
'''

ENHANCED['生态系统碳循环'] = '''
const C={t:0,co2Particles:[],phase:0};
function sceneInit(){sceneReset();for(let i=0;i<20;i++)C.co2Particles.push({x:Math.random(),y:Math.random()*0.3,vx:(Math.random()-0.5)*0.1,vy:(Math.random()-0.5)*0.05});}
function sceneReset(){C.t=0;C.phase=0;C.co2Particles=[];for(let i=0;i<20;i++)C.co2Particles.push({x:Math.random(),y:Math.random()*0.3,vx:(Math.random()-0.5)*0.1,vy:(Math.random()-0.5)*0.05});}
function sceneUpdate(dt){C.t+=dt;C.phase+=dt*0.2;
  C.co2Particles.forEach(p=>{p.x+=p.vx*dt;p.y+=p.vy*dt;if(p.x<0||p.x>1)p.vx*=-1;if(p.y<0||p.y>0.35)p.vy*=-1;});
}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H=cv.height;
  // 大气层
  ctx.fillStyle='rgba(99,110,114,0.1)';ctx.fillRect(0,0,W,H*0.35);
  ctx.fillStyle='#aaa';ctx.font='13px sans-serif';ctx.textAlign='center';ctx.fillText('大气CO₂',W/2,25);
  // CO2粒子
  C.co2Particles.forEach(p=>{
    ctx.fillStyle='rgba(99,110,114,0.7)';ctx.beginPath();ctx.arc(p.x*W,p.y*H,4,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#fff';ctx.font='6px sans-serif';ctx.fillText('C',p.x*W,p.y*H+2);
  });
  // 地面
  ctx.fillStyle='rgba(0,184,148,0.15)';ctx.fillRect(0,H*0.7,W,H*0.3);
  ctx.strokeStyle='#00b894';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(0,H*0.7);ctx.lineTo(W,H*0.7);ctx.stroke();
  // 植物(光合作用)
  const treeX=W*0.2,treeY=H*0.7;
  ctx.fillStyle='#2d3436';ctx.fillRect(treeX-5,treeY-60,10,60);
  ctx.fillStyle='#00b894';ctx.beginPath();ctx.arc(treeX,treeY-80,30,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='11px sans-serif';ctx.fillText('植物',treeX,treeY-75);
  // 光合箭头
  const photoP=Math.sin(C.phase)*0.5+0.5;
  ctx.strokeStyle='#00b894';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(treeX,treeY-110);ctx.lineTo(treeX,treeY-90);ctx.stroke();
  ctx.fillStyle='#00b894';ctx.font='10px sans-serif';ctx.fillText('CO₂↓ 光合',treeX+40,treeY-100);
  // 动物
  const animX=W*0.5,animY=H*0.8;
  ctx.fillStyle='#e17055';ctx.beginPath();ctx.ellipse(animX,animY,20,12,0,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='10px sans-serif';ctx.fillText('动物',animX,animY+4);
  // 食物链箭头
  ctx.strokeStyle='#fbbf24';ctx.lineWidth=1.5;ctx.setLineDash([4,4]);
  ctx.beginPath();ctx.moveTo(treeX+30,treeY-60);ctx.lineTo(animX-25,animY);ctx.stroke();ctx.setLineDash([]);
  ctx.fillStyle='#fbbf24';ctx.font='9px sans-serif';ctx.fillText('有机物',treeX+60,treeY-40);
  // 呼吸作用箭头
  ctx.strokeStyle='#e17055';ctx.lineWidth=1.5;
  ctx.beginPath();ctx.moveTo(animX,animY-15);ctx.quadraticCurveTo(animX,H*0.4,treeX+50,H*0.15);ctx.stroke();
  ctx.fillStyle='#e17055';ctx.font='10px sans-serif';ctx.fillText('呼吸→CO₂↑',animX+30,H*0.45);
  // 微生物分解
  const micX=W*0.75,micY=H*0.85;
  ctx.fillStyle='#636e72';for(let i=0;i<5;i++){ctx.beginPath();ctx.arc(micX+i*8-16,micY+Math.sin(C.t+i)*3,3,0,Math.PI*2);ctx.fill();}
  ctx.fillStyle='#aaa';ctx.font='10px sans-serif';ctx.fillText('分解者',micX,micY+18);
  ctx.strokeStyle='#636e72';ctx.beginPath();ctx.moveTo(micX,micY-10);ctx.quadraticCurveTo(micX,H*0.3,W*0.6,H*0.1);ctx.stroke();
  ctx.fillStyle='#636e72';ctx.fillText('分解→CO₂↑',micX+40,H*0.4);
  // 人类活动
  const facX=W*0.9,facY=H*0.65;
  ctx.fillStyle='#2d3436';ctx.fillRect(facX-15,facY-30,30,30);ctx.fillRect(facX+5,facY-50,8,20);
  ctx.fillStyle='#e17055';ctx.font='9px sans-serif';ctx.fillText('工厂',facX,facY+15);
  // 工厂排放
  for(let i=0;i<3;i++){
    const smokeY=facY-50-i*15-Math.sin(C.t*2+i)*5;
    ctx.fillStyle=`rgba(99,110,114,${0.5-i*0.15})`;ctx.beginPath();ctx.arc(facX+8+Math.sin(C.t+i)*5,smokeY,5+i*2,0,Math.PI*2);ctx.fill();
  }
  ctx.fillStyle='#e17055';ctx.font='10px sans-serif';ctx.fillText('化石燃料燃烧→CO₂↑',facX-20,facY-60);
  // 海洋吸收
  ctx.fillStyle='rgba(9,132,227,0.15)';ctx.fillRect(0,H*0.35,W*0.1,H*0.35);
  ctx.fillStyle='#0984e3';ctx.font='10px sans-serif';ctx.textAlign='center';ctx.fillText('海洋',W*0.05,H*0.5);
  ctx.fillText('吸收CO₂',W*0.05,H*0.55);
  // 碳失衡警示
  const imbalance=Math.sin(C.t*0.5)*0.3+0.7;
  ctx.fillStyle=`rgba(225,69,83,${imbalance})`;ctx.font='bold 12px sans-serif';ctx.textAlign='center';
  ctx.fillText('⚠ 人类活动打破碳平衡：大气CO₂浓度持续上升',W/2,H-15);
  statusEl.textContent='碳循环：大气CO₂↔光合作用↔食物链↔呼吸/分解，人类活动导致失衡';
}
'''

ENHANCED['神经调节'] = '''
const N={t:0,signal:0,step:0,ions:[],vesicles:[]};
function sceneInit(){sceneReset();}
function sceneReset(){N.t=0;N.signal=0;N.step=0;N.ions=[];N.vesicles=[];}
function sceneStep(d){N.step=Math.max(0,Math.min(4,N.step+d));N.signal=0;}
function sceneUpdate(dt){
  N.t+=dt;N.signal=Math.min(1,N.signal+dt*0.5);
  // 离子运动
  if(N.step>=1&&Math.random()<0.1){
    N.ions.push({x:0.2+N.step*0.15,y:0.5,vx:0,vy:(Math.random()-0.5)*2,life:2,type:Math.random()>0.5?'Na':'K'});
  }
  N.ions.forEach(i=>{i.x+=i.vx*dt;i.y+=i.vy*dt*0.3;i.life-=dt;});
  N.ions=N.ions.filter(i=>i.life>0);
  // 囊泡
  if(N.step>=3&&Math.random()<0.05){
    N.vesicles.push({x:0.72,y:0.4,vy:0.5,life:2});
  }
  N.vesicles.forEach(v=>{v.y+=v.vy*dt;v.life-=dt;});
  N.vesicles=N.vesicles.filter(v=>v.life>0);
}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H=cv.height;
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
  const names=['① 感受器接受刺激','② 传入神经（电信号传导）','③ 神经中枢（突触传递）','④ 传出神经','⑤ 效应器反应'];
  ctx.fillText(names[N.step],W/2,25);
  for(let i=0;i<5;i++){ctx.fillStyle=i<=N.step?'#00b894':'rgba(255,255,255,0.2)';ctx.fillRect(W/2-120+i*50,35,46,4);}
  // 反射弧路径
  const path=[[W*0.08,H*0.7],[W*0.25,H*0.4],[W*0.5,H*0.5],[W*0.7,H*0.4],[W*0.9,H*0.6]];
  // 画神经纤维
  ctx.strokeStyle='rgba(127,147,181,0.5)';ctx.lineWidth=4;ctx.beginPath();
  path.forEach((p,i)=>i===0?ctx.moveTo(p[0],p[1]):ctx.lineTo(p[0],p[1]));ctx.stroke();
  // 信号传播
  if(N.signal>0){
    const sigX=path[0][0]+(path[path.length-1][0]-path[0][0])*N.signal;
    const sigIdx=Math.min(path.length-2,Math.floor(N.signal*(path.length-1)));
    const localP=(N.signal*(path.length-1))-sigIdx;
    const sx=path[sigIdx][0]+(path[sigIdx+1][0]-path[sigIdx][0])*localP;
    const sy=path[sigIdx][1]+(path[sigIdx+1][1]-path[sigIdx][1])*localP;
    // 动作电位波形
    ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;ctx.beginPath();
    for(let i=-30;i<=30;i++){
      const px=sx+i;const py=sy-20*Math.exp(-i*i/100)*Math.sin(i*0.3+N.t*5);
      i===-30?ctx.moveTo(px,py):ctx.lineTo(px,py);
    }
    ctx.stroke();
    // 信号点
    ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(sx,sy,6,0,Math.PI*2);ctx.fill();
  }
  // 各节点标注
  const labels=['感受器','传入神经','神经中枢','传出神经','效应器'];
  const icons=['👁','→','🧠','→','💪'];
  path.forEach((p,i)=>{
    ctx.fillStyle=i===N.step?'#00b894':'#7f93b5';
    ctx.beginPath();ctx.arc(p[0],p[1],15,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#fff';ctx.font='12px sans-serif';ctx.textAlign='center';ctx.fillText(icons[i],p[0],p[1]+4);
    ctx.fillStyle='#cdd7ea';ctx.font='11px sans-serif';ctx.fillText(labels[i],p[0],p[1]+30);
  });
  // 突触细节(步骤2-3)
  if(N.step>=2){
    const synX=W*0.5,synY=H*0.5;
    ctx.strokeStyle='#e17055';ctx.lineWidth=1;ctx.setLineDash([2,2]);
    ctx.strokeRect(synX-20,synY-25,40,50);ctx.setLineDash([]);
    ctx.fillStyle='#e17055';ctx.font='9px sans-serif';ctx.fillText('突触',synX+25,synY-20);
    // 神经递质
    if(N.step>=2){
      for(let i=0;i<3;i++){
        const vx=synX+Math.sin(N.t*3+i*2)*8;
        const vy=synY-10+i*10+Math.cos(N.t*2+i)*3;
        ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(vx,vy,3,0,Math.PI*2);ctx.fill();
      }
    }
  }
  // 离子通道
  N.ions.forEach(ion=>{
    ctx.fillStyle=ion.type==='Na'?'#f87171':'#60a5fa';
    ctx.beginPath();ctx.arc(ion.x*W,ion.y*H,3,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#fff';ctx.font='6px sans-serif';ctx.fillText(ion.type,ion.x*W,ion.y*H+2);
  });
  ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('兴奋在神经纤维上以电信号传导，在突触处通过神经递质化学传递',W/2,H-15);
  statusEl.textContent='反射弧：感受器→传入神经→中枢→传出神经→效应器';
}
'''

ENHANCED['人体内环境'] = '''
const H={t:0,glucose:5.0,target:5.0,water:0.5,temp:37,step:0};
function sceneInit(){sceneReset();}
function sceneReset(){H.t=0;H.glucose=5.0;H.target=5.0;H.water=0.5;H.temp=37;H.step=0;}
function sceneStep(d){H.step=Math.max(0,Math.min(2,H.step+d));}
function sceneUpdate(dt){
  H.t+=dt;
  // 血糖调节
  const diff=H.target-H.glucose;
  H.glucose+=diff*dt*0.3;
  H.glucose+=Math.sin(H.t*2)*0.05;
  // 体温
  H.temp=37+Math.sin(H.t*0.5)*0.3;
}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H2=cv.height;
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
  ctx.fillText('人体内环境与稳态调节',W/2,25);
  // 血糖调节图
  const gx=W*0.15,gy=80,gw=W*0.3,gh=150;
  ctx.strokeStyle='#7f93b5';ctx.lineWidth=1;ctx.strokeRect(gx,gy,gw,gh);
  ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('血糖浓度调节',gx+gw/2,gy-8);
  // Y轴标签
  ctx.textAlign='right';ctx.fillText('8 mmol/L',gx-5,gy+10);ctx.fillText('4 mmol/L',gx-5,gy+gh);
  // 正常范围
  ctx.fillStyle='rgba(0,184,148,0.1)';ctx.fillRect(gx,gy+gh*0.4,gw,gh*0.3);
  ctx.strokeStyle='#00b894';ctx.setLineDash([3,3]);
  ctx.beginPath();ctx.moveTo(gx,gy+gh*0.4);ctx.lineTo(gx+gw,gy+gh*0.4);ctx.stroke();
  ctx.beginPath();ctx.moveTo(gx,gy+gh*0.7);ctx.lineTo(gx+gw,gy+gh*0.7);ctx.stroke();
  ctx.setLineDash([]);
  // 血糖曲线
  ctx.strokeStyle='#e17055';ctx.lineWidth=2;ctx.beginPath();
  for(let i=0;i<gw;i++){
    const t2=i/gw*10;
    const val=5+Math.sin(t2*0.8)*2*Math.exp(-t2*0.1);
    const y=gy+gh-(val-3)/6*gh;
    i===0?ctx.moveTo(gx+i,y):ctx.lineTo(gx+i,y);
  }
  ctx.stroke();
  // 当前值标记
  const curY=gy+gh-(H.glucose-3)/6*gh;
  ctx.fillStyle='#e17055';ctx.beginPath();ctx.arc(gx+gw-5,curY,5,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='11px sans-serif';ctx.textAlign='left';
  ctx.fillText(H.glucose.toFixed(1)+' mmol/L',gx+gw+8,curY+4);
  // 胰岛素/胰高血糖素标注
  if(H.glucose>6){ctx.fillStyle='#0984e3';ctx.fillText('↑胰岛素分泌',gx+gw-60,curY-15);}
  if(H.glucose<4.5){ctx.fillStyle='#e17055';ctx.fillText('↑胰高血糖素',gx+gw-70,curY+20);}
  // 体温调节
  const tx=W*0.55,ty=80,tw=W*0.35,th=150;
  ctx.strokeStyle='#7f93b5';ctx.lineWidth=1;ctx.strokeRect(tx,ty,tw,th);
  ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('体温调节',tx+tw/2,ty-8);
  // 体温曲线
  ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;ctx.beginPath();
  for(let i=0;i<tw;i++){
    const t2=i/tw*8;
    const val=37+Math.sin(t2*0.5)*1.5*Math.exp(-t2*0.15);
    const y=ty+th-(val-35)/4*th;
    i===0?ctx.moveTo(tx+i,y):ctx.lineTo(tx+i,y);
  }
  ctx.stroke();
  // 正常范围
  ctx.fillStyle='rgba(253,203,110,0.1)';ctx.fillRect(tx,ty+th*0.3,tw,th*0.35);
  ctx.fillStyle='#fbbf24';ctx.font='11px sans-serif';ctx.textAlign='center';
  ctx.fillText('37°C',tx+tw/2,ty+th+15);
  // 产热/散热
  ctx.fillStyle='#e17055';ctx.font='10px sans-serif';
  ctx.fillText('寒冷→骨骼肌战栗产热',tx+tw*0.25,ty+th+30);
  ctx.fillStyle='#0984e3';
  ctx.fillText('炎热→汗腺分泌散热',tx+tw*0.7,ty+th+30);
  // 水盐平衡
  ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('水盐平衡',W/2,ty+th+55);
  ctx.fillStyle='#74b9ff';ctx.font='10px sans-serif';
  ctx.fillText('饮水不足→细胞外液渗透压↑→下丘脑→抗利尿激素↑→肾小管重吸收↑→尿量↓',W/2,ty+th+72);
  // 调节网络总结
  ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.textAlign='center';
  ctx.fillText('稳态通过 神经-体液-免疫 调节网络维持',W/2,H2-15);
  statusEl.textContent='内环境稳态：血糖、体温、水盐平衡通过负反馈调节维持动态平衡';
}
'''

ENHANCED['群落演替'] = '''
const E={t:0,day:0,plants:[]};
function sceneInit(){sceneReset();for(let i=0;i<30;i++)E.plants.push({x:Math.random(),type:0,growth:Math.random(),delay:Math.random()*5});}
function sceneReset(){E.t=0;E.day=0;E.plants=[];for(let i=0;i<30;i++)E.plants.push({x:Math.random(),type:0,growth:Math.random(),delay:Math.random()*5});}
function sceneUpdate(dt){E.t+=dt;E.day=Math.min(200,E.t*5);}
function sceneDraw(){
  ctx.clearRect(0,0,cv.width,cv.height);
  const W=cv.width,H=cv.height;
  const groundY=H*0.75;
  // 天空渐变
  const skyGrad=ctx.createLinearGradient(0,0,0,groundY);
  skyGrad.addColorStop(0,'#1a1a2e');skyGrad.addColorStop(1,'#16213e');
  ctx.fillStyle=skyGrad;ctx.fillRect(0,0,W,groundY);
  // 地面
  ctx.fillStyle='#2d3436';ctx.fillRect(0,groundY,W,H-groundY);
  // 时间轴
  ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';
  const year=Math.floor(E.day/365);const day=E.day%365;
  ctx.fillText('群落演替 — 第 '+year+' 年 '+Math.floor(day)+' 天',W/2,25);
  // 阶段标注
  let stage='裸地';if(E.day>10)stage='地衣苔藓阶段';if(E.day>40)stage='草本植物阶段';if(E.day>100)stage='灌木阶段';if(E.day>180)stage='森林阶段(顶极群落)';
  ctx.fillStyle='#00b894';ctx.font='13px sans-serif';ctx.fillText(stage,W/2,45);
  // 植物生长
  E.plants.forEach(p=>{
    const px=p.x*W;
    const age=Math.max(0,E.day-p.delay*30);
    if(age<=0)return;
    ctx.save();ctx.translate(px,groundY);
    if(age<30){
      // 地衣苔藓
      ctx.fillStyle='rgba(0,184,148,0.5)';
      for(let i=0;i<3;i++){ctx.beginPath();ctx.arc(Math.sin(i+age)*5,-i*2,3+age*0.1,0,Math.PI*2);ctx.fill();}
    }else if(age<100){
      // 草本
      const h=Math.min(40,(age-30)*0.5);
      ctx.strokeStyle='#00b894';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(0,-h);ctx.stroke();
      ctx.fillStyle='#00b894';ctx.beginPath();ctx.ellipse(0,-h,8,5,0,0,Math.PI*2);ctx.fill();
    }else if(age<180){
      // 灌木
      const h=Math.min(60,(age-100)*0.6);
      ctx.strokeStyle='#6c5228';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(0,-h*0.6);ctx.stroke();
      ctx.fillStyle='#00b894';ctx.beginPath();ctx.ellipse(0,-h,15,12,0,0,Math.PI*2);ctx.fill();
    }else{
      // 乔木(森林)
      const h=Math.min(120,(age-180)*0.8+60);
      ctx.strokeStyle='#6c5228';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(0,-h*0.5);ctx.stroke();
      // 树冠
      ctx.fillStyle='#00b894';
      ctx.beginPath();ctx.moveTo(-20,-h*0.4);ctx.lineTo(0,-h);ctx.lineTo(20,-h*0.4);ctx.closePath();ctx.fill();
      ctx.beginPath();ctx.moveTo(-25,-h*0.3);ctx.lineTo(0,-h*0.7);ctx.lineTo(25,-h*0.3);ctx.closePath();ctx.fill();
    }
    ctx.restore();
  });
  // 时间进度条
  ctx.fillStyle='rgba(255,255,255,0.1)';ctx.fillRect(30,H-30,W-60,8);
  ctx.fillStyle='#00b894';ctx.fillRect(30,H-30,(W-60)*Math.min(1,E.day/200),8);
  ctx.fillStyle='#aaa';ctx.font='10px sans-serif';ctx.textAlign='left';ctx.fillText('裸地',30,H-10);
  ctx.textAlign='right';ctx.fillText('顶极群落',W-30,H-10);
  ctx.textAlign='center';ctx.fillText('初生演替需数百年，次生演替更快（土壤已存在）',W/2,H-45);
  statusEl.textContent='群落演替：裸地→地衣→苔藓→草本→灌木→森林（顶极群落）';
}
'''

def get_dirname(filepath):
    return os.path.basename(os.path.dirname(filepath))

def find_enhancement(dirname):
    for key in ENHANCED:
        if key in dirname:
            return ENHANCED[key]
    return None

def enhance_file(filepath):
    dirname = get_dirname(filepath)
    enhancement = find_enhancement(dirname)
    if not enhancement:
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 <script> 和 </script> 之间的内容
    script_match = re.search(r'(<script>\n)(.*?)(\n</script>)', content, re.DOTALL)
    if not script_match:
        return False
    
    old_script = script_match.group(2)
    
    # 保留通用的 fit/canvas 设置和控制面板代码
    common_header = '''const cv=document.getElementById('cv');const ctx=cv.getContext('2d');
const statusEl=document.getElementById('status');
function fit(){const r=cv.parentElement.getBoundingClientRect();cv.width=Math.max(360,Math.min(980,r.width-8));cv.height=Math.max(360,Math.min(560,r.height-8));}
window.addEventListener('resize',()=>{fit();draw();});fit();
'''
    common_footer = '''
let playing=false,lastT=0,speed=1,t=0;
const playBtn=document.getElementById('playBtn'),resetBtn=document.getElementById('resetBtn');
const stepBackBtn=document.getElementById('stepBackBtn'),stepFwdBtn=document.getElementById('stepFwdBtn');
const speedEl=document.getElementById('speed');
function loop(ts){if(!lastT)lastT=ts;const dt=(ts-lastT)/1000;lastT=ts;if(playing){t+=dt*speed;if(window.sceneUpdate)sceneUpdate(dt*speed);}draw();requestAnimationFrame(loop);}
requestAnimationFrame(loop);
playBtn.onclick=()=>{playing=!playing;playBtn.textContent=playing?'⏸ 暂停':'▶ 播放';};
resetBtn.onclick=()=>{if(window.sceneReset)sceneReset();t=0;playing=false;playBtn.textContent='▶ 播放';draw();};
stepFwdBtn.onclick=()=>{if(window.sceneStep)sceneStep(1);draw();};
stepBackBtn.onclick=()=>{if(window.sceneStep)sceneStep(-1);draw();};
speedEl.oninput=()=>{speed=parseFloat(speedEl.value);};
function draw(){if(window.sceneDraw)sceneDraw();}
if(window.sceneInit)sceneInit();
draw();'''
    
    new_script = common_header + enhancement + common_footer
    content = content[:script_match.start(2)] + new_script + content[script_match.end(2):]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def main():
    count = 0
    for root, dirs, files in os.walk(BASE):
        if '.workbuddy' in root:
            continue
        for fname in files:
            if fname == 'index.html':
                fpath = os.path.join(root, fname)
                dirname = get_dirname(fpath)
                if find_enhancement(dirname):
                    # 只增强行数少于200行的文件（简陋的模板文件）
                    with open(fpath, 'r', encoding='utf-8') as f:
                        lines = sum(1 for _ in f)
                    if lines < 200:
                        if enhance_file(fpath):
                            print(f'  Enhanced: {dirname} ({lines} lines)')
                            count += 1
    print(f'\n共增强 {count} 个文件')

if __name__ == '__main__':
    main()
