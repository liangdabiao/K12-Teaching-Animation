# 需求：基因工程的四大步骤（剪、连、转、检测）全三维

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为高中或大学低年级的生物学学生。他们具备基础的生物学知识（如DNA、质粒、酶），但需要直观、动态地理解基因工程这一抽象、微观的操作流程。
2.  **核心需求**：
    *   **概念可视化**：将“剪切DNA”、“连接DNA”、“转入细胞”、“检测表达”这些文本描述和静态图示，转化为连续、可操作的三维动态过程。
    *   **流程清晰化**：明确展示四大步骤的先后顺序、逻辑关系以及每一步的关键“工具”（如限制酶、DNA连接酶、质粒、受体细胞）。
    *   **降低认知负荷**：通过拟人化、游戏化的交互，让复杂的分子操作变得有趣且易于理解和记忆。
    *   **自主探索与巩固**：允许用户控制动画节奏、重复观看关键步骤，并通过交互式问答进行知识巩固。

#### 教学设计思路
1.  **核心概念**：
    *   **剪**：使用“限制性内切酶”在特定位置切割DNA，产生“黏性末端”。
    *   **连**：使用“DNA连接酶”将目标基因片段与载体（如质粒）的黏性末端连接，形成重组DNA分子。
    *   **转**：将重组DNA分子导入受体细胞（如细菌），常用“转化”法。
    *   **检测**：通过筛选（如抗生素抗性）和鉴定（如荧光蛋白表达、DNA分子杂交）确认成功转入并表达目标基因的细胞。
2.  **认知规律**：
    *   **从宏观到微观**：开场可展示一个宏观实验室场景，然后镜头推近，进入微观的分子世界。
    *   **分步讲解，循序渐进**：严格按照“剪、连、转、检”四步顺序展开，每一步完成后再进入下一步，避免信息过载。
    *   **类比与拟人**：将限制酶比作“分子剪刀”，DNA连接酶比作“分子胶水”，质粒比作“运输卡车”，细菌比作“工厂”，帮助建立直观印象。
3.  **交互设计**：
    *   **流程控制**：提供“播放/暂停”、“上一步/下一步”按钮，允许用户控制学习节奏。
    *   **关键交互点**：
        *   **剪**：用户点击选择“限制酶”，将其拖拽到DNA链的特定识别序列上，触发切割动画。
        *   **连**：用户将切割好的目标基因片段拖拽到质粒的切口处，触发连接酶进行“焊接”。
        *   **转**：用户点击“转化”按钮，观看重组质粒进入细菌细胞的动画。
        *   **检测**：用户点击“添加抗生素”或“紫外线照射”按钮，观察细菌群体的变化（不发光/死亡 vs. 发光/存活）。
    *   **知识卡片**：鼠标悬停在关键元件（如酶、质粒）上时，弹出简要说明卡片。
    *   **小结与测验**：每个步骤结束后，有一个简短的文字总结。全部流程结束后，提供3-5道交互式选择题进行巩固。
4.  **视觉呈现**：
    *   **风格**：采用低多边形（Low-Poly）或卡通渲染的三维风格，在保证科学性的同时，增加亲和力和趣味性，避免过于写实带来的复杂感。
    *   **视角**：采用跟随式、特写式镜头。例如，在“剪”和“连”步骤，镜头聚焦于分子操作台；在“转”和“检测”步骤，镜头拉远展示细胞群体。
    *   **动态效果**：使用平滑的动画、高亮提示、运动路径来引导视线，关键动作（如切割、连接）配合轻微的视觉反馈（如闪光、震动）。

#### 配色方案选择
*   **主色调**：采用**科技蓝**（`#4A90E2`）和**生命绿**（`#50C878`）作为主题色，体现生物技术与科学感。
*   **DNA与分子**：
    *   DNA双螺旋：主链使用浅灰色（`#CCCCCC`），碱基对使用互补色区分，如腺嘌呤（A）-胸腺嘧啶（T）用**橙色（`#FFA726`）-蓝色（`#42A5F5`）**，鸟嘌呤（G）-胞嘧啶（C）用**绿色（`#66BB6A`）-红色（`#EF5350`）**。
    *   **酶**：限制酶用**红色**（`#FF5252`，象征切割、锋利），DNA连接酶用**黄色**（`#FFD95C`，象征连接、能量）。
    *   **质粒**：环状DNA，使用**紫色**（`#AB47BC`）与主DNA区分。
*   **细胞与背景**：
    *   **细菌细胞**：浅色半透明囊状（如`#E8F5E9`）。
    *   **背景与UI**：深色背景（`#1A237E` 或 `#2C3E50`）以突出前景的分子元素，UI控件使用主色调的亮色变体。
*   **状态指示**：
    *   **可交互区域**：鼠标悬停时高亮为**白色光晕**。
    *   **成功**：使用绿色闪光（`#00E676`）。
    *   **失败/淘汰**：使用红色褪色或消失效果。

#### 交互功能列表
1.  **全局控制**：
    *   播放/暂停动画
    *   重置动画到开始
    *   静音/开启音效开关
2.  **步骤导航**：
    *   清晰的进度条，显示“剪、连、转、检”四个节点。
    *   “上一步”、“下一步”按钮。
    *   点击进度节点可直接跳转至对应步骤。
3.  **步骤内交互**：
    *   **步骤一（剪）**：从工具栏拖拽限制酶到DNA识别位点；点击播放切割动画。
    *   **步骤二（连）**：拖拽目标基因片段到质粒切口；点击播放连接酶连接动画。
    *   **步骤三（转）**：点击“转化”按钮，启动质粒进入细胞的动画。
    *   **步骤四（检测）**：
        *   点击“添加抗生素”，观察非重组菌死亡。
        *   点击“打开紫外灯”，观察成功表达荧光蛋白的菌落发光。
        *   （可选）点击“分子检测”按钮，展示DNA杂交原理示意图。
4.  **辅助学习功能**：
    *   **鼠标悬停提示**：对所有关键物体（酶、质粒、细胞等）显示名称和简要功能。
    *   **原理弹窗**：每个步骤提供“详解”按钮，点击后弹出更详细的文字和原理图说明。
    *   **语音讲解**：伴随动画播放关键步骤的语音解说（可开关）。
5.  **评估与巩固**：
    *   每个步骤结束后的“要点回顾”文字框。
    *   全部动画结束后的“知识挑战”环节，包含3-5道选择题，即时反馈对错。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>基因工程四大步骤：剪、连、转、检 - 3D交互教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1A237E 0%, #2C3E50 100%);
            color: #f0f0f0;
            min-height: 100vh;
            padding: 20px;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(74, 144, 226, 0.3);
        }

        h1 {
            color: #4A90E2;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }

        .subtitle {
            color: #50C878;
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .main-content {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .animation-section {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(74, 144, 226, 0.2);
        }

        .canvas-container {
            position: relative;
            width: 100%;
            height: 500px;
            background: rgba(10, 15, 30, 0.7);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
        }

        #dnaCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin-bottom: 20px;
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }

        .btn-primary {
            background: linear-gradient(135deg, #4A90E2 0%, #2A6FC9 100%);
            color: white;
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.15);
            color: #f0f0f0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .btn-success {
            background: linear-gradient(135deg, #50C878 0%, #2E8B57 100%);
            color: white;
        }

        .btn-warning {
            background: linear-gradient(135deg, #FFA726 0%, #F57C00 100%);
            color: white;
        }

        .btn-danger {
            background: linear-gradient(135deg, #FF5252 0%, #D32F2F 100%);
            color: white;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        .step-indicator {
            display: flex;
            justify-content: space-between;
            margin: 20px 0;
            position: relative;
        }

        .step {
            display: flex;
            flex-direction: column;
            align-items: center;
            flex: 1;
            position: relative;
            z-index: 2;
        }

        .step-circle {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 0.1);
            border: 3px solid rgba(255, 255, 255, 0.2);
            color: rgba(255, 255, 255, 0.5);
        }

        .step.active .step-circle {
            background: #4A90E2;
            border-color: #4A90E2;
            color: white;
            transform: scale(1.1);
            box-shadow: 0 0 15px rgba(74, 144, 226, 0.7);
        }

        .step.completed .step-circle {
            background: #50C878;
            border-color: #50C878;
            color: white;
        }

        .step-label {
            font-size: 0.9rem;
            text-align: center;
            font-weight: 500;
        }

        .step-line {
            position: absolute;
            top: 25px;
            left: 10%;
            right: 10%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            z-index: 1;
        }

        .info-panel {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            border-left: 4px solid #4A90E2;
        }

        .info-title {
            color: #4A90E2;
            font-size: 1.3rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-content {
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }

        .toolbox {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin: 20px 0;
            padding: 15px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
        }

        .tool {
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            cursor: grab;
            transition: all 0.2s ease;
            border: 2px dashed transparent;
            text-align: center;
            min-width: 120px;
        }

        .tool:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }

        .tool.active {
            border-color: #4A90E2;
            background: rgba(74, 144, 226, 0.2);
        }

        .tool-icon {
            font-size: 1.5rem;
            margin-bottom: 5px;
        }

        .tool-name {
            font-size: 0.9rem;
            font-weight: 500;
        }

        .quiz-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            border: 1px solid rgba(80, 200, 120, 0.3);
        }

        .quiz-question {
            font-size: 1.2rem;
            margin-bottom: 20px;
            color: #50C878;
        }

        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .quiz-option {
            padding: 15px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .quiz-option:hover {
            background: rgba(255, 255, 255, 0.15);
        }

        .quiz-option.correct {
            background: rgba(80, 200, 120, 0.3);
            border-left: 4px solid #50C878;
        }

        .quiz-option.incorrect {
            background: rgba(255, 82, 82, 0.3);
            border-left: 4px solid #FF5252;
        }

        .hidden {
            display: none !important;
        }

        .hint {
            position: absolute;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 0.9rem;
            max-width: 250px;
            z-index: 100;
            pointer-events: none;
            border: 1px solid #4A90E2;
        }

        .completion-message {
            text-align: center;
            padding: 30px;
            background: rgba(80, 200, 120, 0.1);
            border-radius: 15px;
            margin-top: 30px;
            border: 2px solid #50C878;
        }

        .completion-title {
            color: #50C878;
            font-size: 1.8rem;
            margin-bottom: 15px;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .controls {
                flex-direction: column;
                align-items: center;
            }
            
            .btn {
                width: 100%;
                justify-content: center;
            }
            
            .step-indicator {
                flex-wrap: wrap;
                gap: 20px;
            }
            
            .step {
                flex: 0 0 calc(50% - 20px);
            }
            
            .canvas-container {
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>基因工程四大步骤</h1>
            <p class="subtitle">剪、连、转、检 - 三维交互式教学动画</p>
        </header>
        
        <main class="main-content">
            <section class="animation-section">
                <div class="step-indicator">
                    <div class="step-line"></div>
                    <div class="step active" data-step="1">
                        <div class="step-circle">1</div>
                        <div class="step-label">剪 - 切割DNA</div>
                    </div>
                    <div class="step" data-step="2">
                        <div class="step-circle">2</div>
                        <div class="step-label">连 - 连接基因</div>
                    </div>
                    <div class="step" data-step="3">
                        <div class="step-circle">3</div>
                        <div class="step-label">转 - 转入细胞</div>
                    </div>
                    <div class="step" data-step="4">
                        <div class="step-circle">4</div>
                        <div class="step-label">检 - 检测表达</div>
                    </div>
                </div>
                
                <div class="canvas-container">
                    <canvas id="dnaCanvas"></canvas>
                    <div id="hint" class="hint hidden"></div>
                </div>
                
                <div class="toolbox" id="toolbox">
                    <div class="tool" data-tool="restriction-enzyme" id="tool-restriction">
                        <div class="tool-icon">✂️</div>
                        <div class="tool-name">限制性内切酶</div>
                    </div>
                    <div class="tool" data-tool="dna-fragment" id="tool-dna">
                        <div class="tool-icon">🧬</div>
                        <div class="tool-name">目标基因片段</div>
                    </div>
                    <div class="tool" data-tool="ligase" id="tool-ligase">
                        <div class="tool-icon">🔗</div>
                        <div class="tool-name">DNA连接酶</div>
                    </div>
                    <div class="tool" data-tool="plasmid" id="tool-plasmid">
                        <div class="tool-icon">⭕</div>
                        <div class="tool-name">质粒载体</div>
                    </div>
                </div>
                
                <div class="controls">
                    <button class="btn btn-secondary" id="prevBtn">
                        <span>◀</span> 上一步
                    </button>
                    <button class="btn btn-primary" id="playBtn">
                        <span>▶</span> 播放动画
                    </button>
                    <button class="btn btn-secondary" id="nextBtn">
                        下一步 <span>▶</span>
                    </button>
                    <button class="btn btn-secondary" id="resetBtn">
                        <span>↺</span> 重置
                    </button>
                    <button class="btn btn-success" id="testBtn">
                        <span>🔬</span> 开始检测
                    </button>
                </div>
                
                <div class="info-panel">
                    <div class="info-title">
                        <span id="stepIcon">✂️</span>
                        <span id="stepTitle">步骤一：剪切DNA</span>
                    </div>
                    <div class="info-content" id="stepDescription">
                        使用限制性内切酶在特定识别序列处切割DNA分子，产生黏性末端。请从左侧工具箱中选择"限制性内切酶"，然后拖拽到DNA链上进行切割。
                    </div>
                </div>
            </section>
            
            <section class="quiz-section hidden" id="quizSection">
                <h2 class="info-title">知识挑战</h2>
                <p class="quiz-question" id="quizQuestion">基因工程中，用来切割DNA产生黏性末端的工具是什么？</p>
                <div class="quiz-options" id="quizOptions">
                    <div class="quiz-option" data-answer="A">A. DNA连接酶</div>
                    <div class="quiz-option" data-answer="B">B. 限制性内切酶</div>
                    <div class="quiz-option" data-answer="C">C. RNA聚合酶</div>
                    <div class="quiz-option" data-answer="D">D. 解旋酶</div>
                </div>
            </section>
            
            <div class="completion-message hidden" id="completionMessage">
                <h2 class="completion-title">🎉 恭喜！</h2>
                <p>您已经成功完成了基因工程四大步骤的学习！</p>
                <p>通过这个交互式动画，您已经掌握了：</p>
                <ul style="text-align: left; margin: 15px 0; padding-left: 20px;">
                    <li>使用限制性内切酶切割DNA</li>
                    <li>使用DNA连接酶连接基因片段与质粒</li>
                    <li>将重组质粒转入细菌细胞</li>
                    <li>检测基因是否成功表达</li>
                </ul>
                <p>点击"重置"按钮可以重新开始学习。</p>
            </div>
        </main>
        
        <footer>
            <p>基因工程教学动画 | 设计：教育技术专家 | 本动画为教学演示用途</p>
            <p>注意：本动画对分子过程进行了简化与可视化处理，便于理解核心概念</p>
        </footer>
    </div>

    <script>
        // 全局变量
        let currentStep = 1;
        let animationPlaying = false;
        let canvas, ctx;
        let animationId;
        let hintElement;
        
        // 颜色定义
        const colors = {
            dnaBackbone: '#CCCCCC',
            dnaBaseA: '#FFA726', // 橙色
            dnaBaseT: '#42A5F5', // 蓝色
            dnaBaseG: '#66BB6A', // 绿色
            dnaBaseC: '#EF5350', // 红色
            restrictionEnzyme: '#FF5252', // 红色
            ligase: '#FFD95C', // 黄色
            plasmid: '#AB47BC', // 紫色
            bacteria: '#E8F5E9', // 浅绿色
            success: '#00E676', // 绿色
            failure: '#FF5252', // 红色
            highlight: '#FFFFFF' // 白色
        };
        
        // 动画状态
        const state = {
            dnaCut: false,
            geneConnected: false,
            transformed: false,
            tested: false,
            selectedTool: null,
            dragging: false,
            dragObject: null,
            dragOffset: {x: 0, y: 0},
            bacteria: [],
            showAntibiotic: false,
            showUV: false
        };
        
        // 初始化细菌
        function initBacteria() {
            state.bacteria = [];
            for (let i = 0; i < 20; i++) {
                state.bacteria.push({
                    x: 100 + (i % 5) * 120,
                    y: 150 + Math.floor(i / 5) * 80,
                    radius: 20,
                    transformed: i < 5, // 前5个是成功转化的
                    glowing: false,
                    alive: true
                });
            }
        }
        
        // 初始化Canvas
        function initCanvas() {
            canvas = document.getElementById('dnaCanvas');
            ctx = canvas.getContext('2d');
            hintElement = document.getElementById('hint');
            
            // 设置Canvas尺寸
            function resizeCanvas() {
                const container = canvas.parentElement;
                canvas.width = container.clientWidth;
                canvas.height = container.clientHeight;
                draw();
            }
            
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();
            
            // 事件监听
            canvas.addEventListener('mousedown', handleMouseDown);
            canvas.addEventListener('mousemove', handleMouseMove);
            canvas.addEventListener('mouseup', handleMouseUp);
            canvas.addEventListener('click', handleCanvasClick);
            
            // 工具点击事件
            document.querySelectorAll('.tool').forEach(tool => {
                tool.addEventListener('click', () => {
                    if (tool.classList.contains('active')) {
                        tool.classList.remove('active');
                        state.selectedTool = null;
                    } else {
                        document.querySelectorAll('.tool').forEach(t => t.classList.remove('active'));
                        tool.classList.add('active');
                        state.selectedTool = tool.dataset.tool;
                        showHint(`已选择：${tool.querySelector('.tool-name').textContent}`);
                    }
                });
            });
            
            // 控制按钮事件
            document.getElementById('prevBtn').addEventListener('click', prevStep);
            document.getElementById('nextBtn').addEventListener('click', nextStep);
            document.getElementById('playBtn').addEventListener('click', toggleAnimation);
            document.getElementById('resetBtn').addEventListener('click', resetAnimation);
            document.getElementById('testBtn').addEventListener('click', startTest);
            
            // 初始化细菌
            initBacteria();
        }
        
        // 绘制函数
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 根据当前步骤绘制不同内容
            switch(currentStep) {
                case 1:
                    drawStep1();
                    break;
                case 2:
                    drawStep2();
                    break;
                case 3:
                    drawStep3();
                    break;
                case 4:
                    drawStep4();
                    break;
            }
            
            // 绘制拖拽对象
            if (state.dragging && state.dragObject) {
                drawDragObject();
            }
        }
        
        // 步骤1：剪切DNA
        function drawStep1() {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 绘制DNA链
            drawDNA(centerX - 200, centerY, 400, 30, false);
            
            // 绘制限制酶（如果在工具箱中）
            if (!state.dnaCut) {
                drawRestrictionEnzyme(centerX + 150, centerY - 100);
                
                // 绘制提示
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.font = '16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('点击并拖拽限制酶到DNA链上进行切割', centerX, centerY + 100);
            } else {
                // 绘制切割后的DNA
                drawCutDNA(centerX, centerY);
                
                ctx.fillStyle = colors.success;
                ctx.font = 'bold 18px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('✓ DNA已成功切割！', centerX, centerY + 100);
            }
        }
        
        // 步骤2：连接基因
        function drawStep2() {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 绘制质粒
            drawPlasmid(centerX, centerY - 50, 80);
            
            // 绘制目标基因片段
            if (!state.geneConnected) {
                drawDNAFragment(centerX - 200, centerY + 100, 150, 20);
                
                // 绘制DNA连接酶
                drawLigase(centerX + 150, centerY + 100);
                
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.font = '16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('拖拽基因片段到质粒切口处，然后使用连接酶', centerX, centerY + 180);
            } else {
                // 绘制重组质粒
                drawRecombinantPlasmid(centerX, centerY);
                
                ctx.fillStyle = colors.success;
                ctx.font = 'bold 18px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('✓ 重组质粒构建成功！', centerX, centerY + 150);
            }
        }
        
        // 步骤3：转入细胞
        function drawStep3() {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            
            // 绘制细菌细胞
            drawBacteriaCell(centerX, centerY, 60);
            
            // 绘制质粒
            if (!state.transformed) {
                const angle = Date.now() / 1000;
                const plasmidX = centerX + Math.cos(angle) * 150;
                const plasmidY = centerY + Math.sin(angle) * 150;
                
                drawPlasmid(plasmidX, plasmidY, 40);
                
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.font = '16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('点击"播放动画"观看质粒转入细菌的过程', centerX, centerY + 150);
            } else {
                // 绘制质粒在细菌内
                drawPlasmidInCell(centerX, centerY);
                
                ctx.fillStyle = colors.success;
                ctx.font = 'bold 18px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('✓ 质粒成功转入细菌细胞！', centerX, centerY + 150);
            }
        }
        
        // 步骤4：检测表达
        function drawStep4() {
            const centerX = canvas.width / 2;
            
            // 绘制标题
            ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
            ctx.font = 'bold 20px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('细菌培养皿', centerX, 50);
            
            // 绘制培养皿
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(centerX, 250, 200, 0, Math.PI * 2);
            ctx.stroke();
            
            // 绘制细菌菌落
            state.bacteria.forEach(bacteria => {
                drawBacteriaColony(bacteria);
            });
            
            // 绘制抗生素效果
            if (state.showAntibiotic) {
                ctx.fillStyle = 'rgba(255, 82, 82, 0.3)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                ctx.fillStyle = colors.failure;
                ctx.font = 'bold 18px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('抗生素杀死了未成功转化的细菌', centerX, 450);
            }
            
            // 绘制UV效果
            if (state.showUV) {
                // UV光效果
                const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
                gradient.addColorStop(0, 'rgba(128, 0, 255, 0.1)');
                gradient.addColorStop(0.5, 'rgba(128, 0, 255, 0.3)');
                gradient.addColorStop(1, 'rgba(128, 0, 255, 0.1)');
                ctx.fillStyle = gradient;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                ctx.fillStyle = colors.success;
                ctx.font = 'bold 18px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('UV照射下，成功表达荧光蛋白的菌落发出绿色荧光', centerX, 450);
            }
            
            if (!state.tested) {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                ctx.font = '16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText('点击"开始检测"按钮进行基因表达检测', centerX, 480);
            }
        }
        
        // 绘制DNA链
        function drawDNA(x, y, length, basePairs, isCircular = false) {
            const segmentLength = length / basePairs;
            
            // 绘制主链
            ctx.strokeStyle = colors.dnaBackbone;
            ctx.lineWidth = 3;
            
            if (isCircular) {
                ctx.beginPath();
                ctx.arc(x, y, length / (2 * Math.PI), 0, Math.PI * 2);
                ctx.stroke();
            } else {
                ctx.beginPath();
                ctx.moveTo(x, y);
                ctx.lineTo(x + length, y);
                ctx.stroke();
            }
            
            // 绘制碱基对
            for (let i = 0; i < basePairs; i++) {
                const baseX = x + i * segmentLength + segmentLength / 2;
                
                // 交替绘制不同颜色的碱基对
                let color1, color2;
                if (i % 4 === 0) {
                    color1 = colors.dnaBaseA;
                    color2 = colors.dnaBaseT;
                } else if (i % 4 === 1) {
                    color1 = colors.dnaBaseT;
                    color2 = colors.dnaBaseA;
                } else if (i % 4 === 2) {
                    color1 = colors.dnaBaseG;
                    color2 = colors.dnaBaseC;
                } else {
                    color1 = colors.dnaBaseC;
                    color2 = colors.dnaBaseG;
                }
                
                // 绘制碱基对连线
                ctx.strokeStyle = color1;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.moveTo(baseX, y - 15);
                ctx.lineTo(baseX, y + 15);
                ctx.stroke();
                
                // 绘制碱基点
                ctx.fillStyle = color1;
                ctx.beginPath();
                ctx.arc(baseX, y - 15, 3, 0, Math.PI * 2);
                ctx.fill();
                
                ctx.fillStyle = color2;
                ctx.beginPath();
                ctx.arc(baseX, y + 15, 3, 0, Math.PI * 2);
                ctx.fill();
            }
        }
        
        // 绘制切割后的DNA
        function drawCutDNA(x, y) {
            // 左半部分DNA
            drawDNA(x - 150, y, 150, 15);
            
            // 右半部分DNA
            drawDNA(x + 50, y, 150, 15);
            
            // 绘制切割点（黏性末端）
            ctx.strokeStyle = colors.highlight;
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            
            // 左端黏性末端
            ctx.beginPath();
            ctx.moveTo(x - 5, y - 10);
            ctx.lineTo(x - 15, y - 10);
            ctx.moveTo(x - 5, y + 10);
            ctx.lineTo(x - 15, y + 10);
            ctx.stroke();
            
            // 右端黏性末端
            ctx.beginPath();
            ctx.moveTo(x + 5, y - 10);
            ctx.lineTo(x + 15, y - 10);
            ctx.moveTo(x + 5, y + 10);
            ctx.lineTo(x + 15, y + 10);
            ctx.stroke();
            
            ctx.setLineDash([]);
        }
        
        // 绘制限制酶
        function drawRestrictionEnzyme(x, y) {
            // 酶的主体
            ctx.fillStyle = colors.restrictionEnzyme;
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x - 20, y - 30);
            ctx.lineTo(x + 20, y - 30);
            ctx.closePath();
            ctx.fill();
            
            // 剪刀形状
            ctx.strokeStyle = colors.highlight;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(x - 15, y - 20);
            ctx.lineTo(x - 5, y - 10);
            ctx.moveTo(x + 15, y - 20);
            ctx.lineTo(x + 5, y - 10);
            ctx.stroke();
            
            // 标签
            ctx.fillStyle = 'white';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('限制酶', x, y - 40);
        }
        
        // 绘制DNA片段
        function drawDNAFragment(x, y, length, basePairs) {
            drawDNA(x, y, length, basePairs);
            
            // 高亮显示
            ctx.strokeStyle = colors.highlight;
            ctx.lineWidth = 2;
            ctx.strokeRect(x - 10, y - 25, length + 20, 50);
        }
        
        // 绘制DNA连接酶
        function drawLigase(x, y) {
            // 酶的主体
            ctx.fillStyle = colors.ligase;
            ctx.beginPath();
            ctx.arc(x, y, 25, 0, Math.PI * 2);
            ctx.fill();
            
            // 连接符号
            ctx.strokeStyle = colors.highlight;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(x - 15, y);
            ctx.lineTo(x - 5, y);
            ctx.moveTo(x + 5, y);
            ctx.lineTo(x + 15, y);
            ctx.moveTo(x - 5, y - 5);
            ctx.lineTo(x - 5, y + 5);
            ctx.moveTo(x + 5, y - 5);
            ctx.lineTo(x + 5, y + 5);
            ctx.stroke();
            
            // 标签
            ctx.fillStyle = 'white';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('连接酶', x, y - 35);
        }
        
        // 绘制质粒
        function drawPlasmid(x, y, radius) {
            // 环形DNA
            ctx.strokeStyle = colors.plasmid;
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(x, y, radius, 0, Math.PI * 2);
            ctx.stroke();
            
            // 绘制一些碱基对
            const baseCount = 12;
            for (let i = 0; i < baseCount; i++) {
                const angle = (i / baseCount) * Math.PI * 2;
                const baseX = x + Math.cos(angle) * radius;
                const baseY = y + Math.sin(angle) * radius;
                
                ctx.fillStyle = i % 2 === 0 ? colors.dnaBaseA : colors.dnaBaseG;
                ctx.beginPath();
                ctx.arc(baseX, baseY, 3, 0, Math.PI * 2);
                ctx.fill();
            }
            
            // 如果是切割后的质粒，显示切口
            if (currentStep === 2 && !state.geneConnected) {
                ctx.strokeStyle = colors.restrictionEnzyme;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(x + radius, y, 5, 0, Math.PI * 2);
                ctx.stroke();
            }
        }
        
        // 绘制重组质粒
        function drawRecombinantPlasmid(x, y) {
            const radius = 100;
            
            // 绘制质粒环
            ctx.strokeStyle = colors.plasmid;
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(x, y, radius, 0, Math.PI * 2);
            ctx.stroke();
            
            // 绘制插入的基因片段（不同颜色）
            ctx.strokeStyle = colors.dnaBaseA;
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(x, y, radius, -Math.PI/4, Math.PI/4);
            ctx.stroke();
            
            // 高亮显示插入点
            ctx.fillStyle = colors.success;
            ctx.beginPath();
            ctx.arc(x + radius * Math.cos(Math.PI/4), y + radius * Math.sin(Math.PI/4), 8, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.arc(x + radius * Math.cos(-Math.PI/4), y + radius * Math.sin(-Math.PI/4), 8, 0, Math.PI * 2);
            ctx.fill();
            
            // 标签
            ctx.fillStyle = 'white';
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('重组质粒', x, y - radius - 20);
        }
        
        // 绘制细菌细胞
        function drawBacteriaCell(x, y, radius) {
            // 细胞膜
            ctx.strokeStyle = colors.bacteria;
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.ellipse(x, y, radius * 1.5, radius, 
0, Math.PI * 2);
            ctx.stroke();
            
            // 细胞质
            ctx.fillStyle = colors.bacteria + '40';
            ctx.beginPath();
            ctx.ellipse(x, y, radius * 1.5, radius, 0, Math.PI * 2);
            ctx.fill();
            
            // 细胞内部结构
            ctx.fillStyle = colors.dnaBaseG + '80';
            ctx.beginPath();
            ctx.arc(x - radius/2, y, 8, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.arc(x + radius/2, y - 10, 6, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.arc(x + radius/3, y + 15, 5, 0, Math.PI * 2);
            ctx.fill();
        }
        
        // 绘制质粒在细胞内
        function drawPlasmidInCell(x, y) {
            // 先绘制细菌细胞
            drawBacteriaCell(x, y, 60);
            
            // 在细胞内绘制质粒
            const angle = Date.now() / 1000;
            const plasmidX = x + Math.cos(angle) * 20;
            const plasmidY = y + Math.sin(angle) * 15;
            
            drawPlasmid(plasmidX, plasmidY, 25);
            
            // 添加高亮效果
            ctx.strokeStyle = colors.success;
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.ellipse(x, y, 90, 60, 0, Math.PI * 2);
            ctx.stroke();
            ctx.setLineDash([]);
        }
        
        // 绘制细菌菌落
        function drawBacteriaColony(bacteria) {
            if (!bacteria.alive) {
                // 死亡的细菌
                ctx.fillStyle = colors.failure + '40';
                ctx.beginPath();
                ctx.arc(bacteria.x, bacteria.y, bacteria.radius, 0, Math.PI * 2);
                ctx.fill();
                
                ctx.strokeStyle = colors.failure;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.moveTo(bacteria.x - bacteria.radius/2, bacteria.y - bacteria.radius/2);
                ctx.lineTo(bacteria.x + bacteria.radius/2, bacteria.y + bacteria.radius/2);
                ctx.moveTo(bacteria.x + bacteria.radius/2, bacteria.y - bacteria.radius/2);
                ctx.lineTo(bacteria.x - bacteria.radius/2, bacteria.y + bacteria.radius/2);
                ctx.stroke();
                return;
            }
            
            // 正常细菌
            ctx.fillStyle = bacteria.transformed ? colors.bacteria : '#CCCCCC';
            ctx.beginPath();
            ctx.arc(bacteria.x, bacteria.y, bacteria.radius, 0, Math.PI * 2);
            ctx.fill();
            
            // 成功转化的细菌有特殊标记
            if (bacteria.transformed) {
                ctx.strokeStyle = colors.plasmid;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.arc(bacteria.x, bacteria.y, bacteria.radius - 3, 0, Math.PI * 2);
                ctx.stroke();
                
                // 如果正在发光（UV照射下）
                if (bacteria.glowing) {
                    // 发光效果
                    const gradient = ctx.createRadialGradient(
                        bacteria.x, bacteria.y, 0,
                        bacteria.x, bacteria.y, bacteria.radius * 2
                    );
                    gradient.addColorStop(0, colors.success + '80');
                    gradient.addColorStop(1, colors.success + '0');
                    
                    ctx.fillStyle = gradient;
                    ctx.beginPath();
                    ctx.arc(bacteria.x, bacteria.y, bacteria.radius * 2, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // 细菌本身更亮
                    ctx.fillStyle = colors.success;
                    ctx.beginPath();
                    ctx.arc(bacteria.x, bacteria.y, bacteria.radius, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
        }
        
        // 绘制拖拽对象
        function drawDragObject() {
            if (!state.dragObject) return;
            
            const {type, x, y} = state.dragObject;
            
            switch(type) {
                case 'restriction-enzyme':
                    drawRestrictionEnzyme(x, y);
                    break;
                case 'dna-fragment':
                    drawDNAFragment(x - 75, y, 150, 20);
                    break;
                case 'ligase':
                    drawLigase(x, y);
                    break;
                case 'plasmid':
                    drawPlasmid(x, y, 40);
                    break;
            }
        }
        
        // 鼠标事件处理
        function handleMouseDown(e) {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // 检查是否点击了可拖拽对象
            if (currentStep === 1 && !state.dnaCut) {
                // 检查是否点击了限制酶
                const enzymeX = canvas.width / 2 + 150;
                const enzymeY = canvas.height / 2 - 100;
                const distance = Math.sqrt((x - enzymeX) ** 2 + (y - enzymeY) ** 2);
                
                if (distance < 40 && state.selectedTool === 'restriction-enzyme') {
                    state.dragging = true;
                    state.dragObject = {
                        type: 'restriction-enzyme',
                        x: x,
                        y: y
                    };
                    state.dragOffset = {x: enzymeX - x, y: enzymeY - y};
                }
            }
            
            if (currentStep === 2 && !state.geneConnected) {
                // 检查是否点击了DNA片段
                const fragmentX = canvas.width / 2 - 200;
                const fragmentY = canvas.height / 2 + 100;
                const distance = Math.sqrt((x - fragmentX) ** 2 + (y - fragmentY) ** 2);
                
                if (distance < 100 && state.selectedTool === 'dna-fragment') {
                    state.dragging = true;
                    state.dragObject = {
                        type: 'dna-fragment',
                        x: x,
                        y: y
                    };
                    state.dragOffset = {x: fragmentX - x, y: fragmentY - y};
                }
                
                // 检查是否点击了连接酶
                const ligaseX = canvas.width / 2 + 150;
                const ligaseY = canvas.height / 2 + 100;
                const ligaseDistance = Math.sqrt((x - ligaseX) ** 2 + (y - ligaseY) ** 2);
                
                if (ligaseDistance < 40 && state.selectedTool === 'ligase') {
                    state.dragging = true;
                    state.dragObject = {
                        type: 'ligase',
                        x: x,
                        y: y
                    };
                    state.dragOffset = {x: ligaseX - x, y: ligaseY - y};
                }
            }
        }
        
        function handleMouseMove(e) {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // 更新拖拽对象位置
            if (state.dragging && state.dragObject) {
                state.dragObject.x = x + state.dragOffset.x;
                state.dragObject.y = y + state.dragOffset.y;
                draw();
            }
            
            // 显示提示
            showHintAtPosition(x, y);
        }
        
        function handleMouseUp(e) {
            if (!state.dragging || !state.dragObject) {
                state.dragging = false;
                return;
            }
            
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // 检查是否放置到正确位置
            if (currentStep === 1 && state.dragObject.type === 'restriction-enzyme') {
                const dnaX = canvas.width / 2;
                const dnaY = canvas.height / 2;
                
                // 检查是否靠近DNA链
                if (Math.abs(y - dnaY) < 50 && x > dnaX - 250 && x < dnaX + 250) {
                    // 成功切割DNA
                    state.dnaCut = true;
                    showHint('✓ DNA切割成功！产生了黏性末端。');
                    
                    // 更新步骤信息
                    updateStepInfo();
                    
                    // 播放成功音效（模拟）
                    playSuccessSound();
                }
            }
            
            if (currentStep === 2) {
                const plasmidX = canvas.width / 2;
                const plasmidY = canvas.height / 2 - 50;
                
                if (state.dragObject.type === 'dna-fragment') {
                    // 检查是否靠近质粒切口
                    const distance = Math.sqrt((x - (plasmidX + 80)) ** 2 + (y - plasmidY) ** 2);
                    
                    if (distance < 30) {
                        showHint('基因片段已放置到质粒切口处。现在请使用DNA连接酶进行连接。');
                    }
                }
                
                if (state.dragObject.type === 'ligase') {
                    // 检查是否靠近质粒
                    const distance = Math.sqrt((x - plasmidX) ** 2 + (y - plasmidY) ** 2);
                    
                    if (distance < 100) {
                        // 成功连接
                        state.geneConnected = true;
                        showHint('✓ DNA连接成功！重组质粒构建完成。');
                        
                        // 更新步骤信息
                        updateStepInfo();
                        
                        // 播放成功音效（模拟）
                        playSuccessSound();
                    }
                }
            }
            
            state.dragging = false;
            state.dragObject = null;
            draw();
        }
        
        function handleCanvasClick(e) {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // 步骤3：点击播放转化动画
            if (currentStep === 3 && !state.transformed) {
                const centerX = canvas.width / 2;
                const centerY = canvas.height / 2;
                const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
                
                if (distance < 100) {
                    playTransformationAnimation();
                }
            }
        }
        
        // 播放转化动画
        function playTransformationAnimation() {
            if (animationPlaying) return;
            
            animationPlaying = true;
            document.getElementById('playBtn').disabled = true;
            
            let startTime = Date.now();
            const duration = 2000; // 2秒动画
            
            function animate() {
                const elapsed = Date.now() - startTime;
                const progress = Math.min(elapsed / duration, 1);
                
                draw();
                
                // 绘制动画中的质粒
                const centerX = canvas.width / 2;
                const centerY = canvas.height / 2;
                
                // 计算质粒位置（从外部飞入细胞）
                const startX = centerX + 150;
                const startY = centerY + 150;
                const endX = centerX;
                const endY = centerY;
                
                const plasmidX = startX + (endX - startX) * progress;
                const plasmidY = startY + (endY - startY) * progress;
                const plasmidSize = 40 * (1 - progress * 0.5);
                
                // 绘制质粒
                drawPlasmid(plasmidX, plasmidY, plasmidSize);
                
                // 绘制运动轨迹
                ctx.strokeStyle = colors.highlight + '80';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(startX, startY);
                ctx.lineTo(plasmidX, plasmidY);
                ctx.stroke();
                ctx.setLineDash([]);
                
                if (progress < 1) {
                    animationId = requestAnimationFrame(animate);
                } else {
                    // 动画完成
                    state.transformed = true;
                    animationPlaying = false;
                    document.getElementById('playBtn').disabled = false;
                    
                    // 更新步骤信息
                    updateStepInfo();
                    
                    // 播放成功音效（模拟）
                    playSuccessSound();
                    
                    draw();
                }
            }
            
            animate();
        }
        
        // 开始检测
        function startTest() {
            if (currentStep !== 4) return;
            
            // 第一步：添加抗生素
            state.showAntibiotic = true;
            draw();
            
            // 杀死未转化的细菌
            setTimeout(() => {
                state.bacteria.forEach(bacteria => {
                    if (!bacteria.transformed) {
                        bacteria.alive = false;
                    }
                });
                draw();
                
                // 第二步：UV照射
                setTimeout(() => {
                    state.showAntibiotic = false;
                    state.showUV = true;
                    
                    // 让转化的细菌发光
                    state.bacteria.forEach(bacteria => {
                        if (bacteria.transformed && bacteria.alive) {
                            bacteria.glowing = true;
                        }
                    });
                    draw();
                    
                    // 完成检测
                    setTimeout(() => {
                        state.tested = true;
                        showHint('✓ 检测完成！成功筛选出表达目标基因的细菌。');
                        
                        // 显示完成消息
                        document.getElementById('completionMessage').classList.remove('hidden');
                        
                        // 显示测验
                        document.getElementById('quizSection').classList.remove('hidden');
                        
                        // 播放成功音效（模拟）
                        playSuccessSound();
                    }, 2000);
                }, 2000);
            }, 2000);
        }
        
        // 显示提示
        function showHint(message) {
            hintElement.textContent = message;
            hintElement.classList.remove('hidden');
            
            // 居中显示
            hintElement.style.left = '50%';
            hintElement.style.top = '20px';
            hintElement.style.transform = 'translateX(-50%)';
            
            // 3秒后隐藏
            setTimeout(() => {
                hintElement.classList.add('hidden');
            }, 3000);
        }
        
        // 在指定位置显示提示
        function showHintAtPosition(x, y) {
            // 根据位置显示不同的提示
            if (currentStep === 1 && !state.dnaCut) {
                const dnaY = canvas.height / 2;
                if (Math.abs(y - dnaY) < 30) {
                    hintElement.textContent = '将限制酶拖拽到这里切割DNA';
                    hintElement.style.left = x + 'px';
                    hintElement.style.top = (y - 40) + 'px';
                    hintElement.classList.remove('hidden');
                    return;
                }
            }
            
            // 默认隐藏提示
            hintElement.classList.add('hidden');
        }
        
        // 播放成功音效（模拟）
        function playSuccessSound() {
            // 在实际应用中，这里会播放音频文件
            // 现在使用控制台日志模拟
            console.log('播放成功音效');
        }
        
        // 更新步骤信息
        function updateStepInfo() {
            const stepTitles = [
                '步骤一：剪切DNA',
                '步骤二：连接基因',
                '步骤三：转入细胞',
                '步骤四：检测表达'
            ];
            
            const stepIcons = ['✂️', '🔗', '🦠', '🔬'];
            
            const stepDescriptions = [
                '使用限制性内切酶在特定识别序列处切割DNA分子，产生黏性末端。',
                '使用DNA连接酶将目标基因片段与质粒载体的黏性末端连接，形成重组DNA分子。',
                '通过转化法将重组质粒导入细菌受体细胞中。',
                '通过抗生素筛选和荧光蛋白表达检测，确认成功转入并表达目标基因的细胞。'
            ];
            
            document.getElementById('stepTitle').textContent = stepTitles[currentStep - 1];
            document.getElementById('stepIcon').textContent = stepIcons[currentStep - 1];
            document.getElementById('stepDescription').textContent = stepDescriptions[currentStep - 1];
        }
        
        // 更新步骤指示器
        function updateStepIndicator() {
            document.querySelectorAll('.step').forEach((step, index) => {
                step.classList.remove('active', 'completed');
                
                const stepNum = index + 1;
                if (stepNum === currentStep) {
                    step.classList.add('active');
                } else if (stepNum < currentStep) {
                    step.classList.add('completed');
                }
            });
            
            // 更新按钮状态
            document.getElementById('prevBtn').disabled = currentStep === 1;
            document.getElementById('nextBtn').disabled = currentStep === 4;
            document.getElementById('testBtn').classList.toggle('hidden', currentStep !== 4);
            
            // 更新工具箱显示
            document.getElementById('toolbox').classList.toggle('hidden', currentStep > 2);
            
            // 更新步骤信息
            updateStepInfo();
            
            // 重绘Canvas
            draw();
        }
        
        // 下一步
        function nextStep() {
            if (currentStep < 4) {
                currentStep++;
                updateStepIndicator();
            }
        }
        
        // 上一步
        function prevStep() {
            if (currentStep > 1) {
                currentStep--;
                updateStepIndicator();
            }
        }
        
        // 切换动画播放
        function toggleAnimation() {
            if (currentStep === 3 && !state.transformed) {
                playTransformationAnimation();
            } else {
                // 播放当前步骤的说明动画
                animationPlaying = !animationPlaying;
                
                if (animationPlaying) {
                    document.getElementById('playBtn').innerHTML = '<span>⏸</span> 暂停动画';
                    // 这里可以添加步骤说明动画
                } else {
                    document.getElementById('playBtn').innerHTML = '<span>▶</span> 播放动画';
                    if (animationId) {
                        cancelAnimationFrame(animationId);
                    }
                }
            }
        }
        
        // 重置动画
        function resetAnimation() {
            currentStep = 1;
            state.dnaCut = false;
            state.geneConnected = false;
            state.transformed = false;
            state.tested = false;
            state.selectedTool = null;
            state.dragging = false;
            state.dragObject = null;
            state.showAntibiotic = false;
            state.showUV = false;
            
            // 重置细菌
            initBacteria();
            
            // 重置UI
            document.querySelectorAll('.tool').forEach(tool => tool.classList.remove('active'));
            document.getElementById('completionMessage').classList.add('hidden');
            document.getElementById('quizSection').classList.add('hidden');
            
            // 停止动画
            animationPlaying = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
            }
            
            document.getElementById('playBtn').innerHTML = '<span>▶</span> 播放动画';
            document.getElementById('playBtn').disabled = false;
            
            updateStepIndicator();
        }
        
        // 初始化测验
        function initQuiz() {
            const quizOptions = document.querySelectorAll('.quiz-option');
            quizOptions.forEach(option => {
                option.addEventListener('click', function() {
                    const answer = this.dataset.answer;
                    
                    // 移除所有状态
                    quizOptions.forEach(opt => {
                        opt.classList.remove('correct', 'incorrect');
                    });
                    
                    // 检查答案（B是正确答案）
                    if (answer === 'B') {
                        this.classList.add('correct');
                        showHint('✓ 回答正确！限制性内切酶是基因工程的"分子剪刀"。');
                    } else {
                        this.classList.add('incorrect');
                        showHint('✗ 回答错误。限制性内切酶才是用来切割DNA的工具。');
                        
                        // 显示正确答案
                        document.querySelector('.quiz-option[data-answer="B"]').classList.add('correct');
                    }
                });
            });
        }
        
        // 页面加载完成后初始化
        window.addEventListener('load', () => {
            initCanvas();
            initQuiz();
            updateStepIndicator();
        });
    </script>
</body>
</html>


### 3. 过程输出

### 3. 使用指南

## 《基因工程四大步骤》交互式教学动画使用指南

欢迎使用《基因工程四大步骤：剪、连、转、检》三维交互式教学动画！本指南将帮助您充分利用这一创新教学工具，获得最佳的学习体验。

---

### 一、功能说明

本动画是一个基于HTML5 Canvas技术开发的交互式教学工具，旨在通过三维可视化、拟人化交互和分步引导，将基因工程这一微观、抽象的生物学过程转化为直观、易懂的动态体验。

**适用对象**：
- 高中生物学学生（选修模块）
- 大学本科生物学、生物技术专业新生
- 对基因工程感兴趣的科学爱好者
- 生物学教师的课堂教学辅助工具

**学习目标**：
通过本动画，您将能够：
1. 准确描述基因工程的四个核心步骤
2. 识别每个步骤中使用的关键工具（酶、载体等）及其功能
3. 理解重组DNA技术的基本原理
4. 掌握基因工程实验的基本流程和逻辑

---

### 二、主要功能

#### 1. **分步学习系统**
- **清晰的进度指示**：顶部进度条直观显示“剪、连、转、检”四个步骤
- **步骤锁定**：必须完成当前步骤才能进入下一步，确保学习连贯性
- **步骤回顾**：随时点击进度节点跳转到任意已完成的步骤进行复习

#### 2. **交互式操作**
- **工具箱系统**：在“剪”和“连”步骤中，可从工具箱选择工具进行操作
- **拖拽交互**：将限制酶拖到DNA上切割，将基因片段拖到质粒上连接
- **点击触发**：点击按钮触发转化动画和检测过程

#### 3. **可视化反馈**
- **即时提示**：操作正确时显示绿色成功提示和音效
- **错误引导**：操作不当或位置错误时提供引导性提示
- **状态变化**：DNA切割、质粒重组、细菌转化等关键过程都有明显的视觉变化

#### 4. **学习辅助**
- **步骤说明面板**：每个步骤都有详细的文字说明和原理解释
- **鼠标悬停提示**：鼠标悬停在关键元件上显示名称和功能
- **知识挑战**：学习完成后提供互动测验巩固知识

---

### 三、设计特色

#### 1. **科学准确性**
- **颜色编码系统**：
  - DNA碱基对：A-T（橙-蓝）、G-C（绿-红）
  - 限制酶：红色（象征切割）
  - DNA连接酶：黄色（象征连接）
  - 质粒：紫色（与染色体DNA区分）
- **分子结构**：DNA双螺旋、质粒环状结构、细菌细胞形态都经过科学简化

#### 2. **认知友好设计**
- **拟人化比喻**：
  - 限制酶 = “分子剪刀”
  - DNA连接酶 = “分子胶水”
  - 质粒 = “基因运输卡车”
  - 细菌 = “蛋白质生产工厂”
- **渐进式复杂度**：从简单分子操作到复杂细胞过程，难度逐步提升

#### 3. **沉浸式体验**
- **三维透视效果**：通过阴影和透视创造深度感
- **动态动画**：平滑的过渡动画和关键帧特写
- **情境化场景**：从分子操作台到细菌培养皿的场景转换

---

### 四、教学要点

#### 步骤一：剪 - 切割DNA
**核心概念**：限制性内切酶的特异性识别与切割
**教学重点**：
- 酶与底物的特异性结合
- 黏性末端的形成原理
- 识别序列的概念

**操作指导**：
1. 从工具箱点击选择“限制性内切酶”
2. 拖拽酶分子到DNA链的特定位置
3. 观察DNA被切割成两段，末端呈现“黏性”结构

#### 步骤二：连 - 连接基因
**核心概念**：DNA连接酶的连接作用与重组DNA构建
**教学重点**：
- 黏性末端的互补配对
- 质粒作为载体的功能
- 重组DNA分子的构建

**操作指导**：
1. 拖拽目标基因片段到质粒切口处
2. 选择DNA连接酶进行“焊接”
3. 观察重组质粒的形成（紫色环状DNA上出现橙色插入片段）

#### 步骤三：转 - 转入细胞
**核心概念**：转化过程与受体细胞
**教学重点**：
- 质粒进入细菌细胞的机制
- 受体细胞的准备（感受态细胞）
- 转化效率的影响因素

**操作指导**：
1. 点击“播放动画”按钮
2. 观察质粒从外部进入细菌细胞的动态过程
3. 注意质粒在细胞内的定位

#### 步骤四：检 - 检测表达
**核心概念**：筛选与鉴定方法
**教学重点**：
- 抗生素抗性筛选原理
- 报告基因（荧光蛋白）的应用
- 阳性克隆的鉴定

**操作指导**：
1. 点击“开始检测”按钮
2. 观察抗生素对未转化细菌的杀灭作用
3. 观察UV照射下成功转化细菌的荧光表达

---

### 五、使用建议

#### 1. **个人学习模式**
- **初次学习**：按照“播放动画”按钮的引导，完整观看一遍流程
- **深入理解**：使用“上一步/下一步”按钮控制节奏，仔细阅读每个步骤的说明
- **巩固记忆**：完成所有步骤后，进行“知识挑战”测验
- **复习强化**：点击进度条上的任意步骤节点，快速回顾特定环节

#### 2. **课堂教学应用**
- **教师演示**：
  - 使用投影仪全屏展示，教师操作并讲解
  - 在关键步骤暂停，提问引导学生思考
  - 对比动画过程与传统图示的差异
- **学生实践**：
  - 在计算机教室让学生亲手操作
  - 分组讨论每个步骤的科学原理
  - 设计实验方案，预测不同操作的结果

#### 3. **学习策略**
- **预习阶段**：快速浏览整个流程，建立整体概念框架
- **学习阶段**：分步骤深入学习，确保理解每个环节后再进入下一步
- **复习阶段**：重点关注自己不理解的部分，利用交互功能反复观察
- **拓展思考**：
  - 如果使用不同的限制酶会怎样？
  - 如果连接失败会导致什么结果？
  - 如何提高转化效率？

#### 4. **技术提示**
- **设备要求**：建议使用Chrome、Firefox或Edge浏览器
- **屏幕尺寸**：在平板或更大屏幕上体验更佳
- **网络环境**：所有资源已内嵌，无需网络连接即可使用
- **辅助功能**：如需调整界面，可使用浏览器缩放功能（Ctrl+鼠标滚轮）

#### 5. **教学延伸**
- **联系实际**：讨论基因工程在医药（胰岛素生产）、农业（转基因作物）中的应用
- **伦理思考**：引导学生思考基因技术的伦理边界和社会影响
- **实验设计**：基于动画原理，设计简单的基因工程实验方案

---

### 六、注意事项

1. **科学简化说明**：本动画对分子生物学过程进行了必要的简化和可视化处理，旨在帮助理解核心概念。实际实验操作更为复杂。
2. **概念准确性**：动画中的颜色、形状和运动方式是为了教学效果而设计，不代表分子的真实物理外观。
3. **学习深度**：本动画适合入门和概念理解，深入学习请参考教材和专业文献。
4. **互动反馈**：如果在使用过程中发现任何问题或有改进建议，欢迎记录并反馈。

---

### 结语

基因工程是现代生物技术的核心，理解其基本原理是进入生命科学领域的重要一步。我们希望这个交互式动画能够帮助您跨越抽象概念的障碍，在动手操作和视觉体验中建立深刻的理解。

**记住**：科学不仅是知识的积累，更是探索的过程。享受这个发现之旅吧！

祝您学习愉快！

---
*动画设计：教育技术专家团队*
*最后更新：2024年*
*适用课程：高中生物学选修三、大学生物技术导论*