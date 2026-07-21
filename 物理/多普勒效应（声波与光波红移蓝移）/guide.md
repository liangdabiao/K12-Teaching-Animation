# 需求：多普勒效应（声波与光波红移蓝移）

### 1. 专业思考


#### 用户需求分析
本动画面向高中或大学低年级的物理学习者。用户的核心需求是：
1.  **理解核心现象**：直观地看到并理解为什么波源运动时，观察者接收到的频率会发生变化。
2.  **区分声波与光波**：理解多普勒效应在声波（机械波，需要介质）和光波（电磁波，无需介质）上的共同原理与不同表现（红移/蓝移）。
3.  **掌握公式与应用**：将动画中的直观现象与抽象的物理公式（频率变化公式）联系起来，并了解其在现实中的应用（如雷达测速、宇宙学红移）。
4.  **降低认知负荷**：通过可控的交互和清晰的视觉引导，将复杂的相对运动概念分解，使学习过程循序渐进。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）

*   **核心概念**：
    *   **核心机制**：波源与观察者之间的相对运动导致单位时间内接收到的波阵面数量（即频率）发生变化。
    *   **声波多普勒**：波源运动导致波前疏密变化，进而引起音高变化（接近时音调变高，远离时音调变低）。
    *   **光波多普勒**：原理相同，表现为光波频率变化，即颜色在光谱上的移动（接近时为蓝移，远离时为红移）。
    *   **公式联系**：将动画中观察到的波阵面挤压或拉伸现象，与频率变化公式 `f' = f * (v ± vo) / (v ∓ vs)` 中的变量动态关联。

*   **认知规律**：
    1.  **从具体到抽象**：先展示最直观的声波（以圆形波模拟），建立“运动导致波密波疏”的感性认识。
    2.  **从共性到特性**：在理解共同原理后，切换到光波场景，引入“红移”和“蓝移”的术语及视觉表现（颜色变化）。
    3.  **从现象到公式**：在动画过程中，实时显示关键参数（波源速度、观察者位置、接收频率），并可选显示公式及当前数值代入过程。
    4.  **从学习到应用**：设置独立的应用场景模块（如警车鸣笛经过、恒星光谱分析），巩固理解。

*   **交互设计**：
    *   **主体控制**：用户可拖拽调整**波源**和**观察者**的位置，或直接控制波源的**运动速度**和**方向**。
    *   **场景切换**：通过标签页或按钮在“声波模拟”、“光波模拟”和“应用示例”三个主场景间切换。
    *   **视图控制**：
        *   **播放/暂停/重置**：控制动画运行。
        *   **显示/隐藏**：可切换显示波阵面、波前法线、参数读数、公式推导等图层，避免界面杂乱。
        *   **轨迹开关**：可显示波源的运动轨迹和历史波阵面，帮助理解波传播的延时效应。
    *   **参数反馈**：实时显示波源速度、理论发射频率、观察者接收频率、频率变化比等数据。

*   **视觉呈现**：
    *   **画布布局**：左侧为大型动画演示区，右侧为控制面板和数据面板。
    *   **声波表现**：
        *   使用**同心圆环**表示波阵面，圆环随时间向外扩散并淡化。
        *   波源运动时，圆环的中心点沿轨迹移动，导致波前在运动方向密集（蓝色调），反方向稀疏（红色调），用颜色渐变直观表示压力/密度变化。
        *   在观察者位置提供一个“听觉指示器”（如跳动的柱状条或显示接收频率），并可能配有可开关的模拟音高变化。
    *   **光波表现**：
        *   背景变为深空黑色。
        *   波阵面用更细、颜色更鲜明的同心圆表示，颜色本身代表频率：静止时为黄色（中性），蓝移区域变为蓝紫色，红移区域变为橙红色。
        *   观察者处显示一个“光谱仪”或简单的色块，实时显示接收到的光的“颜色”（频率）。
    *   **应用场景**：
        *   **警车场景**：一个简化的街道背景，用户可控制警车（波源）运动，街道旁有一个静止的观察者小人。听到的音高变化与上方波动画联动。
        *   **宇宙红移场景**：展示一个遥远的恒星（波源）相对于地球（观察者）运动，其发出的光谱线发生移动，旁边展示实际光谱图的对比动画。

#### 配色方案选择
*   **主色调**：
    *   **深空蓝/暗灰色**：作为画布背景，专业、沉稳，能突出前景的动画元素，尤其适合光波场景。
    *   **亮色/白色**：用于坐标轴、控制面板背景和文字，确保清晰可读。
*   **功能色**：
    *   **声波密度色**：**蓝色**表示高密度/高压区（波前密集），**红色**表示低密度/低压区（波前稀疏）。采用渐变过渡。
    *   **光波频率色**：**蓝紫色**表示高频（蓝移），**黄白色**表示原频率，**橙红色**表示低频（红移）。符合物理学中对光谱颜色的约定。
    *   **交互元素色**：
        *   波源：用**亮黄色**或**橙色**的醒目图形表示。
        *   观察者：用**绿色**或**青色**的图形表示，与波源区分。
        *   控制按钮：使用简洁的扁平化设计，主操作按钮用温和的**蓝色**，重置等用**灰色**。
*   **原则**：保证高对比度以突出关键元素，同时整体色调和谐，不刺眼，符合长时间学习的视觉舒适度要求。

#### 交互功能列表
1.  **场景选择器**：按钮组，用于在“声波模拟”、“光波模拟”、“警车示例”、“宇宙红移”场景间切换。
2.  **动画控制**：播放、暂停、重置（回到初始状态）按钮。
3.  **实体控制**：
    *   可拖拽**波源**和**观察者**图标到画布任意位置。
    *   滑块控制**波源速度**（大小和方向，正负值表示接近或远离观察者）。
    *   复选框控制波源是否**匀速直线运动**或由用户拖拽自由运动。
4.  **视觉辅助开关**（复选框组）：
    *   `显示波阵面`：开关圆形波的扩散动画。
    *   `显示波前法线`：显示从波源发出时的波前径向线，帮助理解波传播方向。
    *   `显示轨迹与历史波`：显示波源运动路径和过去发出的波阵面，理解延时。
    *   `显示参数`：实时显示速度、频率等数值。
    *   `显示公式`：在面板上显示频率公式，并高亮当前正在变化的变量。
5.  **声波专属控制**：一个“启用声音”开关，打开后，观察者位置会根据接收频率播放相应的合成音调。
6.  **数据面板**：实时显示：
    *   波源速度 `v_s`
    *   波速（声速 `v` 或光速 `c`）
    *   发射频率 `f`
    *   接收频率 `f'`
    *   频率变化比 `f'/f`
    *   （可选）多普勒频移公式及当前数值代入的算式。
7.  **预设案例按钮**：如“警车接近”、“警车远离”、“恒星高速远离”等，一键设置典型场景参数，便于快速演示。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>多普勒效应教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e6e6e6;
            line-height: 1.6;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid #3498db;
        }

        h1 {
            color: #3498db;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            color: #95a5a6;
            font-size: 1.2rem;
        }

        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 20px;
        }

        .animation-area {
            flex: 1;
            min-width: 700px;
            background: rgba(25, 25, 35, 0.9);
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid #2c3e50;
        }

        .control-panel {
            flex: 0 0 400px;
            background: rgba(30, 30, 40, 0.9);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid #2c3e50;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .panel-section {
            background: rgba(40, 40, 50, 0.7);
            border-radius: 8px;
            padding: 15px;
            border-left: 4px solid #3498db;
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

        h3 {
            color: #2ecc71;
            font-size: 1.1rem;
            margin: 15px 0 10px 0;
        }

        .scene-selector {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .scene-btn {
            flex: 1;
            min-width: 120px;
            padding: 12px;
            background: #2c3e50;
            color: #ecf0f1;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            text-align: center;
        }

        .scene-btn:hover {
            background: #34495e;
            transform: translateY(-2px);
        }

        .scene-btn.active {
            background: #3498db;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
        }

        .control-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #bdc3c7;
            font-size: 0.95rem;
        }

        .slider-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        input[type="range"] {
            flex: 1;
            height: 6px;
            -webkit-appearance: none;
            background: #34495e;
            border-radius: 3px;
            outline: none;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: #3498db;
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }

        .value-display {
            min-width: 50px;
            text-align: center;
            background: rgba(52, 152, 219, 0.2);
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
        }

        .checkbox-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 10px;
        }

        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
        }

        .checkbox-item input[type="checkbox"] {
            width: 16px;
            height: 16px;
            cursor: pointer;
        }

        .animation-controls {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .ctrl-btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.95rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .play-btn {
            background: #2ecc71;
            color: white;
        }

        .play-btn:hover {
            background: #27ae60;
        }

        .reset-btn {
            background: #e74c3c;
            color: white;
        }

        .reset-btn:hover {
            background: #c0392b;
        }

        .data-panel {
            background: rgba(25, 25, 35, 0.9);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid #2c3e50;
        }

        .data-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 10px;
        }

        .data-item {
            background: rgba(52, 152, 219, 0.1);
            padding: 12px;
            border-radius: 6px;
            border-left: 3px solid #3498db;
        }

        .data-label {
            font-size: 0.85rem;
            color: #95a5a6;
            margin-bottom: 5px;
        }

        .data-value {
            font-size: 1.2rem;
            font-family: 'Courier New', monospace;
            color: #2ecc71;
            font-weight: bold;
        }

        .formula-display {
            background: rgba(46, 204, 113, 0.1);
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            border-left: 3px solid #2ecc71;
            font-family: 'Cambria Math', 'Times New Roman', serif;
        }

        .formula {
            font-size: 1.3rem;
            text-align: center;
            margin: 10px 0;
            color: #f1c40f;
        }

        .formula-legend {
            font-size: 0.9rem;
            color: #bdc3c7;
            margin-top: 10px;
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
            font-size: 0.9rem;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }

        canvas {
            display: block;
            background: #0f1525;
            border-radius: 8px;
            width: 100%;
            height: 500px;
            cursor: crosshair;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #2c3e50;
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        @media (max-width: 1200px) {
            .main-content {
                flex-direction: column;
            }
            
            .animation-area, .control-panel {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>多普勒效应教学动画</h1>
            <p class="subtitle">声波与光波的红移与蓝移现象 | 交互式物理模拟</p>
        </header>

        <div class="main-content">
            <div class="animation-area">
                <canvas id="animationCanvas"></canvas>
                <div class="legend">
                    <div class="legend-item">
                        <div class="legend-color" style="background: #f1c40f;"></div>
                        <span>波源</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background: #2ecc71;"></div>
                        <span>观察者</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background: #3498db;"></div>
                        <span>高频/蓝移区</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background: #e74c3c;"></div>
                        <span>低频/红移区</span>
                    </div>
                </div>
            </div>

            <div class="control-panel">
                <div class="panel-section">
                    <h2>🎯 场景选择</h2>
                    <div class="scene-selector">
                        <button class="scene-btn active" data-scene="sound">声波模拟</button>
                        <button class="scene-btn" data-scene="light">光波模拟</button>
                        <button class="scene-btn" data-scene="police">警车示例</button>
                        <button class="scene-btn" data-scene="cosmic">宇宙红移</button>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>🎮 实体控制</h2>
                    <div class="control-group">
                        <label>波源速度: <span id="speedValue">0.0</span> m/s</label>
                        <div class="slider-container">
                            <input type="range" id="sourceSpeed" min="-100" max="100" value="0" step="1">
                            <div class="value-display" id="speedDisplay">0.0</div>
                        </div>
                    </div>
                    
                    <div class="control-group">
                        <label>发射频率 (f₀): <span id="freqValue">440</span> Hz</label>
                        <div class="slider-container">
                            <input type="range" id="sourceFreq" min="200" max="800" value="440" step="10">
                            <div class="value-display" id="freqDisplay">440</div>
                        </div>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>👁️ 视觉辅助</h2>
                    <div class="checkbox-group">
                        <label class="checkbox-item">
                            <input type="checkbox" id="showWavefronts" checked>
                            <span>显示波阵面</span>
                        </label>
                        <label class="checkbox-item">
                            <input type="checkbox" id="showNormals">
                            <span>显示波前法线</span>
                        </label>
                        <label class="checkbox-item">
                            <input type="checkbox" id="showTrajectory">
                            <span>显示运动轨迹</span>
                        </label>
                        <label class="checkbox-item">
                            <input type="checkbox" id="showHistory">
                            <span>显示历史波</span>
                        </label>
                        <label class="checkbox-item">
                            <input type="checkbox" id="enableSound">
                            <span>启用声音反馈</span>
                        </label>
                    </div>
                </div>

                <div class="panel-section">
                    <h2>⏯️ 动画控制</h2>
                    <div class="animation-controls">
                        <button class="ctrl-btn play-btn" id="playPauseBtn">⏸️ 暂停</button>
                        <button class="ctrl-btn reset-btn" id="resetBtn">🔄 重置</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="data-panel">
            <h2>📊 实时数据</h2>
            <div class="data-grid">
                <div class="data-item">
                    <div class="data-label">波源速度 (vₛ)</div>
                    <div class="data-value" id="dataSpeed">0.0 m/s</div>
                </div>
                <div class="data-item">
                    <div class="data-label">波速 (v/c)</div>
                    <div class="data-value" id="dataWaveSpeed">340 m/s</div>
                </div>
                <div class="data-item">
                    <div class="data-label">发射频率 (f₀)</div>
                    <div class="data-value" id="dataEmitFreq">440 Hz</div>
                </div>
                <div class="data-item">
                    <div class="data-label">接收频率 (f')</div>
                    <div class="data-value" id="dataRecvFreq">440.0 Hz</div>
                </div>
                <div class="data-item">
                    <div class="data-label">频率变化比 (f'/f₀)</div>
                    <div class="data-value" id="dataFreqRatio">1.000</div>
                </div>
                <div class="data-item">
                    <div class="data-label">多普勒频移</div>
                    <div class="data-value" id="dataShift">0.0 Hz</div>
                </div>
            </div>

            <div class="formula-display">
                <h3>多普勒效应公式</h3>
                <div class="formula" id="formulaDisplay">
                    f' = f₀ × (v ± vₒ) / (v ∓ vₛ)
                </div>
                <div class="formula-legend">
                    <div>f' = 观察者接收频率 | f₀ = 波源发射频率</div>
                    <div>v = 波速 | vₛ = 波源速度 | vₒ = 观察者速度</div>
                    <div>符号规则：接近时取正号，远离时取负号</div>
                    <div id="currentFormula">当前：f' = 440 × (340 + 0) / (340 - 0) = 440.0 Hz</div>
                </div>
            </div>
        </div>

        <footer>
            <p>多普勒效应教学动画 | 交互式物理模拟 | 使用HTML5 Canvas实现</p>
            <p>提示：拖动画布上的波源或观察者可以改变它们的位置</p>
        </footer>
    </div>

    <script>
        // 音频上下文（用于声音反馈）
        let audioContext = null;
        let oscillator = null;
        let lastFrequency = 440;

        // 主Canvas和上下文
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

        // 物理参数
        const config = {
            scene: 'sound', // sound, light, police, cosmic
            isPlaying: true,
            waveSpeed: 340, // 声速 m/s
            sourceFreq: 440, // Hz
            sourceSpeed: 0, // m/s
            sourcePos: { x: 300, y: 250 },
            observerPos: { x: 700, y: 250 },
            wavefronts: [],
            trajectory: [],
            lastWaveTime: 0,
            waveInterval: 100, // 毫秒
            time: 0,
            showWavefronts: true,
            showNormals: false,
            showTrajectory: false,
            showHistory: false,
            enableSound: false,
            draggedObject: null
        };

        // 场景配置
        const scenes = {
            sound: {
                name: '声波模拟',
                waveSpeed: 340,
                waveColor: 'rgba(52, 152, 219, 0.7)',
                bgColor: '#0f1525',
                compressColor: '#3498db',
                stretchColor: '#e74c3c',
                sourceColor: '#f1c40f',
                observerColor: '#2ecc71'
            },
            light: {
                name: '光波模拟',
                waveSpeed: 3e8,
                waveColor: 'rgba(241, 196, 15, 0.6)',
                bgColor: '#000814',
                compressColor: '#9b59b6', // 蓝紫色
                stretchColor: '#e67e22', // 橙红色
                sourceColor: '#ffffff',
                observerColor: '#2ecc71'
            },
            police: {
                name: '警车示例',
                waveSpeed: 340,
                waveColor: 'rgba(52, 152, 219, 0.7)',
                bgColor: '#1a3c2e',
                compressColor: '#3498db',
                stretchColor: '#e74c3c',
                sourceColor: '#f1c40f',
                observerColor: '#2ecc71'
            },
            cosmic: {
                name: '宇宙红移',
                waveSpeed: 3e8,
                waveColor: 'rgba(155, 89, 182, 0.6)',
                bgColor: '#000000',
                compressColor: '#3498db',
                stretchColor: '#e74c3c',
                sourceColor: '#f1c40f',
                observerColor: '#2ecc71'
            }
        };

        // 初始化
        function init() {
            config.wavefronts = [];
            config.trajectory = [];
            config.lastWaveTime = 0;
            config.time = 0;
            
            // 根据场景设置初始位置
            if (config.scene === 'police') {
                config.sourcePos = { x: 200, y: 250 };
                config.observerPos = { x: 700, y: 300 };
            } else if (config.scene === 'cosmic') {
                config.sourcePos = { x: 200, y: 250 };
                config.observerPos = { x: 700, y: 250 };
            } else {
                config.sourcePos = { x: 300, y: 250 };
                config.observerPos = { x: 700, y: 250 };
            }
            
            updateWaveSpeed();
            updateUI();
            animate();
        }

        // 更新波速
        function updateWaveSpeed() {
            config.waveSpeed = scenes[config.scene].waveSpeed;
            document.getElementById('dataWaveSpeed').textContent = 
                config.scene === 'sound' || config.scene === 'police' ? 
                `${config.waveSpeed} m/s` : '3.0×10⁸ m/s';
        }

        // 计算接收频率
        function calculateReceivedFrequency() {
            const v = config.waveSpeed;
            const vs = config.sourceSpeed;
            const f0 = config.sourceFreq;
            
            // 计算波源到观察者的方向向量
            const dx = config.observerPos.x - config.sourcePos.x;
            const dy = config.observerPos.y - config.sourcePos.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance === 0) return f0;
            
            // 计算相对速度在连线方向上的分量
            const directionX = dx / distance;
            const directionY = dy / distance;
            
            // 波源速度在连线方向上的分量（正表示远离观察者）
            const vs_proj = vs * (directionX * Math.cos(0) + directionY * Math.sin(0));
            
            // 多普勒公式（观察者静止）
            let f_prime;
            if (vs_proj < 0) { // 波源接近观察者
                f_prime = f0 * v / (v + vs_proj);
            } else { // 波源远离观察者
                f_prime = f0 * v / (v - vs_proj);
            }
            
            return f_prime;
        }

        // 更新声音
        function updateSound() {
            if (!config.enableSound || !audioContext) return;
            
            const freq = calculateReceivedFrequency();
            
            if (Math.abs(freq - lastFrequency) > 0.1) {
                if (oscillator) {
                    oscillator.frequency.setValueAtTime(freq, audioContext.currentTime);
                }
                lastFrequency = freq;
            }
        }

        // 开始/停止声音
        function toggleSound(enable) {
            if (enable) {
                if (!audioContext) {
                    audioContext = new (window.AudioContext || window.webkitAudioContext)();
                }
                
                if (!oscillator) {
                    oscillator = audioContext.createOscillator();
                    const gainNode = audioContext.createGain();
                    gainNode.gain.value = 0.1;
                    oscillator.connect(gainNode);
                    gainNode.connect(audioContext.destination);
                    oscillator.type = 'sine';
                    oscillator.frequency.setValueAtTime(config.sourceFreq, audioContext.currentTime);
                    oscillator.start();
                }
            } else {
                if (oscillator) {
                    oscillator.stop();
                    oscillator = null;
                }
            }
        }

        // 绘制函数
        function draw() {
            const scene = scenes[config.scene];
            
            // 清空画布
            ctx.fillStyle = scene.bgColor;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制场景特定元素
            if (config.scene === 'police') {
                drawPoliceScene();
            } else if (config.scene === 'cosmic') {
                drawCosmicScene();
            }
            
            // 绘制轨迹
            if (config.showTrajectory && config.trajectory.length > 1) {
                ctx.beginPath();
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.moveTo(config.trajectory[0].x, config.trajectory[0].y);
                for (let i = 1; i < config.trajectory.length; i++) {
                    ctx.lineTo(config.trajectory[i].x, config.trajectory[i].y);
                }
                ctx.stroke();
                ctx.setLineDash([]);
            }
            
            // 绘制波阵面
            if (config.showWavefronts) {
                for (let i = 0; i < config.wavefronts.length; i++) {
                    const wave = config.wavefronts[i];
                    const radius = wave.radius;
                    const age = config.time - wave.time;
                    
                    // 计算透明度
                    let alpha = 1 - age / 3000;
                    if (alpha <= 0) continue;
                    
                    // 根据场景选择颜色
                    let waveColor;
                    if (config.scene === 'light') {
                        // 光波：根据频率偏移选择颜色
                        const angle = Math.atan2(wave.y - config.sourcePos.y, wave.x - config.sourcePos.x);
                        const sourceAngle = Math.atan2(config.observerPos.y - config.sourcePos.y, 
                                                      config.observerPos.x - config.sourcePos.x);
                        const angleDiff = Math.abs(angle - sourceAngle);
                        
                        if (angleDiff < Math.PI/6) {
                            waveColor = scene.compressColor; // 蓝移方向
                        } else if (angleDiff > Math.PI*5/6) {
                            waveColor = scene.stretchColor; // 红移方向
                        } else {
                            waveColor = scene.waveColor;
                        }
                    } else {
                        // 声波：根据压缩/拉伸选择颜色
                        const dx = wave.x - config.sourcePos.x;
                        const dy = wave.y - config.sourcePos.y;
                        const angle = Math.atan2(dy, dx);
                        const motionAngle = config.sourceSpeed >= 0 ? 0 : Math.PI;
                        const angleDiff = Math.abs(angle - motionAngle);
                        
                        if (angleDiff < Math.PI/6) {
                            waveColor = scene.compressColor; // 压缩区（高频）
                        } else if (angleDiff > Math.PI*5/6) {
                            waveColor = scene.stretchColor; // 拉伸区（低频）
                        } else {
                            waveColor = scene.waveColor;
                        }
                    }
                    
                    // 绘制波阵面
                    ctx.beginPath();
                    ctx.arc(wave.x, wave.y, radius, 0, Math.PI * 2);
                    ctx.strokeStyle = waveColor.replace(')', `, ${alpha})`).replace('rgb', 'rgba');
                    ctx.lineWidth = 2;
                    ctx.stroke();
                    
                    // 绘制波前法线
                    if (config.showNormals) {
                        ctx.beginPath();
                        ctx.moveTo(wave.x, wave.y);
                        ctx.lineTo(
                            wave.x + Math.cos(wave.angle) * 20,
                            wave.y + Math.sin(wave.angle) * 20
                        );
                        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
                        ctx.lineWidth = 1;
                        ctx.stroke();
                    }
                }
            }
            
            // 绘制波源
            ctx.beginPath();
            ctx.arc(config.sourcePos.x, config.sourcePos.y, 15, 0, Math.PI * 2);
            ctx.fillStyle = scene.sourceColor;
            ctx.fill();
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // 绘制速度箭头
            if (Math.abs(config.sourceSpeed) > 0.1) {
                const angle = config.sourceSpeed >= 0 ? 0 : Math.PI;
                const arrowLength = Math.min(Math.abs(config.sourceSpeed) * 2, 100);
                
                ctx.beginPath();
                ctx.moveTo(config.sourcePos.x, config.sourcePos.y);
                ctx.lineTo(
                    config.sourcePos.x + Math.cos(angle) * arrowLength,
                    config.sourcePos.y + Math.sin(angle) * arrowLength
                );
                ctx.strokeStyle = config.sourceSpeed > 0 ? '#2ecc71' : '#e74c3c';
                ctx.lineWidth = 3;
                ctx.stroke();
                
                // 箭头头部
                ctx.beginPath();
                ctx.moveTo(
                    config.sourcePos.x + Math.cos(angle) * arrowLength,
                    config.sourcePos.y + Math.sin(angle) * arrowLength
                );
                ctx.lineTo(
                    config.sourcePos.x + Math.cos(angle) * arrowLength - Math.cos(angle - Math.PI/6) * 10,
                    config.sourcePos.y + Math.sin(angle) * arrowLength - Math.sin(angle - Math.PI/6) * 10
                );
                ctx.lineTo(
                    config.sourcePos.x + Math.cos(angle) * arrowLength - Math.cos(angle + Math.PI/6) * 10,
                    config.sourcePos.y + Math.sin(angle) * arrowLength - Math.sin(angle + Math.PI/6) * 10
                );
                ctx.closePath();
                ctx.fillStyle = config.sourceSpeed > 0 ? '#2ecc71' : '#e74c3c';
                ctx.fill();
            }
            
            // 绘制观察者
            ctx.beginPath();
            ctx.arc(config.observerPos.x, config.observerPos.y, 12, 0, Math.PI * 2);
            ctx.fillStyle = scene.observerColor;
            ctx.fill();
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // 绘制观察者接收指示器
            const receivedFreq = calculateReceivedFrequency();
            const freqRatio = receivedFreq / config.sourceFreq;
            
            ctx.beginPath();
            ctx.arc(config.observerPos.x, config.observerPos.y, 30, 0, Math.PI * 2);
            ctx.strokeStyle = freqRatio > 1 ? scene.compressColor : 
                             freqRatio < 1 ? scene.stretchColor : '#ffffff';
            ctx.lineWidth = 3;
            ctx.stroke();
            
            // 绘制频率指示条
            const barWidth = 60;
            const barHeight = 8;
            const freqBar = (freqRatio - 0.5) * barWidth;
            
            ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
            ctx.fillRect(
                config.observerPos.x - barWidth/2,
                config.observerPos.y - 50,
                barWidth,
                barHeight
            );
            
            ctx.fillStyle = freqRatio > 1 ? scene.compressColor : 
                           freqRatio < 1 ? scene.stretchColor : '#2ecc71';
            ctx.fillRect(
                config.observerPos.x - barWidth/2 + barWidth/2,
                config.observerPos.y - 50,
                freqBar,
                barHeight
            );
            
            // 绘制中心线
            ctx.beginPath();
            ctx.moveTo(config.observerPos.x, config.observerPos.y - 50);
            ctx.lineTo(config.observerPos.x, config.observerPos.y - 42);
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.stroke();
        }

        // 绘制警车场景
        function drawPoliceScene() {
            // 绘制道路
            ctx.fillStyle = '#34495e';
            ctx.fillRect(0, 280, canvas.width, 40);
            
            ctx.strokeStyle = '#f1c40f';
            ctx.lineWidth = 3;
            ctx.setLineDash([20, 20]);
            ctx.beginPath();
            ctx.moveTo(0, 300);
            ctx.lineTo(canvas.width, 300);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // 绘制警车
            const carX = config.sourcePos.x;
            const carY = 280;
            
            ctx.fillStyle = '#3498db';
            ctx.fillRect(carX - 30, carY - 20, 60, 20);
            ctx.fillRect(carX - 20, carY - 40, 40, 20);
            
            // 车轮
            ctx.fillStyle = '#2c3e50';
            ctx.beginPath();
            ctx.arc(carX - 15, carY, 8, 0, Math.PI * 2);
            ctx.arc(carX + 15, carY, 8, 0, Math.PI * 2);
            ctx.fill();
            
            // 警灯
            ctx.fillStyle = '#e74c3c';
            ctx.beginPath();
            ctx.arc(carX, carY - 30, 5, 0, Math.PI * 2);
            ctx.fill();
            
            // 观察者（人）
            const personX = config.observerPos.x;
            const personY = config.observerPos.y;
            
            ctx.beginPath();
            ctx.arc(personX, personY - 20, 8, 0, Math.PI * 2); // 头
            ctx.fillStyle = '#ecf0f1';
            ctx.fill();
            
            ctx.fillStyle = '#3498db';
            ctx.fillRect(personX - 6, personY - 12, 12, 20); // 身体
            
            ctx.fillStyle = '#2c3e50';
            ctx.fillRect(personX - 8, personY + 8, 4, 20); // 左腿
            ctx.fillRect(personX + 4, personY + 8, 4, 20); // 右腿
        }

        // 绘制宇宙场景
        function drawCosmicScene() {
            // 绘制星空
            for (let i = 0; i < 100; i++) {
                const x = Math.random() * canvas.width;
                const y = Math.random() * canvas.height;
                const size = Math.random() * 2;
                
                ctx.beginPath();
                ctx.arc(x, y, size, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.fill();
            }
            
            // 绘制地球（观察者）
            ctx.beginPath();
            ctx.arc(config.observerPos.x, config.observerPos.y, 25, 0, Math.PI * 2);
            const earthGradient = ctx.createRadialGradient(
                config.observerPos.x, config.observerPos.y, 0,
                config.observerPos.x, config.observerPos.y, 25
            );
            earthGradient.addColorStop(0, '#3498db');
            earthGradient.addColorStop(1, '#1a5276');
            ctx.fillStyle = earthGradient;
            ctx.fill();
            
            // 绘制恒星（波源）
            ctx.beginPath();
            ctx.arc(config.sourcePos.x, config.sourcePos.y, 20, 0, Math.PI * 2);
            const starGradient = ctx.createRadialGradient(
                config.sourcePos.x, config.sourcePos.y, 0,
                config.sourcePos.x, config.sourcePos.y, 20
            );
            starGradient.addColorStop(0, '#ffffff');
            starGradient.addColorStop(0.5, '#f1c40f');
            starGradient.addColorStop(1, '#e67e22');
            ctx.fillStyle = starGradient;
            ctx.fill();
            
            // 恒星光芒
            for (let i = 0; i < 8; i++) {
                const angle = (i * Math.PI) / 4;
                const length = 30;
                
                ctx.beginPath();
                ctx.moveTo(
                    config.sourcePos.x + Math.cos(angle) * 20,
                    config.sourcePos.y + Math.sin(angle) * 20
                );
                ctx.lineTo(
                    config.sourcePos.x + Math.cos(angle) * (20 + length),
                    config.sourcePos.y + Math.sin(angle) * (20 + length)
                );
                ctx.strokeStyle = 'rgba(241, 196, 15, 0.5)';
                ctx.lineWidth = 3;
                ctx.stroke();
            }
            
            // 绘制光谱图
            const spectrumX = canvas.width - 200;
            const spectrumY = 100;
            const spectrumWidth = 180;
            const spectrumHeight = 60;
            
            // 光谱背景
            ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
            ctx.fillRect(spect
rumX, spectrumY, spectrumWidth, spectrumHeight);
            
            // 发射光谱线（静止时）
            const lines = [400, 450, 500, 550, 600, 650, 700]; // 不同波长的谱线
            const receivedFreq = calculateReceivedFrequency();
            const freqRatio = receivedFreq / config.sourceFreq;
            
            for (let i = 0; i < lines.length; i++) {
                const originalPos = spectrumX + 20 + (i * 20);
                const shiftedPos = originalPos + (freqRatio - 1) * 50; // 红移/蓝移
                
                // 原始位置（灰色）
                ctx.beginPath();
                ctx.moveTo(originalPos, spectrumY + 10);
                ctx.lineTo(originalPos, spectrumY + spectrumHeight - 10);
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // 偏移后位置（颜色表示红移/蓝移）
                ctx.beginPath();
                ctx.moveTo(shiftedPos, spectrumY + 10);
                ctx.lineTo(shiftedPos, spectrumY + spectrumHeight - 10);
                ctx.strokeStyle = freqRatio > 1 ? '#3498db' : 
                                 freqRatio < 1 ? '#e74c3c' : '#2ecc71';
                ctx.lineWidth = 3;
                ctx.stroke();
                
                // 连接线
                ctx.beginPath();
                ctx.moveTo(originalPos, spectrumY + spectrumHeight/2);
                ctx.lineTo(shiftedPos, spectrumY + spectrumHeight/2);
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
                ctx.lineWidth = 1;
                ctx.setLineDash([2, 2]);
                ctx.stroke();
                ctx.setLineDash([]);
            }
            
            // 光谱标签
            ctx.fillStyle = '#ffffff';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('发射光谱', spectrumX + spectrumWidth/2, spectrumY - 5);
            ctx.fillText('接收光谱', spectrumX + spectrumWidth/2, spectrumY + spectrumHeight + 15);
            
            // 红移/蓝移标签
            if (freqRatio > 1.01) {
                ctx.fillStyle = '#3498db';
                ctx.fillText('蓝移', spectrumX + spectrumWidth + 30, spectrumY + spectrumHeight/2);
            } else if (freqRatio < 0.99) {
                ctx.fillStyle = '#e74c3c';
                ctx.fillText('红移', spectrumX + spectrumWidth + 30, spectrumY + spectrumHeight/2);
            }
        }

        // 动画循环
        function animate() {
            if (config.isPlaying) {
                config.time += 16; // 约60fps
                
                // 更新波源位置
                if (Math.abs(config.sourceSpeed) > 0.1) {
                    const deltaX = (config.sourceSpeed * 16) / 1000; // 转换为像素/帧
                    config.sourcePos.x += deltaX;
                    
                    // 边界检查
                    if (config.sourcePos.x < 50) config.sourcePos.x = 50;
                    if (config.sourcePos.x > canvas.width - 50) config.sourcePos.x = canvas.width - 50;
                    
                    // 记录轨迹
                    if (config.showTrajectory) {
                        config.trajectory.push({...config.sourcePos});
                        if (config.trajectory.length > 100) {
                            config.trajectory.shift();
                        }
                    }
                }
                
                // 生成新的波阵面
                if (config.time - config.lastWaveTime > config.waveInterval) {
                    const angle = Math.atan2(
                        config.observerPos.y - config.sourcePos.y,
                        config.observerPos.x - config.sourcePos.x
                    );
                    
                    config.wavefronts.push({
                        x: config.sourcePos.x,
                        y: config.sourcePos.y,
                        radius: 0,
                        time: config.time,
                        angle: angle
                    });
                    
                    config.lastWaveTime = config.time;
                }
                
                // 更新波阵面半径
                for (let i = config.wavefronts.length - 1; i >= 0; i--) {
                    const wave = config.wavefronts[i];
                    const age = config.time - wave.time;
                    wave.radius = (config.waveSpeed * age) / 1000; // 转换为像素
                    
                    // 移除太老的波
                    if (age > 3000) {
                        config.wavefronts.splice(i, 1);
                    }
                }
                
                // 限制波阵面数量
                if (!config.showHistory) {
                    while (config.wavefronts.length > 10) {
                        config.wavefronts.shift();
                    }
                }
                
                // 更新声音
                updateSound();
                
                // 更新UI数据
                updateDataDisplay();
            }
            
            draw();
            requestAnimationFrame(animate);
        }

        // 更新UI数据
        function updateDataDisplay() {
            const receivedFreq = calculateReceivedFrequency();
            const freqRatio = receivedFreq / config.sourceFreq;
            const shift = receivedFreq - config.sourceFreq;
            
            // 更新数据面板
            document.getElementById('dataSpeed').textContent = 
                `${config.sourceSpeed.toFixed(1)} m/s`;
            document.getElementById('dataEmitFreq').textContent = 
                `${config.sourceFreq} Hz`;
            document.getElementById('dataRecvFreq').textContent = 
                `${receivedFreq.toFixed(1)} Hz`;
            document.getElementById('dataFreqRatio').textContent = 
                freqRatio.toFixed(3);
            document.getElementById('dataShift').textContent = 
                `${shift.toFixed(1)} Hz`;
            
            // 更新公式显示
            const v = config.waveSpeed;
            const vs = config.sourceSpeed;
            const f0 = config.sourceFreq;
            
            // 计算相对速度分量
            const dx = config.observerPos.x - config.sourcePos.x;
            const dy = config.observerPos.y - config.sourcePos.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            let vs_proj = 0;
            
            if (distance > 0) {
                const directionX = dx / distance;
                vs_proj = vs * directionX;
            }
            
            let formulaText;
            if (vs_proj < 0) { // 接近
                formulaText = `f' = ${f0} × ${v} / (${v} + ${Math.abs(vs_proj).toFixed(1)}) = ${receivedFreq.toFixed(1)} Hz`;
            } else if (vs_proj > 0) { // 远离
                formulaText = `f' = ${f0} × ${v} / (${v} - ${vs_proj.toFixed(1)}) = ${receivedFreq.toFixed(1)} Hz`;
            } else {
                formulaText = `f' = ${f0} × ${v} / ${v} = ${receivedFreq.toFixed(1)} Hz`;
            }
            
            document.getElementById('currentFormula').textContent = `当前：${formulaText}`;
        }

        // 更新UI状态
        function updateUI() {
            // 更新场景按钮
            document.querySelectorAll('.scene-btn').forEach(btn => {
                btn.classList.toggle('active', btn.dataset.scene === config.scene);
            });
            
            // 更新滑块值显示
            document.getElementById('speedValue').textContent = config.sourceSpeed.toFixed(1);
            document.getElementById('speedDisplay').textContent = config.sourceSpeed.toFixed(1);
            document.getElementById('freqValue').textContent = config.sourceFreq;
            document.getElementById('freqDisplay').textContent = config.sourceFreq;
            
            // 更新复选框
            document.getElementById('showWavefronts').checked = config.showWavefronts;
            document.getElementById('showNormals').checked = config.showNormals;
            document.getElementById('showTrajectory').checked = config.showTrajectory;
            document.getElementById('showHistory').checked = config.showHistory;
            document.getElementById('enableSound').checked = config.enableSound;
            
            // 更新播放按钮
            document.getElementById('playPauseBtn').textContent = 
                config.isPlaying ? '⏸️ 暂停' : '▶️ 播放';
            
            // 更新标题
            document.querySelector('h1').textContent = 
                `${scenes[config.scene].name} - 多普勒效应`;
        }

        // 事件监听器
        function setupEventListeners() {
            // 场景切换
            document.querySelectorAll('.scene-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    config.scene = btn.dataset.scene;
                    updateWaveSpeed();
                    init();
                });
            });
            
            // 波源速度滑块
            document.getElementById('sourceSpeed').addEventListener('input', (e) => {
                config.sourceSpeed = parseFloat(e.target.value);
                document.getElementById('speedValue').textContent = config.sourceSpeed.toFixed(1);
                document.getElementById('speedDisplay').textContent = config.sourceSpeed.toFixed(1);
            });
            
            // 发射频率滑块
            document.getElementById('sourceFreq').addEventListener('input', (e) => {
                config.sourceFreq = parseFloat(e.target.value);
                document.getElementById('freqValue').textContent = config.sourceFreq;
                document.getElementById('freqDisplay').textContent = config.sourceFreq;
                
                // 更新声音频率
                if (oscillator && config.enableSound) {
                    oscillator.frequency.setValueAtTime(config.sourceFreq, audioContext.currentTime);
                }
            });
            
            // 复选框
            document.getElementById('showWavefronts').addEventListener('change', (e) => {
                config.showWavefronts = e.target.checked;
            });
            
            document.getElementById('showNormals').addEventListener('change', (e) => {
                config.showNormals = e.target.checked;
            });
            
            document.getElementById('showTrajectory').addEventListener('change', (e) => {
                config.showTrajectory = e.target.checked;
                if (!config.showTrajectory) {
                    config.trajectory = [];
                }
            });
            
            document.getElementById('showHistory').addEventListener('change', (e) => {
                config.showHistory = e.target.checked;
            });
            
            document.getElementById('enableSound').addEventListener('change', (e) => {
                config.enableSound = e.target.checked;
                toggleSound(config.enableSound);
            });
            
            // 播放/暂停按钮
            document.getElementById('playPauseBtn').addEventListener('click', () => {
                config.isPlaying = !config.isPlaying;
                document.getElementById('playPauseBtn').textContent = 
                    config.isPlaying ? '⏸️ 暂停' : '▶️ 播放';
            });
            
            // 重置按钮
            document.getElementById('resetBtn').addEventListener('click', () => {
                init();
            });
            
            // Canvas交互
            canvas.addEventListener('mousedown', (e) => {
                const rect = canvas.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                // 检查是否点击了波源
                const dx1 = x - config.sourcePos.x;
                const dy1 = y - config.sourcePos.y;
                const dist1 = Math.sqrt(dx1 * dx1 + dy1 * dy1);
                
                // 检查是否点击了观察者
                const dx2 = x - config.observerPos.x;
                const dy2 = y - config.observerPos.y;
                const dist2 = Math.sqrt(dx2 * dx2 + dy2 * dy2);
                
                if (dist1 < 20) {
                    config.draggedObject = 'source';
                } else if (dist2 < 20) {
                    config.draggedObject = 'observer';
                }
            });
            
            canvas.addEventListener('mousemove', (e) => {
                if (!config.draggedObject) return;
                
                const rect = canvas.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                if (config.draggedObject === 'source') {
                    config.sourcePos.x = Math.max(50, Math.min(canvas.width - 50, x));
                    config.sourcePos.y = Math.max(50, Math.min(canvas.height - 50, y));
                } else if (config.draggedObject === 'observer') {
                    config.observerPos.x = Math.max(50, Math.min(canvas.width - 50, x));
                    config.observerPos.y = Math.max(50, Math.min(canvas.height - 50, y));
                }
            });
            
            canvas.addEventListener('mouseup', () => {
                config.draggedObject = null;
            });
            
            canvas.addEventListener('mouseleave', () => {
                config.draggedObject = null;
            });
            
            // 触摸事件支持
            canvas.addEventListener('touchstart', (e) => {
                e.preventDefault();
                const touch = e.touches[0];
                const rect = canvas.getBoundingClientRect();
                const x = touch.clientX - rect.left;
                const y = touch.clientY - rect.top;
                
                const dx1 = x - config.sourcePos.x;
                const dy1 = y - config.sourcePos.y;
                const dist1 = Math.sqrt(dx1 * dx1 + dy1 * dy1);
                
                const dx2 = x - config.observerPos.x;
                const dy2 = y - config.observerPos.y;
                const dist2 = Math.sqrt(dx2 * dx2 + dy2 * dy2);
                
                if (dist1 < 30) {
                    config.draggedObject = 'source';
                } else if (dist2 < 30) {
                    config.draggedObject = 'observer';
                }
            });
            
            canvas.addEventListener('touchmove', (e) => {
                e.preventDefault();
                if (!config.draggedObject) return;
                
                const touch = e.touches[0];
                const rect = canvas.getBoundingClientRect();
                const x = touch.clientX - rect.left;
                const y = touch.clientY - rect.top;
                
                if (config.draggedObject === 'source') {
                    config.sourcePos.x = Math.max(50, Math.min(canvas.width - 50, x));
                    config.sourcePos.y = Math.max(50, Math.min(canvas.height - 50, y));
                } else if (config.draggedObject === 'observer') {
                    config.observerPos.x = Math.max(50, Math.min(canvas.width - 50, x));
                    config.observerPos.y = Math.max(50, Math.min(canvas.height - 50, y));
                }
            });
            
            canvas.addEventListener('touchend', () => {
                config.draggedObject = null;
            });
        }

        // 初始化应用
        window.addEventListener('load', () => {
            setupEventListeners();
            init();
        });
    </script>
</body>
</html>

### 3. 过程输出


## 《多普勒效应交互式教学动画使用指南》

欢迎使用这款精心设计的“多普勒效应”交互式教学动画！本工具旨在通过直观、动态的可视化与深度交互，帮助您透彻理解声波与光波中多普勒效应的核心原理。无论您是教师、学生还是物理爱好者，相信它都能为您带来启发性的学习体验。

---

### **一、 功能说明**

本动画是一个基于HTML5 Canvas构建的完整模拟环境，集成了四种学习场景：
1.  **声波模拟**：基础场景，展示机械波在介质中传播时，因波源运动而产生的波前疏密变化。
2.  **光波模拟**：进阶场景，展示电磁波（光）的多普勒效应，引入“红移”与“蓝移”的视觉概念。
3.  **警车示例**：应用场景一，模拟日常生活中警车鸣笛驶过时，观察者听到的音高变化。
4.  **宇宙红移**：应用场景二，模拟天体物理学中恒星远离地球时，其光谱发生的特征性红移现象。

所有场景共享同一套物理引擎和控制逻辑，确保原理的一致性。

---

### **二、 主要功能**

您可以通过以下方式与动画深度互动：

*   **场景自由切换**：点击顶部控制面板的四个场景按钮，瞬间在不同物理情境间切换，对比学习。
*   **实体动态操控**：
    *   **拖拽放置**：直接用鼠标（或手指）在画布上拖拽**黄色波源**或**绿色观察者**，改变它们的相对位置。
    *   **速度调节**：使用“波源速度”滑块，实时控制波源的运动速度与方向（正值向右/远离，负值向左/接近）。
    *   **频率调节**：使用“发射频率”滑块，改变波源发出的原始频率。
*   **视觉辅助图层**：通过复选框，可独立控制以下视觉元素的显示与隐藏：
    *   `显示波阵面`：核心动画，展示波从源点向外扩散的过程。
    *   `显示波前法线`：显示波的传播方向。
    *   `显示运动轨迹`：显示波源的历史路径。
    *   `显示历史波`：保留更多过去的波阵面，观察波的传播延时效应。
    *   `启用声音反馈`（仅声波/警车场景）：开启后，观察者位置会根据接收到的频率播放相应音调，提供听觉感知。
*   **动画流程控制**：
    *   `播放/暂停`：控制模拟过程的运行与停止，便于仔细观察。
    *   `重置`：一键将模拟恢复至当前场景的初始状态。
*   **数据实时监测**：右侧数据面板实时显示所有关键物理量，包括波源速度、波速、发射/接收频率、频率变化比及多普勒频移量。公式区域会动态代入当前数值，展示计算过程。

---

### **三、 设计特色**

1.  **双通道感知强化**：
    *   **视觉**：采用**蓝-红**色彩编码。蓝色区域表示波前密集（高频/蓝移），红色区域表示波前稀疏（低频/红移），与物理学惯例一致，直观醒目。
    *   **听觉**（可选）：将频率变化转化为可闻的音高变化，实现视听联动，加深理解。

2.  **分层渐进式教学**：
    *   从最直观的**声波**（圆形波）入手，建立“运动导致疏密变化”的物理图像。
    *   过渡到**光波**，引入“颜色代表频率”的概念，自然衔接至“红移蓝移”术语。
    *   最后通过**警车**和**宇宙**两个具体应用案例，将抽象原理与现实世界、前沿科学连接。

3.  **专业级视觉呈现**：
    *   不同场景拥有专属的背景与视觉风格（如宇宙场景的星空、恒星光芒和动态光谱图）。
    *   界面采用深色主题，降低视觉疲劳，并突出核心动画元素。
    *   所有控件布局清晰，符合操作逻辑。

---

### **四、 教学要点**

建议按照以下顺序引导学习或自主探索：

1.  **观察现象**（声波场景）：
    *   将波源速度设为0，观察同心圆波如何均匀扩散。
    *   缓慢增加波源速度（正值），观察波在**运动方向**如何被“挤压”（变密、变蓝），在**反方向**如何被“拉伸”（变疏、变红）。
    *   注意观察者处的**频率指示条**和**数据变化**。

2.  **理解原理**：
    *   开启“显示历史波”和“显示运动轨迹”，理解波传播的**延时性**：波从不同位置发出，但都以固定波速传播。
    *   解释为什么波前密集意味着观察者单位时间内接收到的波更多（频率变高），反之亦然。

3.  **知识迁移**（光波场景）：
    *   切换至光波场景，强调原理完全相同，只是波的类型不同。
    *   指出颜色变化直接对应光的频率变化：向蓝紫色移动即频率升高（蓝移），向橙红色移动即频率降低（红移）。

4.  **公式关联**：
    *   在操作的同时，引导学生关注数据面板中“当前公式”一栏。通过改变波源速度或相对位置，观察公式中变量如何变化，结果如何计算得出。

5.  **应用拓展**：
    *   在“警车示例”中，重现经典的生活体验，将理论具象化。
    *   在“宇宙红移”中，展示光谱线的移动，解释这是天文学家测量天体速度、发现宇宙膨胀的关键证据。

---

### **五、 使用建议**

*   **给教师的建议**：
    *   **课堂演示**：可连接投影仪，作为讲解多普勒效应核心概念的动态板书。通过拖拽和调节参数，即时响应学生提问。
    *   **探究任务**：可给学生布置探索性任务，例如：“请设置参数，使观察者接收到的频率恰好是发射频率的两倍”，或“解释为什么在宇宙场景中，即使波源横向运动，也会产生微小的频率变化？”
    *   **分组讨论**：让学生操作并描述现象，促进主动建构知识。

*   **给学习者的建议**：
    *   **大胆尝试**：不要害怕“调乱”参数。通过反复拖拽、滑动、开关各种选项，观察变化，是理解物理规律的最佳途径。
    *   **先现象后数据**：先专注于动画的视觉表现，形成直观印象，再去解读数据和公式。
    *   **对比学习**：在声波和光波场景间来回切换，思考它们的**相同点**（核心原理）和**不同点**（介质需求、表现方式）。

*   **技术提示**：
    *   本动画为单HTML文件，无需网络连接即可运行，方便在多种环境下使用。
    *   支持触控操作，可在平板电脑上获得良好体验。
    *   首次启用“声音反馈”时，浏览器可能会要求用户交互（如点击页面）后才允许播放音频，这是浏览器的安全策略，请按提示操作。

---

希望这份指南能帮助您充分利用这个交互式工具，揭开多普勒效应的奥秘，享受探索物理规律的乐趣！祝您教学顺利，学习愉快！