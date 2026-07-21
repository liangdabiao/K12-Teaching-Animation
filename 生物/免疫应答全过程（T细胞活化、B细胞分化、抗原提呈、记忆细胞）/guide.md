# 需求：免疫应答全过程（T细胞活化、B细胞分化、抗原提呈、记忆细胞）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：高中或大学低年级的生物学/医学学生。他们具备基础的细胞生物学知识，但需要将零散的知识点（如T细胞、B细胞、抗原等）串联成一个动态、连续的过程，以建立系统性理解。
2.  **核心需求**：用户需要直观地理解免疫应答这一复杂、动态、多细胞协同的过程。静态图表和文字描述难以展现其时空顺序和细胞间相互作用。
3.  **学习痛点**：
    *   **过程抽象**：抗原提呈、双信号激活、克隆选择等概念抽象难懂。
    *   **时空关系混乱**：事件发生的顺序（如先抗原提呈，后T细胞活化）和地点（如淋巴结、感染部位）容易混淆。
    *   **缺乏整体观**：容易孤立地记忆不同细胞的功能，而忽视它们是如何协作的。
4.  **解决方案**：通过一个可交互、分步骤、可视化的动画，将免疫应答分解为清晰的阶段，允许用户控制节奏、聚焦细节，并观察细胞间的“对话”与协作。

#### 教学设计思路
*   **核心概念**：围绕“特异性免疫应答”的主线，突出 **“识别-激活-效应-记忆”** 四个核心阶段。关键子概念包括：抗原提呈细胞（APC）处理与提呈抗原、T细胞通过双信号活化、辅助T细胞（Th）与B细胞相互作用、B细胞分化为浆细胞和记忆细胞、效应机制（抗体）等。
*   **认知规律**：
    1.  **从宏观到微观**：动画起始于一个简化的身体轮廓和感染部位，然后镜头推入到局部组织或淋巴结，聚焦于细胞层面的活动。
    2.  **分步引导**：将全过程分解为4-5个逻辑清晰的步骤，用户需按顺序或选择性地学习每一步。每一步都有简短的文字说明和视觉高亮。
    3.  **类比与拟人化**：将抗原比作“通缉犯”，APC比作“巡逻兵”，T细胞受体（TCR）和MHC分子比作“身份证检查”，抗体比作“定制武器”。这能降低认知负荷。
    4.  **强调因果关系**：用清晰的箭头、信号分子（如细胞因子）的飞溅效果、以及颜色编码来展示“A细胞导致B细胞发生某种变化”。
*   **交互设计**：
    1.  **阶段控制面板**：提供“播放/暂停”、“上一步/下一步”按钮，以及一个可视化的进度条或阶段标签（如“1. 抗原捕获”、“2. T细胞活化”等），让用户掌控学习节奏。
    2.  **焦点与注释**：鼠标悬停在关键细胞或分子（如MHC-II、CD4、抗体）上时，显示其名称和简要功能。
    3.  **视角切换**：提供两个主要“场景”的切换按钮：“感染局部组织”和“次级淋巴器官（淋巴结）”，帮助用户理解免疫反应发生的地理位置。
    4.  **“探索模式”**：在完整播放一次后，允许用户自由点击激活场景中的特定细胞，观察其独立行为或与其他细胞的互动。
*   **视觉呈现**：
    1.  **风格**：采用简洁、扁平化或微质感（soft UI）的矢量图形风格，避免过于写实带来的视觉噪音。细胞形状圆润可爱但保持特征（如树突状细胞的星形突起）。
    2.  **动态效果**：细胞移动平滑；分子结合时有轻微的“吸附”动画；信号传递用脉动光波或粒子流表示；细胞分化时用生长动画或分身效果。
    3.  **视觉层次**：当前讲解的步骤中，核心细胞和路径高亮显示（如加粗边框、发光），背景元素则半透明化。使用指向性箭头和动态流线清晰展示细胞移动和分子扩散方向。

#### 配色方案选择
选择一套清晰、科学且友好的配色，以区分不同细胞类型和功能状态：
*   **背景与组织**：使用浅灰色或极浅的米色，营造干净的画布感。血管或淋巴管可用更浅的蓝色/灰色线条表示。
*   **病原体（抗原）**：醒目的**红色**（代表危险），形状不规则。
*   **抗原提呈细胞（APC，如树突状细胞）**：**深蓝色或深紫色**，显得沉稳、专业。
*   **T细胞**：
    *   初始/静止T细胞：**浅绿色**。
    *   活化的辅助T细胞（Th）：变为明亮的**绿色**，并可能带有动态光效。
*   **B细胞**：
    *   初始B细胞：**浅橙色**。
    *   活化/增殖中的B细胞：变为明亮的**橙色**。
    *   分化的浆细胞：**深橙色**，形状可变为典型的“车轮状”核形态。
*   **记忆细胞（T/B）**：在原有细胞颜色基础上，增加一个**金色边框或星标**，象征其长期存在的价值。
*   **分子与信号**：
    *   MHC-抗原复合物：APC表面显示为一个小红点（抗原）嵌在深蓝色背景上。
    *   抗体：**Y形**，用**亮蓝色**表示，与病原体的红色形成对比（互补色），突出其结合作用。
    *   细胞因子：可以用小而亮的**黄色光点或星星**表示其扩散。

#### 交互功能列表
1.  **主流程控制**：播放、暂停、重置、跳转到特定阶段。
2.  **信息提示**：鼠标悬停（Hover）在任何细胞、分子或结构上时，弹出工具提示框显示名称和关键功能。
3.  **阶段导航**：点击导航栏上的阶段标签（如“抗原提呈”、“克隆扩增”），直接跳转到对应动画片段。
4.  **场景切换**：在“感染部位”和“淋巴结”两个视图间切换，观察免疫反应的不同战场。
5.  **细节开关**：可勾选/取消勾选“显示分子标签”、“显示信号路径”等，以简化或丰富视图。
6.  **知识卡片**：在动画区域侧边或底部，随步骤变化显示当前步骤的文本解说和关键术语。
7.  **“快进”效果**：在展示克隆扩增等耗时过程时，提供一个加速动画的按钮。
8.  **小结与测试**：动画结束后，提供一个简短的图文小结，并可选择进入2-3道互动选择题（如“哪个细胞负责抗原提呈？”），点击选项后动画会高亮正确答案所在的环节。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>免疫应答全过程教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
            color: #333;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 25px;
            max-width: 900px;
            width: 100%;
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 2.4rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }

        .subtitle {
            color: #5d6d7e;
            font-size: 1.1rem;
            margin-bottom: 20px;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            max-width: 1200px;
            width: 100%;
            gap: 25px;
        }

        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 25px;
            justify-content: center;
            width: 100%;
        }

        .animation-area {
            flex: 1;
            min-width: 700px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        #animationCanvas {
            width: 100%;
            height: 500px;
            display: block;
            background: #f8fafc;
            border-radius: 10px;
        }

        .controls-panel {
            width: 300px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            padding: 25px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .panel-section {
            border-bottom: 1px solid #eee;
            padding-bottom: 20px;
        }

        .panel-section:last-child {
            border-bottom: none;
        }

        h2 {
            color: #3498db;
            font-size: 1.4rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        h2 i {
            font-size: 1.2rem;
        }

        .stage-nav {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .stage-btn {
            padding: 14px 18px;
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            color: #495057;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: left;
            display: flex;
            align-items: center;
            gap: 10px;
            position: relative;
        }

        .stage-btn:hover {
            background: #e9ecef;
            transform: translateY(-2px);
        }

        .stage-btn.active {
            background: #e3f2fd;
            border-color: #3498db;
            color: #3498db;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2);
        }

        .stage-btn .stage-number {
            background: #dee2e6;
            color: #6c757d;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.9rem;
        }

        .stage-btn.active .stage-number {
            background: #3498db;
            color: white;
        }

        .player-controls {
            display: flex;
            gap: 12px;
            justify-content: center;
        }

        .control-btn {
            padding: 12px 20px;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .control-btn.primary {
            background: #3498db;
            color: white;
            flex: 1;
        }

        .control-btn.primary:hover {
            background: #2980b9;
            transform: translateY(-2px);
        }

        .control-btn.secondary {
            background: #f8f9fa;
            color: #495057;
            border: 2px solid #dee2e6;
        }

        .control-btn.secondary:hover {
            background: #e9ecef;
        }

        .scene-toggle {
            display: flex;
            background: #f8f9fa;
            border-radius: 10px;
            padding: 4px;
        }

        .scene-btn {
            flex: 1;
            padding: 12px;
            text-align: center;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .scene-btn.active {
            background: white;
            color: #3498db;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .legend {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.9rem;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
            flex-shrink: 0;
        }

        .info-panel {
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            padding: 25px;
            width: 100%;
            max-width: 1200px;
        }

        .info-content {
            min-height: 120px;
            padding: 15px;
            background: #f8fafc;
            border-radius: 10px;
            line-height: 1.6;
        }

        .info-content h3 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .info-content p {
            color: #5d6d7e;
            margin-bottom: 8px;
        }

        .highlight {
            background: #fffacd;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }

        .footer {
            margin-top: 20px;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9rem;
            padding: 15px;
        }

        @media (max-width: 1100px) {
            .main-content {
                flex-direction: column;
                align-items: center;
            }
            
            .animation-area, .controls-panel {
                min-width: 100%;
                max-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧬 免疫应答全过程</h1>
        <p class="subtitle">T细胞活化 · B细胞分化 · 抗原提呈 · 记忆细胞形成</p>
    </div>

    <div class="container">
        <div class="main-content">
            <div class="animation-area">
                <canvas id="animationCanvas"></canvas>
            </div>

            <div class="controls-panel">
                <div class="panel-section">
                    <h2>📋 阶段导航</h2>
                    <div class="stage-nav">
                        <button class="stage-btn active" data-stage="0">
                            <span class="stage-number">1</span>
                            <span>抗原入侵与捕获</span>
                        </button>
                        <button class="stage-btn" data-stage="1">
                            <span class="stage-number">2</span>
                            <span>抗原提呈与T细胞活化</span>
                        </button>
                        <button class="stage-btn" data-stage="2">
                            <span class="stage-number">3</span>
                            <span>B细胞激活与分化</span>
                        </button>
                        <button class="stage-btn" data-stage="3">
                            <span class="stage-number">4</span>
                            <span>抗体产生与清除</span>
                        </button>
                        <button class="stage-btn" data-stage="4">
                            <span class="stage-number">5</span>
                            <span>记忆细胞形成</span>
                        </button>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>🎮 动画控制</h2>
                    <div class="player-controls">
                        <button class="control-btn secondary" id="prevBtn">
                            ◀ 上一步
                        </button>
                        <button class="control-btn primary" id="playPauseBtn">
                            ▶ 播放
                        </button>
                        <button class="control-btn secondary" id="nextBtn">
                            下一步 ▶
                        </button>
                    </div>
                    <div style="margin-top: 15px;">
                        <button class="control-btn secondary" id="resetBtn" style="width: 100%;">
                            🔄 重新开始
                        </button>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>📍 场景切换</h2>
                    <div class="scene-toggle">
                        <div class="scene-btn active" data-scene="tissue">感染局部组织</div>
                        <div class="scene-btn" data-scene="lymph">淋巴结</div>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>🎨 图例说明</h2>
                    <div class="legend">
                        <div class="legend-item">
                            <div class="legend-color" style="background: #e74c3c;"></div>
                            <span>病原体/抗原</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #3498db;"></div>
                            <span>抗原提呈细胞</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #2ecc71;"></div>
                            <span>T细胞</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #e67e22;"></div>
                            <span>B细胞</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #9b59b6;"></div>
                            <span>浆细胞</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background: #f1c40f; border: 2px solid #d35400;"></div>
                            <span>记忆细胞</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="info-panel">
            <h2>📚 当前阶段说明</h2>
            <div class="info-content" id="infoContent">
                <h3>阶段 1: 抗原入侵与捕获</h3>
                <p>病原体（<span class="highlight">红色抗原</span>）突破皮肤或黏膜屏障，侵入机体组织。</p>
                <p>专业的<span class="highlight">抗原提呈细胞（APC，蓝色）</span>，如树突状细胞，像巡逻兵一样识别并捕获这些抗原。</p>
                <p>APC将抗原吞噬、处理成小片段，准备进行"展示"。</p>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>教学动画 | 免疫学可视化 | 设计：熊猫老师 | 提示：鼠标悬停在细胞上查看详细信息</p>
    </div>

    <script>
        // 获取Canvas和上下文
        const canvas = document.getElementById('animationCanvas');
        const ctx = canvas.getContext('2d');

        // 设置Canvas尺寸
        function resizeCanvas() {
            const container = canvas.parentElement;
            canvas.width = container.clientWidth;
            canvas.height = 500;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        // 动画状态
        let currentStage = 0;
        let isPlaying = false;
        let currentScene = 'tissue'; // 'tissue' 或 'lymph'
        let animationTime = 0;
        let hoveredCell = null;

        // 细胞和对象定义
        const cells = [];
        const pathogens = [];
        const antibodies = [];
        const signals = [];

        // 颜色定义
        const colors = {
            pathogen: '#e74c3c',
            apc: '#3498db',
            tCell: '#2ecc71',
            bCell: '#e67e22',
            plasmaCell: '#9b59b6',
            memoryCell: '#f1c40f',
            memoryBorder: '#d35400',
            signal: '#f39c12',
            antibody: '#1abc9c',
            tissue: '#a3d9b1',
            lymph: '#d6eaf8',
            bloodVessel: '#e74c3c',
            lymphVessel: '#3498db'
        };

        // 细胞类
        class Cell {
            constructor(type, x, y, radius, options = {}) {
                this.type = type; // 'pathogen', 'apc', 'tCell', 'bCell', 'plasma', 'memory'
                this.x = x;
                this.y = y;
                this.radius = radius;
                this.color = colors[type] || '#ccc';
                this.state = options.state || 'resting'; // 'resting', 'active', 'presenting', 'dividing'
                this.targetX = x;
                this.targetY = y;
                this.speed = options.speed || 1;
                this.antigen = options.antigen || null;
                this.label = options.label || '';
                this.info = options.info || '';
                this.pulse = 0;
                this.isMemory = options.isMemory || false;
            }

            update() {
                // 向目标移动
                const dx = this.targetX - this.x;
                const dy = this.targetY - this.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance > 1) {
                    this.x += (dx / distance) * this.speed;
                    this.y += (dy / distance) * this.speed;
                }
                
                // 脉冲效果
                this.pulse = (this.pulse + 0.05) % (Math.PI * 2);
            }

            draw() {
                ctx.save();
                
                // 细胞主体
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                
                // 根据状态调整颜色和效果
                let fillColor = this.color;
                let strokeColor = '#333';
                let lineWidth = 1;
                
                if (this.state === 'active') {
                    // 激活状态发光效果
                    const glow = Math.sin(this.pulse) * 3 + 5;
                    ctx.shadowColor = fillColor;
                    ctx.shadowBlur = glow;
                    lineWidth = 2;
                }
                
                if (this.isMemory) {
                    // 记忆细胞金色边框
                    strokeColor = colors.memoryBorder;
                    lineWidth = 3;
                }
                
                ctx.fillStyle = fillColor;
                ctx.fill();
                ctx.strokeStyle = strokeColor;
                ctx.lineWidth = lineWidth;
                ctx.stroke();
                
                // 如果是APC且携带抗原，绘制抗原
                if (this.antigen && this.type === 'apc') {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y - this.radius * 0.6, this.radius * 0.4, 0, Math.PI * 2);
                    ctx.fillStyle = colors.pathogen;
                    ctx.fill();
                    ctx.strokeStyle = '#333';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
                
                // 如果是树突状细胞（APC），绘制突起
                if (this.type === 'apc') {
                    ctx.strokeStyle = colors.apc;
                    ctx.lineWidth = 2;
                    for (let i = 0; i < 8; i++) {
                        const angle = (i / 8) * Math.PI * 2;
                        const length = this.radius * 1.5;
                        ctx.beginPath();
                        ctx.moveTo(this.x, this.y);
                        const endX = this.x + Math.cos(angle) * length;
                        const endY = this.y + Math.sin(angle) * length;
                        ctx.lineTo(endX, endY);
                        ctx.stroke();
                    }
                }
                
                // 绘制标签
                if (this.label) {
                    ctx.fillStyle = '#2c3e50';
                    ctx.font = '14px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(this.label, this.x, this.y + this.radius + 18);
                }
                
                // 如果是浆细胞，绘制抗体
                if (this.type === 'plasma') {
                    for (let i = 0; i < 4; i++) {
                        const angle = (i / 4) * Math.PI * 2 + animationTime * 0.5;
                        const startX = this.x + Math.cos(angle) * this.radius;
                        const startY = this.y + Math.sin(angle) * this.radius;
                        
                        // 绘制Y形抗体
                        ctx.save();
                        ctx.translate(startX, startY);
                        ctx.rotate(angle);
                        ctx.fillStyle = colors.antibody;
                        
                        // 抗体Y形
                        ctx.beginPath();
                        ctx.moveTo(0, 0);
                        ctx.lineTo(10, -5);
                        ctx.lineTo(10, -2);
                        ctx.lineTo(15, -2);
                        ctx.lineTo(15, 2);
                        ctx.lineTo(10, 2);
                        ctx.lineTo(10, 5);
                        ctx.lineTo(0, 0);
                        ctx.lineTo(-10, -5);
                        ctx.lineTo(-10, -2);
                        ctx.lineTo(-15, -2);
                        ctx.lineTo(-15, 2);
                        ctx.lineTo(-10, 2);
                        ctx.lineTo(-10, 5);
                        ctx.closePath();
                        ctx.fill();
                        ctx.restore();
                    }
                }
                
                ctx.restore();
            }

            containsPoint(x, y) {
                const dx = x - this.x;
                const dy = y - this.y;
                return dx * dx + dy * dy <= this.radius * this.radius;
            }
        }

        class Pathogen {
            constructor(x, y) {
                this.x = x;
                this.y = y;
                this.radius = 8;
                this.speed = 0.5;
                this.angle = Math.random() * Math.PI * 2;
                this.captured = false;
            }

            update() {
                if (!this.captured) {
                    this.x += Math.cos(this.angle) * this.speed;
                    this.y += Math.sin(this.angle) * this.speed;
                    
                    // 边界反弹
                    if (this.x < this.radius || this.x > canvas.width - this.radius) {
                        this.angle = Math.PI - this.angle;
                    }
                    if (this.y < this.radius || this.y > canvas.height - this.radius) {
                        this.angle = -this.angle;
                    }
                }
            }

            draw() {
                ctx.save();
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = colors.pathogen;
                ctx.fill();
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 1;
                ctx.stroke();
                
                // 绘制不规则形状
                for (let i = 0; i < 5; i++) {
                    const spikeAngle = (i / 5) * Math.PI * 2;
                    const spikeLength = this.radius * 1.2;
                    const spikeX = this.x + Math.cos(spikeAngle) * spikeLength;
                    const spikeY = this.y + Math.sin(spikeAngle) * spikeLength;
                    
                    ctx.beginPath();
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(spikeX, spikeY);
                    ctx.stroke();
                }
                ctx.restore();
            }
        }

        class Signal {
            constructor(fromX, fromY, toX, toY, type) {
                this.fromX = fromX;
                this.fromY = fromY;
                this.toX = toX;
                this.toY = toY;
                this.type = type; // 'cytokine', 'presentation', 'activation'
                this.progress = 0;
                this.speed = 0.02;
                this.completed = false;
            }

            update() {
                if (this.progress < 1) {
                    this.progress += this.speed;
                } else {
                    this.completed = true;
                }
            }

            draw() {
                ctx.save();
                
                const currentX = this.fromX + (this.toX - this.fromX) * this.progress;
                const currentY = this.fromY + (this.toY - this.fromY) * this.progress;
                
                // 信号路径
                ctx.beginPath();
                ctx.moveTo(this.fromX, this.fromY);
                ctx.lineTo(this.toX, this.toY);
                ctx.strokeStyle = colors.signal + '80';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.stroke();
                
                // 信号粒子
                ctx.beginPath();
                ctx.arc(currentX, currentY, 6, 0, Math.PI * 2);
                
                if (this.type === 'cytokine') {
                    ctx.fillStyle = '#f1c40f';
                } else if (this.type === 'activation') {
                    ctx.fillStyle = '#e74c3c';
                } else {
                    ctx.fillStyle = colors.signal;
                }
                
                ctx.fill();
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 1;
                ctx.stroke();
                
                ctx.restore();
            }
        }

        // 初始化场景
        function initScene() {
            cells.length = 0;
            pathogens.length = 0;
            antibodies.length = 0;
            signals.length = 0;
            animationTime = 0;
            
            // 根据场景和阶段初始化
            if (currentScene === 'tissue') {
                // 感染组织场景
                if (currentStage === 0) {
                    // 阶段1: 抗原入侵
                    for (let i = 0; i < 5; i++) {
                        pathogens.push(new Pathogen(
                            100 + i * 30,
                            150 + Math.random() * 100
                        ));
                    }
                    
                    // 添加APC
                    cells.push(new Cell('apc', 400, 250, 25, {
                        label: '树突状细胞',
                        info: '抗原提呈细胞：识别并捕获病原体，处理抗原片段'
                    }));
                    
                    // 添加一些T细胞（静止）
                    cells.push(new Cell('tCell', 600, 150, 20, {
                        label: '初始T细胞',
                        info: '辅助T细胞：等待被抗原提呈细胞激活',
                        state: 'resting'
                    }));
                    
                } else if (currentStage === 1) {
                    // 阶段2: 抗原提呈
                    cells.push(new Cell('apc', 300, 250, 25, {
                        label: '树突状细胞',
                        info: '已捕获并处理抗原，准备迁移至淋巴结',
                        antigen: true,
                        state: 'active'
                    }));
                    
                    // APC向淋巴结移动
                    cells[0].targetX = 150;
                    cells[0].targetY = 150;
                    
                } else if (currentStage === 4) {
                    // 阶段5: 记忆细胞在组织中
                    cells.push(new Cell('memory', 300, 200, 22, {
                        label: '记忆T细胞',
                        info: '长期存留，对相同病原体能快速响应',
                        isMemory: true
                    }));
                    
                    cells.push(new Cell('memory', 400, 300, 22, {
                        label: '记忆B细胞',
                        info: '长期存留，能快速分化为浆细胞',
                        isMemory: true
                    }));
                }
                
            } else if (currentScene === 'lymph') {
                // 淋巴结场景
                if (currentStage === 1) {
                    // 阶段2: 淋巴结中的抗原提呈
                    cells.push(new Cell('apc', 200, 250, 25, {
                        label: '树突状细胞',
                        info: '在淋巴结中向T细胞提呈抗原',
                        antigen: true,
                        state: 'presenting'
                    }));
                    
                    cells.push(new Cell('tCell', 350, 250, 20, {
                        label: '初始T细胞',
                        info: '通过TCR识别MHC-抗原复合物',
                        state: 'resting'
                    }));
                    
                    // 添加信号
                    signals.push(new Signal(200, 250, 350, 250, 'presentation'));
                    
                } else if (currentStage === 2) {
                    // 阶段3: T-B细胞相互作用
                    cells.push(new Cell('tCell', 250, 250, 22, {
                        label: '活化T细胞',
                        info: '已激活的辅助T细胞，分泌细胞因子',
                        state: 'active'
                    }));
                    
                    cells.push(new Cell('bCell', 450, 250, 22, {
                        label: 'B细胞',
                        info: '通过BCR识别抗原，需要T细胞帮助',
                        state: 'resting'
                    }));
                    
                    // 细胞因子信号
                    signals.push(new Signal(250, 250, 450, 250, 'cytokine'));
                    
                } else if (currentStage === 3) {
                    // 阶段4: B细胞分化
                    cells.push(new Cell('bCell', 300, 250, 22, {
                        label: '活化B细胞',
                        info: '接受T细胞信号后活化，开始克隆扩增',
                        state: 'active'
                    }));
                    
                    // 添加正在分裂的B细胞
                    for (let i = 0; i < 3; i++) {
                        cells.push(new Cell('bCell', 
                            350 + i * 40, 
                            200 + Math.random() * 100, 
                            18, {
                            label: '增殖中',
                            state: 'dividing'
                        }));
                    }
                    
                    // 添加浆细胞
                    cells.push(new Cell('plasma', 500, 250, 24, {
                        label: '浆细胞',
                        info: '抗体工厂，大量分泌特异性抗体'
                    }));
                    
                } else if (currentStage === 4) {
                    // 阶段5: 记忆细胞在淋巴结
                    cells.push(new Cell('memory', 300, 200, 22, {
                        label: '记忆T细胞',
                        info: '长期驻留淋巴结，免疫监视',
                        isMemory: true
                    }));
                    
                    cells.push(new Cell('memory', 450, 300, 22, {
                        label: '记忆B细胞',
                        info: '长期驻留，二次应答时快速活化',
                        isMemory: true
                    }));
                }
            }
            
            // 总是添加一些背景细胞
            if (currentStage >= 2) {
                cells.push(new Cell('plasma', 550, 150, 20, {
                    label: '浆细胞'
                }));
            }
        }

        // 绘制背景
        function drawBackground() {
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制场景背景
            if (currentScene === 'tissue') {
                // 组织背景
                ctx.fillStyle = colors.tissue + '40';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // 绘制血管
                ctx.strokeStyle = colors.bloodVessel + '60';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(50, 100);
                ctx.bezierCurveTo(150, 50, 250, 150, 350, 100);
                ctx.stroke();
                
                // 场景标签
                ctx.fillStyle = '#2c3e50';
                ctx.font = 'bold 16px Arial';
                ctx.fillText('感染局部组织', 20, 30);
                
            } else {
                // 淋巴结背景
                ctx.fillStyle = colors.lymph + '40';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // 绘制淋巴结轮廓
                ctx.strokeStyle = colors.lymphVessel;
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.ellipse(canvas.width/2, canvas.height/2, 200, 150, 0, 0, Math.PI * 2);
                ctx.stroke();
                
                // 淋巴管
                ctx.beginPath();
                ctx.moveTo(100, 100);
                ctx.lineTo(200, 150);
                ctx.moveTo(canvas.width - 100, 100);
                ctx.lineTo(canvas.width - 200, 150);
                ctx.stroke();
                
                // 场景标签
                ctx.fillStyle = '#2c3e50';
                ctx.font = 'bold 16px Arial';
                ctx.fillText('淋巴结（免疫反应中心）', 20, 30);
            }
            
            // 绘制阶段标题
            ctx.fillStyle = '#3498db';
            ctx.font = 'bold 20px Arial';
            const stageTitles = [
                '1. 抗原入侵与捕获',
                '2. 抗原提呈与T细胞活化',
                '3. B细胞激活与分化',
                '4. 抗体产生与清除',
                '5. 记忆细胞形成'
            ];
            ctx.fillText(stageTitles[currentStage], canvas.width/2 - 150, 50);
        }

        // 动画循环
        function animate() {
            drawBackground();
            animationTime += 0.05;
            
            // 更新和绘制病原体
            pathogens.forEach(pathogen => {
                pathogen.update();
                pathogen.draw();
                
                // 检查是否被APC捕获
                if (!pathogen.captured && currentStage === 0) {
                    cells.forEach(cell => {
                        if (cell.type === 'apc') {
                            const dx = pathogen.x - cell.x;
                            const dy = pathogen.y - cell.y;
                            const distance = Math.sqrt(dx * dx + dy * dy);
                            
                            if (distance < cell.radius + pathogen.radius) {
                                pathogen.captured = true;
                                cell.antigen = true;
                                cell.state = 'active';
                            }
                        }
                    });
                }
            });
            
            // 更新和绘制信号
            signals.forEach((signal, index) => {
                signal.update();
                signal.draw();
                if (signal.completed) {
                    signals.splice(index, 1);
                }
            });
            
            // 更新和绘制细胞
            cells.forEach(cell => {
                cell.update();
                cell.draw();
                
                // 如果是激活状态且有脉冲效果
                if (cell.state === 'active') {
                    ctx.save();
                    ctx.beginPath();
                    ctx.arc(cell.x, cell.y, cell.radius + 5, 0, Math.PI * 2);
                    ctx.strokeStyle = cell.color + '80';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                    ctx.restore();
                }
            });
            
            // 绘制抗体
            antibodies.forEach(antibody => {
                // 简化的抗体绘制
                ctx.save();
                ctx.translate(antibody.x, antibody.y);
                ctx.rotate(animationTime);
                ctx.fillStyle = colors.antibody;
                
                ctx.beginPath();
                ctx.moveTo(0, 0);
                ctx.lineTo(10, -5);
                ctx.lineTo(10, 5);
                ctx.closePath();
                
                ctx.moveTo(0, 0);
                ctx.lineTo(-10, -5);
                ctx.lineTo(-10, 5);
                ctx.closePath();
                
                ctx.fill();
                ctx.restore();
                
                // 抗体移动
                antibody.x += Math.cos(antibody.angle) * 2;
                antibody.y += Math.sin(antibody.angle) * 2;
            });
            
            // 清除超出边界的抗体
            for (let i = antibodies.length - 1; i >= 0; i--) {
                if (antibodies[i].x < -20 || antibodies[i].x > canvas.width + 20 ||
                    antibodies[i].y < -20 || antibodies[i].y > canvas.height + 20) {
                    antibodies.splice(i, 1);
                }
            }
            
            // 在阶段4生成抗体
            if (currentStage === 3 && animationTime % 1 < 0.1) {
                cells.forEach(cell => {
                    if (cell.type === 'plasma') {
                        antibodies.push({
                            x: cell.x,
                            y: cell.y,
                            angle: Math.random() * Math.PI * 2
                        });
                    }
                });
            }
            
            // 绘制悬停信息
            if (hoveredCell) {
                ctx.save();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.85)';
                ctx.fillRect(hoveredCell.x + 20, hoveredCell.y - 40, 200, 60);
                
                ctx.fillStyle = 'white';
                ctx.font = 'bold 14px Arial';
                ctx.fillText(hoveredCell.label || hoveredCell.type, hoveredCell.x + 30, hoveredCell.y - 20);
                
                ctx.font = '12px Arial';
                ctx.fillText(hoveredCell.info || '点击查看详细信息', hoveredCell.x + 30, hoveredCell.y);
                ctx.restore();
            }
            
            if (isPlaying) {
                requestAnimationFrame(animate);
            }
        }

        // 更新信息面板
        function updateInfoPanel() {
            const infoContent = document.getElementById('infoContent');
            const stageInfos = [
                {
                    title: '阶段 1: 抗原入侵与捕获',
                    content: `<p>病原体（<span class="highlight">红色抗原</span>）突破皮肤或黏膜屏障，侵入机体组织。</p>
                             <p>专业的<span class="highlight">抗原提呈细胞（APC，蓝色）</span>，如树突状细胞，像巡逻兵一样识别并捕获这些抗原。</p>
                             <p>APC将抗原吞噬、处理成小片段，准备进行"展示"。</p>`
                },
                {
                    title: '阶段 2: 抗原提呈与T细胞活化',
                    content: `<p>APC携带抗原片段迁移至<span class="highlight">淋巴结</span>。</p>
                             <p>在淋巴结中，APC通过<span class="highlight">MHC-II分子</span>将抗原片段展示给<span class="highlight">辅助T细胞（绿色）</span>。</p>
                             <p>T细胞通过TCR识别抗原，并在共刺激信号作用下被<span class="highlight">完全激活</span>。</p>`
                },
                {
                    title
: '阶段 3: B细胞激活与分化',
                    content: `<p>活化的辅助T细胞通过分泌<span class="highlight">细胞因子（黄色信号）</span>帮助<span class="highlight">B细胞（橙色）</span>。</p>
                             <p>B细胞通过BCR识别抗原，并在T细胞辅助下被激活。</p>
                             <p>激活的B细胞开始<span class="highlight">克隆扩增</span>，产生大量相同的B细胞。</p>`
                },
                {
                    title: '阶段 4: 抗体产生与清除',
                    content: `<p>部分B细胞分化为<span class="highlight">浆细胞（紫色）</span>，成为抗体工厂。</p>
                             <p>浆细胞大量分泌<span class="highlight">特异性抗体（青色Y形）</span>。</p>
                             <p>抗体与病原体结合，通过多种机制<span class="highlight">中和并清除</span>病原体。</p>`
                },
                {
                    title: '阶段 5: 记忆细胞形成',
                    content: `<p>部分活化的T细胞和B细胞分化为<span class="highlight">记忆细胞（金色边框）</span>。</p>
                             <p>记忆细胞<span class="highlight">长期存活</span>于淋巴组织和外周组织。</p>
                             <p>当相同病原体再次入侵时，记忆细胞能<span class="highlight">快速启动二次免疫应答</span>，反应更快、更强。</p>`
                }
            ];
            
            const info = stageInfos[currentStage];
            infoContent.innerHTML = `
                <h3>${info.title}</h3>
                ${info.content}
            `;
        }

        // 切换阶段
        function goToStage(stage) {
            currentStage = Math.max(0, Math.min(4, stage));
            
            // 更新按钮状态
            document.querySelectorAll('.stage-btn').forEach((btn, index) => {
                if (index === currentStage) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
            
            // 重新初始化场景
            initScene();
            updateInfoPanel();
            
            // 如果动画暂停，绘制一帧
            if (!isPlaying) {
                animate();
            }
        }

        // 切换场景
        function switchScene(scene) {
            currentScene = scene;
            
            // 更新按钮状态
            document.querySelectorAll('.scene-btn').forEach(btn => {
                if (btn.dataset.scene === scene) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
            
            // 重新初始化场景
            initScene();
            
            // 如果动画暂停，绘制一帧
            if (!isPlaying) {
                animate();
            }
        }

        // 事件监听器
        document.querySelectorAll('.stage-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const stage = parseInt(btn.dataset.stage);
                goToStage(stage);
            });
        });

        document.querySelectorAll('.scene-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                switchScene(btn.dataset.scene);
            });
        });

        document.getElementById('playPauseBtn').addEventListener('click', () => {
            isPlaying = !isPlaying;
            const btn = document.getElementById('playPauseBtn');
            
            if (isPlaying) {
                btn.innerHTML = '⏸ 暂停';
                animate();
            } else {
                btn.innerHTML = '▶ 播放';
            }
        });

        document.getElementById('prevBtn').addEventListener('click', () => {
            goToStage(currentStage - 1);
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            goToStage(currentStage + 1);
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            goToStage(0);
            if (!isPlaying) {
                animate();
            }
        });

        // 鼠标悬停检测
        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            hoveredCell = null;
            
            // 检查是否悬停在细胞上
            for (let i = cells.length - 1; i >= 0; i--) {
                if (cells[i].containsPoint(x, y)) {
                    hoveredCell = cells[i];
                    break;
                }
            }
            
            // 如果没有动画播放，重绘一帧以显示悬停信息
            if (!isPlaying) {
                animate();
            }
        });

        canvas.addEventListener('click', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // 检查点击了哪个细胞
            for (let i = cells.length - 1; i >= 0; i--) {
                if (cells[i].containsPoint(x, y)) {
                    // 显示详细信息
                    alert(`${cells[i].label}\n\n${cells[i].info || '暂无详细信息'}`);
                    break;
                }
            }
        });

        // 初始化
        initScene();
        updateInfoPanel();
        animate(); // 绘制初始帧

        // 添加键盘控制
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'ArrowLeft':
                    goToStage(currentStage - 1);
                    break;
                case 'ArrowRight':
                    goToStage(currentStage + 1);
                    break;
                case ' ':
                    e.preventDefault();
                    document.getElementById('playPauseBtn').click();
                    break;
                case '1':
                case '2':
                case '3':
                case '4':
                case '5':
                    goToStage(parseInt(e.key) - 1);
                    break;
            }
        });
    </script>
</body>
</html>

### 3. 过程输出

### 3. 使用指南

## 🧬 免疫应答全过程交互式教学动画使用指南

欢迎使用本交互式教学动画！本指南将帮助您充分利用这一可视化工具，深入理解免疫应答这一复杂而精妙的生物学过程。

---

### 一、功能说明

本动画以**“识别-激活-效应-记忆”**为主线，将免疫应答全过程分解为五个逻辑清晰的阶段，通过**可交互的HTML5 Canvas动画**生动呈现。您可以通过控制面板自主探索，观察细胞间的动态互动，将抽象概念转化为直观的视觉体验。

---

### 二、主要功能

1.  **阶段导航**
    *   **五个核心阶段**：动画严格遵循免疫应答的生物学顺序，分为“抗原入侵与捕获”、“抗原提呈与T细胞活化”、“B细胞激活与分化”、“抗体产生与清除”、“记忆细胞形成”。
    *   **一键跳转**：点击左侧控制面板的阶段按钮，可直接进入任一阶段进行学习或复习。

2.  **动画控制**
    *   **播放/暂停**：控制动画的自动播放，便于在关键步骤暂停观察。
    *   **上一步/下一步**：按逻辑顺序逐步推进或回退，适合跟随教学节奏。
    *   **重新开始**：一键重置动画至初始状态。

3.  **场景切换**
    *   **双场景视图**：在 **“感染局部组织”** 和 **“淋巴结”** 两个关键免疫反应场所间切换。这有助于理解免疫反应发生的**时空顺序**（如APC从组织迁移至淋巴结）。

4.  **交互探索**
    *   **悬停提示**：将鼠标悬停在任意细胞（如树突状细胞、T细胞）上，会弹出**名称和功能说明**。
    *   **点击查看详情**：点击细胞，会弹出更详细的描述框，深化对特定细胞功能的理解。
    *   **视觉图例**：右侧面板提供完整的颜色编码图例，帮助您快速识别不同类型的细胞和分子。

5.  **知识同步**
    *   **动态解说面板**：动画下方区域会随当前阶段变化，同步显示**图文并茂的阶段解说和核心概念**，将视觉观察与理论学习紧密结合。

---

### 三、设计特色

1.  **科学的可视化隐喻**
    *   **颜色编码**：病原体（红）、APC（蓝）、T细胞（绿）、B细胞（橙）、浆细胞（紫）、记忆细胞（金边），符合认知习惯，易于区分。
    *   **动态信号**：用**黄色粒子流**表示细胞因子信号，用**虚线路径**表示细胞迁移和分子传递，清晰展示细胞间的“通信”。
    *   **状态指示**：激活的细胞带有**发光效果**，增殖中的细胞有**动态变化**，记忆细胞有**特殊边框**，直观反映细胞的功能状态。

2.  **符合认知规律的教学设计**
    *   **从宏观到微观**：动画始于组织层面的感染，再聚焦于细胞层面的相互作用。
    *   **因果链条清晰**：每一步动画都强调前因后果（如“APC提呈抗原”导致“T细胞活化”）。
    *   **关键环节高亮**：在当前讲解的步骤中，核心细胞和路径会被高亮显示。

---

### 四、教学要点（建议学习路径）

为达到最佳学习效果，建议按以下路径使用本动画：

1.  **首次学习（按序观看）**
    *   点击 **“播放”** 按钮，让动画自动完整运行一遍，建立对免疫应答全过程的**整体印象**。
    *   关注五个阶段的**顺序衔接**和**场景切换**的逻辑。

2.  **分步精学（主动探索）**
    *   使用 **“暂停”** 和 **“上一步/下一步”** 按钮，在**阶段2（T细胞活化）** 和**阶段3（B细胞活化）** 等关键环节停下来。
    *   **切换场景**，对比观察APC在组织中的“捕获”行为和在淋巴结中的“提呈”行为。
    *   **悬停**在细胞上，仔细阅读其功能描述，特别是“MHC-抗原复合物”、“共刺激信号”、“细胞因子”等关键概念。

3.  **复习与串联（自由探索）**
    *   直接跳转到**阶段5（记忆细胞形成）**，思考记忆细胞与初始T/B细胞在形态和分布上的区别。
    *   尝试回答：如果没有记忆细胞（即跳过阶段5），再次感染会发生什么？从而理解免疫记忆的重要性。
    *   利用**键盘快捷键**（左右箭头切换阶段，空格键播放/暂停）进行快速回顾。

---

### 五、使用建议

*   **对教师**：
    *   **课堂演示**：可在大屏幕上播放，作为讲解免疫应答的动态教具，替代静态幻灯片。
    *   **设置问题**：在播放到关键步骤时暂停，向学生提问（如：“现在T细胞为什么被激活了？需要几个信号？”）。
    *   **翻转课堂**：可将动画链接分享给学生，作为课前预习材料，课堂上则专注于讨论和答疑。
*   **对学生**：
    *   **预习与复习**：在阅读教材前后使用本动画，可极大提升对文字内容的理解。
    *   **构建知识网络**：观看后，尝试在不看动画的情况下，在白纸上画出免疫应答的流程图，并与动画对照。
    *   **关注交互**：不要被动观看，多使用悬停、点击、场景切换功能，主动挖掘信息。
*   **技术提示**：
    *   本动画支持主流现代浏览器（Chrome, Firefox, Edge, Safari）。
    *   在平板电脑上也可获得良好的触控体验。
    *   使用 **F11键** 进入全屏模式，可获得更沉浸的观看体验。

---

**祝您探索愉快！通过这个动态的窗口，您将不仅能“知道”免疫系统如何工作，更能“看见”和“理解”其精妙绝伦的协作之美。** 🐼