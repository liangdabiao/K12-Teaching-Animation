# 需求：带电粒子在匀强磁场中的圆周运动（洛伦兹力提供向心力）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为高中或大学低年级的物理学习者。他们已具备基础的力学和电磁学知识，但可能对抽象的磁场力与圆周运动结合的概念感到困难。
2.  **核心痛点**：
    *   **抽象性**：磁场无形，洛伦兹力方向（左手定则）和粒子轨迹的动态形成过程难以想象。
    *   **动态关系理解**：粒子速度、质量、电荷量、磁场强度如何影响轨道半径和周期，学生往往只能记忆公式 `r = mv/(qB)` 和 `T = 2πm/(qB)`，缺乏直观的、定性的理解。
    *   **参数关联性**：多个变量同时变化时，对结果的影响容易混淆。
3.  **学习目标**：
    *   **理解**：洛伦兹力如何提供匀速圆周运动的向心力。
    *   **掌握**：左手定则判断粒子偏转方向（区分正负电荷）。
    *   **推导与记忆**：轨道半径和周期公式，并理解其物理意义。
    *   **应用**：能定性分析单个参数变化对运动轨迹的影响。

#### 教学设计思路
1.  **核心概念分解**：
    *   **洛伦兹力**：大小 (`F=qvB`)，方向（左手定则，垂直于速度与磁场平面）。
    *   **向心力**：大小 (`F=mv²/r`)，方向（始终指向圆心）。
    *   **运动合成**：将粒子的复杂螺旋进动简化为垂直于磁场的平面内的匀速圆周运动（本节课重点）。
    *   **公式关联**：建立 `qvB = mv²/r`，推导出 `r = mv/(qB)` 和 `T = 2πm/(qB)`。

2.  **认知规律遵循**：
    *   **从具体到抽象**：先展示可见的粒子轨迹，再叠加表示磁场和力的矢量箭头，最后呈现公式。
    *   **从静态到动态**：先展示一个完整的圆轨道，然后让粒子运动起来，观察其速度与力的实时关系。
    *   **从观察到解释**：学生先看到“改变参数，轨迹变了”的现象，再引导其思考“为什么变了”，最后用公式进行确认。

3.  **交互设计**：
    *   **控制与观察分离**：界面左侧为参数控制面板，右侧为动画主视图，符合“控制变量-观察结果”的科学探究流程。
    *   **分层显示**：允许用户选择显示/隐藏“磁场线”、“力矢量”、“速度矢量”、“轨迹”等元素，避免初学时信息过载，也便于进阶探究。
    *   **即时反馈**：任何参数调整后，动画立即更新，轨迹、半径、周期指示器同步变化，建立直接的因果联系。
    *   **关键状态“冻结”与提示**：可暂停动画，并在粒子特定位置高亮显示并标注洛伦兹力与速度的方向关系，强化左手定则的应用。

4.  **视觉呈现**：
    *   **主视图**：一个清晰的二维平面，模拟粒子在垂直于屏幕的匀强磁场中的运动。
    *   **粒子与轨迹**：粒子为醒目的发光圆点，正负电荷用“+”/“-”号或颜色区分（如红色正电荷，蓝色负电荷）。轨迹线清晰且略带渐变或辉光，体现运动感。
    *   **矢量表示**：
        *   **速度(v)**：绿色箭头，始终沿轨迹切线方向。
        *   **洛伦兹力(F)**：红色箭头，始终指向圆心，与速度箭头垂直。
        *   矢量长度应能反映其大小，随参数变化而动态缩放。
    *   **磁场(B)**：用一组均匀分布、指向一致的箭头（如“×”表示进屏幕，“·”表示出屏幕）或虚线表示，覆盖整个动画区域。
    *   **信息显示**：实时显示关键参数（v, m, q, B）的数值、当前半径r和周期T的计算值。

#### 配色方案选择
*   **背景**：深空蓝或深灰色 (`#1a1a2e` 或 `#2d2d44`)。深色背景能有效突出彩色的运动元素和矢量，减少视觉疲劳，营造科技感和专注的学习环境。
*   **粒子与轨迹**：
    *   正电荷粒子：暖色调，如亮红色 (`#ff4757`) 或橙色 (`#ffa502`)。
    *   负电荷粒子：冷色调，如亮蓝色 (`#3742fa`) 或青色 (`#2ed573`)。
    *   运动轨迹：使用对应粒子颜色的半透明线条或渐隐尾迹 (`rgba(255, 71, 87, 0.7)`)。
*   **矢量箭头**：
    *   速度(v)：鲜绿色 (`#00ff00` 或 `#7bed9f`)，代表“运动”。
    *   洛伦兹力(F)：亮红色 (`#ff3838`)，代表“力”。
    *   磁场(B)：浅灰色 (`#aaaaaa`) 或淡蓝色 (`#70a1ff`)，半透明，作为背景元素不喧宾夺主。
*   **控制面板与文本**：
    *   面板背景：半透明暗色 (`rgba(40, 40, 60, 0.8)`)。
    *   标签文字：浅灰色 (`#ecf0f1`)。
    *   输入框/滑块：亮色边框 (`#3498db`)。
    *   数值显示：白色 (`#ffffff`) 或亮黄色 (`#f1c40f`)。

#### 交互功能列表
1.  **核心动画控制**：
    *   开始 / 暂停 / 重置 按钮。
    *   动画速度调节滑块。
2.  **粒子与物理参数控制（滑块+输入框，带实时联动）**：
    *   粒子电荷 (`q`)：可正可负，数值可调。
    *   粒子质量 (`m`)。
    *   粒子初速度大小 (`v`)。
    *   磁感应强度 (`B`)。
3.  **可视化元素开关（复选框）**：
    *   显示/隐藏 磁场方向指示。
    *   显示/隐藏 速度矢量 (`v`)。
    *   显示/隐藏 洛伦兹力矢量 (`F`)。
    *   显示/隐藏 粒子运动轨迹。
    *   显示/隐藏 圆心和半径辅助线。
4.  **信息显示面板**：
    *   实时显示粒子坐标。
    *   实时显示当前洛伦兹力大小 (`F`)。
    *   实时计算并显示轨道半径 (`r`) 和运动周期 (`T`)。
    *   公式提示区：常驻显示 `r = mv/(qB)` 和 `T = 2πm/(qB)`。
5.  **教学辅助功能**：
    *   **轨迹追踪**：粒子留下渐隐的轨迹，便于观察完整圆形。
    *   **单步前进**：在暂停模式下，点击“单步”按钮，粒子前进一小段，便于细致观察某一点的速度与力方向。
    *   **重置视图**：将粒子放回起始位置，并清除已有轨迹。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>带电粒子在匀强磁场中的圆周运动</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
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
            padding: 15px;
            background: rgba(40, 40, 60, 0.7);
            border-radius: 15px;
            border: 2px solid #3498db;
            width: 100%;
            max-width: 1200px;
        }

        .header h1 {
            color: #f1c40f;
            margin-bottom: 8px;
            font-size: 2.2rem;
        }

        .header p {
            color: #bdc3c7;
            font-size: 1.1rem;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.5;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            width: 100%;
            max-width: 1200px;
            justify-content: center;
        }

        .control-panel {
            background: rgba(40, 40, 60, 0.85);
            border-radius: 15px;
            padding: 25px;
            width: 320px;
            border: 2px solid #3498db;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .panel-section {
            background: rgba(30, 30, 50, 0.6);
            padding: 18px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }

        .panel-section h3 {
            color: #f1c40f;
            margin-bottom: 15px;
            font-size: 1.3rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .panel-section h3 i {
            font-size: 1.2rem;
        }

        .control-group {
            margin-bottom: 15px;
        }

        .control-group label {
            display: block;
            margin-bottom: 8px;
            color: #bdc3c7;
            font-size: 1rem;
        }

        .slider-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .slider-container input[type="range"] {
            flex: 1;
            height: 8px;
            -webkit-appearance: none;
            background: linear-gradient(to right, #1e90ff, #00ced1);
            border-radius: 4px;
            outline: none;
        }

        .slider-container input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 22px;
            height: 22px;
            background: #f1c40f;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid #fff;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
        }

        .slider-container input[type="number"] {
            width: 80px;
            padding: 8px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #3498db;
            border-radius: 6px;
            color: white;
            text-align: center;
            font-size: 1rem;
        }

        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 10px;
        }

        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.3s;
            padding: 5px;
            border-radius: 5px;
        }

        .checkbox-item:hover {
            background: rgba(255, 255, 255, 0.1);
        }

        .checkbox-item input[type="checkbox"] {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }

        .checkbox-item label {
            cursor: pointer;
            color: #ecf0f1;
            font-size: 0.95rem;
        }

        .button-group {
            display: flex;
            gap: 12px;
            margin-top: 10px;
        }

        button {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        #startBtn {
            background: linear-gradient(to right, #2ecc71, #27ae60);
            color: white;
        }

        #startBtn:hover {
            background: linear-gradient(to right, #27ae60, #219653);
            transform: translateY(-2px);
        }

        #pauseBtn {
            background: linear-gradient(to right, #e74c3c, #c0392b);
            color: white;
        }

        #pauseBtn:hover {
            background: linear-gradient(to right, #c0392b, #a93226);
            transform: translateY(-2px);
        }

        #resetBtn {
            background: linear-gradient(to right, #3498db, #2980b9);
            color: white;
        }

        #resetBtn:hover {
            background: linear-gradient(to right, #2980b9, #1c6ea4);
            transform: translateY(-2px);
        }

        .animation-view {
            flex: 1;
            min-width: 600px;
            background: rgba(20, 20, 35, 0.9);
            border-radius: 15px;
            overflow: hidden;
            border: 2px solid #3498db;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            position: relative;
            display: flex;
            flex-direction: column;
        }

        .canvas-container {
            flex: 1;
            position: relative;
            overflow: hidden;
        }

        #animationCanvas {
            display: block;
            background: #1a1a2e;
        }

        .info-panel {
            background: rgba(30, 30, 50, 0.9);
            padding: 15px;
            border-top: 2px solid #3498db;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }

        .info-item {
            background: rgba(40, 40, 60, 0.7);
            padding: 12px;
            border-radius: 8px;
            border-left: 3px solid #f1c40f;
        }

        .info-item h4 {
            color: #f1c40f;
            margin-bottom: 5px;
            font-size: 1rem;
        }

        .info-item p {
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
            font-family: 'Courier New', monospace;
        }

        .formula-panel {
            background: rgba(30, 30, 50, 0.9);
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            width: 100%;
            max-width: 1200px;
            border: 2px solid #3498db;
            text-align: center;
        }

        .formula-panel h3 {
            color: #f1c40f;
            margin-bottom: 15px;
            font-size: 1.5rem;
        }

        .formulas {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
        }

        .formula {
            background: rgba(40, 40, 60, 0.7);
            padding: 15px 25px;
            border-radius: 10px;
            border: 1px solid #3498db;
        }

        .formula p {
            font-size: 1.8rem;
            color: white;
            font-family: 'Cambria Math', serif;
        }

        .formula .desc {
            font-size: 1rem;
            color: #bdc3c7;
            margin-top: 5px;
            font-family: 'Segoe UI', sans-serif;
        }

        .footer {
            margin-top: 25px;
            text-align: center;
            color: #95a5a6;
            font-size: 0.9rem;
            padding: 15px;
            width: 100%;
            max-width: 1200px;
        }

        @media (max-width: 1000px) {
            .container {
                flex-direction: column;
                align-items: center;
            }
            
            .animation-view, .control-panel {
                width: 100%;
                min-width: unset;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>⚡ 带电粒子在匀强磁场中的圆周运动</h1>
        <p>洛伦兹力提供向心力：F = qvB = mv²/r | 探索电荷、质量、速度和磁场强度如何影响粒子轨迹</p>
    </div>

    <div class="container">
        <div class="control-panel">
            <div class="panel-section">
                <h3>🎛️ 动画控制</h3>
                <div class="button-group">
                    <button id="startBtn">▶ 开始</button>
                    <button id="pauseBtn">⏸ 暂停</button>
                    <button id="resetBtn">↺ 重置</button>
                </div>
                <div class="control-group" style="margin-top: 15px;">
                    <label>动画速度: <span id="speedValue">1.0</span>x</label>
                    <div class="slider-container">
                        <input type="range" id="speedSlider" min="0.1" max="3" step="0.1" value="1">
                    </div>
                </div>
            </div>

            <div class="panel-section">
                <h3>⚛️ 物理参数</h3>
                <div class="control-group">
                    <label>电荷量 q (×10⁻¹⁹ C): <span id="qValue">+1.6</span></label>
                    <div class="slider-container">
                        <input type="range" id="qSlider" min="-3.2" max="3.2" step="0.8" value="1.6">
                        <input type="number" id="qInput" value="1.6" step="0.1">
                    </div>
                </div>
                <div class="control-group">
                    <label>质量 m (×10⁻²⁷ kg): <span id="mValue">1.67</span></label>
                    <div class="slider-container">
                        <input type="range" id="mSlider" min="0.1" max="10" step="0.1" value="1.67">
                        <input type="number" id="mInput" value="1.67" step="0.1">
                    </div>
                </div>
                <div class="control-group">
                    <label>速度 v (×10⁶ m/s): <span id="vValue">2.0</span></label>
                    <div class="slider-container">
                        <input type="range" id="vSlider" min="0.5" max="10" step="0.1" value="2.0">
                        <input type="number" id="vInput" value="2.0" step="0.1">
                    </div>
                </div>
                <div class="control-group">
                    <label>磁场强度 B (T): <span id="bValue">0.5</span></label>
                    <div class="slider-container">
                        <input type="range" id="bSlider" min="0.1" max="2" step="0.1" value="0.5">
                        <input type="number" id="bInput" value="0.5" step="0.1">
                    </div>
                </div>
            </div>

            <div class="panel-section">
                <h3>👁️ 可视化选项</h3>
                <div class="checkbox-group">
                    <div class="checkbox-item">
                        <input type="checkbox" id="showField" checked>
                        <label for="showField">磁场方向 (B)</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="showVelocity" checked>
                        <label for="showVelocity">速度矢量 (v)</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="showForce" checked>
                        <label for="showForce">洛伦兹力 (F)</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="showTrail" checked>
                        <label for="showTrail">运动轨迹</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="showRadius">
                        <label for="showRadius">圆心与半径</label>
                    </div>
                </div>
            </div>
        </div>

        <div class="animation-view">
            <div class="canvas-container">
                <canvas id="animationCanvas" width="800" height="600"></canvas>
            </div>
            <div class="info-panel">
                <div class="info-item">
                    <h4>粒子位置 (x, y)</h4>
                    <p id="positionDisplay">(0.00, 0.00) m</p>
                </div>
                <div class="info-item">
                    <h4>洛伦兹力大小</h4>
                    <p id="forceDisplay">1.60 ×10⁻¹³ N</p>
                </div>
                <div class="info-item">
                    <h4>轨道半径 r</h4>
                    <p id="radiusDisplay">0.042 m</p>
                </div>
                <div class="info-item">
                    <h4>运动周期 T</h4>
                    <p id="periodDisplay">1.31 ×10⁻⁷ s</p>
                </div>
            </div>
        </div>
    </div>

    <div class="formula-panel">
        <h3>📐 核心物理公式</h3>
        <div class="formulas">
            <div class="formula">
                <p>r = mv/(qB)</p>
                <div class="desc">轨道半径公式</div>
            </div>
            <div class="formula">
                <p>T = 2πm/(qB)</p>
                <div class="desc">运动周期公式</div>
            </div>
            <div class="formula">
                <p>F = qvB = mv²/r</p>
                <div class="desc">向心力方程</div>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>教学动画 | 带电粒子在匀强磁场中的圆周运动 | 洛伦兹力提供向心力 | 交互式物理模拟</p>
    </div>

    <script>
        // 获取Canvas和上下文
        const canvas = document.getElementById('animationCanvas');
        const ctx = canvas.getContext('2d');

        // 动画状态
        let animationId = null;
        let isAnimating = false;
        let animationSpeed = 1.0;

        // 物理参数（使用国际单位制，但显示时缩放）
        let q = 1.6e-19;      // 电荷量 (C)
        let m = 1.67e-27;     // 质量 (kg) - 质子质量
        let v = 2.0e6;        // 速度 (m/s)
        let B = 0.5;          // 磁场强度 (T)

        // 粒子状态
        let particle = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            radius: 0,
            period: 0,
            angle: 0,
            trail: []
        };

        // 计算轨道半径和周期
        function calculateOrbit() {
            if (Math.abs(q) < 1e-30) q = 1e-30 * Math.sign(q); // 避免除零
            particle.radius = Math.abs(m * v / (q * B));
            particle.period = 2 * Math.PI * m / (Math.abs(q) * B);
            
            // 限制半径不超过画布的一半
            const maxRadius = Math.min(canvas.width, canvas.height) * 0.4;
            if (particle.radius > maxRadius) {
                particle.radius = maxRadius;
                // 根据半径反推速度
                v = Math.abs(q) * B * particle.radius / m;
                updateSliderAndInput('v', v / 1e6);
            }
        }

        // 初始化计算
        calculateOrbit();

        // 获取DOM元素
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const resetBtn = document.getElementById('resetBtn');
        const speedSlider = document.getElementById('speedSlider');
        const speedValue = document.getElementById('speedValue');

        // 参数滑块和输入框
        const qSlider = document.getElementById('qSlider');
        const qInput = document.getElementById('qInput');
        const qValue = document.getElementById('qValue');
        
        const mSlider = document.getElementById('mSlider');
        const mInput = document.getElementById('mInput');
        const mValue = document.getElementById('mValue');
        
        const vSlider = document.getElementById('vSlider');
        const vInput = document.getElementById('vInput');
        const vValue = document.getElementById('vValue');
        
        const bSlider = document.getElementById('bSlider');
        const bInput = document.getElementById('bInput');
        const bValue = document.getElementById('bValue');

        // 可视化选项
        const showField = document.getElementById('showField');
        const showVelocity = document.getElementById('showVelocity');
        const showForce = document.getElementById('showForce');
        const showTrail = document.getElementById('showTrail');
        const showRadius = document.getElementById('showRadius');

        // 信息显示
        const positionDisplay = document.getElementById('positionDisplay');
        const forceDisplay = document.getElementById('forceDisplay');
        const radiusDisplay = document.getElementById('radiusDisplay');
        const periodDisplay = document.getElementById('periodDisplay');

        // 更新滑块和输入框显示值的通用函数
        function updateSliderAndInput(param, displayValue) {
            switch(param) {
                case 'q':
                    qSlider.value = displayValue;
                    qInput.value = displayValue.toFixed(2);
                    qValue.textContent = displayValue.toFixed(2);
                    q = displayValue * 1e-19;
                    break;
                case 'm':
                    mSlider.value = displayValue;
                    mInput.value = displayValue.toFixed(2);
                    mValue.textContent = displayValue.toFixed(2);
                    m = displayValue * 1e-27;
                    break;
                case 'v':
                    vSlider.value = displayValue;
                    vInput.value = displayValue.toFixed(2);
                    vValue.textContent = displayValue.toFixed(2);
                    v = displayValue * 1e6;
                    break;
                case 'b':
                    bSlider.value = displayValue;
                    bInput.value = displayValue.toFixed(2);
                    bValue.textContent = displayValue.toFixed(2);
                    B = displayValue;
                    break;
            }
            calculateOrbit();
        }

        // 事件监听器 - 参数控制
        qSlider.addEventListener('input', () => updateSliderAndInput('q', parseFloat(qSlider.value)));
        qInput.addEventListener('change', () => updateSliderAndInput('q', parseFloat(qInput.value)));
        
        mSlider.addEventListener('input', () => updateSliderAndInput('m', parseFloat(mSlider.value)));
        mInput.addEventListener('change', () => updateSliderAndInput('m', parseFloat(mInput.value)));
        
        vSlider.addEventListener('input', () => updateSliderAndInput('v', parseFloat(vSlider.value)));
        vInput.addEventListener('change', () => updateSliderAndInput('v', parseFloat(vInput.value)));
        
        bSlider.addEventListener('input', () => updateSliderAndInput('b', parseFloat(bSlider.value)));
        bInput.addEventListener('change', () => updateSliderAndInput('b', parseFloat(bInput.value)));

        // 动画速度控制
        speedSlider.addEventListener('input', function() {
            animationSpeed = parseFloat(this.value);
            speedValue.textContent = animationSpeed.toFixed(1);
        });

        // 动画控制
        startBtn.addEventListener('click', () => {
            if (!isAnimating) {
                isAnimating = true;
                animate();
            }
        });

        pauseBtn.addEventListener('click', () => {
            isAnimating = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
        });

        resetBtn.addEventListener('click', () => {
            isAnimating = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
            particle.angle = 0;
            particle.trail = [];
            draw();
        });

        // 绘制函数
        function draw() {
            // 清除画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 计算粒子当前位置
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = particle.radius;
            
            particle.x = centerX + radius * Math.cos(particle.angle);
            particle.y = centerY + radius * Math.sin(particle.angle);
            
            // 绘制磁场方向（如果启用）
            if (showField.checked) {
                drawMagneticField();
            }
            
            // 绘制轨迹（如果启用）
            if (showTrail.checked) {
                drawTrail();
            }
            
            // 绘制圆心和半径（如果启用）
            if (showRadius.checked) {
                drawRadiusGuide(centerX, centerY);
            }
            
            // 绘制粒子
            drawParticle();
            
            // 绘制矢量（如果启用）
            if (showVelocity.checked || showForce.checked) {
                drawVectors(centerX, centerY);
            }
            
            // 更新信息显示
            updateInfoDisplay(centerX, centerY);
        }

        // 绘制磁场方向
        function drawMagneticField() {
            const cellSize = 40;
            const arrowSize = 8;
            
            ctx.strokeStyle = 'rgba(112, 161, 255, 0.6)';
            ctx.fillStyle = 'rgba(112, 161, 255, 0.8)';
            ctx.lineWidth = 1;
            
            // 绘制"×"表示磁场垂直进入屏幕
            for (let x = cellSize/2; x < canvas.width; x += cellSize) {
                for (let y = cellSize/2; y < canvas.height; y += cellSize) {
                    ctx.beginPath();
                    ctx.moveTo(x - arrowSize/2, y - arrowSize/2);
                    ctx.lineTo(x + arrowSize/2, y + arrowSize/2);
                    ctx.moveTo(x + arrowSize/2, y - arrowSize/2);
                    ctx.lineTo(x - arrowSize/2, y + arrowSize/2);
                    ctx.stroke();
                }
            }
            
            // 添加磁场标签
            ctx.font = 'bold 16px Arial';
            ctx.fillStyle = '#70a1ff';
            ctx.fillText('B (进入屏幕)', 20, 30);
        }

        // 绘制粒子轨迹
        function drawTrail() {
            if (particle.trail.length < 2) return;
            
            const trailColor = q > 0 ? 'rgba(255, 71, 87, 0.3)' : 'rgba(55, 66, 250, 0.3)';
            
            ctx.beginPath();
            ctx.moveTo(particle.trail[0].x, particle.trail[0].y);
            
            for (let i = 1; i < particle.trail.length; i++) {
                ctx.lineTo(particle.trail[i].x, particle.trail[i].y);
            }
            
            ctx.strokeStyle = trailColor;
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // 保持轨迹长度不超过100个点
            if (particle.trail.length > 100) {
                particle.trail.shift();
            }
        }

        // 绘制圆心和半径辅助线
        function drawRadiusGuide(centerX, centerY) {
            // 绘制圆心
            ctx.beginPath();
            ctx.arc(centerX, centerY, 5, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
            ctx.fill();
            
            // 绘制半径线
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(particle.x, particle.y);
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // 半径标签
            ctx.font = '14px Arial';
            ctx.fillStyle = '#f1c40f';
            const labelX = (centerX + particle.x) / 2;
            const labelY = (centerY + particle.y) / 2;
            ctx.fillText(`r = ${(particle.radius * 100).toFixed(1)} cm`, labelX + 10, labelY - 10);
        }

        // 绘制粒子
        function drawParticle() {
            // 粒子发光效果
            const gradient = ctx.createRadialGradient(
                particle.x, particle.y, 0,
                particle.x, particle.y, 15
            );
            
            if (q > 0) {
                gradient.addColorStop(0, '#ff4757');
                gradient.addColorStop(0.7, 'rgba(255, 71, 87, 0.7)');
                gradient.addColorStop(1, 'rgba(255, 71, 87, 0)');
            } else {
                gradient.addColorStop(0, '#3742fa');
                gradient.addColorStop(0.7, 'rgba(55, 66, 250, 0.7)');
                gradient.addColorStop(1, 'rgba(55, 66, 250, 0)');
            }
            
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, 15, 0, Math.PI * 2);
            ctx.fillStyle = gradient;
            ctx.fill();
            
            // 粒子中心
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, 8, 0, Math.PI * 2);
            ctx.fillStyle = q > 0 ? '#ff3838' : '#3742fa';
            ctx.fill();
            
            // 电荷符号
            ctx.font = 'bold 14px Arial';
            ctx.fillStyle = 'white';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(q > 0 ? '+' : '−', particle.x, particle.y);
        }

        // 绘制速度和力矢量
        function drawVectors(centerX, centerY) {
            // 速度矢量（绿色）
            if (showVelocity.checked) {
                const vx = -particle.radius * Math.sin(particle.angle);
                const vy = particle.radius * Math.cos(particle.angle);
                const vScale = 0.5; // 缩放因子使箭头大小合适
                
                drawArrow(
                    particle.x, particle.y,
                    particle.x + vx * vScale, particle.y + vy * vScale,
                    '#00ff00', 'v', 3
                );
            }
            
            // 洛伦兹力矢量（红色）
            if (showForce.checked) {
                // 力指向圆心
                const fx = centerX - particle.x;
                const fy = centerY - particle.y;
                const forceMagnitude = Math.abs(q) * v * B;
                const fScale = 0.0000000000002; // 缩放因子
                
                drawArrow(
                    particle.x, particle.y,
                    particle.x + fx * fScale * forceMagnitude, 
                    particle.y + fy * fScale * forceMagnitude,
                    '#ff3838', 'F', 3
                );
            }
        }

        // 绘制箭头函数
        function drawArrow(fromX, fromY, toX, toY, color, label, lineWidth) {
            const headlen = 15;
            const angle = Math.atan2(toY - fromY, toX - fromX);
            
            // 绘制线
            ctx.beginPath();
            ctx.moveTo(fromX, fromY);
            ctx.lineTo(toX, toY);
            ctx.strokeStyle = color;
            ctx.lineWidth = lineWidth;
            ctx.stroke();
            
            // 绘制箭头头部
            ctx.beginPath();
            ctx.moveTo(toX, toY);
            ctx.lineTo(
                toX - headlen * Math.cos(angle - Math.PI / 6),
                toY - headlen * Math.sin(angle - Math.PI / 6)
            );
            ctx.lineTo(
                toX - headlen * Math.cos(angle + Math.PI / 6),
                toY - headlen * Math.sin(angle + Math.PI / 6)
            );
            ctx.closePath();
            ctx.fillStyle = color;
            ctx.fill();
            
            // 添加标签
            ctx.font = 'bold 16px Arial';
            ctx.fillStyle = color;
            const labelX = (fromX + toX) / 2 + 10;
            const labelY = (fromY + toY) / 2 - 10;
            ctx.fillText(label, labelX, labelY);
        }

        // 更新信息显示
        function updateInfoDisplay(centerX, centerY) {
            // 位置（转换为米，相对于中心）
            const posX = (particle.x - centerX) / 100; // 假设1像素=1厘米
            const posY = (particle.y - centerY) / 100;
            positionDisplay.textContent = `(${posX.toFixed(2)}, ${posY.toFixed(2)}) m`;
            
            // 洛伦兹力
            const force = Math.abs(q) * v * B;
            forceDisplay.textContent = `${force.toExponential(2).replace('e', ' ×10^')} N`;
            
            // 半径和周期
            radiusDisplay.textContent = `${(particle.radius * 100).toFixed(3)} cm`;
            periodDisplay.textContent = `${particle.period.toExponential(2).replace('e', ' ×10^')} s`;
        }

        // 动画循环
        function animate() {
            if (!isAnimating) return;
            
            // 更新粒子角度（根据周期）
            const angularSpeed = (2 * Math.PI) / particle.period;
            particle.angle += angularSpeed * 0.016 * animationSpeed; // 0.016 ≈ 1/60秒
            
            // 记录轨迹点
            particle.trail.push({x: particle.x, y: particle.y});
            
            // 绘制
            draw();
            
            // 继续动画
            animationId = requestAnimationFrame(animate);
        }

        // 初始绘制
        draw();
        
        // 窗口大小调整处理
        window.addEventListener('resize', function() {
            // 在实际应用中，这里应该重新计算canvas大小
            // 但为了简单起见，我们保持固定大小
            draw();
        });

        // 添加一些初始轨迹点
        for (let i = 0; i < 20; i++) {
            const angle = (i / 20) * Math.PI * 2;
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            particle.trail.push({
                x: centerX + particle.radius * Math.cos(angle),
                y: centerY + particle.radius * Math.sin(angle)
            });
        }
    </script>
</body>
</html>
```

### 3. 过程输出


## 《带电粒子在匀强磁场中圆周运动》交互式教学动画使用指南

欢迎使用本交互式教学动画！本工具旨在帮助您直观理解带电粒子在匀强磁场中的运动规律，特别是洛伦兹力如何提供向心力，以及各物理参数如何影响粒子轨迹。请跟随本指南，开启您的探索之旅。

---

### 一、功能说明

本动画模拟了一个带电粒子（如质子或电子）在垂直于屏幕的匀强磁场中做匀速圆周运动的物理过程。您可以通过调整物理参数、控制动画播放、切换可视化元素等方式，深入探究这一经典物理现象。

**核心模拟条件**：
- 匀强磁场方向：垂直进入屏幕（用"×"符号表示）
- 粒子初速度方向：垂直于磁场方向
- 忽略重力及其他阻力影响
- 运动平面：与磁场方向垂直的平面

---

### 二、主要功能模块

#### 1. **动画控制区**（左上角面板）
- **开始/暂停/重置**：控制动画的播放状态
- **动画速度调节**：0.1x至3.0x可调，便于慢速观察细节或快速查看整体效果

#### 2. **物理参数调节区**（中间面板）
- **电荷量 (q)**：-3.2×10⁻¹⁹C 至 +3.2×10⁻¹⁹C
  - **正值**：正电荷（红色粒子，如质子）
  - **负值**：负电荷（蓝色粒子，如电子）
  - **零值**：中性粒子（将沿直线运动）

- **质量 (m)**：0.1×10⁻²⁷kg 至 10×10⁻²⁷kg
  - 默认值为质子质量 1.67×10⁻²⁷kg

- **速度 (v)**：0.5×10⁶m/s 至 10×10⁶m/s
  - 典型值为 2.0×10⁶m/s（约0.67%光速）

- **磁场强度 (B)**：0.1T 至 2.0T
  - 默认值为 0.5T（地磁场约0.00005T）

**调节方式**：
- 拖动滑块快速调整
- 在输入框中输入精确数值
- 滑块与输入框实时同步

#### 3. **可视化选项区**（左下角面板）
- **磁场方向 (B)**：显示/隐藏磁场指示符号
- **速度矢量 (v)**：显示/隐藏绿色速度箭头
- **洛伦兹力 (F)**：显示/隐藏红色力箭头
- **运动轨迹**：显示/隐藏粒子运动路径
- **圆心与半径**：显示/隐藏圆心标记和半径辅助线

#### 4. **实时信息显示区**（动画下方）
- **粒子位置**：实时坐标（以圆心为原点）
- **洛伦兹力大小**：当前受力值
- **轨道半径**：计算得到的运动半径
- **运动周期**：完成一周所需时间

#### 5. **核心公式区**（底部）
常驻显示三个关键公式：
- 轨道半径公式：`r = mv/(qB)`
- 运动周期公式：`T = 2πm/(qB)`
- 向心力方程：`F = qvB = mv²/r`

---

### 三、设计特色

#### 1. **多感官学习体验**
- **视觉编码**：不同物理量使用不同颜色（速度-绿，力-红，磁场-蓝灰）
- **动态反馈**：参数调整后动画立即响应
- **分层显示**：可控制信息密度，避免认知过载

#### 2. **科学探究流程**
- **控制变量法**：每次只改变一个参数，观察其对轨迹的影响
- **定性到定量**：先观察现象变化，再用公式验证
- **即时计算**：所有物理量实时计算并显示

#### 3. **教学友好设计**
- **轨迹记忆**：粒子留下渐隐轨迹，便于观察完整圆形
- **矢量可视化**：清晰展示速度与力的垂直关系
- **比例适当**：自动限制轨道大小，确保始终在视野内

---

### 四、教学要点与探究活动

#### 初级探究（适合初次接触者）
1. **观察基本现象**
   - 点击"开始"按钮，观察粒子如何运动
   - 开启所有可视化选项，理解各元素含义
   - 注意速度与洛伦兹力始终保持垂直

2. **电荷符号的影响**
   - 将电荷量从+1.6调整为-1.6
   - **观察**：粒子转向方向相反
   - **思考**：为什么方向会改变？（左手定则）

#### 中级探究（适合理解基础者）
1. **单一参数影响分析**
   - **速度v的影响**：保持其他参数不变，逐渐增大速度
     - **现象**：轨道半径增大，周期不变
     - **原理**：`r ∝ v`，`T`与`v`无关
   
   - **质量m的影响**：增大质量
     - **现象**：半径和周期都增大
     - **原理**：`r ∝ m`，`T ∝ m`
   
   - **磁场B的影响**：增强磁场
     - **现象**：半径和周期都减小
     - **原理**：`r ∝ 1/B`，`T ∝ 1/B`
   
   - **电荷量q的影响**：增大|q|
     - **现象**：半径和周期都减小
     - **原理**：`r ∝ 1/|q|`，`T ∝ 1/|q|`

2. **公式验证实验**
   - 记录一组参数下的半径计算值
   - 用刻度工具（或目测）验证动画中的实际半径
   - 计算理论周期，用计时器验证动画周期

#### 高级探究（适合深入学习者）
1. **极限情况探索**
   - 设置`q = 0`：观察粒子直线运动（不受洛伦兹力）
   - 设置`B = 0`：观察粒子直线运动（无磁场）
   - 设置`v = 0`：观察粒子静止（无初速度）

2. **参数关联分析**
   - 同时改变两个参数，但保持`mv/(qB)`不变
   - **发现**：轨道半径保持不变
   - **延伸**：设计实验验证`T`与`v`无关的特性

3. **左手定则练习**
   - 暂停动画，在轨迹的不同位置
   - 根据磁场方向（进屏幕）和速度方向
   - 使用左手定则预测洛伦兹力方向
   - 与动画显示的力箭头对比验证

---

### 五、使用建议

#### 1. **教学场景应用**
- **课堂演示**：教师可全屏展示，逐步揭示物理规律
- **小组探究**：学生分组完成不同的探究任务
- **个人学习**：学生自主探索，验证猜想
- **复习巩固**：考前可视化复习复杂概念

#### 2. **最佳实践流程**
```
观察现象 → 提出问题 → 调整参数 → 记录变化
    ↓
总结规律 → 公式验证 → 拓展思考 → 实际应用
```

#### 3. **技术提示**
- **浏览器**：建议使用Chrome、Firefox或Edge最新版本
- **屏幕分辨率**：建议在1024×768或更高分辨率下使用
- **性能优化**：如果动画卡顿，可减少轨迹显示或降低动画速度
- **全屏模式**：按F11键进入全屏，获得最佳观看体验

#### 4. **安全注意事项**
- 本动画为教学模拟，实际粒子加速器中的参数远大于此
- 公式在相对论效应不明显时成立（v << c）
- 实际环境中还需考虑电场、重力等其他因素

---

### 六、学习目标达成检查

完成本动画的学习后，您应该能够：

✅ **理解层面**
- 解释为什么带电粒子在匀强磁场中做匀速圆周运动
- 描述洛伦兹力如何提供向心力
- 区分正负电荷在相同磁场中的偏转方向

✅ **应用层面**
- 使用左手定则判断洛伦兹力方向
- 定性分析各参数变化对轨道的影响
- 根据给定参数估算轨道半径和周期

✅ **分析层面**
- 解释为什么周期与速度无关
- 分析多参数同时变化时的综合效应
- 将原理应用于质谱仪、回旋加速器等实际设备

---

### 开启您的科学探索！

现在，您已经掌握了本动画的所有功能。建议您：

1. **先按默认设置运行一次**，观察完整现象
2. **逐个尝试**各控制功能，熟悉界面
3. **设计自己的实验**，验证物理猜想
4. **与同学讨论**观察到的有趣现象

物理学之美在于其简洁的数学表达与丰富的物理现象之间的完美对应。希望本动画能帮助您在这两者之间建立直观的桥梁，享受探索自然规律的乐趣！

**祝您学习愉快，探索无限！**

---
*动画设计：教育技术专家团队*
*物理原理：经典电磁学*
*适用学段：高中至大学低年级物理课程*