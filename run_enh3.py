#!/usr/bin/env python3
from enh3 import walk
anims = {
'钠与水反应': '''
const S={t:0,b:[],nx:0,ny:0};
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.b=[];S.nx=0;S.ny=0;}
function sceneUpdate(dt){S.t+=dt;S.nx=cv.width*0.4+Math.sin(S.t*3)*15;S.ny=cv.height*0.45+Math.cos(S.t*2)*5;if(Math.random()<0.3)S.b.push({x:S.nx+(Math.random()-0.5)*20,y:S.ny,vy:-30-Math.random()*20,life:1.5,r:2+Math.random()*3});S.b.forEach(b=>{b.y+=b.vy*dt;b.life-=dt;b.r+=dt*2;});S.b=S.b.filter(b=>b.life>0);}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,wY=H*0.4;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('钠与水反应：2Na + 2H₂O → 2NaOH + H₂↑',W/2,25);
ctx.fillStyle='rgba(9,132,227,0.2)';ctx.fillRect(50,wY,W-100,H-wY-40);ctx.strokeStyle='#0984e3';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(50,wY);ctx.lineTo(W-50,wY);ctx.stroke();
ctx.fillStyle='#e0e0e0';ctx.beginPath();ctx.arc(S.nx,S.ny,10,0,Math.PI*2);ctx.fill();
const g=ctx.createRadialGradient(S.nx,S.ny,5,S.nx,S.ny,30);g.addColorStop(0,'rgba(253,203,110,0.3)');g.addColorStop(1,'rgba(253,203,110,0)');ctx.fillStyle=g;ctx.beginPath();ctx.arc(S.nx,S.ny,30,0,Math.PI*2);ctx.fill();
S.b.forEach(b=>{ctx.strokeStyle='rgba(116,185,255,0.7)';ctx.lineWidth=1;ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,Math.PI*2);ctx.stroke();});
ctx.fillStyle='#fdcb6e';ctx.font='bold 13px sans-serif';ctx.fillText('2Na + 2H₂O → 2NaOH + H₂↑',W/2,H-50);
ctx.fillStyle='rgba(225,69,83,0.15)';ctx.fillRect(50,wY,W-100,H-wY-40);ctx.fillStyle='#e17055';ctx.font='12px sans-serif';ctx.fillText('溶液变红(酚酞→碱性→NaOH)',W/2,H-30);
statusEl.textContent='2Na+2H₂O→2NaOH+H₂↑：浮熔游响红';}
''',
'AVL树': '''
const S={t:0,step:0};const C=['LL旋转(右旋)','RR旋转(左旋)','LR旋转','RL旋转'];
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;}
function sceneStep(d){S.step=Math.max(0,Math.min(3,S.step+d));}
function sceneUpdate(dt){S.t+=dt;}
function nN(x,y,v,c){ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,18,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 12px sans-serif';ctx.textAlign='center';ctx.fillText(v,x,y+4);}
function eE(a,b,c,d){ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(a,b);ctx.lineTo(c,d);ctx.stroke();}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,cx=W/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('AVL树旋转 — '+C[S.step],cx,25);
for(let i=0;i<4;i++){ctx.fillStyle=i<=S.step?'#6C5CE7':'rgba(255,255,255,0.2)';ctx.fillRect(cx-100+i*52,35,48,4);}
const p=Math.min(1,S.t*0.5),y1=100,y2=180,y3=260;
if(S.step===0){nN(cx-150,y1,'#e17055','30');eE(cx-150,y1,cx-190,y2);eE(cx-150,y1,cx-110,y2);nN(cx-190,y2,'#6C5CE7','20');eE(cx-190,y2,cx-210,y3);eE(cx-190,y2,cx-170,y3);nN(cx-110,y2,'#7f93b5','25');nN(cx-210,y3,'#7f93b5','15');nN(cx-170,y3,'#7f93b5','15');
if(p>0.3){ctx.fillStyle='#00cec9';ctx.font='20px sans-serif';ctx.fillText('→',cx,180);}
if(p>0.5){const a=cx+150;nN(a,y1,'#00cec9','20');eE(a,y1,a-40,y2);eE(a,y1,a+40,y2);nN(a-40,y2,'#7f93b5','30');eE(a-40,y2,a-60,y3);eE(a-40,y2,a-20,y3);nN(a+40,y2,'#7f93b5','25');nN(a-60,y3,'#6C5CE7','15');nN(a-20,y3,'#7f93b5','15');}
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('左子树过高→右旋',cx,H-40);}
else if(S.step===1){nN(cx-150,y1,'#e17055','30');eE(cx-150,y1,cx-190,y2);eE(cx-150,y1,cx-110,y2);nN(cx-190,y2,'#7f93b5','25');nN(cx-110,y2,'#6C5CE7','20');eE(cx-110,y2,cx-90,y3);eE(cx-110,y2,cx-130,y3);nN(cx-90,y3,'#7f93b5','15');nN(cx-130,y3,'#7f93b5','15');
if(p>0.3){ctx.fillStyle='#00cec9';ctx.font='20px sans-serif';ctx.fillText('→',cx,180);}
if(p>0.5){const a=cx+150;nN(a,y1,'#00cec9','20');eE(a,y1,a-40,y2);eE(a,y1,a+40,y2);nN(a-40,y2,'#7f93b5','25');nN(a+40,y2,'#7f93b5','30');eE(a+40,y2,a+20,y3);eE(a+40,y2,a+60,y3);nN(a+20,y3,'#7f93b5','15');nN(a+60,y3,'#6C5CE7','15');}
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('右子树过高→左旋',cx,H-40);}
else if(S.step===2){nN(cx-100,y1,'#e17055','30');eE(cx-100,y1,cx-140,y2);eE(cx-100,y1,cx-60,y2);nN(cx-140,y2,'#7f93b5','20');eE(cx-140,y2,cx-140,y3);nN(cx-140,y3,'#6C5CE7','15');nN(cx-60,y2,'#7f93b5','25');
if(p>0.5){nN(cx+120,y1,'#00cec9','20');eE(cx+120,y1,cx+80,y2);eE(cx+120,y1,cx+160,y2);nN(cx+80,y2,'#7f93b5','30');eE(cx+80,y2,cx+60,y3);eE(cx+80,y2,cx+100,y3);nN(cx+60,y3,'#6C5CE7','15');nN(cx+100,y3,'#7f93b5','15');nN(cx+160,y2,'#7f93b5','25');}
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('LR：先左旋再右旋',cx,H-40);}
else{nN(cx-100,y1,'#e17055','30');eE(cx-100,y1,cx-140,y2);eE(cx-100,y1,cx-60,y2);nN(cx-140,y2,'#7f93b5','25');nN(cx-60,y2,'#7f93b5','20');eE(cx-60,y2,cx-60,y3);nN(cx-60,y3,'#6C5CE7','15');
if(p>0.5){nN(cx+120,y1,'#00cec9','20');eE(cx+120,y1,cx+80,y2);eE(cx+120,y1,cx+160,y2);nN(cx+80,y2,'#7f93b5','25');nN(cx+160,y2,'#7f93b5','30');eE(cx+160,y2,cx+140,y3);eE(cx+160,y2,cx+180,y3);nN(cx+140,y3,'#7f93b5','15');nN(cx+180,y3,'#6C5CE7','15');}
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('RL：先右旋再左旋',cx,H-40);}
statusEl.textContent='AVL树：LL/RR/LR/RL旋转维持平衡';}
''',
'电磁波': '''
const S={t:0};function sceneInit(){sceneReset();}function sceneReset(){S.t=0;}
function sceneUpdate(dt){S.t+=dt;}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,cy=H/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('电磁波：E⊥B⊥v',W/2,25);
ctx.strokeStyle='rgba(255,255,255,0.3)';ctx.lineWidth=1;ctx.setLineDash([5,5]);ctx.beginPath();ctx.moveTo(40,cy);ctx.lineTo(W-40,cy);ctx.stroke();ctx.setLineDash([]);
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('传播方向→',W-80,cy-15);
ctx.strokeStyle='#e17055';ctx.lineWidth=2.5;ctx.beginPath();for(let x=50;x<W-50;x+=2){const p=(x-50)/(W-100)*Math.PI*4-S.t*3;const y=cy+Math.sin(p)*60;x===50?ctx.moveTo(x,y):ctx.lineTo(x,y);}ctx.stroke();
ctx.strokeStyle='#0984e3';ctx.lineWidth=2.5;ctx.beginPath();for(let x=50;x<W-50;x+=2){const p=(x-50)/(W-100)*Math.PI*4-S.t*3;const z=Math.cos(p)*40;x===50?ctx.moveTo(x+z*0.5,cy-z*0.3):ctx.lineTo(x+z*0.5,cy-z*0.3);}ctx.stroke();
ctx.fillStyle='#e17055';ctx.font='bold 13px sans-serif';ctx.textAlign='left';ctx.fillText('E 电场(↕)',50,50);ctx.fillStyle='#0984e3';ctx.fillText('B 磁场(↔)',50,70);
ctx.fillStyle='rgba(255,255,255,0.5)';ctx.font='11px sans-serif';ctx.textAlign='center';ctx.fillText('E⊥B⊥传播方向 c=3×10⁸m/s=λf',W/2,H-20);
statusEl.textContent='电磁波：E⊥B⊥v，横波，c=3×10⁸m/s';}
''',
'牛顿第三定律': '''
const S={t:0,step:0,f:0,ax:200,avx:0,bx:500,bvx:0};
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;S.f=0;S.ax=200;S.avx=0;S.bx=500;S.bvx=0;}
function sceneStep(d){S.step=Math.max(0,Math.min(2,S.step+d));}
function sceneUpdate(dt){S.t+=dt;if(S.step===0)S.f=Math.min(1,S.f+dt*0.5);if(S.step===1){S.avx=-S.f*100;S.bvx=S.f*100;S.ax+=S.avx*dt;S.bx+=S.bvx*dt;}if(S.step===2)S.f=Math.min(1,S.f+dt*0.3);}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,cy=H/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('牛顿第三定律 — '+['两人互推','分离','火箭喷气'][S.step],W/2,25);
if(S.step===0){const p=S.f;ctx.fillStyle='#74b9ff';ctx.beginPath();ctx.arc(W/2-60+p*20,cy,25,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='12px sans-serif';ctx.fillText('A',W/2-60+p*20,cy+4);ctx.fillStyle='#f87171';ctx.beginPath();ctx.arc(W/2+60-p*20,cy,25,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.fillText('B',W/2+60-p*20,cy+4);
if(p>0.3){ctx.strokeStyle='#fdcb6e';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(W/2-30+p*15,cy-35);ctx.lineTo(W/2+10-p*15,cy-35);ctx.stroke();ctx.fillStyle='#fdcb6e';ctx.font='11px sans-serif';ctx.fillText('F(A→B)',W/2,cy-45);ctx.beginPath();ctx.moveTo(W/2+30-p*15,cy+35);ctx.lineTo(W/2-10+p*15,cy+35);ctx.stroke();ctx.fillText('F(B→A)',W/2,cy+50);ctx.fillStyle='#00cec9';ctx.font='bold 12px sans-serif';ctx.fillText('F(A→B)=-F(B→A)',W/2,cy+80);}}
if(S.step===1){ctx.fillStyle='#74b9ff';ctx.beginPath();ctx.arc(S.ax,cy,25,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='12px sans-serif';ctx.fillText('A',S.ax,cy+4);ctx.fillStyle='#f87171';ctx.beginPath();ctx.arc(S.bx,cy,25,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.fillText('B',S.bx,cy+4);ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('等大反向→速度等大反向',W/2,H-40);}
if(S.step===2){const rY=cy-S.f*80;ctx.fillStyle='#cdd7ea';ctx.beginPath();ctx.moveTo(W/2,rY-40);ctx.lineTo(W/2-15,rY+20);ctx.lineTo(W/2+15,rY+20);ctx.closePath();ctx.fill();ctx.fillStyle='#fff';ctx.font='10px sans-serif';ctx.fillText('火箭',W/2,rY);for(let i=0;i<8;i++){ctx.fillStyle=`rgba(253,203,110,${1-i*0.12})`;ctx.beginPath();ctx.arc(W/2+(Math.random()-0.5)*15,rY+25+i*10,4-i*0.3,0,Math.PI*2);ctx.fill();}ctx.fillStyle='#00cec9';ctx.font='bold 12px sans-serif';ctx.fillText('火箭推气↓→气推火箭↑',W/2,H-30);}
statusEl.textContent='牛顿第三定律：作用力=反作用力，等大反向共线';}
''',
'哈希表': '''
const S={t:0,step:0,tb:new Array(8).fill(null)};const K=[23,7,31,15,39,47,8,16];
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;S.tb=new Array(8).fill(null);}
function sceneStep(d){S.step=Math.max(0,Math.min(3,S.step+d));}
function sceneUpdate(dt){S.t+=dt;}
function dS(x,y,i,v){ctx.fillStyle='rgba(255,255,255,0.05)';ctx.fillRect(x,y,50,35);ctx.strokeStyle='#7f93b5';ctx.lineWidth=1;ctx.strokeRect(x,y,50,35);ctx.fillStyle='#aaa';ctx.font='10px sans-serif';ctx.textAlign='center';ctx.fillText('['+i+']',x+25,y-5);if(v!==null){ctx.fillStyle='#6C5CE7';ctx.beginPath();ctx.arc(x+25,y+17,12,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='bold 11px sans-serif';ctx.fillText(v,x+25,y+21);}}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,tx=W/2-200,ty=80;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('哈希表 — '+['定址法','拉链法','线性探测','插入'][S.step],W/2,25);
for(let i=0;i<8;i++)dS(tx+i*52,ty,i,S.tb[i]);
if(S.step===0){ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('h(key)=key%8',W/2,ty+60);K.forEach((k,i)=>{const x=tx+i*52+25,y=ty+90;ctx.fillStyle='#fdcb6e';ctx.beginPath();ctx.arc(x,y,10,0,Math.PI*2);ctx.fill();ctx.fillStyle='#000';ctx.font='9px sans-serif';ctx.fillText(k,x,y+3);ctx.strokeStyle='rgba(255,255,255,0.3)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,y+10);ctx.lineTo(tx+(k%8)*52+25,ty+37);ctx.stroke();});}
if(S.step===1){const ch={};K.forEach(k=>{const h=k%8;if(!ch[h])ch[h]=[];ch[h].push(k);});Object.entries(ch).forEach(([h,v])=>{if(v.length>1){const x=tx+parseInt(h)*52+25;ctx.fillStyle='#6C5CE7';ctx.beginPath();ctx.arc(x,ty+70,10,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='9px sans-serif';ctx.fillText(v[0],x,ty+73);v.slice(1).forEach((val,i)=>{const nx=x+(i+1)*28;ctx.strokeStyle='#00cec9';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x+i*28+10,ty+70);ctx.lineTo(nx-10,ty+70);ctx.stroke();ctx.fillStyle='#00cec9';ctx.beginPath();ctx.arc(nx,ty+70,10,0,Math.PI*2);ctx.fill();ctx.fillStyle='#fff';ctx.font='9px sans-serif';ctx.fillText(val,nx,ty+73);});ctx.fillStyle='#e17055';ctx.font='10px sans-serif';ctx.fillText('冲突!',x,ty+55);}});ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText('同一位置用链表存储',W/2,ty+110);}
if(S.step===2){ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('冲突→依次查找下一空位',W/2,ty+60);}
if(S.step===3){const k=K[Math.floor(S.t)%K.length];ctx.fillStyle='#fdcb6e';ctx.font='13px sans-serif';ctx.fillText('插入 key='+k+' → h='+k%8,tx+200,ty+60);for(let i=0;i<8;i++)dS(tx+i*52,ty+80,i,S.tb[i]);}
statusEl.textContent='哈希表：O(1)查找，拉链法/开放定址法解决冲突';}
''',
'链表': '''
const S={t:0,step:0};function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;}
function sceneStep(d){S.step=Math.max(0,Math.min(4,S.step+d));}
function sceneUpdate(dt){S.t+=dt;}
function dN(x,y,v,c){ctx.fillStyle=c||'#6C5CE7';ctx.fillRect(x,y-15,60,28);ctx.strokeStyle='rgba(255,255,255,0.3)';ctx.lineWidth=1;ctx.strokeRect(x,y-15,60,28);ctx.fillStyle='#fff';ctx.font='bold 12px sans-serif';ctx.textAlign='center';ctx.fillText(v,x+30,y+3);ctx.fillStyle='rgba(255,255,255,0.1)';ctx.fillRect(x+45,y-15,15,28);ctx.fillStyle='#aaa';ctx.font='8px sans-serif';ctx.fillText('→',x+52,y+2);}
function dA(a,b,c,d){ctx.strokeStyle='#00cec9';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(a,b);ctx.lineTo(c,d);ctx.stroke();const an=Math.atan2(d-b,c-a);ctx.fillStyle='#00cec9';ctx.beginPath();ctx.moveTo(c,d);ctx.lineTo(c-8*Math.cos(an-0.4),d-8*Math.sin(an-0.4));ctx.lineTo(c-8*Math.cos(an+0.4),d-8*Math.sin(an+0.4));ctx.closePath();ctx.fill();}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,sx=60,sy=H/2-20,g=90;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('链表 — '+['初始','插入25','完成','删除30','完成'][S.step],W/2,25);
let nd=[10,20,30,40];if(S.step>=2&&S.step<=3)nd=[10,20,25,30,40];if(S.step>=4)nd=[10,20,25,40];
nd.forEach((v,i)=>{let c='#6C5CE7';if(S.step===1&&i===2)c='#00cec9';if(S.step===3&&i===3)c='#e17055';dN(sx+i*g,sy,String(v),c);if(i<nd.length-1)dA(sx+i*g+60,sy,sx+(i+1)*g,sy);});
ctx.fillStyle='#fdcb6e';ctx.font='11px sans-serif';ctx.fillText('HEAD',sx+30,sy-30);ctx.fillStyle='#aaa';ctx.fillText('NULL',sx+nd.length*g+10,sy);
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';
if(S.step===1)ctx.fillText('20.next=新节点; 新节点.next=原30',W/2,sy+60);
if(S.step===3)ctx.fillText('20.next=30.next(跳过30)',W/2,sy+60);
if(S.step>=4)ctx.fillText('双向链表:prev+next | 循环链表:尾→头',W/2,sy+80);
statusEl.textContent='链表：插入O(1) 删除O(1) 查找O(n)';}
''',
'堆': '''
const S={t:0,step:0,hp:[50,30,20,15,10,8,12],hl:-1};
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;S.hp=[50,30,20,15,10,8,12];S.hl=-1;}
function sceneStep(d){S.step=Math.max(0,Math.min(3,S.step+d));}
function sceneUpdate(dt){S.t+=dt;S.hl=Math.floor(S.t*2)%S.hp.length;}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,cx=W/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('堆 — '+['大顶堆','插入(上浮)','删除(下沉)','堆排序'][S.step],cx,25);
const lv=[[0],[1,2],[3,4,5,6]];const yS=80,yG=70;
lv.forEach((l,li)=>{const y=yS+li*yG;const xS=cx-(l.length-1)*40;l.forEach((idx,ni)=>{if(idx<S.hp.length){const x=xS+ni*80;ctx.fillStyle=idx===S.hl?'rgba(108,92,231,0.8)':'rgba(108,92,231,0.4)';ctx.beginPath();ctx.arc(x,y,22,0,Math.PI*2);ctx.fill();ctx.strokeStyle=idx===S.hl?'#fdcb6e':'#7f93b5';ctx.lineWidth=idx===S.hl?3:1;ctx.stroke();ctx.fillStyle='#fff';ctx.font='bold 12px sans-serif';ctx.textAlign='center';ctx.fillText(S.hp[idx],x,y+4);
if(idx>0){const pi=Math.floor((idx-1)/2);const pL=lv.findIndex(a=>a.includes(pi));const pI=lv[pL].indexOf(pi);const px=cx-(lv[pL].length-1)*40+pI*80;const py=yS+pL*yG;ctx.strokeStyle='rgba(127,147,181,0.5)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,y-22);ctx.lineTo(px,py+22);ctx.stroke();}}});});
ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('['+S.hp.join(', ')+']',cx,yS+3*yG+20);
ctx.fillStyle='#00cec9';ctx.font='12px sans-serif';ctx.fillText(['每节点≥子节点','放末尾→上浮','末位替代→下沉','反复取最大值→升序'][S.step],cx,H-30);
statusEl.textContent='堆：插入O(logn) 取最值O(1) 堆排序O(nlogn)';}
''',
'电磁感应': '''
const S={t:0};function sceneInit(){sceneReset();}function sceneReset(){S.t=0;}
function sceneUpdate(dt){S.t+=dt;}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height,cx=W/2,cy=H/2;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('电磁感应：ε=-dΦ/dt',W/2,25);
ctx.strokeStyle='#7f93b5';ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(cx,cy,80,25,0,0,Math.PI*2);ctx.stroke();ctx.beginPath();ctx.ellipse(cx,cy+8,80,25,0,0,Math.PI*2);ctx.stroke();
const my=cy-80+Math.sin(S.t*1.5)*60;ctx.fillStyle='#e17055';ctx.fillRect(cx-12,my-30,24,30);ctx.fillStyle='#0984e3';ctx.fillRect(cx-12,my,24,30);ctx.fillStyle='#fff';ctx.font='bold 11px sans-serif';ctx.textAlign='center';ctx.fillText('N',cx,my-12);ctx.fillText('S',cx,my+18);
ctx.strokeStyle='rgba(255,255,255,0.2)';ctx.lineWidth=1;for(let i=-2;i<=2;i++){ctx.beginPath();ctx.moveTo(cx+i*8,my+30);ctx.quadraticCurveTo(cx+i*20,cy-20,cx+i*15,cy+25);ctx.stroke();}
const emf=-Math.sin(S.t*1.5)*1.5;const gx=cx+160;ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.beginPath();ctx.arc(gx,cy,25,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#fff';ctx.font='12px sans-serif';ctx.fillText('G',gx,cy+4);
const na=-Math.PI/2+emf*0.6;ctx.strokeStyle='#e17055';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(gx,cy);ctx.lineTo(gx+Math.cos(na)*20,cy+Math.sin(na)*20);ctx.stroke();
ctx.strokeStyle='#fdcb6e';ctx.lineWidth=1.5;ctx.beginPath();ctx.moveTo(cx+80,cy);ctx.lineTo(gx-25,cy);ctx.stroke();
if(Math.abs(emf)>0.3){ctx.fillStyle='#fdcb6e';ctx.font='12px sans-serif';ctx.fillText('感应电流'+(emf>0?'→':'←'),cx+120,cy-15);}
const wx=50,wy=H-120,ww=W-100,wh=80;ctx.strokeStyle='rgba(255,255,255,0.2)';ctx.lineWidth=1;ctx.strokeRect(wx,wy,ww,wh);
ctx.strokeStyle='#0984e3';ctx.lineWidth=1.5;ctx.beginPath();for(let i=0;i<ww;i++){const t2=(i/ww)*Math.PI*4-S.t*1.5;ctx.lineTo(wx+i,wy+wh/2-Math.cos(t2)*wh*0.4);}ctx.stroke();
ctx.strokeStyle='#e17055';ctx.lineWidth=1.5;ctx.beginPath();for(let i=0;i<ww;i++){const t2=(i/ww)*Math.PI*4-S.t*1.5;ctx.lineTo(wx+i,wy+wh/2+Math.sin(t2)*wh*0.4);}ctx.stroke();
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('磁铁运动→Φ变化→ε→感应电流',W/2,H-15);
statusEl.textContent='法拉第定律：ε=-dΦ/dt';}
''',
'内能改变': '''
const S={t:0,step:0,m:[]};for(let i=0;i<30;i++)S.m.push({x:Math.random(),y:Math.random(),vx:(Math.random()-0.5)*2,vy:(Math.random()-0.5)*2});
function sceneInit(){sceneReset();}function sceneReset(){S.t=0;S.step=0;}
function sceneStep(d){S.step=Math.max(0,Math.min(2,S.step+d));}
function sceneUpdate(dt){S.t+=dt;const s=S.step===1?3:S.step===2?2:1;S.m.forEach(p=>{p.x+=p.vx*dt*s*0.3;p.y+=p.vy*dt*s*0.3;if(p.x<0||p.x>1)p.vx*=-1;if(p.y<0||p.y>1)p.vy*=-1;p.x=Math.max(0,Math.min(1,p.x));p.y=Math.max(0,Math.min(1,p.y));});}
function sceneDraw(){ctx.clearRect(0,0,cv.width,cv.height);const W=cv.width,H=cv.height;
ctx.fillStyle='#fff';ctx.font='bold 14px sans-serif';ctx.textAlign='center';ctx.fillText('改变内能：做功与热传递',W/2,25);
const lx=W*0.25,ly=H/2,lw=W*0.35,lh=H*0.5;ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.strokeRect(lx-lw/2,ly-lh/2,lw,lh);ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('做功',lx,ly-lh/2-10);
if(S.step===1){const pY=ly-lh/2+10+Math.sin(S.t*3)*15;ctx.fillStyle='#7f93b5';ctx.fillRect(lx-lw/2+5,pY,lw-10,8);ctx.fillStyle='#e17055';ctx.font='11px sans-serif';ctx.fillText('↓压缩',lx,pY-5);}
S.m.forEach(p=>{const x=lx-lw/2+10+p.x*(lw-20),y=ly-lh/2+10+p.y*(lh-20);const sp=Math.sqrt(p.vx*p.vx+p.vy*p.vy);ctx.fillStyle=sp>1.5?'#f87171':'#7dd3fc';ctx.beginPath();ctx.arc(x,y,3,0,Math.PI*2);ctx.fill();});
const rx=W*0.7,ry=H/2,rw=W*0.35,rh=H*0.5;ctx.strokeStyle='#7f93b5';ctx.lineWidth=2;ctx.strokeRect(rx-rw/2,ry-rh/2,rw,rh);ctx.fillStyle='#aaa';ctx.font='12px sans-serif';ctx.fillText('热传递',rx,ry-rh/2-10);
if(S.step===2){const gd=ctx.createLinearGradient(rx-rw/2,0,rx+rw/2,0);gd.addColorStop(0,'rgba(225,69,83,0.2)');gd.addColorStop(1,'rgba(9,132,227,0.2)');ctx.fillStyle=gd;ctx.fillRect(rx-rw/2,ry-rh/2,rw,rh);ctx.fillStyle='#e17055';ctx.font='11px sans-serif';ctx.fillText('高温',rx-rw/4,ry);ctx.fillStyle='#0984e3';ctx.fillText('低温',rx+rw/4,ry);}
S.m.forEach((p,i)=>{if(i>=15){const x=rx-rw/2+10+p.x*(rw-20),y=ry-rh/2+10+p.y*(rh-20);ctx.fillStyle='#7dd3fc';ctx.beginPath();ctx.arc(x,y,3,0,Math.PI*2);ctx.fill();}});
ctx.fillStyle='rgba(255,255,255,0.6)';ctx.font='12px sans-serif';ctx.fillText('做功和热传递在改变内能上等效',W/2,H-15);
statusEl.textContent='内能：做功(宏观力→微观动能) 热传递(分子碰撞传能)';}
''',
}
n=walk(anims)
print(f'共增强 {n} 个文件')
