# 需求：动量守恒（完全弹性/非弹性碰撞，显示矢量变化）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：高中物理或大学基础物理的学生。他们已具备基本的力学知识（如质量、速度、动量、动能），但对碰撞过程中的动量与能量变化，特别是矢量性，理解不深。
2.  **核心痛点**：
    *   难以直观理解“动量是矢量”在碰撞中的核心作用（方向性）。
    *   难以区分“完全弹性碰撞”与“完全非弹性碰撞”在能量和速度变化上的根本差异。
    *   对碰撞前后速度、动量矢量的动态变化过程缺乏可视化认知。
3.  **学习目标**：
    *   **知识层面**：掌握动量守恒定律及其矢量性；理解完全弹性碰撞与完全非弹性碰撞的定义与核心区别（动能是否守恒）。
    *   **技能层面**：能够通过观察矢量箭头的变化，定性分析碰撞过程；能够根据给定的碰撞类型和质量，预测碰撞后的大致运动状态。
    *   **情感/认知层面**：建立对物理过程动态、直观的“感觉”，降低对抽象公式的畏惧感。

#### 教学设计思路
1.  **核心概念聚焦**：
    *   **动量守恒定律**：系统不受外力或合外力为零时，总动量保持不变。**重点突出其矢量性**。
    *   **碰撞类型**：
        *   **完全弹性碰撞**：动量守恒 + 动能守恒。碰撞后物体分开。
        *   **完全非弹性碰撞**：动量守恒 + 动能不守恒（损失最大）。碰撞后物体粘合，以共同速度运动。
    *   **矢量表示**：用带箭头的线段（矢量箭头）直观表示速度 `v` 和动量 `p = mv`。箭头方向代表方向，长度代表大小。

2.  **认知规律遵循**：
    *   **从具体到抽象**：先展示两个小球碰撞的生动动画，再同步显示其矢量变化和数值计算。
    *   **对比学习**：将两种碰撞类型并置（或通过切换），让学生直观对比碰撞结果和能量条的变化。
    *   **多通道编码**：视觉（动画、颜色、箭头）、数字（实时数据）、交互（拖拽、选择）相结合，强化记忆。
    *   **即时反馈**：用户调整参数后，动画和计算结果立即更新，形成探索-观察-理解的闭环。

3.  **交互设计**：
    *   **探索式学习环境**：用户不是被动观看，而是可以主动改变变量（质量、初速度、碰撞类型），观察系统如何响应。
    *   **分层信息呈现**：
        *   **主舞台**：核心动画，清晰展示小球运动与碰撞。
        *   **控制面板**：提供参数调节和模式选择。
        *   **数据面板**：实时显示关键物理量（速度、动量、动能）的数值和矢量图。
    *   **引导与聚焦**：通过高亮、闪烁或平滑的箭头变形动画，引导用户关注关键变化时刻（碰撞瞬间）和关键物理量（总动量矢量）。

4.  **视觉呈现**：
    *   **主体**：两个颜色对比鲜明的小球在水平轨道上运动，模拟一维碰撞场景，简化问题以突出核心。
    *   **矢量可视化**：
        *   每个小球上方或下方跟随一个**速度矢量箭头**（例如，用 `v1`， `v2` 标签，颜色与小球匹配）。
        *   在舞台中央或侧边，绘制一个**动量矢量合成图**，动态展示两个小球动量矢量 (`p1=m1*v1`， `p2=m2*v2`) 的合成与守恒。碰撞前后，两个分矢量的和（总矢量）应保持不变（长度和方向）。
    *   **能量可视化**：用横向进度条表示每个小球的动能以及系统总动能，用不同颜色区分。在完全非弹性碰撞中，总动能条会明显“缩短”。
    *   **时间控制**：提供播放/暂停/重置按钮，允许用户仔细端详碰撞瞬间。

#### 配色方案选择
*   **主色调**：深蓝或深灰色背景，模拟科学演示的严肃感和深邃感，能有效突出前景元素。
*   **小球与矢量**：
    *   小球1：`#FF6B6B`（珊瑚红），其速度/动量矢量也用同色系（如 `#FF8E8E`）。
    *   小球2：`#4ECDC4`（青绿色），其速度/动量矢量也用同色系（如 `#6EDBD3`）。
    *   鲜明的冷暖对比，易于区分和追踪。
*   **总动量矢量**：`#FFD166`（亮黄色）或白色，作为合成量，颜色应中立且醒目。
*   **能量条**：
    *   小球动能条：使用对应小球的颜色（半透明）。
    *   总动能条：`#9B5DE5`（紫色），代表系统整体属性。
    *   动能损失部分：可以用灰色或暗红色表示，在非弹性碰撞中显示。
*   **UI控件**：浅灰色 (`#E0E0E0`) 背景，深灰色 (`#333`) 文字和边框，保持清晰和中性。

#### 交互功能列表
1.  **场景控制**：
    *   播放 / 暂停 / 重置 按钮。
    *   单步前进/后退按钮（用于精细观察碰撞帧）。
2.  **参数调节面板**：
    *   **滑块**：调节小球1和小球2的质量 (`m1`， `m2`)。
    *   **滑块**：调节小球1和小球2的初始速度 (`v1`， `v2`)，可正可负（代表方向）。
    *   **选择器**：选择碰撞类型（“完全弹性碰撞” / “完全非弹性碰撞”）。
3.  **可视化显示面板**：
    *   **实时数值显示**：显示两球碰撞前后的速度、动量、动能数值。
    *   **矢量图**：
        *   动态显示每个球的速度矢量箭头（随球移动）。
        *   独立的“动量矢量合成图”，动态展示 `p1` 和 `p2` 的矢量加法，并高亮显示守恒的总动量矢量。
    *   **能量条**：实时显示并对比碰撞前后系统总动能及每个球动能的变化。
4.  **教学提示**：
    *   可选的文字说明框，在关键步骤（如碰撞瞬间）自动弹出简要提示。
    *   一个“显示/隐藏公式”的开关，供学有余力的学生查看动量守恒和动能守恒的公式。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>动量守恒定律：碰撞可视化教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .container {
            max-width: 1200px;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        header {
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        h1 {
            color: #ffd166;
            margin-bottom: 10px;
            font-size: 2.2rem;
        }
        
        .subtitle {
            color: #9b5de5;
            font-size: 1.1rem;
        }
        
        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        
        .simulation-area {
            flex: 1;
            min-width: 600px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .control-panel {
            flex: 0 0 350px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .canvas-container {
            position: relative;
            width: 100%;
            height: 400px;
            background: rgba(10, 15, 30, 0.7);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        #simulationCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }
        
        .vector-display {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .vector-title {
            color: #ffd166;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        
        .vector-canvas-container {
            width: 100%;
            height: 150px;
            background: rgba(10, 15, 30, 0.7);
            border-radius: 5px;
            overflow: hidden;
        }
        
        #vectorCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }
        
        .panel-section {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .section-title {
            color: #4ecdc4;
            margin-bottom: 15px;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .section-title i {
            font-size: 1.1rem;
        }
        
        .control-group {
            margin-bottom: 15px;
        }
        
        .control-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            font-size: 0.95rem;
        }
        
        .value-display {
            color: #ffd166;
            font-weight: bold;
        }
        
        input[type="range"] {
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.1);
            outline: none;
            -webkit-appearance: none;
        }
        
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #ff6b6b;
            cursor: pointer;
            border: 2px solid rgba(255, 255, 255, 0.8);
        }
        
        input[type="range"]#mass2Slider::-webkit-slider-thumb {
            background: #4ecdc4;
        }
        
        input[type="range"]#velocity1Slider::-webkit-slider-thumb {
            background: #ff6b6b;
        }
        
        input[type="range"]#velocity2Slider::-webkit-slider-thumb {
            background: #4ecdc4;
        }
        
        .collision-type-selector {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        
        .collision-btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: #e0e0e0;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .collision-btn:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        
        .collision-btn.active {
            background: #9b5de5;
            color: white;
            box-shadow: 0 0 10px rgba(155, 93, 229, 0.5);
        }
        
        .control-buttons {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }
        
        .control-btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: #e0e0e0;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .control-btn:hover {
            background: rgba(255, 255, 255, 0.2);
        }
        
        .control-btn#playBtn {
            background: rgba(78, 205, 196, 0.2);
        }
        
        .control-btn#playBtn:hover {
            background: rgba(78, 205, 196, 0.4);
        }
        
        .control-btn#resetBtn {
            background: rgba(255, 107, 107, 0.2);
        }
        
        .control-btn#resetBtn:hover {
            background: rgba(255, 107, 107, 0.4);
        }
        
        .data-panel {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 10px;
        }
        
        .data-box {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 12px;
            border-left: 4px solid;
        }
        
        .data-box.ball1 {
            border-left-color: #ff6b6b;
        }
        
        .data-box.ball2 {
            border-left-color: #4ecdc4;
        }
        
        .data-box.system {
            border-left-color: #9b5de5;
            grid-column: span 2;
        }
        
        .data-title {
            font-size: 0.9rem;
            color: #aaa;
            margin-bottom: 5px;
        }
        
        .data-value {
            font-size: 1.2rem;
            font-weight: bold;
            color: #ffd166;
        }
        
        .energy-bars {
            margin-top: 15px;
        }
        
        .energy-bar-container {
            margin-bottom: 10px;
        }
        
        .energy-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            font-size: 0.9rem;
        }
        
        .energy-bar {
            height: 20px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            overflow: hidden;
            position: relative;
        }
        
        .energy-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
        }
        
        .energy-fill.ball1 {
            background: linear-gradient(90deg, rgba(255, 107, 107, 0.7), rgba(255, 107, 107, 1));
        }
        
        .energy-fill.ball2 {
            background: linear-gradient(90deg, rgba(78, 205, 196, 0.7), rgba(78, 205, 196, 1));
        }
        
        .energy-fill.system {
            background: linear-gradient(90deg, rgba(155, 93, 229, 0.7), rgba(155, 93, 229, 1));
        }
        
        .energy-fill.lost {
            background: linear-gradient(90deg, rgba(128, 128, 128, 0.7), rgba(128, 128, 128, 1));
        }
        
        .formula-box {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 15px;
            margin-top: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.9rem;
            line-height: 1.5;
        }
        
        .formula {
            color: #ffd166;
            font-family: 'Cambria Math', serif;
            margin: 5px 0;
        }
        
        .hint {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 0.9rem;
            color: #ffd166;
            border-left: 4px solid #ffd166;
            display: none;
        }
        
        footer {
            text-align: center;
            margin-top: 20px;
            padding: 15px;
            color: #888;
            font-size: 0.9rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            width: 100%;
        }
        
        @media (max-width: 1000px) {
            .main-content {
                flex-direction: column;
            }
            
            .simulation-area, .control-panel {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>动量守恒定律：碰撞可视化教学动画</h1>
            <p class="subtitle">探索完全弹性碰撞与完全非弹性碰撞中的动量与能量变化</p>
        </header>
        
        <div class="main-content">
            <div class="simulation-area">
                <div class="canvas-container">
                    <canvas id="simulationCanvas"></canvas>
                    <div class="hint" id="collisionHint">碰撞发生！观察速度矢量和动量的变化。</div>
                </div>
                
                <div class="vector-display">
                    <div class="vector-title">动量矢量合成图 (总动量守恒)</div>
                    <div class="vector-canvas-container">
                        <canvas id="vectorCanvas"></canvas>
                    </div>
                </div>
            </div>
            
            <div class="control-panel">
                <div class="panel-section">
                    <div class="section-title">🎮 场景控制</div>
                    <div class="control-buttons">
                        <button class="control-btn" id="playBtn">
                            <span id="playIcon">▶</span> <span id="playText">播放</span>
                        </button>
                        <button class="control-btn" id="resetBtn">↺ 重置</button>
                    </div>
                </div>
                
                <div class="panel-section">
                    <div class="section-title">⚙️ 参数调节</div>
                    
                    <div class="control-group">
                        <div class="control-label">
                            <span>小球1质量 (m₁): <span class="value-display" id="mass1Value">2.0 kg</span></span>
                        </div>
                        <input type="range" id="mass1Slider" min="0.5" max="5" step="0.1" value="2">
                    </div>
                    
                    <div class="control-group">
                        <div class="control-label">
                            <span>小球2质量 (m₂): <span class="value-display" id="mass2Value">1.0 kg</span></span>
                        </div>
                        <input type="range" id="mass2Slider" min="0.5" max="5" step="0.1" value="1">
                    </div>
                    
                    <div class="control-group">
                        <div class="control-label">
                            <span>小球1初速度 (v₁): <span class="value-display" id="velocity1Value">2.0 m/s</span></span>
                        </div>
                        <input type="range" id="velocity1Slider" min="-5" max="5" step="0.1" value="2">
                    </div>
                    
                    <div class="control-group">
                        <div class="control-label">
                            <span>小球2初速度 (v₂): <span class="value-display" id="velocity2Value">-1.0 m/s</span></span>
                        </div>
                        <input type="range" id="velocity2Slider" min="-5" max="5" step="0.1" value="-1">
                    </div>
                    
                    <div class="collision-type-selector">
                        <button class="collision-btn active" id="elasticBtn">完全弹性碰撞</button>
                        <button class="collision-btn" id="inelasticBtn">完全非弹性碰撞</button>
                    </div>
                </div>
                
                <div class="panel-section">
                    <div class="section-title">📊 实时数据</div>
                    <div class="data-panel">
                        <div class="data-box ball1">
                            <div class="data-title">小球1 (红色)</div>
                            <div class="data-value" id="ball1Speed">v₁ = 2.00 m/s</div>
                            <div class="data-value" id="ball1Momentum">p₁ = 4.00 kg·m/s</div>
                            <div class="data-value" id="ball1Energy">Eₖ₁ = 4.00 J</div>
                        </div>
                        
                        <div class="data-box ball2">
                            <div class="data-title">小球2 (青色)</div>
                            <div class="data-value" id="ball2Speed">v₂ = -1.00 m/s</div>
                            <div class="data-value" id="ball2Momentum">p₂ = -1.00 kg·m/s</div>
                            <div class="data-value" id="ball2Energy">Eₖ₂ = 0.50 J</div>
                        </div>
                        
                        <div class="data-box system">
                            <div class="data-title">系统总量</div>
                            <div class="data-value" id="totalMomentum">P = 3.00 kg·m/s</div>
                            <div class="data-value" id="totalEnergy">Eₖ = 4.50 J</div>
                            <div class="data-value" id="energyLost">动能损失: 0.00 J</div>
                        </div>
                    </div>
                    
                    <div class="energy-bars">
                        <div class="energy-bar-container">
                            <div class="energy-label">
                                <span>系统总动能</span>
                                <span id="totalEnergyValue">4.50 J</span>
                            </div>
                            <div class="energy-bar">
                                <div class="energy-fill system" id="totalEnergyBar" style="width: 100%"></div>
                                <div class="energy-fill lost" id="lostEnergyBar" style="width: 0%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="formula-box">
                    <div><strong>核心公式:</strong></div>
                    <div class="formula">动量守恒: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'</div>
                    <div class="formula">完全弹性碰撞动能守恒: (1/2)m₁v₁² + (1/2)m₂v₂² = (1/2)m₁v₁'² + (1/2)m₂v₂'²</div>
                    <div class="formula">完全非弹性碰撞后共同速度: v' = (m₁v₁ + m₂v₂) / (m₁ + m₂)</div>
                </div>
            </div>
        </div>
        
        <footer>
            动量守恒定律教学动画 | 设计原理：系统不受外力时，总动量保持不变 | 注意观察碰撞前后动量矢量的合成关系
        </footer>
    </div>

    <script>
        // 获取Canvas元素和上下文
        const simCanvas = document.getElementById('simulationCanvas');
        const vecCanvas = document.getElementById('vectorCanvas');
        const simCtx = simCanvas.getContext('2d');
        const vecCtx = vecCanvas.getContext('2d');
        
        // 设置Canvas尺寸
        function resizeCanvases() {
            const simContainer = document.querySelector('.canvas-container');
            const vecContainer = document.querySelector('.vector-canvas-container');
            
            simCanvas.width = simContainer.clientWidth;
            simCanvas.height = simContainer.clientHeight;
            
            vecCanvas.width = vecContainer.clientWidth;
            vecCanvas.height = vecContainer.clientHeight;
        }
        
        window.addEventListener('resize', resizeCanvases);
        resizeCanvases();
        
        // 物理参数
        let m1 = 2.0; // 小球1质量 (kg)
        let m2 = 1.0; // 小球2质量 (kg)
        let v1 = 2.0; // 小球1初速度 (m/s)
        let v2 = -1.0; // 小球2初速度 (m/s)
        
        let v1_final = v1; // 小球1最终速度
        let v2_final = v2; // 小球2最终速度
        
        let isElastic = true; // 碰撞类型：true=完全弹性，false=完全非弹性
        let isPlaying = false; // 动画是否播放中
        let animationId = null; // 动画ID
        
        // 小球对象
        const ball1 = {
            x: 150,
            y: simCanvas.height / 2,
            radius: 30,
            color: '#FF6B6B',
            vx: v1,
            vy: 0,
            mass: m1
        };
        
        const ball2 = {
            x: simCanvas.width - 150,
            y: simCanvas.height / 2,
            radius: 30,
            color: '#4ECDC4',
            vx: v2,
            vy: 0,
            mass: m2
        };
        
        // 轨道参数
        const trackY = simCanvas.height / 2;
        const trackHeight = 10;
        
        // 初始化小球位置
        function resetBallPositions() {
            ball1.x = 150;
            ball2.x = simCanvas.width - 150;
            ball1.vx = v1;
            ball2.vx = v2;
            
            // 计算碰撞后的最终速度
            calculateFinalVelocities();
        }
        
        // 计算碰撞后的最终速度
        function calculateFinalVelocities() {
            if (isElastic) {
                // 完全弹性碰撞公式
                v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2);
                v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2);
            } else {
                // 完全非弹性碰撞公式
                const commonVelocity = (m1 * v1 + m2 * v2) / (m1 + m2);
                v1_final = commonVelocity;
                v2_final = commonVelocity;
            }
        }
        
        // 绘制主模拟场景
        function drawSimulation() {
            // 清除画布
            simCtx.clearRect(0, 0, simCanvas.width, simCanvas.height);
            
            // 绘制轨道
            simCtx.fillStyle = 'rgba(255, 255, 255, 0.1)';
            simCtx.fillRect(0, trackY - trackHeight/2, simCanvas.width, trackHeight);
            
            // 绘制轨道边缘
            simCtx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            simCtx.lineWidth = 2;
            simCtx.beginPath();
            simCtx.moveTo(0, trackY - trackHeight/2);
            simCtx.lineTo(simCanvas.width, trackY - trackHeight/2);
            simCtx.moveTo(0, trackY + trackHeight/2);
            simCtx.lineTo(simCanvas.width, trackY + trackHeight/2);
            simCtx.stroke();
            
            // 绘制小球
            drawBall(ball1);
            drawBall(ball2);
            
            // 绘制速度矢量
            drawVelocityVectors();
            
            // 绘制碰撞检测区域
            const collisionDistance = ball1.radius + ball2.radius;
            const actualDistance = Math.abs(ball2.x - ball1.x);
            
            // 如果小球即将碰撞，绘制提示
            if (actualDistance < collisionDistance + 50 && actualDistance > collisionDistance) {
                simCtx.fillStyle = 'rgba(255, 215, 102, 0.2)';
                simCtx.fillRect(
                    Math.min(ball1.x, ball2.x) - 10,
                    trackY - 60,
                    actualDistance + 20,
                    40
                );
                
                simCtx.fillStyle = '#FFD166';
                simCtx.font = '14px Arial';
                simCtx.textAlign = 'center';
                simCtx.fillText('即将碰撞', (ball1.x + ball2.x) / 2, trackY - 40);
            }
            
            // 如果小球正在碰撞（重叠）
            if (actualDistance < collisionDistance) {
                // 显示碰撞提示
                document.getElementById('collisionHint').style.display = 'block';
                
                // 绘制碰撞效果
                simCtx.fillStyle = 'rgba(255, 215, 102, 0.3)';
                simCtx.beginPath();
                simCtx.arc(
                    (ball1.x + ball2.x) / 2,
                    trackY,
                    collisionDistance * 1.2,
                    0,
                    Math.PI * 2
                );
                simCtx.fill();
                
                // 绘制"碰撞!"文字
                simCtx.fillStyle = '#FFD166';
                simCtx.font = 'bold 18px Arial';
                simCtx.textAlign = 'center';
                simCtx.fillText('碰撞!', (ball1.x + ball2.x) / 2, trackY - collisionDistance * 1.5);
            } else {
                document.getElementById('collisionHint').style.display = 'none';
            }
        }
        
        // 绘制单个小球
        function drawBall(ball) {
            // 小球阴影
            simCtx.beginPath();
            simCtx.arc(ball.x, ball.y + 5, ball.radius, 0, Math.PI * 2);
            simCtx.fillStyle = 'rgba(0, 0, 0, 0.3)';
            simCtx.fill();
            
            // 小球主体
            simCtx.beginPath();
            simCtx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
            simCtx.fillStyle = ball.color;
            simCtx.fill();
            
            // 小球边框
            simCtx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
            simCtx.lineWidth = 2;
            simCtx.stroke();
            
            // 小球标签
            simCtx.fillStyle = 'white';
            simCtx.font = 'bold 16px Arial';
            simCtx.textAlign = 'center';
            simCtx.textBaseline = 'middle';
            simCtx.fillText(ball === ball1 ? 'm₁' : 'm₂', ball.x, ball.y);
            
            // 小球质量显示
            simCtx.font = '14px Arial';
            simCtx.fillText(`${ball.mass.toFixed(1)} kg`, ball.x, ball.y + ball.radius + 20);
        }
        
        // 绘制速度矢量
        function drawVelocityVectors() {
            // 小球1速度矢量
            drawVector(
                ball1.x, 
                ball1.y - ball1.radius - 30, 
                ball1.vx * 20, 
                0, 
                '#FF8E8E', 
                `v₁ = ${ball1.vx.toFixed(2)} m/s`
            );
            
            // 小球2速度矢量
            drawVector(
                ball2.x, 
                ball2.y - ball2.radius - 30, 
                ball2.vx * 20, 
                0, 
                '#6EDBD3', 
                `v₂ = ${ball2.vx.toFixed(2)} m/s`
            );
            
            // 绘制最终速度预测（虚线）
            if (isPlaying) {
                // 小球1最终速度预测
                if (Math.abs(v1_final) > 0.01) {
                    drawVector(
                        ball1.x, 
                        ball1.y + ball1.radius + 30, 
                        v1_final * 20, 
                        0, 
                        '#FF8E8E', 
                        `v₁' = ${v1_final.toFixed(2)} m/s`,
                        true
                    );
                }
                
                // 小球2最终速度预测
                if (Math.abs(v2_final) > 0.01) {
                    drawVector(
                        ball2.x, 
                        ball2.y + ball2.radius + 30, 
                        v2_final * 20, 
                        0, 
                        '#6EDBD3', 
                        `v₂' = ${v2_final.toFixed(2)} m/s`,
                        true
                    );
                }
            }
        }
        
        // 绘制矢量箭头
        function drawVector(x, y, dx, dy, color, label, isDashed = false) {
            const magnitude = Math.sqrt(dx * dx + dy * dy);
            if (magnitude < 0.5) return; // 忽略太小的矢量
            
            simCtx.save();
            
            // 设置线条样式
            if (isDashed) {
                simCtx.setLineDash([5, 5]);
                simCtx.strokeStyle = color + 'AA';
                simCtx.fillStyle = color + 'AA';
            } else {
                simCtx.setLineDash([]);
                simCtx.strokeStyle = color;
                simCtx.fillStyle = color;
            }
            
            simCtx.lineWidth = 3;
            
            // 绘制矢量线
            simCtx.beginPath();
            simCtx.moveTo(x, y);
            simCtx.lineTo(x + dx, y + dy);
            simCtx.stroke();
            
            // 绘制箭头头部
            const angle = Math.atan2(dy, dx);
            const arrowSize = 10;
            
            simCtx.beginPath();
            simCtx.moveTo(x + dx, y + dy);
            simCtx.lineTo(
                x + dx - arrowSize * Math.cos(angle - Math.PI / 6),
                y + dy - arrowSize * Math.sin(angle - Math.PI / 6)
            );
            simCtx.lineTo(
                x + dx - arrowSize * Math.cos(angle + Math.PI / 6),
                y + dy - arrowSize * Math.sin(angle + Math.PI / 6)
            );
            simCtx.closePath();
            simCtx.fill();
            
            // 绘制标签
            simCtx.fillStyle = isDashed ? color + 'AA' : color;
            simCtx.font = '12px Arial';
            simCtx.textAlign = dx >= 0 ? 'left' : 'right';
            simCtx.fillText(
                label, 
                x + dx + (dx >= 0 ? 5 : -5), 
                y + dy - 10
            );
            
            simCtx.restore();
        }
        
        // 绘制动量矢量合成图
        function drawVectorDiagram() {
            // 清除画布
            vecCtx.clearRect(0, 0, vecCanvas.width, vecCanvas.height);
            
            // 计算动量
            const p1 = ball1.mass * ball1.vx; // 小球1动量
            const p2 = ball2.mass * ball2.vx; // 小球2动量
            const totalP = p1 + p2; // 总动量
            
            // 计算预测的最终动量
            const p1_final = ball1.mass * v1_final;
            const p2_final = ball2.mass * v2_final;
            const totalP_final = p1_final + p2_final;
            
            // 矢量图中心点
            const centerX = vecCanvas.width / 2;
            const centerY = vecCanvas.height / 2;
            
            // 缩放因子（使矢量适应画布）
            const scale = 15;
            
            // 绘制坐标轴
            vecCtx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            vecCtx.lineWidth = 1;
            
            // X轴
            vecCtx.beginPath();
            vecCtx.moveTo(50, centerY);
            vecCtx.lineTo(vecCanvas.width - 50, centerY);
            vecCtx.stroke();
            
            // Y轴
            vecCtx.beginPath();
            vecCtx.moveTo(centerX, 20);
            vecCtx.lineTo(centerX, vecCanvas.height - 20);
            vecCtx.stroke();
            
            // 绘制当前动量矢量
            drawMomentumVector(centerX, centerY, p1, 0, '#FF8E8E', 'p₁', scale);
            drawMomentumVector(centerX + p1 * scale, centerY, p2, 0, '#6EDBD3', 'p₂', scale);
            
            // 绘制总动量矢量（从起点到p1+p2的终点）
            drawMomentumVector(centerX, centerY, totalP, 0, '#FFD166', 'P = p₁ + p₂', scale, 4);
            
            // 绘制最终动量预测（虚线）
            if (isPlaying) {
                vecCtx.setLineDash([5, 5]);
                
                // 最终动量矢量p1'
                if (Math.abs(p1_final) > 0.1) {
                    drawMomentumVector(centerX, centerY, p1_final, 0, '#FF8E8E', `p₁'`, scale, 2, true);
                }
                
                // 最终动量矢量p2'
                if (Math.abs(p2_final) > 0.1) {
                    drawMomentumVector(centerX + p1_final * scale, centerY, p2_final, 0, '#6EDBD3', `p₂'`, scale, 2, true);
                }
                
                // 最终总动量矢量（应该与初始总动量相同）
                drawMomentumVector(centerX, centerY, totalP_final, 0, '#FFD166AA', `P'`, scale, 2, true);
                
                vecCtx.setLineDash([]);
            }
            
            // 绘制标题
            vecCtx.fillStyle = '#FFD166';
            vecCtx.font = 'bold 14px Arial';
            vecCtx.textAlign = 'center';
            vecCtx.fillText('动量矢量合成 (总动量守恒)', centerX, 15);
            
            // 绘制图例
            const legendY = vecCanvas.height - 10;
            vecCtx.font = '12px Arial';
            vecCtx.textAlign = 'left';
            
            vecCtx.fillStyle = '#FF8E8E';
            vecCtx.fillText('p₁: 小球1动量', 10, legendY - 30);
            
            vecCtx.fillStyle = '#6EDBD3';
            vecCtx.fillText('p₂: 小球2动量', 10, legendY - 15);
            
            vecCtx.fillStyle = '#FFD166';
            vecCtx.fillText('P: 总动量 (守恒)', 10, legendY);
        }
        
        // 绘制动量矢量
        function drawMomentumVector(x, y, px, py, color, label, scale, lineWidth = 3, isDashed = false) {
            const dx = px * scale;
            const dy = py * scale;
            const magnitude = Math.sqrt(dx * dx + dy * dy);
            
            if (magnitude < 2) return; // 忽略太小的矢量
            
            vecCtx.save();
            
            if (isDashed) {
                vecCtx.setLineDash([5, 5]);
                vecCtx.strokeStyle = color + 'AA';
                vecCtx.fillStyle = color + 'AA';
            } else {
                vecCtx.setLineDash([]);
                vecCtx.strokeStyle = color;
                vecCtx.fillStyle = color;
            }
            
            vecCtx.lineWidth = lineWidth;
            
            // 绘制矢量线
            vecCtx.beginPath();
            vecCtx.moveTo(x, y);
            vecCtx.lineTo(x + dx, y + dy);
            vecCtx.stroke();
            
            // 绘制箭头头部
            const angle = Math.atan2(dy, dx);
            const arrowSize = 8;
            
            vecCtx.beginPath();
            vecCtx.moveTo(x + dx, y + dy);
            vecCtx.lineTo(
                x + dx - arrowSize * Math.cos(angle - Math.PI / 6),
                y + dy - arrowSize * Math.sin(angle - Math.PI / 6)
            );
            vecCtx.lineTo(
                x + dx - arrowSize * Math.cos(angle + Math.PI / 6),
                y + dy - arrowSize * Math.sin(angle + Math.PI / 6)
            );
            vecCtx.closePath();
            vecCtx.fill();
            
            // 绘制
// 绘制标签
            vecCtx.fillStyle = isDashed ? color + 'AA' : color;
            vecCtx.font = '12px Arial';
            vecCtx.textAlign = dx >= 0 ? 'left' : 'right';
            vecCtx.fillText(
                label, 
                x + dx + (dx >= 0 ? 10 : -10), 
                y + dy - (dy >= 0 ? 10 : -10)
            );
            
            vecCtx.restore();
        }
        
        // 更新小球位置
        function updateBalls() {
            // 更新小球1位置
            ball1.x += ball1.vx;
            
            // 更新小球2位置
            ball2.x += ball2.vx;
            
            // 边界检测
            if (ball1.x < ball1.radius) {
                ball1.x = ball1.radius;
                if (ball1.vx < 0) ball1.vx = -ball1.vx;
            }
            
            if (ball1.x > simCanvas.width - ball1.radius) {
                ball1.x = simCanvas.width - ball1.radius;
                if (ball1.vx > 0) ball1.vx = -ball1.vx;
            }
            
            if (ball2.x < ball2.radius) {
                ball2.x = ball2.radius;
                if (ball2.vx < 0) ball2.vx = -ball2.vx;
            }
            
            if (ball2.x > simCanvas.width - ball2.radius) {
                ball2.x = simCanvas.width - ball2.radius;
                if (ball2.vx > 0) ball2.vx = -ball2.vx;
            }
            
            // 碰撞检测
            const dx = ball2.x - ball1.x;
            const distance = Math.abs(dx);
            const minDistance = ball1.radius + ball2.radius;
            
            if (distance < minDistance) {
                // 处理碰撞
                handleCollision();
            }
        }
        
        // 处理碰撞
        function handleCollision() {
            // 计算碰撞后的速度
            if (isElastic) {
                // 完全弹性碰撞
                const v1_new = ((m1 - m2) * ball1.vx + 2 * m2 * ball2.vx) / (m1 + m2);
                const v2_new = ((m2 - m1) * ball2.vx + 2 * m1 * ball1.vx) / (m1 + m2);
                
                ball1.vx = v1_new;
                ball2.vx = v2_new;
            } else {
                // 完全非弹性碰撞
                const commonVelocity = (m1 * ball1.vx + m2 * ball2.vx) / (m1 + m2);
                ball1.vx = commonVelocity;
                ball2.vx = commonVelocity;
            }
            
            // 防止小球粘在一起
            const overlap = (ball1.radius + ball2.radius) - Math.abs(ball2.x - ball1.x);
            if (overlap > 0) {
                if (ball1.x < ball2.x) {
                    ball1.x -= overlap / 2;
                    ball2.x += overlap / 2;
                } else {
                    ball1.x += overlap / 2;
                    ball2.x -= overlap / 2;
                }
            }
        }
        
        // 更新数据显示
        function updateDataDisplay() {
            // 计算物理量
            const p1 = m1 * ball1.vx;
            const p2 = m2 * ball2.vx;
            const totalP = p1 + p2;
            
            const ek1 = 0.5 * m1 * ball1.vx * ball1.vx;
            const ek2 = 0.5 * m2 * ball2.vx * ball2.vx;
            const totalEk = ek1 + ek2;
            
            // 计算初始动能（用于能量条显示）
            const ek1_initial = 0.5 * m1 * v1 * v1;
            const ek2_initial = 0.5 * m2 * v2 * v2;
            const totalEk_initial = ek1_initial + ek2_initial;
            
            // 计算动能损失（仅非弹性碰撞）
            let energyLost = 0;
            if (!isElastic) {
                const ek1_final = 0.5 * m1 * v1_final * v1_final;
                const ek2_final = 0.5 * m2 * v2_final * v2_final;
                const totalEk_final = ek1_final + ek2_final;
                energyLost = totalEk_initial - totalEk_final;
            }
            
            // 更新小球1数据
            document.getElementById('ball1Speed').textContent = `v₁ = ${ball1.vx.toFixed(2)} m/s`;
            document.getElementById('ball1Momentum').textContent = `p₁ = ${p1.toFixed(2)} kg·m/s`;
            document.getElementById('ball1Energy').textContent = `Eₖ₁ = ${ek1.toFixed(2)} J`;
            
            // 更新小球2数据
            document.getElementById('ball2Speed').textContent = `v₂ = ${ball2.vx.toFixed(2)} m/s`;
            document.getElementById('ball2Momentum').textContent = `p₂ = ${p2.toFixed(2)} kg·m/s`;
            document.getElementById('ball2Energy').textContent = `Eₖ₂ = ${ek2.toFixed(2)} J`;
            
            // 更新系统数据
            document.getElementById('totalMomentum').textContent = `P = ${totalP.toFixed(2)} kg·m/s`;
            document.getElementById('totalEnergy').textContent = `Eₖ = ${totalEk.toFixed(2)} J`;
            document.getElementById('energyLost').textContent = `动能损失: ${energyLost.toFixed(2)} J`;
            
            // 更新能量条
            document.getElementById('totalEnergyValue').textContent = `${totalEk.toFixed(2)} J`;
            
            // 计算能量条宽度
            const maxEnergy = Math.max(totalEk_initial, 10); // 防止除零
            const currentEnergyPercent = (totalEk / maxEnergy) * 100;
            const lostEnergyPercent = (energyLost / maxEnergy) * 100;
            
            document.getElementById('totalEnergyBar').style.width = `${currentEnergyPercent}%`;
            document.getElementById('lostEnergyBar').style.width = `${lostEnergyPercent}%`;
            
            // 更新滑块值显示
            document.getElementById('mass1Value').textContent = `${m1.toFixed(1)} kg`;
            document.getElementById('mass2Value').textContent = `${m2.toFixed(1)} kg`;
            document.getElementById('velocity1Value').textContent = `${v1.toFixed(1)} m/s`;
            document.getElementById('velocity2Value').textContent = `${v2.toFixed(1)} m/s`;
        }
        
        // 动画循环
        function animate() {
            if (!isPlaying) return;
            
            updateBalls();
            drawSimulation();
            drawVectorDiagram();
            updateDataDisplay();
            
            animationId = requestAnimationFrame(animate);
        }
        
        // 初始化事件监听器
        function initEventListeners() {
            // 质量滑块
            document.getElementById('mass1Slider').addEventListener('input', function() {
                m1 = parseFloat(this.value);
                ball1.mass = m1;
                ball1.radius = 20 + m1 * 5; // 质量越大，半径越大
                calculateFinalVelocities();
                updateDataDisplay();
            });
            
            document.getElementById('mass2Slider').addEventListener('input', function() {
                m2 = parseFloat(this.value);
                ball2.mass = m2;
                ball2.radius = 20 + m2 * 5; // 质量越大，半径越大
                calculateFinalVelocities();
                updateDataDisplay();
            });
            
            // 速度滑块
            document.getElementById('velocity1Slider').addEventListener('input', function() {
                v1 = parseFloat(this.value);
                calculateFinalVelocities();
                if (!isPlaying) {
                    ball1.vx = v1;
                    updateDataDisplay();
                }
            });
            
            document.getElementById('velocity2Slider').addEventListener('input', function() {
                v2 = parseFloat(this.value);
                calculateFinalVelocities();
                if (!isPlaying) {
                    ball2.vx = v2;
                    updateDataDisplay();
                }
            });
            
            // 碰撞类型按钮
            document.getElementById('elasticBtn').addEventListener('click', function() {
                isElastic = true;
                this.classList.add('active');
                document.getElementById('inelasticBtn').classList.remove('active');
                calculateFinalVelocities();
                updateDataDisplay();
            });
            
            document.getElementById('inelasticBtn').addEventListener('click', function() {
                isElastic = false;
                this.classList.add('active');
                document.getElementById('elasticBtn').classList.remove('active');
                calculateFinalVelocities();
                updateDataDisplay();
            });
            
            // 播放/暂停按钮
            document.getElementById('playBtn').addEventListener('click', function() {
                isPlaying = !isPlaying;
                
                if (isPlaying) {
                    document.getElementById('playIcon').textContent = '⏸';
                    document.getElementById('playText').textContent = '暂停';
                    animate();
                } else {
                    document.getElementById('playIcon').textContent = '▶';
                    document.getElementById('playText').textContent = '播放';
                    if (animationId) {
                        cancelAnimationFrame(animationId);
                    }
                }
            });
            
            // 重置按钮
            document.getElementById('resetBtn').addEventListener('click', function() {
                isPlaying = false;
                document.getElementById('playIcon').textContent = '▶';
                document.getElementById('playText').textContent = '播放';
                
                if (animationId) {
                    cancelAnimationFrame(animationId);
                }
                
                resetBallPositions();
                drawSimulation();
                drawVectorDiagram();
                updateDataDisplay();
            });
        }
        
        // 初始化
        function init() {
            resizeCanvases();
            calculateFinalVelocities();
            drawSimulation();
            drawVectorDiagram();
            updateDataDisplay();
            initEventListeners();
        }
        
        // 页面加载完成后初始化
        window.addEventListener('load', init);
    </script>
</body>
</html>
```

### 3. 过程输出

### 3. 使用指南

## 动量守恒定律交互式教学动画使用指南

欢迎使用这款专门设计的动量守恒定律教学动画！本指南将帮助您充分利用这个交互式工具，深入理解碰撞过程中的动量与能量变化。

### 🎯 功能说明

本动画模拟了一维空间中的两个小球碰撞过程，直观展示了**完全弹性碰撞**与**完全非弹性碰撞**的物理规律。通过实时可视化、参数调节和数据分析，您将能够：

1. **观察动量守恒定律**：在不受外力的情况下，系统总动量保持不变
2. **区分碰撞类型**：理解弹性碰撞（动能守恒）与非弹性碰撞（动能损失）的本质区别
3. **掌握矢量概念**：直观理解动量作为矢量的方向性和合成规律
4. **探索物理规律**：通过改变参数，自主发现质量、速度对碰撞结果的影响

### 🎮 主要功能

#### 1. 模拟控制区
- **播放/暂停按钮**：控制动画运行与暂停
- **重置按钮**：将小球恢复到初始位置，重新开始模拟
- **实时动画**：观察小球在轨道上的运动与碰撞过程

#### 2. 参数调节区
- **质量调节滑块**：调整小球1和小球2的质量（0.5-5.0 kg）
- **速度调节滑块**：调整小球的初速度（-5.0 到 +5.0 m/s，负值表示向左运动）
- **碰撞类型选择**：在"完全弹性碰撞"和"完全非弹性碰撞"之间切换

#### 3. 可视化显示区
- **主模拟画面**：显示小球运动轨迹、速度矢量和碰撞效果
- **动量矢量合成图**：动态展示动量矢量的合成与守恒
- **实时数据面板**：显示速度、动量、动能的精确数值
- **能量变化条**：直观显示动能的变化与损失情况

#### 4. 教学辅助区
- **核心公式展示**：显示动量守恒和能量守恒的关键公式
- **碰撞提示**：在碰撞发生时显示教学提示
- **预测显示**：用虚线显示碰撞后的预测速度

### ✨ 设计特色

#### 1. 多层级可视化
- **第一层**：小球实体运动（最直观）
- **第二层**：速度矢量箭头（显示方向与大小）
- **第三层**：动量矢量合成图（展示守恒原理）
- **第四层**：能量变化条（量化能量转移）

#### 2. 智能教学引导
- **碰撞预警**：小球接近时显示提示区域
- **关键帧突出**：碰撞瞬间有特殊视觉效果
- **对比学习**：通过切换碰撞类型，直观对比不同结果

#### 3. 专业配色方案
- **红色系**：小球1及相关数据（#FF6B6B）
- **青色系**：小球2及相关数据（#4ECDC4）
- **黄色系**：总动量矢量（#FFD166）
- **紫色系**：系统总能量（#9B5DE5）
- **深色背景**：减少视觉干扰，突出核心内容

### 📚 教学要点

#### 核心概念理解
1. **动量守恒定律**
   - 观察：无论碰撞类型如何，**总动量矢量始终保持不变**
   - 验证：在矢量合成图中，黄色总动量箭头长度和方向不变
   - 公式：m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'

2. **碰撞类型差异**
   - **完全弹性碰撞**：动能守恒，碰撞后小球分开
     - 能量条：总动能条长度不变
     - 速度：两球速度不同（除非质量相等）
   - **完全非弹性碰撞**：动能损失最大，碰撞后粘在一起
     - 能量条：总动能条缩短，出现灰色"损失"部分
     - 速度：两球以相同速度运动

3. **矢量性质**
   - 方向重要性：速度的正负代表方向
   - 矢量合成：动量矢量按平行四边形法则合成
   - 守恒验证：碰撞前后，总动量矢量完全相同

#### 典型实验场景
1. **质量相等，速度相反**
   - 设置：m₁ = m₂ = 2.0 kg，v₁ = 2.0 m/s，v₂ = -2.0 m/s
   - 弹性碰撞：速度交换（v₁' = -2.0，v₂' = 2.0）
   - 观察：动量守恒，动能守恒

2. **质量悬殊，轻球静止**
   - 设置：m₁ = 5.0 kg，m₂ = 0.5 kg，v₁ = 2.0 m/s，v₂ = 0
   - 弹性碰撞：重球几乎不停，轻球高速弹出
   - 非弹性碰撞：两球以接近重球原速度运动

3. **追尾碰撞**
   - 设置：m₁ = 1.0 kg，m₂ = 3.0 kg，v₁ = 4.0 m/s，v₂ = 1.0 m/s
   - 观察：同向运动时的碰撞结果

### 💡 使用建议

#### 对于学生
1. **探索式学习**
   - 先随意调节参数，观察现象，培养物理直觉
   - 再系统测试，记录数据，寻找规律
   - 最后用公式验证观察结果

2. **分步理解**
   - 第一步：只看小球运动，理解碰撞的基本过程
   - 第二步：关注速度矢量，理解方向变化
   - 第三步：研究动量矢量图，掌握守恒原理
   - 第四步：分析能量变化，区分碰撞类型

3. **问题导向**
   - "如果质量增加三倍，会发生什么？"
   - "为什么非弹性碰撞后动能会减少？"
   - "总动量矢量为什么保持不变？"

#### 对于教师
1. **课堂演示**
   - 用于引入新概念，激发学生兴趣
   - 对比讲解两种碰撞类型的根本区别
   - 可视化抽象概念，降低理解难度

2. **探究活动设计**
   - 设计实验任务单，引导学生系统探索
   - 组织小组讨论，分析观察到的现象
   - 联系实际应用（汽车碰撞、台球运动等）

3. **概念巩固**
   - 在讲解公式后，用动画验证计算结果
   - 针对常见误解，设计特定场景进行澄清
   - 作为形成性评价工具，检查学生理解程度

#### 最佳实践流程
1. **初始探索**（5分钟）
   - 自由调节参数，熟悉界面功能
   - 观察不同设置下的碰撞现象

2. **系统实验**（15分钟）
   - 测试建议的典型场景
   - 记录数据，填写实验表格
   - 对比弹性与非弹性碰撞的结果

3. **深入分析**（10分钟）
   - 专注于矢量图，理解动量守恒
   - 分析能量条，理解动能变化
   - 用公式计算，验证动画结果

4. **拓展思考**（5分钟）
   - "如果增加第三个球会怎样？"
   - "在二维空间中碰撞会有什么不同？"
   - "这个原理在哪些实际场景中应用？"

### 🔧 技术提示

1. **浏览器兼容性**
   - 建议使用Chrome、Firefox或Edge最新版本
   - 确保启用JavaScript
   - 屏幕分辨率建议1920×1080或更高

2. **性能优化**
   - 动画运行流畅，支持实时参数调整
   - 所有计算在本地完成，无需网络连接
   - 响应式设计，适应不同屏幕尺寸

3. **教学扩展**
   - 可结合传统板书，推导相关公式
   - 可设计工作纸，引导学生记录观察
   - 可组织小组竞赛，预测碰撞结果

### 🎓 学习目标达成

通过本动画的学习，您将能够：

- ✅ 解释动量守恒定律及其矢量性
- ✅ 区分完全弹性与完全非弹性碰撞
- ✅ 预测给定条件下的碰撞结果
- ✅ 分析碰撞过程中的能量转化
- ✅ 将一维碰撞原理应用于简单实际问题

---

**开始您的探索之旅吧！** 拖动滑块，点击按钮，观察现象，思考原理。物理学的美妙在于发现规律，而最好的发现方式就是亲手实验。祝您学习愉快，收获满满！

> 提示：遇到不理解的现象时，不妨暂停动画，仔细观察矢量图和能量条的变化，再结合公式思考其中的物理原理。