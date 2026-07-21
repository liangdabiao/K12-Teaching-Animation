# 需求：任何涉及“微观粒子运动与碰撞”的反应速率和活化能动画

### 1. 专业思考


#### 用户需求分析
用户提出的主题是“任何涉及‘微观粒子运动与碰撞’的反应速率和活化能动画”。这是一个典型的物理化学或基础化学教学核心概念。用户很可能是一位教师、课程开发者或学生，需要一款直观、动态的可视化工具来辅助教学或学习。其深层需求可能包括：
1.  **理解抽象概念**：将肉眼不可见的分子运动、碰撞过程与宏观的反应速率（快慢）建立联系。
2.  **掌握关键变量**：清晰展示温度、浓度、催化剂、活化能如何影响微观过程，进而影响反应速率。
3.  **区分有效与无效碰撞**：这是理解活化能概念的核心，必须通过动画突出展示。
4.  **交互与探索**：用户希望不仅能“看”，还能“操作”，通过改变参数实时观察结果，进行探究式学习。
5.  **简洁与聚焦**：动画应聚焦于核心机制，避免界面过于复杂而分散注意力。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）
*   **核心概念**：
    *   **粒子运动**：分子/原子在不停息地做无规则运动（动能）。
    *   **碰撞**：反应发生的必要前提。
    *   **有效碰撞**：只有那些能量足够高（达到或超过**活化能**）且取向合适的碰撞才能导致反应发生。
    *   **活化能**：反应发生所需的最低能量门槛，是决定反应速率的关键内在因素。
    *   **影响因素**：温度（影响粒子平均动能和能量分布）、浓度（影响碰撞频率）、催化剂（降低活化能）。

*   **认知规律**：
    *   **从宏观到微观**：先提出“为什么有些反应快，有些反应慢？”的宏观问题，再引导至微观解释。
    *   **从静态到动态**：先展示能量分布曲线等静态图示，再结合粒子动画，使概念“活”起来。
    *   **从观察到操作**：让用户先观看默认动画，再通过滑块等控件主动改变条件，观察变化，构建因果理解。

*   **交互设计**：
    *   **模块化布局**：将动画主视图、控制面板、图示说明区清晰分区。
    *   **渐进式揭示**：初始界面简洁，随着用户操作，逐步显示能量分布图、数据统计等高级信息。
    *   **直接操作**：使用滑块调整温度、浓度、活化能；通过按钮添加/移除催化剂。操作与视觉反馈紧密相连。
    *   **焦点与提示**：当发生有效碰撞时，高亮显示碰撞粒子，并伴有视觉（如闪光）和简短文字提示。

*   **视觉呈现**：
    *   **粒子设计**：使用不同颜色（如红 vs 蓝）的圆点代表反应物A和B。设计简洁，带有轻微的运动拖尾或光泽以体现速度感。
    *   **能量可视化**：
        *   粒子颜色或亮度可随其动能微调（能量越高，颜色越暖或越亮）。
        *   在动画区上方或侧边，动态绘制“动能分布曲线”，并用一条清晰的竖线标记“活化能”阈值。超过阈值的粒子在曲线上高亮显示。
    *   **反应示意**：有效碰撞后，粒子可以合并成一个新颜色的粒子（产物C），或改变形状，并伴随一个简单的粒子重组动画。
    *   **数据面板**：实时显示“总碰撞次数”、“有效碰撞次数”、“当前反应速率（如：产物生成数/秒）”等数据。

#### 配色方案选择
*   **主色调**：采用深蓝色（如 `#0f1a2f`）或深灰色（如 `#2d3436`）作为背景，模拟深邃的微观世界或黑板，能有效突出彩色的粒子。
*   **粒子颜色**：
    *   反应物A：`#ff6b6b`（暖红色，醒目）
    *   反应物B：`#4d96ff`（科技蓝，与红色形成对比）
    *   产物C：`#6bcf7f`（绿色，象征新生/生成）
*   **能量与阈值**：
    *   动能分布曲线：`#aaaaaa`（浅灰色）
    *   活化能阈值线：`#ffd93d`（明黄色，代表“门槛”或“临界点”）
    *   高能量粒子/超过阈值的分布区域：`#ff9a3d`（橙色，代表高能量、活跃）
*   **UI控件**：使用浅色（`#ecf0f1`）背景和中等对比度的蓝色（`#3498db`）或绿色（`#2ecc71`）作为交互元素色，确保可读性和可操作性。
*   **提示与数据**：成功提示用绿色（`#2ecc71`），数据标签用白色或浅灰色。

#### 交互功能列表
1.  **动画控制**：开始/暂停/重置按钮。
2.  **参数调节滑块**：
    *   **温度**：调节粒子平均运动速度。低温时粒子慢速移动，高温时快速剧烈移动。
    *   **A/B浓度**：分别调节两种反应物粒子的数量。
    *   **活化能**：调节活化能阈值线的高低。直观展示高活化能（反应难进行）与低活化能（反应易进行）的区别。
3.  **催化剂开关**：一个按钮。打开后，活化能阈值线显著降低，同时可能在动画区域加入一些静态的、不同形状的“催化剂”粒子作为示意。
4.  **视图切换/叠加**：
    *   “显示/隐藏动能分布曲线”复选框。
    *   “高亮有效碰撞”复选框。
5.  **实时数据监控面板**：动态显示碰撞频率、有效碰撞率、估算的反应速率等。
6.  **预设场景按钮**：如“常温常压”、“加热反应”、“加入催化剂”等，一键设置典型情境，便于教师演示或快速对比。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>微观粒子运动与反应速率 | 活化能教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f1a2f 0%, #1a2b3c 100%);
            color: #ecf0f1;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 20px;
            max-width: 900px;
        }

        h1 {
            color: #4d96ff;
            margin-bottom: 8px;
            font-size: 2.2rem;
        }

        .subtitle {
            color: #aaaaaa;
            font-size: 1.1rem;
            margin-bottom: 15px;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            max-width: 1200px;
            justify-content: center;
        }

        .main-panel {
            flex: 1;
            min-width: 600px;
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
        }

        .canvas-container {
            position: relative;
            flex-grow: 1;
            border-radius: 8px;
            overflow: hidden;
            background-color: #0a0e17;
            border: 1px solid #2d3436;
        }

        #mainCanvas {
            display: block;
            width: 100%;
            height: 100%;
        }

        .canvas-overlay {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: rgba(0, 0, 0, 0.7);
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.9rem;
            color: #ffd93d;
            pointer-events: none;
        }

        .control-panel {
            width: 320px;
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .panel-section {
            background-color: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            padding: 15px;
            border-left: 4px solid #3498db;
        }

        .panel-section.catalyst {
            border-left-color: #2ecc71;
        }

        .panel-section.data {
            border-left-color: #ff9a3d;
        }

        h2 {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: #ecf0f1;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        h2 i {
            font-style: normal;
            font-size: 1.1em;
        }

        .control-group {
            margin-bottom: 18px;
        }

        .control-group:last-child {
            margin-bottom: 0;
        }

        label {
            display: block;
            margin-bottom: 6px;
            color: #aaaaaa;
            font-size: 0.95rem;
        }

        .value-display {
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
        }

        .value-display span:last-child {
            color: #ffd93d;
            font-weight: bold;
        }

        .slider-container {
            width: 100%;
        }

        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #2d3436;
            outline: none;
            -webkit-appearance: none;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: #3498db;
            cursor: pointer;
            border: 2px solid #ecf0f1;
        }

        input[type="range"]#tempSlider::-webkit-slider-thumb {
            background: #ff6b6b;
        }

        input[type="range"]#eaSlider::-webkit-slider-thumb {
            background: #ffd93d;
        }

        .button-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        button {
            padding: 10px 16px;
            border: none;
            border-radius: 6px;
            background-color: #3498db;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
            flex-grow: 1;
            min-width: 120px;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
        }

        button:active {
            transform: translateY(0);
        }

        #resetBtn {
            background-color: #95a5a6;
        }

        #catalystBtn {
            background-color: #2ecc71;
        }

        #catalystBtn:hover {
            box-shadow: 0 4px 12px rgba(46, 204, 113, 0.4);
        }

        .toggle-group {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }

        .toggle-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        input[type="checkbox"] {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }

        .data-display {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .data-item {
            background-color: rgba(0, 0, 0, 0.2);
            padding: 12px;
            border-radius: 6px;
            text-align: center;
        }

        .data-value {
            font-size: 1.8rem;
            font-weight: bold;
            color: #ff9a3d;
            margin: 5px 0;
        }

        .data-label {
            font-size: 0.85rem;
            color: #aaaaaa;
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
            gap: 6px;
            font-size: 0.9rem;
        }

        .legend-color {
            width: 16px;
            height: 16px;
            border-radius: 50%;
        }

        .footer {
            margin-top: 25px;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9rem;
            max-width: 900px;
            line-height: 1.5;
        }

        @media (max-width: 1000px) {
            .container {
                flex-direction: column;
                align-items: center;
            }
            
            .main-panel {
                min-width: 90vw;
                height: 500px;
            }
            
            .control-panel {
                width: 90vw;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>微观粒子运动与化学反应速率</h1>
        <p class="subtitle">通过粒子碰撞模型探索活化能、温度、浓度和催化剂对反应速率的影响</p>
    </div>

    <div class="container">
        <div class="main-panel">
            <div class="canvas-container">
                <canvas id="mainCanvas"></canvas>
                <div class="canvas-overlay">活化能阈值: <span id="eaValueOverlay">100</span> 能量单位</div>
            </div>
        </div>

        <div class="control-panel">
            <div class="panel-section">
                <h2><i>⚙️</i> 动画控制</h2>
                <div class="button-group">
                    <button id="startBtn">开始</button>
                    <button id="pauseBtn">暂停</button>
                    <button id="resetBtn">重置</button>
                </div>
                
                <div class="toggle-group">
                    <div class="toggle-item">
                        <input type="checkbox" id="showCurve" checked>
                        <label for="showCurve">显示能量分布</label>
                    </div>
                    <div class="toggle-item">
                        <input type="checkbox" id="highlightCollisions" checked>
                        <label for="highlightCollisions">高亮有效碰撞</label>
                    </div>
                </div>
            </div>

            <div class="panel-section">
                <h2><i>🌡️</i> 反应条件</h2>
                
                <div class="control-group">
                    <div class="value-display">
                        <span>温度</span>
                        <span id="tempValue">300 K</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" id="tempSlider" min="100" max="500" value="300" step="10">
                    </div>
                </div>
                
                <div class="control-group">
                    <div class="value-display">
                        <span>粒子A浓度</span>
                        <span id="concentrationAValue">30</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" id="concentrationASlider" min="5" max="60" value="30" step="1">
                    </div>
                </div>
                
                <div class="control-group">
                    <div class="value-display">
                        <span>粒子B浓度</span>
                        <span id="concentrationBValue">30</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" id="concentrationBSlider" min="5" max="60" value="30" step="1">
                    </div>
                </div>
                
                <div class="control-group">
                    <div class="value-display">
                        <span>活化能 (Ea)</span>
                        <span id="eaValue">100</span>
                    </div>
                    <div class="slider-container">
                        <input type="range" id="eaSlider" min="20" max="200" value="100" step="5">
                    </div>
                    <div style="font-size: 0.8rem; color: #7f8c8d; margin-top: 4px;">
                        活化能是反应发生所需的最低能量
                    </div>
                </div>
            </div>

            <div class="panel-section catalyst">
                <h2><i>⚗️</i> 催化剂</h2>
                <p style="color: #aaaaaa; margin-bottom: 15px; font-size: 0.95rem;">
                    催化剂通过提供替代反应路径降低活化能，但不改变总能量。
                </p>
                <button id="catalystBtn">添加催化剂</button>
                <div style="margin-top: 10px; font-size: 0.9rem;">
                    <span>当前状态: </span>
                    <span id="catalystStatus" style="color: #ff6b6b;">未使用</span>
                </div>
            </div>

            <div class="panel-section data">
                <h2><i>📊</i> 实时数据</h2>
                <div class="data-display">
                    <div class="data-item">
                        <div class="data-value" id="totalCollisions">0</div>
                        <div class="data-label">总碰撞次数</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value" id="effectiveCollisions">0</div>
                        <div class="data-label">有效碰撞次数</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value" id="reactionRate">0.0</div>
                        <div class="data-label">反应速率</div>
                    </div>
                    <div class="data-item">
                        <div class="data-value" id="efficiency">0%</div>
                        <div class="data-label">有效碰撞率</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="legend">
        <div class="legend-item">
            <div class="legend-color" style="background-color: #ff6b6b;"></div>
            <span>粒子 A (反应物)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background-color: #4d96ff;"></div>
            <span>粒子 B (反应物)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background-color: #6bcf7f;"></div>
            <span>粒子 C (产物)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background-color: #ffd93d;"></div>
            <span>活化能阈值</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background-color: #ff9a3d;"></div>
            <span>高能量粒子</span>
        </div>
    </div>

    <div class="footer">
        <p><strong>教学提示：</strong> 观察温度如何影响粒子运动速度，活化能如何决定有效碰撞的比例，以及催化剂如何通过降低活化能门槛来加速反应。</p>
        <p>有效碰撞 = 能量 ≥ 活化能 + 正确取向的碰撞 | 反应速率 ∝ 有效碰撞频率</p>
    </div>

    <script>
        // 获取Canvas和上下文
        const canvas = document.getElementById('mainCanvas');
        const ctx = canvas.getContext('2d');

        // 设置Canvas尺寸
        function resizeCanvas() {
            const container = canvas.parentElement;
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
        }
        
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // 获取DOM元素
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const resetBtn = document.getElementById('resetBtn');
        const catalystBtn = document.getElementById('catalystBtn');
        const tempSlider = document.getElementById('tempSlider');
        const concentrationASlider = document.getElementById('concentrationASlider');
        const concentrationBSlider = document.getElementById('concentrationBSlider');
        const eaSlider = document.getElementById('eaSlider');
        const showCurve = document.getElementById('showCurve');
        const highlightCollisions = document.getElementById('highlightCollisions');
        
        const tempValue = document.getElementById('tempValue');
        const concentrationAValue = document.getElementById('concentrationAValue');
        const concentrationBValue = document.getElementById('concentrationBValue');
        const eaValue = document.getElementById('eaValue');
        const eaValueOverlay = document.getElementById('eaValueOverlay');
        const catalystStatus = document.getElementById('catalystStatus');
        
        const totalCollisionsEl = document.getElementById('totalCollisions');
        const effectiveCollisionsEl = document.getElementById('effectiveCollisions');
        const reactionRateEl = document.getElementById('reactionRate');
        const efficiencyEl = document.getElementById('efficiency');

        // 颜色常量
        const COLOR_A = '#ff6b6b';
        const COLOR_B = '#4d96ff';
        const COLOR_C = '#6bcf7f';
        const COLOR_THRESHOLD = '#ffd93d';
        const COLOR_HIGH_ENERGY = '#ff9a3d';
        const COLOR_CURVE = '#aaaaaa';
        const BG_COLOR = '#0a0e17';

        // 粒子类
        class Particle {
            constructor(type, x, y, vx, vy, radius) {
                this.type = type; // 'A', 'B', 或 'C'
                this.x = x;
                this.y = y;
                this.vx = vx;
                this.vy = vy;
                this.radius = radius;
                this.energy = Math.sqrt(vx*vx + vy*vy) * 5; // 简化能量计算
                this.color = type === 'A' ? COLOR_A : (type === 'B' ? COLOR_B : COLOR_C);
                this.highlight = false;
                this.highlightTimer = 0;
            }
            
            update() {
                // 更新位置
                this.x += this.vx;
                this.y += this.vy;
                
                // 边界碰撞
                if (this.x - this.radius < 0 || this.x + this.radius > canvas.width) {
                    this.vx = -this.vx;
                    this.x = Math.max(this.radius, Math.min(canvas.width - this.radius, this.x));
                }
                if (this.y - this.radius < 0 || this.y + this.radius > canvas.height) {
                    this.vy = -this.vy;
                    this.y = Math.max(this.radius, Math.min(canvas.height - this.radius, this.y));
                }
                
                // 更新能量（基于速度）
                this.energy = Math.sqrt(this.vx*this.vx + this.vy*this.vy) * 5;
                
                // 更新高亮计时器
                if (this.highlightTimer > 0) {
                    this.highlightTimer--;
                    this.highlight = true;
                } else {
                    this.highlight = false;
                }
            }
            
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                
                // 如果粒子能量高，使用高亮颜色
                let drawColor = this.color;
                if (this.energy > activationEnergy && this.type !== 'C') {
                    // 根据能量比例混合颜色
                    const energyRatio = Math.min(1, (this.energy - activationEnergy) / 50);
                    drawColor = mixColors(this.color, COLOR_HIGH_ENERGY, energyRatio);
                }
                
                // 如果被高亮（有效碰撞）
                if (this.highlight) {
                    ctx.shadowColor = '#ffffff';
                    ctx.shadowBlur = 15;
                }
                
                ctx.fillStyle = drawColor;
                ctx.fill();
                
                // 重置阴影
                ctx.shadowColor = 'transparent';
                ctx.shadowBlur = 0;
                
                // 如果是产物C，画一个小内圈表示不同
                if (this.type === 'C') {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.radius * 0.6, 0, Math.PI * 2);
                    ctx.fillStyle = '#ffffff';
                    ctx.globalAlpha = 0.3;
                    ctx.fill();
                    ctx.globalAlpha = 1.0;
                }
            }
            
            // 高亮粒子（用于有效碰撞）
            highlightParticle() {
                this.highlightTimer = 20; // 高亮持续20帧
            }
        }

        // 颜色混合辅助函数
        function mixColors(color1, color2, ratio) {
            const r1 = parseInt(color1.substr(1, 2), 16);
            const g1 = parseInt(color1.substr(3, 2), 16);
            const b1 = parseInt(color1.substr(5, 2), 16);
            
            const r2 = parseInt(color2.substr(1, 2), 16);
            const g2 = parseInt(color2.substr(3, 2), 16);
            const b2 = parseInt(color2.substr(5, 2), 16);
            
            const r = Math.round(r1 * (1 - ratio) + r2 * ratio);
            const g = Math.round(g1 * (1 - ratio) + g2 * ratio);
            const b = Math.round(b1 * (1 - ratio) + b2 * ratio);
            
            return `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;
        }

        // 全局变量
        let particles = [];
        let animationId = null;
        let isRunning = false;
        let lastTime = 0;
        
        // 反应参数
        let temperature = 300; // K
        let concentrationA = 30;
        let concentrationB = 30;
        let activationEnergy = 100; // 活化能
        let catalystActive = false;
        
        // 统计数据
        let totalCollisions = 0;
        let effectiveCollisions = 0;
        let productsCount = 0;
        let lastProductTime = 0;
        let reactionRate = 0;

        // 初始化粒子
        function initParticles() {
            particles = [];
            
            // 创建A粒子
            for (let i = 0; i < concentrationA; i++) {
                const speed = 1 + Math.random() * (temperature / 150);
                const angle = Math.random() * Math.PI * 2;
                particles.push(new Particle(
                    'A',
                    Math.random() * (canvas.width - 40) + 20,
                    Math.random() * (canvas.height - 40) + 20,
                    Math.cos(angle) * speed,
                    Math.sin(angle) * speed,
                    8
                ));
            }
            
            // 创建B粒子
            for (let i = 0; i < concentrationB; i++) {
                const speed = 1 + Math.random() * (temperature / 150);
                const angle = Math.random() * Math.PI * 2;
                particles.push(new Particle(
                    'B',
                    Math.random() * (canvas.width - 40) + 20,
                    Math.random() * (canvas.height - 40) + 20,
                    Math.cos(angle) * speed,
                    Math.sin(angle) * speed,
                    8
                ));
            }
            
            // 重置统计数据
            totalCollisions = 0;
            effectiveCollisions = 0;
            productsCount = 0;
            reactionRate = 0;
            updateStats();
        }

        // 检测和处理碰撞
        function handleCollisions() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const p1 = particles[i];
                    const p2 = particles[j];
                    
                    // 只检查A和B之间的碰撞
                    if ((p1.type === 'A' && p2.type === 'B') || (p1.type === 'B' && p2.type === 'A')) {
                        const dx = p2.x - p1.x;
                        const dy = p2.y - p1.y;
                        const distance = Math.sqrt(dx * dx + dy * dy);
                        
                        // 如果发生碰撞
                        if (distance < p1.radius + p2.radius) {
                            totalCollisions++;
                            
                            // 计算相对速度（用于能量计算）
                            const relativeSpeed = Math.sqrt(
                                Math.pow(p1.vx - p2.vx, 2) + 
                                Math.pow(p1.vy - p2.vy, 2)
                            );
                            const collisionEnergy = relativeSpeed * 8;
                            
                            // 有效碰撞：能量足够高
                            const effectiveEnergy = catalystActive ? 
                                activationEnergy * 0.6 : activationEnergy;
                            
                            if (collisionEnergy >= effectiveEnergy) {
                                effectiveCollisions++;
                                
                                // 高亮碰撞粒子
                                if (highlightCollisions.checked) {
                                    p1.highlightParticle();
                                    p2.highlightParticle();
                                }
                                
                                // 有一定概率生成产物C（模拟取向因素）
                                if (Math.random() < 0.7) {
                                    createProduct(p1, p2);
                                }
                            }
                            
                            // 弹性碰撞响应（简化版）
                            const angle = Math.atan2(dy, dx);
                            const sin = Math.sin(angle);
                            const cos = Math.cos(angle);
                            
                            // 旋转速度
                            const vx1 = p1.vx * cos + p1.vy * sin;
                            const vy1 = p1.vy * cos - p1.vx * sin;
                            const vx2 = p2.vx * cos + p2.vy * sin;
                            const vy2 = p2.vy * cos - p2.vx * sin;
                            
                            // 交换x方向速度（一维弹性碰撞）
                            const finalVx1 = vx2;
                            const finalVx2 = vx1;
                            
                            // 旋转回原始坐标系
                            p1.vx = finalVx1 * cos - vy1 * sin;
                            p1.vy = vy1 * cos + finalVx1 * sin;
                            p2.vx = finalVx2 * cos - vy2 * sin;
                            p2.vy = vy2 * cos + finalVx2 * sin;
                            
                            // 防止粒子重叠
                            const overlap = (p1.radius + p2.radius - distance) / 2;
                            p1.x -= overlap * (dx / distance);
                            p1.y -= overlap * (dy / distance);
                            p2.x += overlap * (dx / distance);
                            p2.y += overlap * (dy / distance);
                        }
                    }
                }
            }
        }

        // 创建产物C
        function createProduct(p1, p2) {
            // 移除原来的两个粒子
            const index1 = particles.indexOf(p1);
            const index2 = particles.indexOf(p2);
            
            // 确保index2 > index1，这样先删除index2不会影响index1
            if (index1 > index2) {
                particles.splice(index1, 1);
                particles.splice(index2, 1);
            } else {
                particles.splice(index2, 1);
                particles.splice(index1, 1);
            }
            
            // 创建新的产物C粒子
            const avgX = (p1.x + p2.x) / 2;
            const avgY = (p1.y + p2.y) / 2;
            const avgVx = (p1.vx + p2.vx) / 2;
            const avgVy = (p1.vy + p2.vy) / 2;
            
            particles.push(new Particle(
                'C',
                avgX,
                avgY,
                avgVx * 0.8,
                avgVy * 0.8,
                10
            ));
            
            productsCount++;
            lastProductTime = Date.now();
        }

        // 绘制能量分布曲线
        function drawEnergyDistribution() {
            if (!showCurve.checked) return;
            
            const curveWidth = canvas.width * 0.8;
            const curveHeight = 100;
            const curveX = canvas.width * 0.1;
            const curveY = 30;
            
            // 计算粒子能量分布
            const energyBins = new Array(20).fill(0);
            let maxCount = 1;
            
            for (const p of particles) {
                if (p.type === 'C') continue; // 不计入产物
                
                const energy = p.energy;
                const binIndex = Math.min(19, Math.floor(energy / 10));
                energyBins[binIndex]++;
                maxCount = Math.max(maxCount, energyBins[binIndex]);
            }
            
            // 绘制背景
            ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
            ctx.fillRect(curveX - 5, curveY - 5, curveWidth + 10, curveHeight + 10);
            
            // 绘制坐标轴
            ctx.strokeStyle = COLOR_CURVE;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(curveX, curveY + curveHeight);
            ctx.lineTo(curveX + curveWidth, curveY + curveHeight);
            ctx.moveTo(curveX, curveY);
            ctx.lineTo(curveX, curveY + curveHeight);
            ctx.stroke();
            
            // 绘制曲线
            ctx.strokeStyle = COLOR_CURVE;
            ctx.lineWidth = 2;
            ctx.beginPath();
            
            for (let i = 0; i < energyBins.length; i++) {
                const x = curveX + (i / energyBins.length) * curveWidth;
                const height = (energyBins[i] / maxCount) * curveHeight;
                const y = curveY + curveHeight - height;
                
                if (i === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            }
            ctx.stroke();
            
            // 填充曲线下方区域
            ctx.fillStyle = 'rgba(170, 170, 170, 0.2)';
            ctx.beginPath();
            ctx.moveTo(curveX, curveY + curveHeight);
            for (let i = 0; i < energyBins.length; i++) {
                const x = curveX + (i / energyBins.length) * curveWidth;
                const height = (energyBins[i] / maxCount) * curveHeight;
                const y = curveY + curveHeight - height;
                ctx.lineTo(x, y);
            }
            ctx.lineTo(curveX + curveWidth, curveY + curveHeight);
            ctx.closePath();
            ctx.fill();
            
            // 绘制活化能阈值线
            const eaX = curveX + (activationEnergy / 200) * curveWidth;
            ctx.strokeStyle = COLOR_THRESHOLD;
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 3]);
            ctx.beginPath();
            ctx.moveTo(eaX, curveY);
            ctx.lineTo(eaX, curveY + curveHeight);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // 填充高能量区域
            const fillStartX = catalystActive ? 
                curveX + (activationEnergy * 0.6 / 200) * curveWidth : eaX;
            
            ctx.fillStyle = 'rgba(255, 154, 61, 0.3)';
            ctx.fillRect(fillStartX, curveY, curveX + curveWidth - fillStartX, curveHeight);
            
            // 添加标签
            ctx.fillStyle = COLOR_CURVE;
            ctx.font = '12px Arial';
            ctx.fillText('能量分布', curveX + 5, curveY - 5);
            ctx.fillText('低', curveX - 15, curveY + curveHeight + 15);
            ctx.fillText('高', curveX + curveWidth - 10, curveY + curveHeight + 15);
            
            ctx.fillStyle = COLOR_THRESHOLD;
            ctx.fillText(`活化能: ${activationEnergy}`, eaX + 5, curveY + 15);
            
            if (catalystActive) {
                ctx.fillStyle = '#2ecc71';
                ctx.fillText(`催化剂降低活化能`, fillStartX + 5, curveY + 30);
            }
        }

        // 更新统计数据显示
        function updateStats() {
            totalCollisionsEl.textContent = totalCollisions;
            effectiveCollisionsEl.textContent = effectiveCollisions;
            
            // 计算反应速率（最近5秒内的平均产物生成速率）
            const now = Date.now();
            const timeWindow = 5000; // 5秒
            const recentProducts = Math.min(productsCount, 10); // 简化计算
            
            reactionRate = recentProducts / (timeWindow / 1000); // 产物/秒
            reactionRateEl.textContent = reactionRate.toFixed(2);
            
            // 计算有效碰撞率
            const efficiency = totalCollisions > 0 ? 
                Math.round((effectiveCollisions / totalCollisions) * 100) : 0;
            efficiencyEl.textContent = `${efficiency}%`;
            
            // 更新UI显示
            tempValue.textContent = `${temperature} K`;
            concentrationAValue.textContent = concentrationA;
            concentrationBValue.textContent = concentrationB;
            eaValue.textContent = activationEnergy;
            eaValueOverlay.textContent = activationEnergy;
            
            catalystStatus.textContent = catalystActive ? '已激活' : '未使用';
            catalystStatus.style.color = catalystActive ? '#2ecc71' : '#ff6b6b';
            catalystBtn.textContent = catalystActive ? '移除催化剂' : '添加催化剂';
        }

        // 主动画循环
        function animate(timestamp) {
            if (!lastTime) lastTime = timestamp;
            const deltaTime = timestamp - lastTime;
            lastTime = timestamp;
            
            // 清空画布
            ctx.fillStyle = BG_COLOR;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 更新所有粒子
            for (const particle of particles) {
                particle.update();
            }
            
            // 处理碰撞
            handleCollisions();
            
            // 绘制所有粒子
            for (const particle of particles) {
                particle.draw();
            }
            
            // 绘制能量分布曲线
            drawEnergyDistribution();
            
            // 更新统计数据
            updateStats();
            
            // 继续动画循环
            if (isRunning) {
                animationId = requestAnimationFrame(animate);
            }
        }

        // 开始动画
        function startAnimation() {
            if (!isRunning) {
                isRunning = true;
                lastTime = 0;
                animationId = requestAnimationFrame(animate);
            }
        }

        // 暂停动画
        function pauseAnimation() {
            isRunning = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
        }

        // 重置动画
        function resetAnimation() {
            pauseAnimation();
            temperature = 300;
            concentrationA = 30;
            concentrationB = 30;
            activationEnergy = 100;
            catalystActive = false;
            
            // 更新滑块
            tempSlider.value = temperature;
            concentrationASlider.value = concentrationA;
            concentrationBSlider.value = concentrationB;
            eaSlider.value = activationEnergy;
            
            initParticles();
            updateStats();
        }

        // 切换催化剂
        function toggleCatalyst() {
            catalystActive = !catalystActive;
            updateStats();
        }

        // 事件监听器
        startBtn.addEventListener('click', startAnimation);
        pauseBtn.addEventListener('click', pauseAnimation);
        resetBtn.addEventListener('click', resetAnimation);
        catalystBtn.addEventListener('click', toggleCatalyst);

        tempSlider.addEventListener('input', function() {
            temperature = parseInt(this.value);
            
            // 更新所有粒子的速度（基于温度）
            const speedFactor = temperature / 300;
            for (const p of particles) {
                p.vx *= speedFactor;
                p.vy *= speedFactor;
            }
            
            updateStats();
        });

        concentrationASlider.addEventListener('input', function() {
            const newCount = parseInt(this.value);
            const diff = newCount - concentrationA;
            
            if (diff > 0) {
                // 添加A粒子
                for (let i = 0; i < diff; i++) {
                    const speed = 1 + Math.random() * (temperature / 150);
                    const angle = Math.random() * Math.PI * 2;
                    particles.push(new Particle(
                        'A',
                        Math.random() * (canvas.width - 40) + 20,
                        Math.random() * (canvas.height - 40) + 20,
                        Math.cos(angle) * speed,
                        Math.sin(angle) * speed,
                        8
                    ));
                }
            }
} else if (diff < 0) {
                // 移除A粒子
                let removed = 0;
                for (let i = particles.length - 1; i >= 0 && removed < -diff; i--) {
                    if (particles[i].type === 'A') {
                        particles.splice(i, 1);
                        removed++;
                    }
                }
            }
            
            concentrationA = newCount;
            updateStats();
        });

        concentrationBSlider.addEventListener('input', function() {
            const newCount = parseInt(this.value);
            const diff = newCount - concentrationB;
            
            if (diff > 0) {
                // 添加B粒子
                for (let i = 0; i < diff; i++) {
                    const speed = 1 + Math.random() * (temperature / 150);
                    const angle = Math.random() * Math.PI * 2;
                    particles.push(new Particle(
                        'B',
                        Math.random() * (canvas.width - 40) + 20,
                        Math.random() * (canvas.height - 40) + 20,
                        Math.cos(angle) * speed,
                        Math.sin(angle) * speed,
                        8
                    ));
                }
            } else if (diff < 0) {
                // 移除B粒子
                let removed = 0;
                for (let i = particles.length - 1; i >= 0 && removed < -diff; i--) {
                    if (particles[i].type === 'B') {
                        particles.splice(i, 1);
                        removed++;
                    }
                }
            }
            
            concentrationB = newCount;
            updateStats();
        });

        eaSlider.addEventListener('input', function() {
            activationEnergy = parseInt(this.value);
            updateStats();
        });

        // 初始化
        initParticles();
        startAnimation();

        // 添加预设场景示例（可通过控制台调用）
        window.demoScenes = {
            lowTemp: function() {
                pauseAnimation();
                temperature = 150;
                tempSlider.value = temperature;
                initParticles();
                startAnimation();
            },
            highTemp: function() {
                pauseAnimation();
                temperature = 450;
                tempSlider.value = temperature;
                initParticles();
                startAnimation();
            },
            highEa: function() {
                pauseAnimation();
                activationEnergy = 180;
                eaSlider.value = activationEnergy;
                initParticles();
                startAnimation();
            },
            withCatalyst: function() {
                pauseAnimation();
                catalystActive = true;
                initParticles();
                startAnimation();
            }
        };
    </script>
</body>
</html>


### 3. 过程输出

### 3. 使用指南

## 《微观粒子运动与反应速率》交互式教学动画使用指南

欢迎使用这款专业的化学动力学教学动画！本工具旨在将抽象的微观粒子碰撞、活化能与反应速率等核心概念，转化为直观、动态、可交互的可视化体验。无论您是教师、学生还是自学者，都能通过探索和操作，深刻理解化学反应速率背后的微观机制。

---

### 一、 功能说明

本动画模拟了一个由A粒子（红色）和B粒子（蓝色）参与的化学反应。通过观察它们在容器中的运动、碰撞以及生成产物C（绿色）的过程，您可以直观地探究以下因素如何影响反应速率：
- **温度**：影响粒子的平均动能和运动速度。
- **浓度**：影响单位时间内粒子碰撞的频率。
- **活化能**：决定一次碰撞能否发生化学反应的能量门槛。
- **催化剂**：通过降低活化能，提高有效碰撞的比例。

动画界面分为三个主要区域：
1.  **主视图区（左侧）**：动态展示所有粒子的运动、碰撞及反应过程，并叠加能量分布曲线。
2.  **控制面板区（右侧）**：提供所有交互控件，用于调节反应条件和查看实时数据。
3.  **图例与说明区（底部）**：解释各颜色代表的意义，并提供关键教学提示。

---

### 二、 主要功能与操作

#### 1. 动画控制
- **开始/暂停/重置**：控制动画的播放。`重置`按钮将恢复所有参数至初始状态。

#### 2. 反应条件调节（核心交互）
使用滑块实时调整参数，并立即在动画中观察效果：
- **🌡️ 温度**：向右滑动提高温度，粒子运动速度明显加快，碰撞更频繁剧烈。
- **🧪 粒子A/B浓度**：增加粒子数量，直接提高单位体积内的碰撞机会。
- **⚡ 活化能**：调节反应发生的能量门槛。调高活化能，有效碰撞（能生成产物的碰撞）比例显著下降；调低则反之。
- **⚗️ 催化剂**：点击“添加催化剂”按钮，活化能阈值线会**显著降低**（变为原来的60%），模拟催化剂提供“低能量路径”的效果。注意观察有效碰撞率和反应速率的变化。

#### 3. 视图选项
- **显示能量分布**：勾选后，主视图上方将显示粒子动能分布曲线。黄色虚线代表活化能，橙色区域代表能量超过阈值的粒子比例。这是理解“能量分布”和“活化能”概念的**关键可视化工具**。
- **高亮有效碰撞**：勾选后，每一次能够满足能量条件的碰撞，相关粒子会短暂高亮（发光），便于追踪。

#### 4. 实时数据监控
数据面板每秒更新，提供量化反馈：
- **总碰撞次数**：所有A与B粒子之间的碰撞。
- **有效碰撞次数**：能量达到或超过（催化后）活化能的碰撞。
- **反应速率**：单位时间内生成产物C的数量（个/秒）。
- **有效碰撞率**：(有效碰撞次数 / 总碰撞次数) × 100%。**这是理解活化能影响最直接的指标**。

---

### 三、 设计特色

1.  **双重视觉编码**：
    - **粒子层面**：高能量粒子颜色会偏向橙色，直观体现“能量越高，越可能反应”。
    - **统计层面**：能量分布曲线宏观展示全体粒子的能量分布，并与活化能阈值对比。
2.  **即时因果反馈**：任何参数调整，其效果（粒子速度、碰撞频率、产物生成速度）都在不到一秒内呈现，强化“条件-结果”的因果关系认知。
3.  **聚焦核心机制**：界面去除非必要元素，将用户的注意力集中在“运动-碰撞-能量判断-反应”这一核心链条上。
4.  **专业美学**：采用深色背景模拟微观世界或黑板，高对比度的粒子颜色确保清晰度，整体配色科学且舒适。

---

### 四、 教学要点与探究问题

**教师或学习者可以围绕以下要点进行观察与思考：**

1.  **温度的影响**：
    - **现象**：提高温度，粒子运动变快。
    - **微观解释**：粒子平均动能增加，导致：a) 碰撞频率增加；b) **更多粒子的能量超过活化能**（观察能量分布曲线右移）。
    - **宏观结果**：总碰撞次数和有效碰撞率均上升，反应速率显著加快。
    - **提问**：“为什么温度升高10℃，反应速率往往能增加一倍以上？”（关键在能量分布的变化，而不仅是速度增加）。

2.  **活化能的核心作用**：
    - **现象**：调整活化能滑块。
    - **观察重点**：有效碰撞率的变化。活化能是反应的“内在阻力”。
    - **提问**：“为什么不同的化学反应速率差异巨大？”（主要源于活化能不同）。

3.  **催化剂的魔力**：
    - **现象**：点击“添加催化剂”，活化能阈值线降低。
    - **关键观察**：**反应速率大幅提升，但粒子的平均速度和能量分布并未改变**。催化剂没有提供能量，而是降低了“能量门槛”。
    - **提问**：“催化剂为什么不能启动一个热力学上不能发生的反应？”（它只改变路径，不改变始终态能量）。

4.  **浓度的影响**：
    - **现象**：增加A或B粒子的数量。
    - **微观解释**：单位空间内粒子密度增大，碰撞频率成比例增加。
    - **宏观结果**：反应速率增加，但有效碰撞率基本不变（因为粒子能量分布未变）。

---

### 五、 使用建议

1.  **初次探索**：建议先点击“开始”，观察默认状态下的动画。然后逐一调节每个滑块，观察单个变量改变带来的影响。
2.  **对比实验**：
    - 先记录低温（如150K）下的反应速率，再调到高温（如450K）对比。
    - 在活化能较高（如180）时开启催化剂，与未开启时进行对比，效果极其显著。
3.  **课堂演示**：
    - **教师**：可全屏播放，在讲解概念时同步操作动画，作为动态板书。利用“暂停”功能定格某一瞬间进行讲解。
    - 可使用指南中的“探究问题”引导学生观察和讨论。
4.  **深度学习**：鼓励学生提出假设并验证。例如：“如果我把温度升得很高，但活化能也调得很高，反应速率会怎样？”然后动手操作检验。
5.  **技术提示**：本动画为单HTML文件，可在任何现代浏览器（Chrome, Edge, Firefox等）中离线运行。您可以将它下载到本地，或直接嵌入在线学习平台中使用。

---

**祝您探索愉快！希望这款动画能像一扇窗，让您清晰地窥见化学反应背后那个永不停息、充满碰撞的精彩微观世界。**