# 需求：镁条在空气中燃烧（剧烈白光+微观：Mg原子与O₂分子反应）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为初中或高中化学初学者。他们需要直观地理解一个抽象的化学反应过程。
2.  **核心需求**：
    *   **宏观现象可视化**：清晰、生动地展示镁条燃烧时“剧烈白光”这一显著且危险的实验现象，弥补课堂演示因强光、短暂而难以观察的不足。
    *   **微观本质解释**：将宏观现象与微观的原子、分子反应过程联系起来，建立“宏观-微观-符号”三重表征的化学思维，这是教学的重点和难点。
    *   **安全与可控**：提供一个绝对安全、可反复观看、可控制的虚拟实验环境。
    *   **主动探索**：允许用户通过交互操作，控制动画进程，加深对反应条件和过程的理解。

#### 教学设计思路
1.  **核心概念**：
    *   化学反应的本质是原子的重新组合（分子破裂，原子重组）。
    *   该反应为氧化反应（与氧气反应），伴随发光、放热等现象。
    *   化学方程式：2Mg + O₂ → 2MgO。
2.  **认知规律（流程设计）**：
    *   **从已知到未知**：先展示学生熟悉的“镁条”和“空气”背景。
    *   **从宏观到微观**：先呈现震撼的燃烧白光现象，引发疑问“为什么会这样？”，再切入微观世界揭示本质。
    *   **从静态到动态**：先展示反应物（Mg原子、O₂分子）的静止状态，再动态演示化学键断裂、原子移动、新键形成的过程。
    *   **归纳总结**：动画结束后，清晰呈现反应方程式和文字描述，将动态过程符号化。
3.  **交互设计**：
    *   **分步引导**：设计“下一步”按钮，将学习过程分解为可控的步骤，避免信息过载。
    *   **关键控制**：提供“点燃/开始反应”、“暂停/继续”、“重置”按钮，让用户掌握学习节奏。
    *   **视角切换**：提供“宏观视图”与“微观视图”的切换按钮，帮助用户建立两者联系。
    *   **提示与标签**：在微观视图中，鼠标悬停在原子或分子上时显示名称（如“Mg原子”、“O₂分子”），降低认知负荷。
4.  **视觉呈现**：
    *   **宏观场景**：采用写实风格，深色背景（模拟实验室或夜晚）以突出白光。镁条有金属质感，燃烧时白光有“绽放”和“闪烁”的动态效果。
    *   **微观场景**：采用简明的球棍模型或比例模型。
        *   **Mg原子**：用银灰色小球表示。
        *   **O原子**：用红色小球表示。
        *   **O₂分子**：用两个由化学键（短线）连接的红色小球表示。
        *   **MgO**：用银灰色小球和红色小球紧密相邻（或由短线连接）表示。
    *   **动画效果**：
        *   **化学键断裂**：用短线拉伸、变淡、消失的动画表示。
        *   **原子运动**：原子从原位置平滑移动到新位置，路径清晰。
        *   **能量释放**：用从反应中心向外扩散的同心圆波纹或光晕表示“放热”，与宏观的白光相呼应。

#### 配色方案选择
*   **主背景色**：深灰蓝色 (#1a2734)。营造专注的“实验室”或“夜空”感，能极致地衬托白光。
*   **宏观镁条**：银白色线性渐变，模拟金属光泽。
*   **燃烧白光**：核心为亮白色 (#ffffff)，向外渐变为淡黄色 (#ffff99) 和浅橙色 (#ffcc66)，表现高温和强光。
*   **微观模型**：
    *   **镁原子 (Mg)**：浅灰色 (#cccccc) 或银灰色 (#c0c0c0)。
    *   **氧原子 (O)**：红色 (#ff3333)，符合化学教学中对氧元素的常规配色。
    *   **化学键**：深灰色 (#555555)。
*   **界面与控制按钮**：半透明深色背景，按钮使用蓝色系 (#4a9eff) 表示可操作，绿色 (#4CAF50) 表示开始/继续，红色 (#f44336) 表示重置。
*   **文本与提示**：白色或浅灰色，确保在深色背景上清晰可读。

#### 交互功能列表
1.  **流程控制按钮**：
    *   `下一步`：按预设教学步骤（如：展示材料 -> 宏观现象 -> 切入微观 -> 展示反应 -> 总结）推进动画与解说。
    *   `上一步`：返回上一个教学步骤。
2.  **动画控制按钮**：
    *   `点燃 / 开始反应`：在宏观视图下，触发燃烧动画；在微观视图下，触发原子分子反应动画。
    *   `暂停 / 继续`：在反应过程中随时暂停，观察中间状态。
    *   `重置`：将动画恢复到初始状态。
3.  **视图切换按钮**：
    *   `宏观视图`：切换到展示镁条燃烧的宏观场景。
    *   `微观视图`：切换到展示原子、分子反应的微观场景。
4.  **信息提示交互**：
    *   **鼠标悬停提示**：在微观视图中，将鼠标悬停在原子、分子或生成物上时，显示其化学名称和符号（如“镁原子， Mg”）。
    *   **高亮与标签**：在分步讲解时，自动高亮当前正在讲解的部分，并配以文字标签。
5.  **化学方程式展示**：在动画的总结阶段，动态地、逐步地显示并高亮化学方程式 `2Mg + O₂ → 2MgO`，与刚观看的动画过程对应。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>镁条在空气中燃烧 - 宏观与微观教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
            color: #e0e0e0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
            width: 100%;
            max-width: 900px;
        }

        h1 {
            color: #ffffff;
            margin-bottom: 8px;
            font-size: 2.2rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }

        .subtitle {
            color: #a0d2ff;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 900px;
            gap: 20px;
        }

        .animation-area {
            width: 100%;
            height: 500px;
            background-color: #1a2734;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            border: 1px solid #2a3a4a;
        }

        #mainCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 12px;
            width: 100%;
            padding: 15px;
            background: rgba(30, 40, 55, 0.8);
            border-radius: 10px;
            border: 1px solid #3a4a5a;
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            min-width: 120px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn-primary {
            background-color: #4a9eff;
            color: white;
        }

        .btn-primary:hover {
            background-color: #3a8eef;
        }

        .btn-success {
            background-color: #4CAF50;
            color: white;
        }

        .btn-success:hover {
            background-color: #3d9b41;
        }

        .btn-warning {
            background-color: #ff9800;
            color: white;
        }

        .btn-warning:hover {
            background-color: #e68900;
        }

        .btn-danger {
            background-color: #f44336;
            color: white;
        }

        .btn-danger:hover {
            background-color: #e53935;
        }

        .btn-view {
            background-color: #673ab7;
            color: white;
        }

        .btn-view:hover {
            background-color: #5e35b1;
        }

        .btn:disabled {
            background-color: #555;
            color: #999;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .info-panel {
            width: 100%;
            background: rgba(25, 35, 50, 0.9);
            border-radius: 10px;
            padding: 20px;
            border-left: 5px solid #4a9eff;
            line-height: 1.6;
        }

        .info-panel h3 {
            color: #4a9eff;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .step-indicator {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 15px;
        }

        .step {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #3a4a5a;
            transition: background-color 0.3s;
        }

        .step.active {
            background-color: #4a9eff;
            box-shadow: 0 0 8px #4a9eff;
        }

        .equation {
            text-align: center;
            font-size: 1.8rem;
            margin: 15px 0;
            padding: 15px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            font-family: 'Cambria', 'Times New Roman', serif;
        }

        .highlight {
            color: #ffcc00;
            font-weight: bold;
        }

        .legend {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }

        .tooltip {
            position: absolute;
            background: rgba(0, 0, 0, 0.85);
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.9rem;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
            z-index: 100;
            border: 1px solid #444;
            max-width: 200px;
        }

        @media (max-width: 768px) {
            .controls {
                flex-direction: column;
                align-items: center;
            }
            
            .btn {
                width: 100%;
                max-width: 300px;
            }
            
            .animation-area {
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔥 镁条在空气中燃烧</h1>
        <p class="subtitle">宏观现象与微观反应过程的可视化教学动画</p>
    </div>

    <div class="container">
        <div class="step-indicator">
            <div class="step active" data-step="0"></div>
            <div class="step" data-step="1"></div>
            <div class="step" data-step="2"></div>
            <div class="step" data-step="3"></div>
            <div class="step" data-step="4"></div>
        </div>

        <div class="animation-area">
            <canvas id="mainCanvas"></canvas>
            <div class="tooltip" id="tooltip"></div>
        </div>

        <div class="controls">
            <button class="btn btn-primary" id="prevBtn">
                <span>◀</span> 上一步
            </button>
            <button class="btn btn-success" id="nextBtn">
                下一步 <span>▶</span>
            </button>
            <button class="btn btn-warning" id="startBtn">
                🔥 点燃/开始反应
            </button>
            <button class="btn btn-warning" id="pauseBtn">
                ⏸️ 暂停/继续
            </button>
            <button class="btn btn-danger" id="resetBtn">
                ↺ 重置
            </button>
            <button class="btn btn-view" id="macroViewBtn">
                🔍 宏观视图
            </button>
            <button class="btn btn-view" id="microViewBtn">
                ⚛️ 微观视图
            </button>
        </div>

        <div class="info-panel">
            <h3>📚 教学信息</h3>
            <div id="infoText">
                <p><strong>当前步骤：</strong> 准备阶段 - 观察镁条和空气环境</p>
                <p><strong>说明：</strong> 这是一个安全、可控的虚拟实验环境。请点击"下一步"开始学习，或直接使用"点燃"按钮触发反应。</p>
            </div>
            
            <div class="equation" id="equation">
                2Mg + O₂ → 2MgO
            </div>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #cccccc;"></div>
                    <span>镁原子 (Mg)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #ff3333;"></div>
                    <span>氧原子 (O)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #ffff99;"></div>
                    <span>燃烧白光</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #4CAF50;"></div>
                    <span>氧化镁 (MgO)</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 全局变量和状态管理
        const canvas = document.getElementById('mainCanvas');
        const ctx = canvas.getContext('2d');
        const tooltip = document.getElementById('tooltip');
        const infoText = document.getElementById('infoText');
        const equation = document.getElementById('equation');
        
        // 设置Canvas尺寸
        function resizeCanvas() {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        }
        
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();
        
        // 动画状态
        let animationState = {
            currentStep: 0,
            totalSteps: 5,
            isMacroView: true,
            isReactionStarted: false,
            isPaused: false,
            reactionProgress: 0,
            animationFrameId: null,
            lastTimestamp: 0
        };
        
        // 步骤信息
        const stepInfo = [
            {
                title: "准备阶段",
                description: "观察实验材料：镁条（银白色金属）和空气中的氧气。在宏观视图中，你可以看到镁条放置在空气中。点击'微观视图'按钮可以查看原子和分子的初始状态。",
                equation: "准备反应物..."
            },
            {
                title: "宏观现象：点燃镁条",
                description: "点击'点燃'按钮，观察镁条在空气中燃烧的宏观现象。你会看到剧烈的白光，这是镁与氧气反应释放大量能量的表现。",
                equation: "2Mg + O₂ + 能量 → ?"
            },
            {
                title: "微观视角：化学键断裂",
                description: "切换到微观视图。氧气分子（O₂）中的化学键和镁原子之间的金属键在能量作用下断裂。注意观察化学键（灰色短线）的断裂过程。",
                equation: "2Mg + O₂ → 2Mg + 2O (原子)"
            },
            {
                title: "微观视角：原子重组",
                description: "自由的镁原子和氧原子重新组合，形成新的化学键，生成氧化镁（MgO）。注意原子移动的路径和新键的形成。",
                equation: "2Mg + 2O → 2MgO"
            },
            {
                title: "总结与化学方程式",
                description: "反应完成！镁与氧气反应生成氧化镁，同时释放大量能量（以光和热的形式）。这就是镁条燃烧发出剧烈白光的原因。",
                equation: "2Mg + O₂ → 2MgO + 能量（光与热）"
            }
        ];
        
        // 微观元素定义
        const microElements = {
            mgAtoms: [],
            o2Molecules: [],
            freeOAtoms: [],
            mgoMolecules: [],
            bonds: []
        };
        
        // 宏观元素定义
        const macroElements = {
            magnesiumStrip: {
                x: 0,
                y: 0,
                width: 0,
                height: 0,
                color: '#e0e0e0'
            },
            flames: [],
            lightEffects: []
        };
        
        // 初始化微观元素
        function initMicroElements() {
            microElements.mgAtoms = [];
            microElements.o2Molecules = [];
            microElements.freeOAtoms = [];
            microElements.mgoMolecules = [];
            microElements.bonds = [];
            
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 创建镁原子（左侧）
            for (let i = 0; i < 4; i++) {
                microElements.mgAtoms.push({
                    x: centerX - 150 + i * 40,
                    y: centerY,
                    radius: 12,
                    color: '#cccccc',
                    targetX: centerX - 150 + i * 40,
                    targetY: centerY,
                    isMoving: false,
                    type: 'mg'
                });
            }
            
            // 创建氧气分子（右侧）
            for (let i = 0; i < 2; i++) {
                const o2X = centerX + 100 + i * 80;
                const o2Y = centerY;
                
                microElements.o2Molecules.push({
                    x: o2X,
                    y: o2Y,
                    atoms: [
                        {x: o2X - 8, y: o2Y, radius: 10, color: '#ff3333', type: 'o'},
                        {x: o2X + 8, y: o2Y, radius: 10, color: '#ff3333', type: 'o'}
                    ],
                    bondLength: 16,
                    isBondBroken: false
                });
                
                // 添加化学键
                microElements.bonds.push({
                    x1: o2X - 8,
                    y1: o2Y,
                    x2: o2X + 8,
                    y2: o2Y,
                    width: 3,
                    color: '#555555',
                    isVisible: true
                });
            }
        }
        
        // 初始化宏观元素
        function initMacroElements() {
            macroElements.magnesiumStrip = {
                x: canvas.width / 2 - 100,
                y: canvas.height / 2 - 15,
                width: 200,
                height: 30,
                color: '#e0e0e0'
            };
            
            macroElements.flames = [];
            macroElements.lightEffects = [];
        }
        
        // 更新步骤指示器
        function updateStepIndicator() {
            const steps = document.querySelectorAll('.step');
            steps.forEach((step, index) => {
                if (index === animationState.currentStep) {
                    step.classList.add('active');
                } else {
                    step.classList.remove('active');
                }
            });
        }
        
        // 更新信息面板
        function updateInfoPanel() {
            const step = stepInfo[animationState.currentStep];
            infoText.innerHTML = `
                <p><strong>当前步骤：</strong> ${step.title}</p>
                <p><strong>说明：</strong> ${step.description}</p>
            `;
            
            // 高亮方程式的不同部分
            let eqHTML = step.equation;
            if (animationState.currentStep === 4) {
                eqHTML = eqHTML.replace(/(2Mg)/g, '<span class="highlight">$1</span>')
                              .replace(/(O₂)/g, '<span class="highlight">$1</span>')
                              .replace(/(2MgO)/g, '<span class="highlight">$1</span>');
            }
            equation.innerHTML = eqHTML;
        }
        
        // 绘制微观场景
        function drawMicroScene() {
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景
            ctx.fillStyle = '#1a2734';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制标题
            ctx.fillStyle = '#4a9eff';
            ctx.font = 'bold 20px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('微观视图：原子与分子的反应', canvas.width / 2, 40);
            
            // 绘制反应物标签
            ctx.fillStyle = '#a0d2ff';
            ctx.font = '16px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('反应物', canvas.width / 2 - 200, 80);
            ctx.textAlign = 'right';
            ctx.fillText('生成物', canvas.width / 2 + 200, 80);
            ctx.textAlign = 'center';
            
            // 绘制化学键
            microElements.bonds.forEach(bond => {
                if (bond.isVisible) {
                    ctx.beginPath();
                    ctx.moveTo(bond.x1, bond.y1);
                    ctx.lineTo(bond.x2, bond.y2);
                    ctx.strokeStyle = bond.color;
                    ctx.lineWidth = bond.width;
                    ctx.stroke();
                }
            });
            
            // 绘制镁原子
            microElements.mgAtoms.forEach(atom => {
                // 绘制原子
                const gradient = ctx.createRadialGradient(
                    atom.x, atom.y, 0,
                    atom.x, atom.y, atom.radius
                );
                gradient.addColorStop(0, '#ffffff');
                gradient.addColorStop(1, atom.color);
                
                ctx.beginPath();
                ctx.arc(atom.x, atom.y, atom.radius, 0, Math.PI * 2);
                ctx.fillStyle = gradient;
                ctx.fill();
                
                // 绘制原子符号
                ctx.fillStyle = '#333';
                ctx.font = 'bold 14px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('Mg', atom.x, atom.y);
            });
            
            // 绘制氧气分子和自由氧原子
            microElements.o2Molecules.forEach(molecule => {
                molecule.atoms.forEach(atom => {
                    const gradient = ctx.createRadialGradient(
                        atom.x, atom.y, 0,
                        atom.x, atom.y, atom.radius
                    );
                    gradient.addColorStop(0, '#ffffff');
                    gradient.addColorStop(1, atom.color);
                    
                    ctx.beginPath();
                    ctx.arc(atom.x, atom.y, atom.radius, 0, Math.PI * 2);
                    ctx.fillStyle = gradient;
                    ctx.fill();
                    
                    ctx.fillStyle = '#333';
                    ctx.font = 'bold 12px Arial';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText('O', atom.x, atom.y);
                });
            });
            
            // 绘制自由氧原子
            microElements.freeOAtoms.forEach(atom => {
                const gradient = ctx.createRadialGradient(
                    atom.x, atom.y, 0,
                    atom.x, atom.y, atom.radius
                );
                gradient.addColorStop(0, '#ffffff');
                gradient.addColorStop(1, atom.color);
                
                ctx.beginPath();
                ctx.arc(atom.x, atom.y, atom.radius, 0, Math.PI * 2);
                ctx.fillStyle = gradient;
                ctx.fill();
                
                ctx.fillStyle = '#333';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('O', atom.x, atom.y);
            });
            
            // 绘制氧化镁分子
            microElements.mgoMolecules.forEach(molecule => {
                // 绘制镁原子
                const mgGradient = ctx.createRadialGradient(
                    molecule.mg.x, molecule.mg.y, 0,
                    molecule.mg.x, molecule.mg.y, molecule.mg.radius
                );
                mgGradient.addColorStop(0, '#ffffff');
                mgGradient.addColorStop(1, molecule.mg.color);
                
                ctx.beginPath();
                ctx.arc(molecule.mg.x, molecule.mg.y, molecule.mg.radius, 0, Math.PI * 2);
                ctx.fillStyle = mgGradient;
                ctx.fill();
                
                ctx.fillStyle = '#333';
                ctx.font = 'bold 14px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('Mg', molecule.mg.x, molecule.mg.y);
                
                // 绘制氧原子
                const oGradient = ctx.createRadialGradient(
                    molecule.o.x, molecule.o.y, 0,
                    molecule.o.x, molecule.o.y, molecule.o.radius
                );
                oGradient.addColorStop(0, '#ffffff');
                oGradient.addColorStop(1, molecule.o.color);
                
                ctx.beginPath();
                ctx.arc(molecule.o.x, molecule.o.y, molecule.o.radius, 0, Math.PI * 2);
                ctx.fillStyle = oGradient;
                ctx.fill();
                
                ctx.fillStyle = '#333';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('O', molecule.o.x, molecule.o.y);
                
                // 绘制化学键
                if (molecule.bondVisible) {
                    ctx.beginPath();
                    ctx.moveTo(molecule.mg.x, molecule.mg.y);
                    ctx.lineTo(molecule.o.x, molecule.o.y);
                    ctx.strokeStyle = '#4CAF50';
                    ctx.lineWidth = 3;
                    ctx.stroke();
                }
            });
            
            // 绘制反应进度箭头
            if (animationState.reactionProgress > 0) {
                ctx.strokeStyle = '#4a9eff';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(canvas.width / 2 - 50, canvas.height / 2);
                ctx.lineTo(canvas.width / 2 + 50, canvas.height / 2);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // 绘制箭头
                ctx.fillStyle = '#4a9eff';
                ctx.beginPath();
                ctx.moveTo(canvas.width / 2 + 50, canvas.height / 2);
                ctx.lineTo(canvas.width / 2 + 40, canvas.height / 2 - 5);
                ctx.lineTo(canvas.width / 2 + 40, canvas.height / 2 + 5);
                ctx.closePath();
                ctx.fill();
            }
        }
        
        // 绘制宏观场景
        function drawMacroScene() {
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景
            const gradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
            gradient.addColorStop(0, '#0a1929');
            gradient.addColorStop(1, '#1a2734');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制标题
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 20px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('宏观视图：镁条在空气中燃烧', canvas.width / 2, 40);
            
            // 绘制实验台
            ctx.fillStyle = '#3a2c1a';
            ctx.fillRect(0, canvas.height - 100, canvas.width, 100);
            
            // 绘制实验台纹理
            ctx.strokeStyle = '#2a1c0a';
            ctx.lineWidth = 2;
            for (let i = 0; i < canvas.width; i += 20) {
                ctx.beginPath();
                ctx.moveTo(i, canvas.height - 100);
                ctx.lineTo(i, canvas.height);
                ctx.stroke();
            }
            
            // 绘制镁条
            const mg = macroElements.magnesiumStrip;
            
            // 金属光泽效果
            const mgGradient = ctx.createLinearGradient(mg.x, mg.y, mg.x, mg.y + mg.height);
            mgGradient.addColorStop(0, '#ffffff');
            mgGradient.addColorStop(0.3, mg.color);
            mgGradient.addColorStop(0.7, mg.color);
            mgGradient.addColorStop(1, '#a0a0a0');
            
            ctx.fillStyle = mgGradient;
            ctx.fillRect(mg.x, mg.y, mg.width, mg.height);
            
            // 镁条高光
            ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.fillRect(mg.x + 5, mg.y + 5, mg.width - 10, 8);
            
            // 绘制燃烧效果
            if (animationState.isReactionStarted && animationState.reactionProgress > 0) {
                // 计算燃烧强度
                const intensity = Math.sin(Date.now() / 100) * 0.3 + 0.7;
                
                // 绘制白光核心
                const lightGradient = ctx.createRadialGradient(
                    mg.x + mg.width / 2, mg.y, 0,
                    mg.x + mg.width / 2, mg.y, 100 * intensity
                );
                lightGradient.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
                lightGradient.addColorStop(0.3, 'rgba(255, 255, 153, 0.7)');
                lightGradient.addColorStop(0.6, 'rgba(255, 204, 102, 0.4)');
                lightGradient.addColorStop(1, 'rgba(255, 153, 51, 0)');
                
                ctx.fillStyle = lightGradient;
                ctx.beginPath();
                ctx.arc(mg.x + mg.width / 2, mg.y, 100 * intensity, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制火花
                const now = Date.now();
                if (now % 100 < 20) {
                    for (let i = 0; i < 5; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const distance = 50 + Math.random() * 50;
                        const sparkX = mg.x + mg.width / 2 + Math.cos(angle) * distance;
                        const sparkY = mg.y + Math.sin(angle) * distance;
                        
                        ctx.beginPath();
                        ctx.arc(sparkX, sparkY, 2 + Math.random() * 3, 0, Math.PI * 2);
                        ctx.fillStyle = `rgba(255, ${200 + Math.random() * 55}, 0, 0.8)`;
                        ctx.fill();
                    }
                }
                
                // 添加光晕效果到整个场景
                ctx.fillStyle = 'rgba(255, 255, 200, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }
            
            // 绘制标签
            ctx.fillStyle = '#a0d2ff';
            ctx.font = '16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('镁条 (Mg)', mg.x + mg.width / 2, mg.y + mg.height + 25);
            
            if (!animationState.isReactionStarted) {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
                ctx.font = 'italic 14px Arial';
                ctx.fillText('点击"点燃"按钮开始反应', canvas.width / 2, canvas.height - 40);
            }
        }
        
        // 微观反应动画
        function animateMicroReaction(timestamp) {
            if (!animationState.lastTimestamp) {
                animationState.lastTimestamp = timestamp;
            }
            
            const deltaTime = timestamp - animationState.lastTimestamp;
            animationState.lastTimestamp = timestamp;
            
            if (animationState.isPaused) {
                animationState.animationFrameId = requestAnimationFrame(animateMicroReaction);
                drawMicroScene();
                return;
            }
            
            // 更新反应进度
            if (animationState.isReactionStarted && animationState.reactionProgress < 1) {
                animationState.reactionProgress += deltaTime / 3000; // 3秒完成反应
                if (animationState.reactionProgress > 1) {
                    animationState.reactionProgress = 1;
                }
            }
            
            // 根据反应进度更新微观元素
            const progress = animationState.reactionProgress;
            
            // 阶段1: 化学键断裂 (0-0.3)
            if (progress > 0 && progress <= 0.3) {
                const bondBreakProgress = progress / 0.3;
                
                // 氧气分子化学键断裂
                microElements.o2Molecules.forEach((molecule, index) => {
                    if (!molecule.isBondBroken) {
                        // 更新原子位置（稍微分开）
                        molecule.atoms[0].x = molecule.x - 8 - bondBreakProgress * 20;
                        molecule.atoms[1].x = molecule.x + 8 + bondBreakProgress * 20;
                        
                        // 更新化学键
                        if (microElements.bonds[index]) {
                            microElements.bonds[index].x1 = molecule.atoms[0].x;
                            microElements.bonds[index].x2 = molecule.atoms[1].x;
                            microElements.bonds[index].width = 3 * (1 - bondBreakProgress);
                        }
                        
                        if (bondBreakProgress >= 1) {
                            molecule.isBondBroken = true;
                            // 将氧原子添加到自由原子列表
                            microElements.freeOAtoms.push(
                                {...molecule.atoms[0], targetX: canvas.width / 2 - 30, targetY: canvas.height / 2},
                                {...molecule.atoms[1], targetX: canvas.width / 2 + 30, targetY: canvas.height / 2}
                            );
                        }
                    }
                });
            }
            
            // 阶段2: 原子移动和重组 (0.3-0.8)
            if (progress > 0.3 && progress <= 0.8) {
                const moveProgress = (progress - 0.3) / 0.5;
                
                // 镁原子移动
                microElements.mgAtoms.forEach((atom, index) => {
                    atom.targetX = canvas.width / 2 - 60 + (index % 2) * 40;
                    atom.targetY = canvas.height / 2 - 20 + Math.floor(index / 2) * 40;
                    
                    atom.x += (atom.targetX - atom.x) * 0.05;
                    atom.y += (atom.targetY - atom.y) * 0.05;
                });
                
                // 自由氧原子移动
                microElements.freeOAtoms.forEach((atom, index) => {
                    atom.x += (atom.targetX - atom.x) * 0.05;
                    atom.y += (atom.targetY - atom.y) * 0.05;
                });
            }
            
            // 阶段3: 形成氧化镁 (0.8-1)
            if (progress > 0.8 && progress <= 1) {
                const formationProgress = (progress - 0.8) / 0.2;
                
                // 创建氧化镁分子（如果尚未创建）
                if (microElements.mgoMolecules.length === 0) {
                    for (let i = 0; i < 4; i++) {
                        const row = Math.floor(i / 2);
                        const col = i % 2;
                        
                        microElements.mgoMolecules.push({
                            mg: {
                                x: canvas.width / 2 + 100 + col * 80,
                                y: canvas.height / 2 - 40 + row * 80,
                                radius: 12,
                                color: '#cccccc',
                                type: 'mg'
                            },
                            o: {
                                x: canvas.width / 2 + 100 + col * 80 + 20,
                                y: canvas.height / 2 - 40 + row * 80,
                                radius: 10,
                                color: '#ff3333',
                                type: 'o'
                            },
                            bondVisible: false
                        });
                    }
                }
                
                // 动画显示氧化镁分子
                microElements.mgoMolecules.forEach(molecule => {
                    molecule.bondVisible = formationProgress > 0.5;
                    
                    // 渐变动画
                    if (formationProgress < 1) {
                        molecule.mg.color = `rgb(${Math.floor(204 + 51 * formationProgress)}, ${Math.floor(204 + 51 * formationProgress)}, ${Math.floor(204 + 51 * formationProgress)})`;
                        molecule.o.color = `rgb(${Math.floor(255 - 102 * formationProgress)}, ${Math.floor(51 + 102 * formationProgress)}, ${Math.floor(51 + 102 * formationProgress)})`;
                    }
                });
            }
            
            drawMicroScene();
            
            if (animationState.isReactionStarted && animationState.reactionProgress < 1) {
                animationState.animationFrameId = requestAnimationFrame(animateMicroReaction);
            }
        }
        
        // 宏观燃烧动画
        function animateMacroReaction(timestamp) {
            if (!animationState.lastTimestamp) {
                animationState.lastTimestamp = timestamp;
            }
            
            const deltaTime = timestamp - animationState.lastTimestamp;
            animationState.lastTimestamp = timestamp;
            
            if (animationState.isPaused) {
                animationState.animationFrameId = requestAnimationFrame(animateMacroReaction);
                drawMacroScene();
                return;
            }
            
            // 更新反应进度
            if (animationState.isReactionStarted && animationState.reactionProgress < 1) {
                animationState.reactionProgress += deltaTime / 2000; // 2秒完成宏观反应
                if (animationState.reactionProgress > 1) {
                    animationState.reactionProgress = 1;
                }
            }
            
            drawMacroScene();
            
            if (animationState.isReactionStarted && animationState.reactionProgress < 1) {
                animationState.animationFrameId = requestAnimationFrame(animateMacroReaction);
            }
        }
        
        // 主动画循环
        function animate(timestamp) {
            if (animationState.isMacroView) {
                animateMacroReaction(timestamp);
            } else {
                animateMicroReaction(timestamp);
            }
        }
        
        // 开始动画
        function startAnimation() {
            if (animationState.animationFrameId) {
                cancelAnimationFrame(animationState.animationFrameId);
            }
            animationState.lastTimestamp = 0;
            animationState.animationFrameId = requestAnimationFrame(animate);
        }
        
        // 事件处理函数
        function goToStep(step) {
            if (step >= 0 && step < animationState.totalSteps) {
                animationState.currentStep = step;
                
                // 根据步骤更新状态
                if (step === 1 || step === 2 || step === 3) {
                    if (!animationState.isReactionStarted) {
                        animationState.isReactionStarted = true;
                        animationState.reactionProgress = 0;
                    }
                }
                
                if (step === 2 || step === 3) {
                    animationState.isMacroView = false;
                    document.getElementById('macroViewBtn').classList.remove('active');
                    document.getElementById('microViewBtn').classList.add('active');
                } else if (step === 1) {
                    animationState.isMacroView = true;
                    document.getElementById('macroViewBtn').classList.add('active');
                    document.getElementById('microViewBtn').classList.remove('active');
                }
                
                updateStepIndicator();
                updateInfoPanel();
                startAnimation();
            }
        }

function nextStep() {
    if (animationState.currentStep < animationState.totalSteps - 1) {
        goToStep(animationState.currentStep + 1);
    }
}

function prevStep() {
    if (animationState.currentStep > 0) {
        goToStep(animationState.currentStep - 1);
    }
}

function startReaction() {
    if (!animationState.isReactionStarted) {
        animationState.isReactionStarted = true;
        animationState.reactionProgress = 0;
        animationState.isPaused = false;
        
        // 如果当前在步骤0，自动跳到步骤1
        if (animationState.currentStep === 0) {
            goToStep(1);
        } else {
            startAnimation();
        }
        
        document.getElementById('startBtn').disabled = true;
        document.getElementById('pauseBtn').textContent = '⏸️ 暂停';
    }
}

function togglePause() {
    animationState.isPaused = !animationState.isPaused;
    document.getElementById('pauseBtn').textContent = animationState.isPaused ? '▶️ 继续' : '⏸️ 暂停';
    
    if (!animationState.isPaused) {
        startAnimation();
    }
}

function resetAnimation() {
    // 停止当前动画
    if (animationState.animationFrameId) {
        cancelAnimationFrame(animationState.animationFrameId);
        animationState.animationFrameId = null;
    }
    
    // 重置状态
    animationState.currentStep = 0;
    animationState.isReactionStarted = false;
    animationState.isPaused = false;
    animationState.reactionProgress = 0;
    animationState.isMacroView = true;
    
    // 重新初始化元素
    initMicroElements();
    initMacroElements();
    
    // 更新UI
    updateStepIndicator();
    updateInfoPanel();
    document.getElementById('startBtn').disabled = false;
    document.getElementById('pauseBtn').textContent = '⏸️ 暂停';
    document.getElementById('macroViewBtn').classList.add('active');
    document.getElementById('microViewBtn').classList.remove('active');
    
    // 绘制初始场景
    drawMacroScene();
}

function switchToMacroView() {
    animationState.isMacroView = true;
    document.getElementById('macroViewBtn').classList.add('active');
    document.getElementById('microViewBtn').classList.remove('active');
    startAnimation();
}

function switchToMicroView() {
    animationState.isMacroView = false;
    document.getElementById('macroViewBtn').classList.remove('active');
    document.getElementById('microViewBtn').classList.add('active');
    startAnimation();
}

// Canvas鼠标交互
canvas.addEventListener('mousemove', function(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    let tooltipText = '';
    
    if (!animationState.isMacroView) {
        // 检查镁原子
        microElements.mgAtoms.forEach(atom => {
            const distance = Math.sqrt((x - atom.x) ** 2 + (y - atom.y) ** 2);
            if (distance <= atom.radius) {
                tooltipText = '镁原子 (Mg)';
            }
        });
        
        // 检查氧气分子
        microElements.o2Molecules.forEach(molecule => {
            molecule.atoms.forEach(atom => {
                const distance = Math.sqrt((x - atom.x) ** 2 + (y - atom.y) ** 2);
                if (distance <= atom.radius) {
                    tooltipText = '氧原子 (O) - 氧气分子(O₂)的一部分';
                }
            });
        });
        
        // 检查自由氧原子
        microElements.freeOAtoms.forEach(atom => {
            const distance = Math.sqrt((x - atom.x) ** 2 + (y - atom.y) ** 2);
            if (distance <= atom.radius) {
                tooltipText = '自由氧原子 (O)';
            }
        });
        
        // 检查氧化镁
        microElements.mgoMolecules.forEach(molecule => {
            const distanceMg = Math.sqrt((x - molecule.mg.x) ** 2 + (y - molecule.mg.y) ** 2);
            const distanceO = Math.sqrt((x - molecule.o.x) ** 2 + (y - molecule.o.y) ** 2);
            
            if (distanceMg <= molecule.mg.radius) {
                tooltipText = '镁原子 (Mg) - 氧化镁(MgO)的一部分';
            } else if (distanceO <= molecule.o.radius) {
                tooltipText = '氧原子 (O) - 氧化镁(MgO)的一部分';
            }
        });
    } else {
        // 宏观视图中的交互
        const mg = macroElements.magnesiumStrip;
        if (x >= mg.x && x <= mg.x + mg.width && 
            y >= mg.y && y <= mg.y + mg.height) {
            tooltipText = '镁条 (Mg) - 银白色金属';
        }
    }
    
    if (tooltipText) {
        tooltip.textContent = tooltipText;
        tooltip.style.left = (event.clientX + 15) + 'px';
        tooltip.style.top = (event.clientY + 15) + 'px';
        tooltip.style.opacity = '1';
    } else {
        tooltip.style.opacity = '0';
    }
});

canvas.addEventListener('mouseleave', function() {
    tooltip.style.opacity = '0';
});

// 按钮事件监听
document.getElementById('nextBtn').addEventListener('click', nextStep);
document.getElementById('prevBtn').addEventListener('click', prevStep);
document.getElementById('startBtn').addEventListener('click', startReaction);
document.getElementById('pauseBtn').addEventListener('click', togglePause);
document.getElementById('resetBtn').addEventListener('click', resetAnimation);
document.getElementById('macroViewBtn').addEventListener('click', switchToMacroView);
document.getElementById('microViewBtn').addEventListener('click', switchToMicroView);

// 键盘快捷键
document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case 'ArrowRight':
        case ' ':
            if (event.target === document.body) {
                event.preventDefault();
                nextStep();
            }
            break;
        case 'ArrowLeft':
            if (event.target === document.body) {
                event.preventDefault();
                prevStep();
            }
            break;
        case 'r':
        case 'R':
            if (event.target === document.body) {
                resetAnimation();
            }
            break;
        case 'p':
        case 'P':
            if (event.target === document.body) {
                togglePause();
            }
            break;
    }
});

// 初始化
function init() {
    initMicroElements();
    initMacroElements();
    updateStepIndicator();
    updateInfoPanel();
    drawMacroScene();
    
    // 设置初始视图按钮状态
    document.getElementById('macroViewBtn').classList.add('active');
}

// 页面加载完成后初始化
window.addEventListener('load', init);

// 初始绘制
drawMacroScene();
</script>
</body>
</html>


### 3. 过程输出


## 《镁条燃烧教学动画》使用指南

欢迎使用“镁条在空气中燃烧”交互式教学动画！本动画旨在通过直观、生动的可视化方式，帮助您深入理解这一经典化学反应的宏观现象与微观本质。无论您是学生、教师还是化学爱好者，本工具都将为您提供一个安全、可控且富有启发性的学习环境。

---

### 一、功能说明

本动画是一个基于HTML5 Canvas技术开发的交互式教学工具，完整运行于您的浏览器中。它通过**宏观视图**与**微观视图**的双重视角，动态展示了镁条燃烧的全过程：

1. **宏观视角**：模拟真实实验场景，生动呈现镁条燃烧时发出的“剧烈白光”现象。
2. **微观视角**：揭示反应的本质，展示镁原子与氧气分子如何断裂旧键、形成新键，生成氧化镁。
3. **交互控制**：您可以通过按钮控制学习进程，随时暂停、回看或切换视角，实现个性化学习。

---

### 二、主要功能

#### 1. 流程控制
*   **下一步 / 上一步**：按照预设的教学逻辑（共5步）循序渐进地学习。步骤包括：准备阶段 → 宏观现象 → 微观键断裂 → 微观原子重组 → 总结。
*   **步骤指示器**：顶部的圆点直观显示当前学习进度。

#### 2. 动画控制
*   **点燃 / 开始反应**：触发燃烧动画。在宏观视图下，您将看到白光绽放；在微观视图下，原子和分子开始反应。
*   **暂停 / 继续**：在动画的任何时刻暂停，以便仔细观察反应的中间状态，例如化学键断裂的瞬间。
*   **重置**：将动画恢复到初始状态，方便重复学习或演示。

#### 3. 视图切换
*   **宏观视图**：切换到实验室场景，观察镁条燃烧的震撼现象。
*   **微观视图**：切换到原子-分子世界，探究化学反应的本质。

#### 4. 交互提示
*   **鼠标悬停提示**：在微观视图中，将鼠标移动到任何原子或分子上，会显示其名称和说明（如“镁原子 (Mg)”）。
*   **动态化学方程式**：信息面板中的化学方程式会随着学习步骤动态变化和高亮，帮助您建立“宏观-微观-符号”的联系。

#### 5. 键盘快捷键
*   **空格键** 或 **右箭头**：下一步
*   **左箭头**：上一步
*   **R键**：重置动画
*   **P键**：暂停/继续

---

### 三、设计特色

1.  **符合认知规律**：严格遵循“从宏观到微观”、“从现象到本质”的教学设计，引导学习者构建完整的知识体系。
2.  **双重表征**：同时呈现反应的**现象**（白光）、**过程**（原子运动）和**符号**（化学方程式），强化化学学科特有的思维方式。
3.  **视觉科学严谨**：
    *   采用化学教学中通用的配色方案（镁：银灰，氧：红色）。
    *   微观模型使用球棍模型，清晰展示化学键的断裂与形成。
    *   宏观燃烧效果模拟了真实白光的光晕和闪烁感。
4.  **友好的用户体验**：界面简洁，功能分区明确，按钮具有明确的状态反馈（如激活、禁用），确保操作流畅。

---

### 四、教学要点

本动画重点阐释了以下核心化学概念：

1.  **化学反应的本质**：化学反应是**原子重新组合**的过程。本动画清晰地展示了氧气分子（O₂）分解为氧原子，镁原子与氧原子结合生成氧化镁（MgO）的完整过程。
2.  **化学键的变化**：反应伴随着**旧化学键的断裂**（O₂中的共价键）和**新化学键的形成**（MgO中的离子键）。微观视图中的“灰色短线”直观代表了化学键。
3.  **能量转化**：反应**放出大量能量**，主要以**光能**（剧烈白光）和**热能**的形式释放。宏观视图中的强光效果正是这一点的直观体现。
4.  **氧化反应**：该反应是物质与氧气发生的化学反应，是氧化反应的典型实例。

**建议学习路径**：首次学习时，建议按照“下一步”按钮的引导，完整经历五个步骤。之后，可以自由使用视图切换和暂停功能，针对不理解的部分进行反复观察和探究。

---

### 五、使用建议

*   **对学生而言**：
    *   在观看真实实验演示**前**使用本动画，可以建立预期，知道要观察什么。
    *   在观看真实实验演示**后**使用本动画，可以解释现象，理解“为什么”。
    *   利用暂停功能，在“化学键断裂”、“原子移动”等关键帧停下来，思考并描述你看到的过程。
*   **对教师而言**：
    *   **课堂演示**：可用于引入新课、解释难点或总结复习。通过切换视图，引导学生将现象与本质联系起来。
    *   **探究任务**：可以提出问题，如：“在微观视图中，为什么氧原子是成对出现的？”“暂停在反应中间，此时有哪些粒子存在？”让学生通过操作动画寻找答案。
    *   **弥补实验不足**：真实镁条燃烧过程过快、光线过强，本动画提供了可慢放、可重复的完美观察条件。
*   **通用建议**：
    1.  首先点击 **“下一步”** 跟随引导学习一遍。
    2.  然后点击 **“重置”**，尝试直接点击 **“点燃”** 按钮，观察完整过程。
    3.  在反应过程中，反复点击 **“宏观视图”** 和 **“微观视图”** 按钮，对比两个视角下发生的变化。
    4.  不要忘记使用 **“鼠标悬停”** 功能来识别微观世界中的各种粒子。

希望这个交互式动画能点燃您对化学的好奇与热情，让学习过程像镁条燃烧一样，充满光亮与发现！祝您探索愉快！