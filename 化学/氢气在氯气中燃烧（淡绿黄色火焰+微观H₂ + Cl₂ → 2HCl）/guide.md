# 需求：氢气在氯气中燃烧（淡绿黄色火焰+微观H₂ + Cl₂ → 2HCl）

### 1. 专业思考


#### 用户需求分析
目标用户主要是初中或高中化学初学者。他们需要：
1.  **直观理解宏观现象**：清晰看到氢气在氯气中燃烧时产生的“淡绿黄色火焰”这一标志性现象。
2.  **建立宏-微联系**：理解宏观现象背后的微观本质，即氢分子（H₂）和氯分子（Cl₂）在点燃条件下破裂成原子，并重新结合成氯化氢分子（HCl）的过程。
3.  **掌握化学方程式**：将动态的微观过程与静态的化学方程式 `H₂ + Cl₂ → 2HCl` 联系起来，理解方程式的含义。
4.  **安全认知**：通过动画的规范演示，间接认识到该实验需要在专业指导下进行（涉及易燃易爆气体）。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）
*   **核心概念**：化学反应、分子、原子、化学键的断裂与形成、化合反应、化学方程式。
*   **认知规律**：遵循“宏观现象 → 微观解释 → 符号表达”的认知顺序，由具体到抽象，逐步构建知识。
*   **交互设计**：
    *   **分步引导**：将动画分为“宏观火焰”、“微观反应”、“方程式总结”三个可自由切换的模块或阶段，允许学习者按自己的节奏探索。
    *   **控制与观察**：提供“播放/暂停/重置”控制，让学习者能仔细观察关键帧（如键的断裂瞬间）。在微观视图中，可考虑鼠标悬停显示分子标签（如H₂）。
    *   **主动建构**：在最后阶段，可以设计一个简单的互动，让学习者拖动氢原子和氯原子来“组装”HCl分子，强化键形成的概念。
*   **视觉呈现**：
    *   **宏观层**：用简化的燃烧器模型，通过粒子系统模拟出动态、摇曳的淡绿黄色火焰，背景为深色以突出火焰颜色。
    *   **微观层**：
        *   采用球棍模型：氢原子（H）为白色小球，氯原子（Cl）为绿色小球，化学键用连接杆表示。
        *   动画过程清晰：`H₂`和`Cl₂`分子相互靠近 → 接触瞬间化学键高亮闪烁并断裂（表示反应所需能量） → 原子分离 → 氢原子和氯原子相互配对 → 形成新的化学键，生成两个`HCl`分子。
        *   使用平滑的补间动画和路径提示，清晰展示原子的运动轨迹。

#### 配色方案选择
*   **主色/科学色**：
    *   **氢气（H₂）**：采用**浅灰色或白色**球体，代表其无色特性，与常用模型一致。
    *   **氯气（Cl₂）**：采用**黄绿色**球体，关联其气体颜色，并在宏观火焰中复用此色彩。
    *   **氯化氢（HCl）**：氢部分保持白色，氯部分保持黄绿色，表明其由两者构成。
    *   **火焰**：核心为**亮黄色**，外围渐变为**淡绿黄色**，准确表现实验现象。
*   **背景与界面**：
    *   **宏观背景**：深灰蓝色或黑色，模拟实验室暗环境，极致凸显火焰。
    *   **微观背景**：浅灰色或极淡的网格背景，避免干扰，聚焦分子模型。
    *   **界面控件**：使用中性色（如深蓝色、灰色），确保清晰且不喧宾夺主。
*   **高亮与动态色**：化学键断裂或形成时，使用**高亮橙色或红色**闪烁，表示能量的变化和过程的激烈。

#### 交互功能列表
1.  **场景切换器**：按钮或标签页，用于在“宏观火焰”、“微观反应”、“方程式”三个主场景间切换。
2.  **动画控制面板**：
    *   **播放/暂停**：控制动画运行。
    *   **重置**：将动画恢复到初始状态。
    *   **进度条**：可拖动，快速跳转到动画的特定时刻。
3.  **微观视图交互**：
    *   **鼠标悬停提示**：当鼠标悬停在分子或原子上时，显示其化学式或名称（如“氢分子 H₂”）。
    *   **逐步解说**：可勾选“显示步骤”，动画会在关键步骤暂停并显示文字说明。
4.  **学习巩固互动**（可选增强功能）：
    *   “组装分子”环节：在特定区域提供自由的氢原子和氯原子，让用户拖动它们相互靠近，当距离合适时自动形成键，完成HCl分子的构建。
5.  **信息显示**：
    *   固定区域显示当前观察的提示或核心化学方程式 `H₂ + Cl₂ →(点燃) 2HCl`。
    *   在微观动画中，关键步骤可有文字标签（如“化学键断裂”、“原子重新组合”）。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>氢气在氯气中燃烧 - 教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1a237e 0%, #283593 100%);
            color: #e8eaf6;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 25px;
            max-width: 800px;
            width: 100%;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: #ffffff;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 20px;
        }

        .equation {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            font-size: 1.8rem;
            font-weight: bold;
            margin: 15px auto;
            display: inline-block;
            border: 2px solid #5c6bc0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .scene-selector {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .scene-btn {
            background: #3949ab;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .scene-btn:hover {
            background: #5c6bc0;
            transform: translateY(-2px);
        }

        .scene-btn.active {
            background: #ff9800;
            box-shadow: 0 0 15px rgba(255, 152, 0, 0.5);
        }

        .animation-container {
            width: 100%;
            max-width: 900px;
            height: 500px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            overflow: hidden;
            position: relative;
            margin-bottom: 25px;
            border: 2px solid #5c6bc0;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }

        #canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .controls {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .control-btn {
            background: #303f9f;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .control-btn:hover {
            background: #3f51b5;
            transform: translateY(-2px);
        }

        .control-btn:active {
            transform: translateY(0);
        }

        .slider-container {
            display: flex;
            align-items: center;
            gap: 15px;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
            border-radius: 50px;
        }

        #progressSlider {
            width: 200px;
            height: 8px;
            -webkit-appearance: none;
            background: #5c6bc0;
            border-radius: 4px;
            outline: none;
        }

        #progressSlider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #ff9800;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .info-panel {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            max-width: 900px;
            width: 100%;
            margin-top: 10px;
            border-left: 5px solid #ff9800;
        }

        .info-title {
            font-size: 1.3rem;
            margin-bottom: 10px;
            color: #ffcc80;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-content {
            line-height: 1.6;
            font-size: 1.05rem;
        }

        .hint {
            position: absolute;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            color: #ffcc80;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            pointer-events: none;
            opacity: 0.9;
        }

        .atom-label {
            position: absolute;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.9rem;
            pointer-events: none;
            z-index: 100;
            white-space: nowrap;
            transform: translateY(-100%);
            display: none;
        }

        @media (max-width: 768px) {
            .animation-container {
                height: 400px;
            }
            
            .scene-btn, .control-btn {
                padding: 10px 20px;
                font-size: 1rem;
            }
            
            h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>氢气在氯气中燃烧</h1>
        <div class="subtitle">宏观现象 · 微观过程 · 化学方程式</div>
        <div class="equation">H₂ + Cl₂ → 2HCl</div>
    </div>

    <div class="scene-selector">
        <button class="scene-btn active" data-scene="macro">🔥 宏观火焰</button>
        <button class="scene-btn" data-scene="micro">🔬 微观反应</button>
        <button class="scene-btn" data-scene="equation">📝 方程式总结</button>
    </div>

    <div class="animation-container">
        <canvas id="canvas"></canvas>
        <div class="hint" id="hintText">鼠标悬停在分子上查看详细信息</div>
        <div class="atom-label" id="atomLabel"></div>
    </div>

    <div class="controls">
        <button class="control-btn" id="playBtn">▶️ 播放</button>
        <button class="control-btn" id="pauseBtn">⏸️ 暂停</button>
        <button class="control-btn" id="resetBtn">🔄 重置</button>
        
        <div class="slider-container">
            <span>进度控制:</span>
            <input type="range" id="progressSlider" min="0" max="100" value="0">
        </div>
    </div>

    <div class="info-panel">
        <div class="info-title">📚 当前学习要点</div>
        <div class="info-content" id="infoContent">
            观察氢气在氯气中燃烧产生的淡绿黄色火焰。这是一个剧烈的化合反应，需要在专业指导下进行。
        </div>
    </div>

    <script>
        // 获取DOM元素
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const sceneBtns = document.querySelectorAll('.scene-btn');
        const playBtn = document.getElementById('playBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const resetBtn = document.getElementById('resetBtn');
        const progressSlider = document.getElementById('progressSlider');
        const hintText = document.getElementById('hintText');
        const atomLabel = document.getElementById('atomLabel');
        const infoContent = document.getElementById('infoContent');

        // 设置Canvas尺寸
        function resizeCanvas() {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // 动画状态
        let currentScene = 'macro';
        let animationTime = 0;
        let isPlaying = true;
        let animationSpeed = 0.01;
        let hoveredObject = null;

        // 颜色定义
        const colors = {
            background: { macro: '#0a0e1a', micro: '#f5f7fa', equation: '#1a237e' },
            hydrogen: '#ffffff',
            chlorine: '#9acd32',
            flameCore: '#ffff00',
            flameEdge: '#adff2f',
            bond: '#666666',
            highlight: '#ff5722',
            text: '#333333'
        };

        // 分子和原子数据
        const molecules = {
            h2: { x: 0, y: 0, atoms: [{type: 'H', x: 0, y: 0}, {type: 'H', x: 0, y: 0}], bondLength: 40 },
            cl2: { x: 0, y: 0, atoms: [{type: 'Cl', x: 0, y: 0}, {type: 'Cl', x: 0, y: 0}], bondLength: 60 },
            hcl1: { x: 0, y: 0, atoms: [{type: 'H', x: 0, y: 0}, {type: 'Cl', x: 0, y: 0}], bondLength: 50 },
            hcl2: { x: 0, y: 0, atoms: [{type: 'H', x: 0, y: 0}, {type: 'Cl', x: 0, y: 0}], bondLength: 50 }
        };

        // 火焰粒子系统
        const flameParticles = [];
        for (let i = 0; i < 80; i++) {
            flameParticles.push({
                x: 0, y: 0,
                vx: (Math.random() - 0.5) * 2,
                vy: -Math.random() * 3 - 1,
                life: Math.random(),
                size: Math.random() * 8 + 4
            });
        }

        // 场景切换
        sceneBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                sceneBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentScene = btn.dataset.scene;
                animationTime = 0;
                updateInfoContent();
                hintText.style.display = currentScene === 'micro' ? 'block' : 'none';
            });
        });

        // 控制按钮事件
        playBtn.addEventListener('click', () => isPlaying = true);
        pauseBtn.addEventListener('click', () => isPlaying = false);
        resetBtn.addEventListener('click', () => {
            animationTime = 0;
            progressSlider.value = 0;
        });

        // 进度条控制
        progressSlider.addEventListener('input', (e) => {
            animationTime = parseInt(e.target.value) / 100;
            isPlaying = false;
        });

        // Canvas鼠标交互
        canvas.addEventListener('mousemove', (e) => {
            if (currentScene !== 'micro') return;
            
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            hoveredObject = null;
            
            // 检查是否悬停在分子上
            Object.keys(molecules).forEach(key => {
                const mol = molecules[key];
                const dx = x - mol.x;
                const dy = y - mol.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 50) {
                    hoveredObject = {
                        type: key,
                        x: mol.x,
                        y: mol.y
                    };
                }
            });
            
            if (hoveredObject) {
                atomLabel.style.display = 'block';
                atomLabel.style.left = hoveredObject.x + 'px';
                atomLabel.style.top = hoveredObject.y + 'px';
                
                let label = '';
                switch(hoveredObject.type) {
                    case 'h2': label = '氢分子 (H₂)'; break;
                    case 'cl2': label = '氯分子 (Cl₂)'; break;
                    case 'hcl1': 
                    case 'hcl2': label = '氯化氢分子 (HCl)'; break;
                }
                atomLabel.textContent = label;
            } else {
                atomLabel.style.display = 'none';
            }
        });

        // 更新信息面板内容
        function updateInfoContent() {
            switch(currentScene) {
                case 'macro':
                    infoContent.innerHTML = `
                        <strong>宏观现象观察：</strong><br>
                        • 氢气在氯气中安静地燃烧<br>
                        • 产生<strong style="color: #adff2f">淡绿黄色火焰</strong><br>
                        • 反应生成氯化氢气体<br>
                        • 实验需在通风橱中进行
                    `;
                    break;
                case 'micro':
                    infoContent.innerHTML = `
                        <strong>微观过程解析：</strong><br>
                        • 氢分子(H₂)和氯分子(Cl₂)在点燃条件下化学键断裂<br>
                        • 氢原子和氯原子重新组合<br>
                        • 形成新的化学键，生成氯化氢分子(HCl)<br>
                        • 这是一个<strong>化合反应</strong>
                    `;
                    break;
                case 'equation':
                    infoContent.innerHTML = `
                        <strong>化学方程式总结：</strong><br>
                        • <strong>H₂ + Cl₂ → 2HCl</strong><br>
                        • 反应类型：化合反应<br>
                        • 反应条件：点燃<br>
                        • 各物质状态：H₂(气态)、Cl₂(气态)、HCl(气态)<br>
                        • 原子守恒：反应前后氢原子和氯原子数目不变
                    `;
                    break;
            }
        }

        // 绘制宏观火焰场景
        function drawMacroScene() {
            const centerX = canvas.width / 2;
            const burnerY = canvas.height * 0.7;
            
            // 绘制背景
            ctx.fillStyle = colors.background.macro;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制燃烧器
            ctx.fillStyle = '#888888';
            ctx.fillRect(centerX - 30, burnerY, 60, 40);
            ctx.fillRect(centerX - 10, burnerY - 20, 20, 20);
            
            // 更新和绘制火焰粒子
            const flameBaseX = centerX;
            const flameBaseY = burnerY - 20;
            
            for (let particle of flameParticles) {
                if (particle.life <= 0) {
                    particle.x = flameBaseX + (Math.random() - 0.5) * 20;
                    particle.y = flameBaseY;
                    particle.life = 1;
                    particle.vx = (Math.random() - 0.5) * 2;
                    particle.vy = -Math.random() * 3 - 1;
                }
                
                particle.x += particle.vx;
                particle.y += particle.vy;
                particle.life -= 0.02;
                
                // 计算粒子颜色（从黄色到黄绿色）
                const gradient = ctx.createRadialGradient(
                    particle.x, particle.y, 0,
                    particle.x, particle.y, particle.size
                );
                
                if (particle.life > 0.5) {
                    gradient.addColorStop(0, colors.flameCore);
                    gradient.addColorStop(1, `rgba(173, 255, 47, ${particle.life * 0.7})`);
                } else {
                    gradient.addColorStop(0, colors.flameEdge);
                    gradient.addColorStop(1, `rgba(173, 255, 47, ${particle.life * 0.5})`);
                }
                
                ctx.fillStyle = gradient;
                ctx.beginPath();
                ctx.arc(particle.x, particle.y, particle.size * particle.life, 0, Math.PI * 2);
                ctx.fill();
            }
            
            // 绘制火焰标签
            ctx.fillStyle = colors.flameEdge;
            ctx.font = 'bold 24px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('淡绿黄色火焰', centerX, burnerY - 100);
        }

        // 绘制微观反应场景
        function drawMicroScene() {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 绘制背景
            ctx.fillStyle = colors.background.micro;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制网格背景
            ctx.strokeStyle = 'rgba(200, 200, 200, 0.2)';
            ctx.lineWidth = 1;
            const gridSize = 40;
            
            for (let x = 0; x < canvas.width; x += gridSize) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();
            }
            
            for (let y = 0; y < canvas.height; y += gridSize) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();
            }
            
            // 计算动画进度
            const t = Math.min(animationTime * 2, 1); // 加快动画速度
            const reactionStage = Math.min(animationTime * 3, 1);
            
            // 更新分子位置
            if (t < 0.5) {
                // 第一阶段：分子相互靠近
                const approachProgress = t * 2;
                molecules.h2.x = centerX - 200 + approachProgress * 150;
                molecules.h2.y = centerY;
                molecules.cl2.x = centerX + 200 - approachProgress * 150;
                molecules.cl2.y = centerY;
            } else if (t < 0.8) {
                // 第二阶段：化学键断裂
                const breakProgress = (t - 0.5) * 3.33;
                molecules.h2.x = centerX - 50;
                molecules.h2.y = centerY;
                molecules.cl2.x = centerX + 50;
                molecules.cl2.y = centerY;
                
                // 高亮显示键断裂
                ctx.fillStyle = colors.highlight;
                ctx.globalAlpha = 0.5;
                ctx.beginPath();
                ctx.arc(centerX, centerY, 30, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1;
            } else {
                // 第三阶段：重新组合成HCl
                const formProgress = (t - 0.8) * 5;
                molecules.hcl1.x = centerX - 100;
                molecules.hcl1.y = centerY - 50;
                molecules.hcl2.x = centerX + 100;
                molecules.hcl2.y = centerY + 50;
            }
            
            // 绘制分子
            function drawMolecule(mol, label) {
                // 更新原子位置
                const angle = Math.PI / 4;
                mol.atoms[0].x = mol.x - Math.cos(angle) * mol.bondLength / 2;
                mol.atoms[0].y = mol.y - Math.sin(angle) * mol.bondLength / 2;
                mol.atoms[1].x = mol.x + Math.cos(angle) * mol.bondLength / 2;
                mol.atoms[1].y = mol.y + Math.sin(angle) * mol.bondLength / 2;
                
                // 绘制化学键
                ctx.strokeStyle = colors.bond;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(mol.atoms[0].x, mol.atoms[0].y);
                ctx.lineTo(mol.atoms[1].x, mol.atoms[1].y);
                ctx.stroke();
                
                // 绘制原子
                mol.atoms.forEach(atom => {
                    ctx.fillStyle = atom.type === 'H' ? colors.hydrogen : colors.chlorine;
                    ctx.beginPath();
                    ctx.arc(atom.x, atom.y, atom.type === 'H' ? 15 : 20, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // 原子标签
                    ctx.fillStyle = colors.text;
                    ctx.font = 'bold 16px Arial';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText(atom.type, atom.x, atom.y);
                });
                
                // 分子标签
                if (label && t < 0.8) {
                    ctx.fillStyle = colors.text;
                    ctx.font = 'bold 18px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(label, mol.x, mol.y + 50);
                }
            }
            
            // 根据动画阶段绘制不同的分子
            if (t < 0.8) {
                drawMolecule(molecules.h2, 'H₂');
                drawMolecule(molecules.cl2, 'Cl₂');
            } else {
                drawMolecule(molecules.hcl1, 'HCl');
                drawMolecule(molecules.hcl2, 'HCl');
            }
            
            // 绘制反应箭头和说明
            ctx.fillStyle = colors.text;
            ctx.font = 'bold 20px Arial';
            ctx.textAlign = 'center';
            
            if (t < 0.5) {
                ctx.fillText('分子相互靠近...', centerX, centerY + 150);
            } else if (t < 0.8) {
                ctx.fillText('化学键断裂，原子分离！', centerX, centerY + 150);
                ctx.fillStyle = colors.highlight;
                ctx.fillText('需要能量！', centerX, centerY + 180);
            } else {
                ctx.fillText('原子重新组合，形成HCl分子', centerX, centerY + 150);
            }
            
            // 高亮悬停的分子
            if (hoveredObject) {
                ctx.strokeStyle = colors.highlight;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(hoveredObject.x, hoveredObject.y, 55, 0, Math.PI * 2);
                ctx.stroke();
            }
        }

        // 绘制方程式总结场景
        function drawEquationScene() {
            // 绘制背景
            ctx.fillStyle = colors.background.equation;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 绘制大标题
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 48px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('氢气在氯气中燃烧', centerX, 80);
            
            // 绘制化学方程式
            ctx.font = 'bold 72px "Courier New", monospace';
            ctx.fillStyle = colors.hydrogen;
            ctx.fillText('H₂', centerX - 180, centerY);
            
            ctx.fillStyle = '#ffffff';
            ctx.fillText('+', centerX - 90, centerY);
            
            ctx.fillStyle = colors.chlorine;
            ctx.fillText('Cl₂', centerX, centerY);
            
            ctx.fillStyle = '#ffffff';
            ctx.fillText('→', centerX + 90, centerY);
            
            ctx.fillStyle = '#ff9800';
            ctx.fillText('2HCl', centerX + 180, centerY);
            
            // 绘制反应条件
            ctx.font = '24px Arial';
            ctx.fillStyle = '#ffcc80';
            ctx.fillText('点燃', centerX, centerY + 40);
            
            // 绘制分子模型图示
            const scale = 0.8 + Math.sin(animationTime * 5) * 0.1;
            
            // 绘制H₂分子
            drawSimpleMolecule(centerX - 250, centerY + 150, 30, colors.hydrogen, 'H', 'H₂', scale);
            
            // 绘制+号
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 36px Arial';
            ctx.fillText('+', centerX - 150, centerY + 150);
            
            // 绘制Cl₂分子
            drawSimpleMolecule(centerX - 50, centerY + 150, 35, colors.chlorine, 'Cl', 'Cl₂', scale);
            
            // 绘制箭头
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 36px Arial';
            ctx.fillText('→', centerX + 50, centerY + 150);
            
            // 绘制2个HCl分子
            drawSimpleMolecule(centerX + 120, centerY + 120, 30, colors.hydrogen, 'H', 'HCl', scale, colors.chlorine);
            drawSimpleMolecule(centerX + 220, centerY + 180, 30, colors.hydrogen, 'H', 'HCl', scale, colors.chlorine);
            
            // 绘制"2×"
            ctx.fillStyle = '#ff9800';
            ctx.font = 'bold 24px Arial';
            ctx.fillText('2 ×', centerX + 70, centerY + 150);
            
            // 绘制说明文字
            ctx.fillStyle = '#c5cae9';
            ctx.font = '20px Arial';
            ctx.textAlign = 'center';
            const lines = [
                '这是一个化合反应',
                '反应前：1个氢分子 + 1个氯分子',
                '反应后：2个氯化氢分子',
                '原子守恒：反应前后原子种类和数目不变'
            ];
            
            lines.forEach((line, i) => {
                ctx.fillText(line, centerX, centerY + 250 + i * 30);
            });
        }
        
        function drawSimpleMolecule(x, y, radius, color1, label1, name, scale, color2 = null) {
            const angle = Math.PI / 4;
            const bondLength = 50 * scale;
            
            const atom1X = x - Math.cos(angle) * bondLength / 2;
            const atom1Y = y - Math.sin(angle) * bondLength / 2;
            const atom2X = x + Math.cos(angle) * bondLength / 2;
            const atom2Y = y + Math.sin(angle) * bondLength / 2;
            
            // 绘制化学键
            ctx.strokeStyle = colors.bond;
            ctx.lineWidth = 3 * scale;
            ctx.beginPath();
            ctx.moveTo(atom1X, atom1Y);
            ctx.lineTo(atom2X, atom2Y);
            ctx.stroke();
            
            // 绘制第一个原子
            ctx.fillStyle = color1;
            ctx.beginPath();
            ctx.arc(atom1X, atom1Y, radius * scale, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.fillStyle = colors.text;
            ctx.font = `bold ${16 * scale}px Arial`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(label1, atom1X, atom1Y);
            
            // 绘制第二个原子
            ctx.fillStyle = color2 || color1;
            ctx.beginPath();
            ctx.arc(atom2X, atom2Y, radius * scale, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.fillStyle = colors.text;
            ctx.fillText(color2 ? 'Cl' : label1, atom2X, atom2Y);
            
            // 绘制分子名称
            ctx.fillStyle = '#ffffff';
            ctx.font = `bold ${18 * scale}px Arial`;
            ctx.fillText(name, x, y + 60 * scale);
        }

        // 主动画循环
        function animate() {
            // 更新动画时间
            if (isPlaying && animationTime < 1) {
                animationTime += animationSpeed;
                progressSlider.value = animationTime * 100;
            }
            
            // 清除画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 根据当前场景绘制
            switch(currentScene) {
                case 'macro':
                    drawMacroScene();
                    break;
                case 'micro':
                    drawMicroScene();
                    break;
                case 'equation':
                    drawEquationScene();
                    break;
            }
            
            requestAnimationFrame(animate);
        }

        // 初始化
        updateInfoContent();
        animate();
    </script>
</body>
</html>
```

### 3. 过程输出


## 《氢气在氯气中燃烧》交互式教学动画使用指南

欢迎使用本交互式教学动画！本工具旨在通过直观、动态的可视化方式，帮助您深入理解氢气在氯气中燃烧这一经典化学反应。无论您是学生、教师还是化学爱好者，都能从中获得启发。

---

### 一、 功能说明

本动画将复杂的化学反应过程拆解为三个相互关联的学习模块，支持您在不同抽象层次之间自由切换和探索：

1.  **宏观火焰模块**：模拟真实的实验现象，展示氢气在氯气中燃烧时产生的标志性**淡绿黄色火焰**。
2.  **微观反应模块**：揭示宏观现象背后的本质，以球棍模型动态演示氢分子与氯分子如何断裂化学键，并重新组合生成氯化氢分子的全过程。
3.  **方程式总结模块**：将动态的微观过程与静态的化学方程式 `H₂ + Cl₂ → 2HCl` 联系起来，并阐释其背后的守恒原理。

---

### 二、 主要功能

*   **场景自由切换**：通过顶部的场景选择按钮（🔥 宏观火焰 / 🔬 微观反应 / 📝 方程式总结），您可以随时在三个核心学习模块间跳转，构建完整的知识链条。
*   **动画全程控制**：
    *   **播放/暂停**：控制动画的进行，便于在关键步骤暂停观察。
    *   **重置**：一键将动画恢复到初始状态。
    *   **进度条**：拖动滑块可以快速定位到动画的任意时间点，方便回顾特定阶段。
*   **智能交互提示**：
    *   在**微观反应**场景中，将鼠标悬停在任意分子上，会高亮显示该分子并弹出其化学式标签（如“氢分子 H₂”）。
    *   界面底部的“当前学习要点”面板会根据您所在的场景，动态更新核心知识说明。
*   **自适应设计**：动画界面会根据您的屏幕尺寸自动调整，确保在电脑、平板等设备上都能获得良好的观看体验。

---

### 三、 设计特色

1.  **遵循科学认知规律**：设计严格遵循“宏观现象 → 微观解释 → 符号表达”的科学认知路径，帮助您逐步建立从感性到理性的深刻理解。
2.  **精准的科学可视化**：
    *   宏观火焰采用粒子系统模拟，生动再现了淡绿黄色的火焰特征。
    *   微观过程使用标准球棍模型（白色小球代表氢原子，黄绿色小球代表氯原子），化学键的断裂与形成过程清晰醒目。
3.  **专业的视觉设计**：
    *   采用深色背景突出火焰，浅色背景聚焦分子模型，色彩运用既符合科学事实，又保证了最佳的视觉清晰度。
    *   在化学键断裂等关键步骤，使用高亮色进行强调，直观展示反应需要能量的概念。
4.  **沉浸式学习体验**：流畅的动画、即时的交互反馈以及同步的知识点提示，共同营造了一个引人入胜的自主探索环境。

---

### 四、 教学要点

通过本动画，您可以重点观察和理解以下核心知识点：

*   **宏观辨识**：认识氢气在氯气中燃烧的**淡绿黄色火焰**这一独特现象。
*   **微观探析**：
    *   理解化学反应是**分子破裂成原子，原子重新组合成新分子**的过程。
    *   观察 **H₂ 分子和 Cl₂ 分子化学键的断裂**，以及 **H 原子与 Cl 原子间新键的形成**。
    *   建立“点燃”条件为反应提供所需能量的初步概念。
*   **符号表征**：
    *   掌握该反应的化学方程式：**H₂ + Cl₂ →(点燃) 2HCl**。
    *   理解方程式中的系数“2”表示生成物的分子数量，并认识该反应属于**化合反应**。
    *   领悟化学反应中**原子种类与数目守恒**的根本规律。

---

### 五、 使用建议

为了获得最佳学习效果，我们建议您按以下流程进行探索：

1.  **初次观看**：点击 **“播放”** 按钮，让动画完整运行一遍，对整个过程形成整体印象。
2.  **分步精研**：
    *   切换到 **“宏观火焰”** 场景，观察火焰颜色和状态。
    *   切换到 **“微观反应”** 场景，使用 **“暂停”** 按钮，在“分子靠近”、“键的断裂”、“原子重组”等关键步骤停下来，结合提示文字仔细观察。
    *   利用**进度条**反复观看难以理解的部分。
    *   尝试**鼠标悬停**在分子上，确认每一种反应物和生成物。
3.  **总结升华**：进入 **“方程式总结”** 场景，回顾整个反应过程，思考化学方程式如何精炼地概括了您刚才看到的所有微观变化和宏观事实。
4.  **教学应用**：教师可将此动画作为课堂演示工具，引导学生逐步探究；学生可将其作为课后复习与自主探究的利器，深化理解。

希望这个交互式动画能点燃您对化学的好奇心，让学习过程像那簇淡绿黄色的火焰一样，生动而明亮！祝您探索愉快！