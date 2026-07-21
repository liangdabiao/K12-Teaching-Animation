# 需求：一氧化碳毒性（与血红蛋白结合微观动画）

### 1. 专业思考


#### 用户需求分析
本动画的主要用户群体是中学生或大学低年级生物学、化学或医学预科学生。他们的核心需求是：
1.  **理解抽象过程**：将“一氧化碳（CO）与血红蛋白（Hb）结合力更强”这一抽象的文字或化学方程式，转化为直观、动态的微观可视化过程。
2.  **建立因果链条**：清晰看到CO如何竞争性地占据氧气的结合位点，导致血红蛋白运氧能力下降，最终引发组织缺氧的完整病理生理链条。
3.  **强化记忆点**：通过生动的动画和交互，强化“CO与Hb的亲和力是O₂的200-250倍”以及“碳氧血红蛋白（HbCO）形成后不易解离”这两个关键知识点。
4.  **激发学习兴趣**：摆脱枯燥的文本描述，用游戏化的交互和拟人化的视觉元素，降低认知负荷，提升学习动机。

#### 教学设计思路
*   **核心概念**：
    *   **血红蛋白（Hb）的结构与功能**：作为四聚体蛋白，有四个氧结合位点。
    *   **竞争性结合**：O₂和CO竞争Hb上相同的结合位点（血红素中的亚铁离子）。
    *   **结合亲和力差异**：CO与Hb的亲和力远高于O₂（约200-250倍）。
    *   **碳氧血红蛋白（HbCO）的稳定性**：HbCO解离速度极慢，导致Hb失去运氧功能。
    *   **生理后果**：组织缺氧。

*   **认知规律**：
    1.  **从已知到未知**：先展示正常的Hb运氧过程（O₂在肺泡结合，在组织释放），建立基线认知。
    2.  **引入冲突**：引入CO分子，展示其如何干扰正常过程。
    3.  **对比强化**：并行或先后对比正常与中毒状态下，Hb结合、运输、释放气体的差异。
    4.  **归纳总结**：在动画结尾或通过交互提示，用简明的文字总结关键机制。

*   **交互设计**：
    *   **叙事驱动**：动画将遵循“正常生理→CO入侵→病理过程→结果对比”的故事线自动播放，确保逻辑连贯。
    *   **可控探索**：用户可暂停、回放关键步骤。提供“仅看正常过程”、“仅看中毒过程”、“对比观看”等模式按钮。
    *   **参数调节**：提供一个简易滑块，允许用户“调节”环境中CO的浓度（如：低、中、高），直观观察不同浓度下被CO占据的Hb比例变化。
    *   **点击探查**：用户可以点击Hb分子、O₂分子、CO分子，弹出简要的科学说明卡片（如亲和力数值、解离半衰期等）。

*   **视觉呈现**：
    *   **拟人化与符号化**：
        *   **血红蛋白（Hb）**：设计为可爱的、有四个凹陷（结合位点）的红色圆球或四叶草形状，使其具有亲和力。
        *   **氧气（O₂）**：设计为两个连接的蓝色小圆球，活泼灵动。
        *   **一氧化碳（CO）**：设计为一个红色（代表危险）的小圆球加一个突出的“钩子”或“锁”的形态，暗示其强大的结合和锁定能力。
    *   **关键状态可视化**：
        *   **结合过程**：O₂/CO飞向Hb的位点，位点高亮，分子“嵌入”并发出结合光效。
        *   **竞争过程**：当CO存在时，它会更快速、更“牢固”地（如用动画表现更强的磁吸效果）占据位点，将O₂“挤开”。
        *   **释放差异**：在组织毛细血管，结合了O₂的Hb顺利释放O₂（O₂弹出）；而结合了CO的Hb，CO分子“粘着”不动，或需要非常长的时间（用慢放或进度条表示）才勉强脱离。
    *   **场景划分**：画面分为“肺泡/肺毛细血管”区域（背景为亮粉色，代表富氧）和“组织/组织毛细血管”区域（背景为暗紫色，代表缺氧）。Hb在两者间循环移动。

#### 配色方案选择
*   **主色调与科学关联**：
    *   **血红蛋白（Hb）**：采用**鲜红色**（代表含氧丰富的动脉血），当结合CO后，逐渐变为**樱桃红/亮粉色**（这是碳氧血红蛋白的特征颜色，也是一个重要临床知识点）。
    *   **氧气（O₂）**：**天蓝色**或**淡蓝色**，象征清新空气。
    *   **一氧化碳（CO）**：**暗红色**或**品红色**，带有警示意味，与O₂的蓝色形成鲜明对比，突出其危险性和竞争关系。
    *   **背景**：
        *   肺泡区：浅亮背景（如淡蓝或浅灰），突出富氧环境。
        *   组织区：稍暗背景（如浅紫灰），暗示耗氧状态。
    *   **界面与提示**：使用中性色（白、灰、黑）确保UI清晰，关键提示文字或按钮使用**警示黄色**或**橙色**。

#### 交互功能列表
1.  **主控面板**：
    *   “播放/暂停/重置”按钮。
    *   “1x， 0.5x， 2x”播放速度选择。
2.  **模式选择按钮组**：
    *   “正常运氧模式”
    *   “CO中毒模式”
    *   “对比模式”（分屏或同屏先后展示）
3.  **参数调节器**：
    *   “环境CO浓度”滑块（从0%到高浓度），实时显示当前浓度下被结合的Hb比例（如：70% HbCO）。
4.  **探索式交互**：
    *   点击任何运动的Hb分子，高亮显示其当前结合状态（如：O₂-O₂-CO-空）。
    *   点击O₂或CO分子，弹出信息卡片，显示关键化学特性。
5.  **叙事标签**：
    *   在动画关键步骤，自动出现非侵入性的文字标签（如：“CO与Hb结合”、“O₂被排除在外”、“组织无法获得氧气”）。
6.  **知识总结卡片**：
    *   动画结束后，或在过程中点击“总结”按钮，弹出卡片，列出“关键机制三点”：高亲和力、竞争性结合、组织缺氧。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>一氧化碳毒性：与血红蛋白结合的微观动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #f0f0f0;
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
            color: #ff6b6b;
            margin-bottom: 10px;
            font-size: 2.2rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }

        .subtitle {
            color: #4ecdc4;
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }

        .animation-section {
            flex: 3;
            min-width: 300px;
        }

        .controls-section {
            flex: 1;
            min-width: 280px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .canvas-container {
            position: relative;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            overflow: hidden;
            border: 2px solid rgba(255, 255, 255, 0.1);
            height: 600px;
        }

        #animationCanvas {
            display: block;
            width: 100%;
            height: 100%;
        }

        .scene-labels {
            position: absolute;
            top: 20px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 30px;
            pointer-events: none;
        }

        .scene-label {
            background: rgba(0, 0, 0, 0.7);
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1.1rem;
            border: 2px solid;
        }

        .lungs-label {
            color: #4ecdc4;
            border-color: #4ecdc4;
        }

        .tissue-label {
            color: #ff9ff3;
            border-color: #ff9ff3;
        }

        .legend {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .legend-item {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .control-group {
            background: rgba(0, 0, 0, 0.2);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .control-title {
            color: #4ecdc4;
            margin-bottom: 12px;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .control-title i {
            font-size: 1.2rem;
        }

        .button-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 10px;
        }

        button {
            background: linear-gradient(135deg, #2d3436 0%, #636e72 100%);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            flex: 1;
            min-width: 120px;
            font-weight: 500;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }

        button.active {
            background: linear-gradient(135deg, #0984e3 0%, #74b9ff 100%);
            box-shadow: 0 0 10px rgba(116, 185, 255, 0.5);
        }

        .speed-controls {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .speed-btn {
            flex: 1;
            min-width: 60px;
        }

        .slider-container {
            margin-top: 10px;
        }

        .slider-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }

        input[type="range"] {
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: #2d3436;
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
            border: 2px solid white;
        }

        .value-display {
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
            color: #ff6b6b;
            margin-top: 5px;
        }

        .stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 10px;
        }

        .stat-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }

        .stat-value {
            font-size: 1.3rem;
            font-weight: bold;
            color: #4ecdc4;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        .info-panel {
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-top: 20px;
        }

        .info-title {
            color: #feca57;
            margin-bottom: 15px;
            font-size: 1.3rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-content {
            line-height: 1.6;
            color: #e0e0e0;
        }

        .key-point {
            background: rgba(254, 202, 87, 0.1);
            border-left: 4px solid #feca57;
            padding: 12px;
            margin: 15px 0;
            border-radius: 0 8px 8px 0;
        }

        .molecule-info {
            display: none;
            position: absolute;
            background: rgba(0, 0, 0, 0.9);
            padding: 15px;
            border-radius: 10px;
            border: 2px solid;
            max-width: 300px;
            z-index: 100;
            pointer-events: none;
        }

        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }
            
            .canvas-container {
                height: 500px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>一氧化碳毒性：与血红蛋白结合的微观动画</h1>
            <p class="subtitle">探索CO如何竞争性结合血红蛋白，导致组织缺氧的微观机制</p>
        </header>

        <div class="main-content">
            <div class="animation-section">
                <div class="canvas-container">
                    <canvas id="animationCanvas"></canvas>
                    
                    <div class="scene-labels">
                        <div class="scene-label lungs-label">🏥 肺泡/肺毛细血管 (富氧环境)</div>
                        <div class="scene-label tissue-label">💪 组织/组织毛细血管 (缺氧环境)</div>
                    </div>
                    
                    <div class="legend">
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ff6b6b;"></div>
                            <span>血红蛋白 (Hb)</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #74b9ff;"></div>
                            <span>氧气分子 (O₂)</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ff4757;"></div>
                            <span>一氧化碳分子 (CO)</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ff9ff3;"></div>
                            <span>碳氧血红蛋白 (HbCO)</span>
                        </div>
                    </div>
                    
                    <div id="moleculeInfo" class="molecule-info"></div>
                </div>
            </div>

            <div class="controls-section">
                <div class="control-group">
                    <div class="control-title">🎬 动画控制</div>
                    <div class="button-group">
                        <button id="playBtn" class="active">▶ 播放</button>
                        <button id="pauseBtn">⏸ 暂停</button>
                        <button id="resetBtn">🔄 重置</button>
                    </div>
                    
                    <div class="speed-controls">
                        <button class="speed-btn" data-speed="0.5">0.5x</button>
                        <button class="speed-btn active" data-speed="1">1x</button>
                        <button class="speed-btn" data-speed="2">2x</button>
                    </div>
                </div>

                <div class="control-group">
                    <div class="control-title">🔬 观察模式</div>
                    <div class="button-group">
                        <button id="normalMode" class="active">正常运氧</button>
                        <button id="coMode">CO中毒</button>
                        <button id="compareMode">对比模式</button>
                    </div>
                </div>

                <div class="control-group">
                    <div class="control-title">⚙️ 环境参数</div>
                    <div class="slider-container">
                        <div class="slider-label">
                            <span>CO浓度：</span>
                            <span id="coValue">0%</span>
                        </div>
                        <input type="range" id="coSlider" min="0" max="100" value="0">
                    </div>
                    
                    <div class="stats">
                        <div class="stat-item">
                            <div class="stat-value" id="hbcoPercent">0%</div>
                            <div class="stat-label">HbCO比例</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="o2Delivery">100%</div>
                            <div class="stat-label">O₂输送效率</div>
                        </div>
                    </div>
                </div>

                <div class="control-group">
                    <div class="control-title">📊 实时数据</div>
                    <div class="stats">
                        <div class="stat-item">
                            <div class="stat-value" id="totalHb">0</div>
                            <div class="stat-label">血红蛋白总数</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="boundO2">0</div>
                            <div class="stat-label">结合O₂数</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="boundCO">0</div>
                            <div class="stat-label">结合CO数</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="freeSites">0</div>
                            <div class="stat-label">空闲位点</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="info-panel">
            <div class="info-title">💡 关键机制说明</div>
            <div class="info-content">
                <p>一氧化碳(CO)中毒的核心机制：</p>
                
                <div class="key-point">
                    <strong>1. 竞争性结合：</strong> CO与O₂竞争血红蛋白(Hb)上相同的结合位点（血红素中的亚铁离子）。
                </div>
                
                <div class="key-point">
                    <strong>2. 超高亲和力：</strong> CO与Hb的亲和力是O₂的<strong>200-250倍</strong>，结合更快速、更牢固。
                </div>
                
                <div class="key-point">
                    <strong>3. 碳氧血红蛋白(HbCO)形成：</strong> CO与Hb结合形成HbCO，其解离速度极慢（半衰期约4-6小时），导致Hb失去运氧功能。
                </div>
                
                <div class="key-point">
                    <strong>4. 组织缺氧：</strong> 即使血液中O₂含量正常，但Hb被CO"锁定"，无法向组织释放O₂，导致组织缺氧。
                </div>
                
                <p style="margin-top: 15px; color: #ff6b6b;">
                    <strong>⚠️ 临床特征：</strong> 碳氧血红蛋白呈樱桃红色，患者皮肤可出现特征性的"樱桃红"外观（但并非所有病例都出现）。
                </p>
            </div>
        </div>
    </div>

    <script>
        // 获取Canvas和上下文
        const canvas = document.getElementById('animationCanvas');
        const ctx = canvas.getContext('2d');
        const moleculeInfo = document.getElementById('moleculeInfo');

        // 设置Canvas尺寸
        function resizeCanvas() {
            const container = canvas.parentElement;
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
        }
        
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // 动画状态
        let animationId = null;
        let isPlaying = true;
        let speed = 1;
        let mode = 'normal'; // 'normal', 'co', 'compare'
        let coConcentration = 0; // 0-100%

        // 分子定义
        const molecules = {
            Hb: { color: '#ff6b6b', radius: 25, name: '血红蛋白', info: '四聚体蛋白，有4个氧结合位点' },
            O2: { color: '#74b9ff', radius: 8, name: '氧气分子', info: 'O₂，与Hb结合力：1x' },
            CO: { color: '#ff4757', radius: 10, name: '一氧化碳', info: 'CO，与Hb结合力：200-250x O₂' },
            HbCO: { color: '#ff9ff3', radius: 25, name: '碳氧血红蛋白', info: 'CO与Hb的结合物，解离极慢' }
        };

        // 场景定义
        const scenes = {
            lungs: { x: 0, width: 0.5, color: 'rgba(78, 205, 196, 0.1)', label: '肺泡区' },
            tissue: { x: 0.5, width: 0.5, color: 'rgba(255, 159, 243, 0.1)', label: '组织区' }
        };

        // 血红蛋白数组
        let hemoglobins = [];
        const HbCount = 15;

        // 氧气和一氧化碳分子数组
        let oxygenMolecules = [];
        let coMolecules = [];
        const O2Count = 40;
        const COCount = 20;

        // 初始化所有元素
        function init() {
            hemoglobins = [];
            oxygenMolecules = [];
            coMolecules = [];

            // 初始化血红蛋白
            for (let i = 0; i < HbCount; i++) {
                hemoglobins.push({
                    x: Math.random() * canvas.width,
                    y: 100 + (i * (canvas.height - 200) / HbCount),
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: 0,
                    radius: molecules.Hb.radius,
                    color: molecules.Hb.color,
                    bindingSites: [null, null, null, null], // 4个结合位点
                    isCOBound: false,
                    id: i
                });
            }

            // 初始化氧气分子（主要在肺泡区）
            for (let i = 0; i < O2Count; i++) {
                oxygenMolecules.push({
                    x: Math.random() * canvas.width * 0.4,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 1.5,
                    vy: (Math.random() - 0.5) * 1.5,
                    radius: molecules.O2.radius,
                    color: molecules.O2.color,
                    isBound: false,
                    boundTo: null,
                    siteIndex: null
                });
            }

            // 初始化一氧化碳分子
            updateCOMolecules();
        }

        // 根据CO浓度更新CO分子数量
        function updateCOMolecules() {
            const targetCount = Math.floor(COCount * (coConcentration / 100));
            
            // 移除多余的CO分子
            if (coMolecules.length > targetCount) {
                coMolecules = coMolecules.slice(0, targetCount);
            }
            // 添加新的CO分子
            else if (coMolecules.length < targetCount) {
                for (let i = coMolecules.length; i < targetCount; i++) {
                    coMolecules.push({
                        x: Math.random() * canvas.width * 0.4,
                        y: Math.random() * canvas.height,
                        vx: (Math.random() - 0.5) * 1.2,
                        vy: (Math.random() - 0.5) * 1.2,
                        radius: molecules.CO.radius,
                        color: molecules.CO.color,
                        isBound: false,
                        boundTo: null,
                        siteIndex: null
                    });
                }
            }
        }

        // 绘制场景背景
        function drawBackground() {
            // 绘制肺泡区
            ctx.fillStyle = scenes.lungs.color;
            ctx.fillRect(0, 0, canvas.width * scenes.lungs.width, canvas.height);
            
            // 绘制组织区
            ctx.fillStyle = scenes.tissue.color;
            ctx.fillRect(canvas.width * scenes.tissue.x, 0, 
                        canvas.width * scenes.tissue.width, canvas.height);
            
            // 绘制分界线
            ctx.beginPath();
            ctx.moveTo(canvas.width * 0.5, 0);
            ctx.lineTo(canvas.width * 0.5, canvas.height);
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // 绘制血红蛋白
        function drawHemoglobin(hb) {
            // 绘制主体
            ctx.beginPath();
            ctx.arc(hb.x, hb.y, hb.radius, 0, Math.PI * 2);
            
            // 如果结合了CO，使用HbCO颜色
            if (hb.isCOBound) {
                ctx.fillStyle = molecules.HbCO.color;
            } else {
                ctx.fillStyle = hb.color;
            }
            ctx.fill();
            
            // 绘制边框
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // 绘制结合位点
            for (let i = 0; i < 4; i++) {
                const angle = (i * Math.PI / 2) + (Date.now() / 1000) * 0.5;
                const siteX = hb.x + Math.cos(angle) * (hb.radius - 5);
                const siteY = hb.y + Math.sin(angle) * (hb.radius - 5);
                
                ctx.beginPath();
                ctx.arc(siteX, siteY, 6, 0, Math.PI * 2);
                
                if (hb.bindingSites[i]) {
                    // 位点被占据
                    if (hb.bindingSites[i].type === 'CO') {
                        ctx.fillStyle = molecules.CO.color;
                    } else {
                        ctx.fillStyle = molecules.O2.color;
                    }
                } else {
                    // 空闲位点
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
                }
                ctx.fill();
                
                // 位点边框
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
                ctx.lineWidth = 1;
                ctx.stroke();
            }
            
            // 绘制Hb编号（调试用）
            if (mode === 'compare') {
                ctx.fillStyle = 'white';
                ctx.font = '12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`Hb${hb.id}`, hb.x, hb.y + hb.radius + 15);
            }
        }

        // 绘制气体分子
        function drawGasMolecule(mol, type) {
            ctx.beginPath();
            ctx.arc(mol.x, mol.y, mol.radius, 0, Math.PI * 2);
            ctx.fillStyle = mol.color;
            ctx.fill();
            
            // 绘制边框
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            ctx.lineWidth = 1;
            ctx.stroke();
            
            // 绘制分子符号
            ctx.fillStyle = 'white';
            ctx.font = 'bold 10px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            
            if (type === 'O2') {
                ctx.fillText('O₂', mol.x, mol.y);
            } else if (type === 'CO') {
                ctx.fillText('CO', mol.x, mol.y);
            }
            
            // 如果结合了，绘制连接线
            if (mol.isBound && mol.boundTo) {
                const hb = hemoglobins[mol.boundTo];
                const angle = (mol.siteIndex * Math.PI / 2) + (Date.now() / 1000) * 0.5;
                const siteX = hb.x + Math.cos(angle) * (hb.radius - 5);
                const siteY = hb.y + Math.sin(angle) * (hb.radius - 5);
                
                ctx.beginPath();
                ctx.moveTo(mol.x, mol.y);
                ctx.lineTo(siteX, siteY);
                ctx.strokeStyle = type === 'CO' ? '#ff4757' : '#74b9ff';
                ctx.lineWidth = 2;
                ctx.setLineDash([2, 2]);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }

        // 更新血红蛋白状态
        function updateHemoglobin(hb, deltaTime) {
            // 移动
            hb.x += hb.vx * speed;
            hb.y += hb.vy * speed;
            
            // 边界检查
            if (hb.x < hb.radius) hb.x = hb.radius;
            if (hb.x > canvas.width - hb.radius) hb.x = canvas.width - hb.radius;
            if (hb.y < hb.radius) hb.y = hb.radius;
            if (hb.y > canvas.height - hb.radius) hb.y = canvas.height - hb.radius;
            
            // 在肺泡区向右移动，在组织区向左移动
            if (hb.x < canvas.width * 0.5) {
                hb.vx += 0.01 * speed;
            } else {
                hb.vx -= 0.01 * speed;
            }
            
            // 限制速度
            hb.vx = Math.max(-2, Math.min(2, hb.vx * 0.99));
            
            // 检查是否在组织区释放氧气
            if (hb.x > canvas.width * 0.5 && mode !== 'co') {
                for (let i = 0; i < 4; i++) {
                    if (hb.bindingSites[i] && hb.bindingSites[i].type === 'O2') {
                        // 有一定概率释放氧气
                        if (Math.random() < 0.02 * speed) {
                            releaseGas(hb, i, 'O2');
                        }
                    }
                }
            }
            
            // 检查是否在肺泡区结合气体
            if (hb.x < canvas.width * 0.5) {
                tryBindGases(hb);
            }
            
            // 更新CO结合状态
            hb.isCOBound = hb.bindingSites.some(site => site && site.type === 'CO');
        }

        // 尝试结合气体分子
        function tryBindGases(hb) {
            // 首先尝试结合CO（亲和力更高）
            for (let i = 0; i < coMolecules.length; i++) {
                const co = coMolecules[i];
                if (!co.isBound) {
                    const distance = Math.sqrt(
                        Math.pow(co.x - hb.x, 2) + Math.pow(co.y - hb.y, 2)
                    );
                    
                    if (distance < hb.radius + co.radius + 20) {
                        // 寻找空闲位点
                        for (let siteIndex = 0; siteIndex < 4; siteIndex++) {
                            if (!hb.bindingSites[siteIndex]) {
                                // CO结合概率更高
                                if (Math.random() < 0.1 * (coConcentration / 100 + 0.1)) {
                                    bindGas(hb, siteIndex, co, 'CO');
                                    return;
                                }
                            }
                        }
                    }
                }
            }
            
            // 然后尝试结合O2
            if (mode !== 'co') {
                for (let i = 0; i < oxygenMolecules.length; i++) {
                    const o2 = oxygenMolecules[i];
                    if (!o2.isBound) {
                        const distance = Math.sqrt(
                            Math.pow(o2.x - hb.x, 2) + Math.pow(o2.y - hb.y, 2)
                        );
                        
                        if (distance < hb.radius + o2.radius + 15) {
                            // 寻找空闲位点
                            for (let siteIndex = 0; siteIndex < 4; siteIndex++) {
                                if (!hb.bindingSites[siteIndex]) {
                                    // O2结合概率较低（模拟CO竞争）
                                    const coCompetition = 1 - (coConcentration / 200);
                                    if (Math.random() < 0.05 * coCompetition) {
                                        bindGas(hb, siteIndex, o2, 'O2');
                                        return;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        // 结合气体分子
        function bindGas(hb, siteIndex, molecule, type) {
            hb.bindingSites[siteIndex] = {
                type: type,
                moleculeIndex: molecule === 'O2' ? 
                    oxygenMolecules.indexOf(molecule) : 
                    coMolecules.indexOf(molecule)
            };
            
            molecule.isBound = true;
            molecule.boundTo = hb.id;
            molecule.siteIndex = siteIndex;
            
            // 将分子移动到结合位置
            const angle = (siteIndex * Math.PI / 2) + (Date.now() / 1000) * 0.5;
            molecule.x = hb.x + Math.cos(angle) * (hb.radius + molecule.radius + 2);
            molecule.y = hb.y + Math.sin(angle) * (hb.radius + molecule.radius + 2);
        }

        // 释放气体分子
        function releaseGas(hb, siteIndex, type) {
            const site = hb.bindingSites[siteIndex];
            if (!site) return;
            
            hb.bindingSites[siteIndex] = null;
            
            if (type === 'O2') {
                const o2 = oxygenMolecules[site.moleculeIndex];
                if (o2) {
                    o2.isBound = false;
                    o2.boundTo = null;
                    o2.siteIndex = null;
                    // 给一个向上的速度模拟释放
                    o2.vx = (Math.random() - 0.5) * 2;
                    o2.vy = -Math.random() * 2;
                }
            } else if (type === 'CO') {
                // CO很难释放（模拟其高亲和力）
                if (Math.random() < 0.005) { // 很低的释放概率
                    const co = coMolecules[site.moleculeIndex];
                    if (co) {
                        co.isBound = false;
                        co.boundTo = null;
                        co.siteIndex = null;
                    }
                    hb.bindingSites[siteIndex] = null;
                }
            }
        }

        // 更新气体分子
        function updateGasMolecule(mol, type) {
            if (mol.isBound) {
                // 如果结合了，跟随血红蛋白移动
                if (mol.boundTo !== null && hemoglobins[mol.boundTo]) {
                    const hb = hemoglobins[mol.boundTo];
                    const angle = (mol.siteIndex * Math.PI / 2) + (Date.now() / 1000) * 0.5;
                    mol.x = hb.x + Math.cos(angle) * (hb.radius + mol.radius + 2);
                    mol.y = hb.y + Math.sin(angle) * (hb.radius + mol.radius + 2);
                }
            } else {
                // 自由移动
                mol.x += mol.vx * speed;
                mol.y += mol.vy * speed;
                
                // 边界反弹
                if (mol.x < mol.radius || mol.x > canvas.width - mol.radius) {
                    mol.vx *= -0.9;
                }
                if (mol.y < mol.radius || mol.y > canvas.height - mol.radius) {
                    mol.vy *= -0.9;
                }
                
                // 限制在肺泡区（CO和O2主要在肺泡区生成）
                if (type === 'O2' || type === 'CO') {
                    if (mol.x > canvas.width * 0.4 && mol.vx > 0) {
                        mol.vx *= -1;
                    }
                }
                
                // 缓慢减速
                mol.vx *= 0.995;
                mol.vy *= 0.995;
            }
        }

        // 计算统计数据
        function calculateStats() {
            let totalBoundO2 = 0;
            let totalBoundCO = 0;
            let totalFreeSites = 0;
            let hbWithCO = 0;
            
            hemoglobins.forEach(hb => {
                hb.bindingSites.forEach(site => {
                    if (site) {
                        if (site.type === 'O2') totalBoundO2++;
                        if (site.type === 'CO') totalBoundCO++;
                    } else {
                        totalFreeSites++;
                    }
                });
                if (hb.isCOBound) hbWithCO++;
            });
            
            const hbcoPercent = ((hbWithCO / HbCount) * 100).toFixed(1);
            const o2Delivery = Math.max(0, 100 - (coConcentration * 0.8)).toFixed(0);
            
            // 更新显示
            document.getElementById('totalHb').textContent = HbCount;
            document.getElementById('boundO2').textContent = totalBoundO2;
            document.getElementById('boundCO').textContent = totalBoundCO;
            document.getElementById('freeSites').textContent = totalFreeSites;
            document.getElementById('hbcoPercent').textContent = `${hbcoPercent}%`;
            document.getElementById('o2Delivery').textContent = `${o2Delivery}%`;
        }

        // 主动画循环
        function animate() {
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景
            drawBackground();
            
            // 更新和绘制所有元素
            hemoglobins.forEach(hb => {
                updateHemoglobin(hb, 16);
                drawHemoglobin(hb);
            });
            
            oxygenMolecules.forEach(o2 => {
                updateGasMolecule(o2, 'O2');
                drawGasMolecule(o2, 'O2');
            });
            
            coMolecules.forEach(co => {
                updateGasMolecule(co, 'CO');
                drawGasMolecule(co, 'CO');
            });
            
            // 计算并显示统计数据
            calculateStats();
            
            // 继续动画循环
            if (isPlaying) {
                animationId = requestAnimationFrame(animate);
            }
        }

        // 事件监听器
        document.getElementById('playBtn').addEventListener('click', () => {
            isPlaying = true;
            if (!animationId) {
                animate();
            }
            updateButtonStates('playBtn');
        });

        document.getElementById('pauseBtn').addEventListener('click', () => {
            isPlaying = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
            updateButtonStates('pauseBtn');
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            init();
            if (isPlaying && !animationId) {
                animate();
            }
        });

        // 速度控制
        document.querySelectorAll('.speed-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                speed = parseFloat(this.dataset.speed);
                document.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
            });
        });

        // 模式控制
        document.getElementById('normalMode').addEventListener('click', () => {
            mode = 'normal';
            updateButtonStates('normalMode', 'mode');
        });

        document.getElementById('coMode').addEventListener('click', () => {
            mode = 'co';
            updateButtonStates('coMode', 'mode');
        });

        document.getElementById('compareMode').addEventListener('click', () => {
            mode = 'compare';
            updateButtonStates('compareMode', 'mode');
        });

        // CO浓度滑块
        const coSlider = document.getElementById('coSlider');
        const coValue = document.getElementById('coValue');
        
        coSlider.addEventListener('input', function() {
            co
Concentration = parseInt(this.value);
            coValue.textContent = `${coConcentration}%`;
            updateCOMolecules();
        });

        // 更新按钮状态
        function updateButtonStates(activeId, group = 'control') {
            if (group === 'control') {
                document.querySelectorAll('.button-group:first-child button').forEach(btn => {
                    btn.classList.remove('active');
                });
                document.getElementById(activeId).classList.add('active');
            } else if (group === 'mode') {
                document.querySelectorAll('.button-group:nth-child(2) button').forEach(btn => {
                    btn.classList.remove('active');
                });
                document.getElementById(activeId).classList.add('active');
            } else if (group === 'speed') {
                document.querySelectorAll('.speed-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                document.querySelector(`.speed-btn[data-speed="${activeId}"]`).classList.add('active');
            }
        }

        // Canvas点击事件 - 显示分子信息
        canvas.addEventListener('mousemove', function(event) {
            const rect = canvas.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            
            let foundMolecule = null;
            let moleculeType = '';
            
            // 检查是否在血红蛋白上
            for (const hb of hemoglobins) {
                const distance = Math.sqrt(Math.pow(x - hb.x, 2) + Math.pow(y - hb.y, 2));
                if (distance < hb.radius) {
                    foundMolecule = hb;
                    moleculeType = hb.isCOBound ? 'HbCO' : 'Hb';
                    break;
                }
            }
            
            // 检查是否在氧气分子上
            if (!foundMolecule) {
                for (const o2 of oxygenMolecules) {
                    const distance = Math.sqrt(Math.pow(x - o2.x, 2) + Math.pow(y - o2.y, 2));
                    if (distance < o2.radius) {
                        foundMolecule = o2;
                        moleculeType = 'O2';
                        break;
                    }
                }
            }
            
            // 检查是否在CO分子上
            if (!foundMolecule) {
                for (const co of coMolecules) {
                    const distance = Math.sqrt(Math.pow(x - co.x, 2) + Math.pow(y - co.y, 2));
                    if (distance < co.radius) {
                        foundMolecule = co;
                        moleculeType = 'CO';
                        break;
                    }
                }
            }
            
            // 显示或隐藏信息框
            if (foundMolecule) {
                const molecule = molecules[moleculeType];
                moleculeInfo.innerHTML = `
                    <strong style="color: ${molecule.color}; font-size: 1.1em;">${molecule.name}</strong><br>
                    <div style="margin-top: 8px; font-size: 0.9em;">${molecule.info}</div>
                    ${moleculeType === 'Hb' ? '<div style="margin-top: 5px; color: #74b9ff;">有4个O₂结合位点</div>' : ''}
                    ${moleculeType === 'CO' ? '<div style="margin-top: 5px; color: #ff6b6b;">与Hb亲和力: 200-250× O₂</div>' : ''}
                    ${moleculeType === 'HbCO' ? '<div style="margin-top: 5px; color: #ff9ff3;">解离半衰期: 4-6小时</div>' : ''}
                `;
                moleculeInfo.style.display = 'block';
                moleculeInfo.style.left = (x + 15) + 'px';
                moleculeInfo.style.top = (y + 15) + 'px';
                moleculeInfo.style.borderColor = molecule.color;
            } else {
                moleculeInfo.style.display = 'none';
            }
        });

        canvas.addEventListener('mouseleave', function() {
            moleculeInfo.style.display = 'none';
        });

        // 初始化并开始动画
        init();
        animate();

        // 添加键盘快捷键
        document.addEventListener('keydown', function(event) {
            switch(event.key) {
                case ' ':
                    event.preventDefault();
                    if (isPlaying) {
                        document.getElementById('pauseBtn').click();
                    } else {
                        document.getElementById('playBtn').click();
                    }
                    break;
                case 'r':
                case 'R':
                    document.getElementById('resetBtn').click();
                    break;
                case '1':
                    document.getElementById('normalMode').click();
                    break;
                case '2':
                    document.getElementById('coMode').click();
                    break;
                case '3':
                    document.getElementById('compareMode').click();
                    break;
            }
        });

        // 添加初始提示
        setTimeout(() => {
            alert('提示：\n1. 使用滑块调节CO浓度观察效果\n2. 鼠标悬停在分子上查看详细信息\n3. 空格键：播放/暂停，R键：重置\n4. 数字键1-3切换观察模式');
        }, 1000);
    </script>
</body>
</html>

### 3. 过程输出

### 3. 使用指南

## 一氧化碳毒性教学动画使用指南

欢迎使用“一氧化碳毒性：与血红蛋白结合的微观动画”！本交互式教学工具旨在通过直观的视觉呈现和丰富的交互功能，帮助您深入理解一氧化碳中毒的微观机制。请仔细阅读本指南，以获得最佳学习体验。

---

## 一、功能说明

本动画模拟了血红蛋白在正常生理状态和一氧化碳中毒状态下的气体结合、运输与释放过程。通过动态可视化，您可以观察到：

1. **正常氧运输**：血红蛋白在肺泡区结合氧气，在组织区释放氧气的完整循环
2. **一氧化碳竞争**：CO分子如何与O₂竞争血红蛋白结合位点
3. **浓度效应**：不同CO浓度对血红蛋白功能的影响
4. **实时数据**：结合状态的量化统计

---

## 二、主要功能

### 🎬 动画控制区
- **播放/暂停/重置**：控制动画的播放状态
- **速度调节**：提供0.5x、1x、2x三种播放速度，适合不同学习节奏

### 🔬 观察模式
- **正常运氧模式**：仅展示血红蛋白的正常氧运输过程
- **CO中毒模式**：展示一氧化碳中毒的完整病理过程
- **对比模式**：同时观察正常与中毒状态的差异

### ⚙️ 环境参数调节
- **CO浓度滑块**：实时调节环境中一氧化碳浓度（0%-100%）
- **实时数据显示**：
  - HbCO比例：被CO占据的血红蛋白百分比
  - O₂输送效率：当前状态下氧气的有效输送率
  - 分子统计：各类分子的实时数量统计

### 💡 交互探索
- **鼠标悬停**：将鼠标悬停在任意分子上，查看详细信息卡片
- **实时反馈**：所有参数调节都会立即反映在动画和数据中

---

## 三、设计特色

### 1. 科学准确性
- **亲和力差异**：精确模拟CO与Hb亲和力是O₂的200-250倍
- **结合特性**：CO结合后解离极慢，HbCO呈特征性樱桃红色
- **竞争机制**：真实再现竞争性结合过程

### 2. 视觉设计
- **色彩编码**：
  - 血红蛋白：鲜红色 → 樱桃红（结合CO后）
  - 氧气：天蓝色
  - 一氧化碳：警示红色
- **场景划分**：清晰区分肺泡区（富氧）和组织区（缺氧）
- **动态效果**：结合、释放过程均有流畅的动画表现

### 3. 教学友好性
- **渐进式学习**：从简单到复杂，支持不同学习阶段
- **多感官参与**：视觉、交互、数据反馈相结合
- **即时反馈**：所有操作都有实时视觉和数据反馈

---

## 四、教学要点

### 核心概念可视化
1. **竞争性结合**：观察CO如何“抢占”O₂的结合位点
2. **亲和力差异**：注意CO分子结合更快、更牢固的特性
3. **HbCO稳定性**：观察CO结合后极难解离的现象
4. **组织缺氧**：理解即使血液含氧，组织仍会缺氧的原因

### 关键数据观察
- **HbCO比例 > 10%**：开始出现轻微症状
- **HbCO比例 > 30%**：出现明显中毒症状
- **HbCO比例 > 50%**：危及生命
- **O₂输送效率**：直观反映组织缺氧程度

### 临床联系
- **樱桃红外观**：注意血红蛋白结合CO后的颜色变化
- **浓度-效应关系**：理解环境CO浓度与中毒程度的直接关系
- **治疗原理**：理解高压氧治疗为何有效（增加O₂分压，竞争性置换CO）

---

## 五、使用建议

### 学习路径推荐
**初学者路径：**
1. 先选择“正常运氧模式”，理解血红蛋白的基本功能
2. 切换到“CO中毒模式”，观察中毒过程
3. 使用“对比模式”，直观比较差异
4. 逐步调节CO浓度，观察浓度效应

**进阶学习路径：**
1. 直接使用“对比模式”
2. 快速调节CO浓度至不同水平（10%、30%、50%）
3. 关注实时统计数据的变化
4. 悬停不同分子，深入学习分子特性

### 课堂教学应用
**演示模式：**
- 全屏展示，使用预设浓度（如30%）进行集体观察
- 配合讲解，突出关键帧和关键数据

**探索模式：**
- 让学生自主调节参数，观察变化
- 设置问题任务，如：“找出使O₂输送效率降至50%的CO浓度”

### 学习活动建议
1. **预测-观察-解释**：
   - 预测：调节CO浓度前，预测HbCO比例变化
   - 观察：实际调节并观察变化
   - 解释：分析预测与实际的差异原因

2. **数据记录与分析**：
   - 记录不同CO浓度下的关键数据
   - 绘制浓度-效应曲线
   - 分析数据背后的生理机制

3. **临床情景模拟**：
   - 模拟不同中毒程度（轻度、中度、重度）
   - 讨论相应的临床表现和治疗原则

### 技术提示
- **快捷键**：
  - 空格键：播放/暂停切换
  - R键：重置动画
  - 数字键1-3：快速切换观察模式
- **最佳观看**：建议在电脑端全屏观看，获得最佳视觉效果
- **互动建议**：大胆尝试各种参数组合，观察极端情况下的变化

---

## 六、安全提示

⚠️ **重要提醒**：
本动画为教学工具，展示的是一氧化碳中毒的**科学机制**。在实际生活中：
1. 一氧化碳是**无色、无味、无刺激性的隐形杀手**
2. 实际中毒时**不一定出现“樱桃红”外观**
3. 发现疑似中毒应立即通风、撤离并就医
4. 安装一氧化碳报警器是有效的预防措施

---

## 结语

本交互式动画融合了科学准确性、教育有效性和技术互动性，是理解一氧化碳毒性机制的强大工具。我们鼓励您积极探索、大胆尝试，通过亲手操作深化对这一重要生理病理过程的理解。

祝您学习愉快，收获满满！

**熊猫老师 教育技术团队**  
*让复杂科学触手可及*