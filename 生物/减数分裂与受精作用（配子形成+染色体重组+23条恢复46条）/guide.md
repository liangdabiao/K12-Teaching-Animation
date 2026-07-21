# 需求：减数分裂与受精作用（配子形成+染色体重组+23条恢复46条）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为高中或大学低年级的生物学学习者。他们需要理解减数分裂和受精作用的动态过程、核心机制及其生物学意义。
2.  **核心痛点**：
    *   **过程抽象**：减数分裂的两次连续分裂、同源染色体配对与分离、非同源染色体自由组合等过程在静态图片中难以连贯理解。
    *   **概念混淆**：容易混淆有丝分裂与减数分裂，对“染色体数目减半”发生在哪个阶段、为何减半、如何通过受精恢复等关键点感到困惑。
    *   **重组机制模糊**：对交叉互换（染色体重组）的具体发生位置（非姐妹染色单体之间）和遗传学意义理解不深。
    *   **整体图景缺失**：难以将配子形成（减数分裂）与个体生命起源（受精作用）联系起来，形成“染色体数目变化：46→23→46”的完整生命循环认知。
3.  **学习目标**：通过动画，用户应能清晰描述减数分裂各阶段的关键事件，解释配子染色体数目减半的原因，理解交叉互换如何增加遗传多样性，并阐明受精作用如何恢复染色体数目及保证物种遗传稳定性。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）
1.  **核心概念聚焦**：
    *   **主线**：体细胞（2n=46）→ **减数分裂I**（同源染色体分离）→ 次级性母细胞（n=23，但每条含两个染色单体）→ **减数分裂II**（姐妹染色单体分离）→ 配子（n=23）→ **受精作用**（雌雄配子结合）→ 受精卵（2n=46）。
    *   **关键机制**：同源染色体的**配对（联会）** 与**分离**；非姐妹染色单体间的**交叉互换**；非同源染色体的**自由组合**；配子细胞核的**融合**。
2.  **认知规律遵循**：
    *   **从整体到局部**：先展示完整的“46→23→46”生命循环概览图，再分步深入减数分裂I、II和受精的细节。
    *   **分解复杂过程**：将连续的减数分裂分解为可暂停、可重复的阶段性动画（间期、前期I、中期I等）。
    *   **对比强化认知**：在关键点（如中期I与中期II的染色体排列方式）提供与有丝分裂的简要对比提示。
    *   **可视化抽象概念**：用不同颜色区分父源和母源染色体，用“交换片段”的动画直观展示交叉互换，用数字（46， 23）实时显示染色体数目变化。
3.  **交互设计策略**：
    *   **叙事控制**：提供“播放/暂停/重置”全局控制，以及“上一步/下一步”的阶段步进控制，让用户自主掌控学习节奏。
    *   **探索式学习**：
        *   点击特定染色体，高亮并显示其信息（如“父源染色体1”）。
        *   在交叉互换环节，允许用户手动点击触发交换，观察片段交换过程。
        *   在自由组合环节，设计一个模拟小实验，让用户多次“生成”配子，观察染色体组合的随机性。
    *   **反馈与提示**：每个阶段有简洁的文字说明；关键步骤有视觉高亮和音效提示；提供“概念检查”弹出式小问题（如：现在细胞中有多少条染色体？）。
4.  **视觉呈现方案**：
    *   **风格**：采用简洁、扁平化的卡通风格，避免过多细节干扰，重点突出染色体结构和运动。
    *   **染色体设计**：用不同颜色的“X”形结构表示复制后的染色体（包含两个姐妹染色单体）。父源与母源同源染色体使用同一色系的不同深浅（如深蓝与浅蓝）表示。
    *   **细胞结构**：细胞膜/壁、纺锤体等背景元素用极简线条表示，颜色浅淡，确保染色体始终为视觉焦点。
    *   **动态效果**：染色体移动平滑，分离过程清晰。交叉互换时，有明确的“断开-重接”动画。受精时，配子结合有吸引和融合的动画。

#### 配色方案选择
*   **主色调**：采用科学、冷静的蓝色系，传达专业和清晰感。
    *   背景/画布：浅灰蓝色 (#F0F5FF)
    *   细胞质/膜：半透明浅蓝色 (#E6F0FF) 与灰色细边框
*   **染色体配色（关键）**：
    *   **父源染色体**：稳重的深蓝色系（如 #2C5AA0 表示染色体， #5A8CD0 表示染色单体）。
    *   **母源染色体**：柔和的红紫色系（如 #A02C6B 表示染色体， #D05A94 表示染色单体）。
    *   *使用对比色系能清晰区分父母来源，同时色系统一保持视觉和谐。*
*   **高亮与交互色**：
    *   选中/高亮：明黄色 (#FFEB3B)
    *   交换片段：橙色 (#FF9800)
    *   纺锤丝：浅灰色 (#CCCCCC)
*   **文字与UI**：
    *   说明文字：深灰色 (#333333)
    *   按钮：主蓝色 (#2C5AA0)，悬停态稍浅 (#5A8CD0)
    *   正确反馈：绿色 (#4CAF50)
    *   错误/提示反馈：橙色 (#FF9800)

#### 交互功能列表
1.  **主流程控制**：
    *   播放/暂停/重置 动画按钮。
    *   “生命循环概览”、“减数分裂详解”、“受精作用”三大模块切换标签。
2.  **减数分裂阶段控制**：
    *   “上一步/下一步”按钮，用于在减数分裂各子阶段（间期，前期I，中期I…末期II）间步进。
    *   可点击的阶段进度条，快速跳转。
3.  **探索性交互**：
    *   **点击染色体**：高亮显示该染色体，并弹出标签说明其来源（父/母）及编号。
    *   **触发交叉互换**：在前期I，提供一个“手动交换”按钮，用户点击后，动画演示指定同源染色体间非姐妹染色单体的片段交换。
    *   **模拟配子生成**：在减数分裂完成后，提供一个“随机生成配子”按钮，多次点击模拟非同源染色体自由组合，生成染色体组成不同的配子，并显示其组合编号。
4.  **认知辅助功能**：
    *   **实时计数器**：始终显示当前细胞中的“染色体数目”（例如：46条 → 23条 → 46条）。
    *   **关键概念提示框**：当动画进行到关键步骤（如联会、交叉互换、同源染色体分离）时，自动弹出简要的文字解释。
    *   **迷你测验**：在关键节点后，弹出选择题（如：“同源染色体分离发生在哪一次分裂？”），提供即时反馈。
5.  **视觉辅助开关**：
    *   显示/隐藏 纺锤体开关。
    *   显示/隐藏 染色体上基因位点（用小圆点表示）的开关，用于辅助解释交叉互换。
    *   切换 染色体简化视图（单色条状）与详细视图（双染色单体“X”形）的开关。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>减数分裂与受精作用教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background-color: #f0f5ff;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid #2c5aa0;
        }

        h1 {
            color: #2c5aa0;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .main-container {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .module-tabs {
            display: flex;
            background: #e6f0ff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 3px 6px rgba(0,0,0,0.08);
        }

        .tab {
            flex: 1;
            padding: 15px;
            text-align: center;
            background: transparent;
            border: none;
            font-size: 16px;
            font-weight: 600;
            color: #2c5aa0;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .tab:hover {
            background: rgba(44, 90, 160, 0.1);
        }

        .tab.active {
            background: #2c5aa0;
            color: white;
        }

        .animation-container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        .canvas-wrapper {
            position: relative;
            width: 100%;
            height: 500px;
            background: #f8fbff;
            border-radius: 8px;
            border: 1px solid #d0e0ff;
            margin-bottom: 20px;
            overflow: hidden;
        }

        #animationCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .chromosome-counter {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255, 255, 255, 0.9);
            padding: 10px 15px;
            border-radius: 20px;
            font-weight: bold;
            box-shadow: 0 3px 8px rgba(0,0,0,0.15);
            border: 2px solid #2c5aa0;
            z-index: 10;
        }

        .counter-number {
            color: #2c5aa0;
            font-size: 1.8em;
            margin: 0 5px;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 20px;
            padding: 15px;
            background: #f8fbff;
            border-radius: 8px;
        }

        .control-group {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        button {
            padding: 10px 18px;
            background: #2c5aa0;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        button:hover {
            background: #5a8cd0;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }

        button:active {
            transform: translateY(0);
        }

        button.secondary {
            background: #a02c6b;
        }

        button.secondary:hover {
            background: #d05a94;
        }

        button.small {
            padding: 8px 14px;
            font-size: 14px;
        }

        .stage-indicator {
            display: flex;
            align-items: center;
            background: white;
            padding: 10px 15px;
            border-radius: 8px;
            border: 1px solid #d0e0ff;
            min-width: 200px;
        }

        .stage-name {
            font-weight: bold;
            color: #2c5aa0;
            margin-right: 10px;
        }

        .stage-progress {
            flex: 1;
            height: 8px;
            background: #e6f0ff;
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #2c5aa0, #5a8cd0);
            width: 0%;
            transition: width 0.5s ease;
        }

        .info-panel {
            background: white;
            border-radius: 8px;
            padding: 20px;
            border-left: 5px solid #4CAF50;
            box-shadow: 0 3px 8px rgba(0,0,0,0.08);
            margin-top: 20px;
        }

        .info-title {
            color: #2c5aa0;
            margin-bottom: 10px;
            font-size: 1.2em;
        }

        .info-content {
            color: #444;
            line-height: 1.7;
        }

        .highlight {
            color: #2c5aa0;
            font-weight: bold;
        }

        .interactive-panel {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
            padding: 20px;
            background: #f8fbff;
            border-radius: 8px;
            border: 1px dashed #5a8cd0;
        }

        .panel-title {
            width: 100%;
            color: #2c5aa0;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .toggle-switch {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .toggle-label {
            font-weight: 500;
        }

        .quiz-popup {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            z-index: 100;
            display: none;
            width: 90%;
            max-width: 500px;
        }

        .quiz-question {
            margin-bottom: 20px;
            font-size: 1.1em;
            color: #333;
        }

        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }

        .quiz-option {
            padding: 12px;
            background: #f0f5ff;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .quiz-option:hover {
            background: #e6f0ff;
        }

        .quiz-option.correct {
            background: #d4edda;
            border-left: 4px solid #4CAF50;
        }

        .quiz-option.incorrect {
            background: #f8d7da;
            border-left: 4px solid #f44336;
        }

        .close-quiz {
            background: #2c5aa0;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            float: right;
        }

        .chromosome-legend {
            display: flex;
            justify-content: center;
            gap: 30px;
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
            border-radius: 4px;
        }

        .legend-text {
            font-size: 14px;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #d0e0ff;
            color: #666;
            font-size: 0.9em;
        }

        @media (max-width: 768px) {
            .controls {
                flex-direction: column;
            }
            
            .stage-indicator {
                min-width: 100%;
            }
            
            .chromosome-legend {
                flex-direction: column;
                gap: 10px;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>减数分裂与受精作用教学动画</h1>
        <p class="subtitle">配子形成 + 染色体重组 + 23条恢复46条的生命循环</p>
    </header>

    <div class="main-container">
        <div class="module-tabs">
            <button class="tab active" data-module="overview">生命循环概览</button>
            <button class="tab" data-module="meiosis">减数分裂详解</button>
            <button class="tab" data-module="fertilization">受精作用</button>
        </div>

        <div class="animation-container">
            <div class="canvas-wrapper">
                <canvas id="animationCanvas" width="1000" height="500"></canvas>
                <div class="chromosome-counter">
                    染色体数目: <span class="counter-number">46</span> 条
                </div>
            </div>

            <div class="controls">
                <div class="control-group">
                    <button id="playBtn">
                        <span>▶</span> 播放
                    </button>
                    <button id="pauseBtn">
                        <span>⏸</span> 暂停
                    </button>
                    <button id="resetBtn">
                        <span>↺</span> 重置
                    </button>
                </div>

                <div class="control-group">
                    <button id="prevBtn" class="small">
                        <span>←</span> 上一步
                    </button>
                    <button id="nextBtn" class="small">
                        下一步 <span>→</span>
                    </button>
                </div>

                <div class="stage-indicator">
                    <div class="stage-name">间期</div>
                    <div class="stage-progress">
                        <div class="progress-bar" id="progressBar"></div>
                    </div>
                </div>

                <div class="control-group">
                    <button id="crossoverBtn" class="secondary small">
                        <span>🔄</span> 手动交叉互换
                    </button>
                    <button id="generateGameteBtn" class="secondary small">
                        <span>🎲</span> 随机生成配子
                    </button>
                </div>
            </div>

            <div class="interactive-panel">
                <div class="panel-title">视觉辅助选项</div>
                <div class="toggle-switch">
                    <input type="checkbox" id="spindleToggle" checked>
                    <label for="spindleToggle" class="toggle-label">显示纺锤体</label>
                </div>
                <div class="toggle-switch">
                    <input type="checkbox" id="geneToggle">
                    <label for="geneToggle" class="toggle-label">显示基因位点</label>
                </div>
                <div class="toggle-switch">
                    <input type="checkbox" id="detailedViewToggle" checked>
                    <label for="detailedViewToggle" class="toggle-label">详细视图 (X形染色体)</label>
                </div>
            </div>

            <div class="chromosome-legend">
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #2c5aa0;"></div>
                    <div class="legend-text">父源染色体</div>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #a02c6b;"></div>
                    <div class="legend-text">母源染色体</div>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: linear-gradient(45deg, #2c5aa0 50%, #a02c6b 50%);"></div>
                    <div class="legend-text">重组染色体 (交叉互换后)</div>
                </div>
            </div>

            <div class="info-panel">
                <div class="info-title" id="infoTitle">减数分裂概述</div>
                <div class="info-content" id="infoContent">
                    减数分裂是产生配子（精子和卵细胞）的特殊细胞分裂方式。一个二倍体细胞经过一次DNA复制和两次连续分裂，产生四个单倍体细胞。染色体数目从<span class="highlight">46条（二倍体）</span>减少到<span class="highlight">23条（单倍体）</span>。
                </div>
            </div>
        </div>
    </div>

    <div class="quiz-popup" id="quizPopup">
        <div class="quiz-question" id="quizQuestion">同源染色体分离发生在哪一次分裂？</div>
        <div class="quiz-options" id="quizOptions">
            <div class="quiz-option" data-correct="true">减数分裂I</div>
            <div class="quiz-option" data-correct="false">减数分裂II</div>
            <div class="quiz-option" data-correct="false">有丝分裂</div>
            <div class="quiz-option" data-correct="false">两次分裂都会发生</div>
        </div>
        <button class="close-quiz" id="closeQuiz">继续学习</button>
    </div>

    <footer>
        <p>教学动画设计 | 减数分裂与受精作用 | 染色体数目变化: 46 → 23 → 46</p>
        <p>提示：点击染色体可查看详细信息，使用控制按钮调节学习进度</p>
    </footer>

    <script>
        // 全局变量和配置
        const canvas = document.getElementById('animationCanvas');
        const ctx = canvas.getContext('2d');
        const counterElement = document.querySelector('.counter-number');
        const infoTitle = document.getElementById('infoTitle');
        const infoContent = document.getElementById('infoContent');
        const progressBar = document.getElementById('progressBar');
        const stageName = document.querySelector('.stage-name');
        const quizPopup = document.getElementById('quizPopup');
        const quizQuestion = document.getElementById('quizQuestion');
        const quizOptions = document.getElementById('quizOptions');
        
        // 模块状态
        let currentModule = 'overview'; // overview, meiosis, fertilization
        let currentStage = 0;
        let isPlaying = false;
        let animationId = null;
        let lastTime = 0;
        
        // 减数分裂阶段定义
        const meiosisStages = [
            { name: "间期", duration: 3, info: "DNA复制，染色体复制，每条染色体由两个姐妹染色单体组成。" },
            { name: "前期 I", duration: 4, info: "同源染色体配对（联会），非姐妹染色单体间可能发生交叉互换。" },
            { name: "中期 I", duration: 3, info: "同源染色体排列在细胞中央的赤道板上，纺锤体形成。" },
            { name: "后期 I", duration: 3, info: "同源染色体分离，分别移向细胞两极。染色体数目开始减半。" },
            { name: "末期 I", duration: 2, info: "细胞一分为二，形成两个次级性母细胞，每个细胞含有单倍体数目的染色体。" },
            { name: "前期 II", duration: 2, info: "两个次级性母细胞准备第二次分裂，染色体不再复制。" },
            { name: "中期 II", duration: 2, info: "染色体排列在每个细胞的赤道板上，着丝粒分裂准备。" },
            { name: "后期 II", duration: 2, info: "姐妹染色单体分离，成为独立的染色体，移向细胞两极。" },
            { name: "末期 II", duration: 2, info: "细胞分裂完成，形成四个单倍体配子，每个配子含有23条染色体。" }
        ];
        
        const overviewStages = [
            { name: "体细胞", duration: 2, info: "二倍体体细胞，含有46条染色体（23对同源染色体）。" },
            { name: "减数分裂", duration: 5, info: "经过减数分裂I和II，产生四个单倍体配子，每个含有23条染色体。" },
            { name: "配子", duration: 2, info: "精子和卵细胞，各含有23条染色体，遗传物质通过交叉互换和自由组合实现重组。" },
            { name: "受精作用", duration: 3, info: "精子和卵细胞结合，染色体数目恢复为46条，形成受精卵。" },
            { name: "新个体", duration: 2, info: "受精卵经过有丝分裂和分化，发育为新个体，维持物种染色体数目的稳定。" }
        ];
        
        const fertilizationStages = [
            { name: "配子相遇", duration: 2, info: "精子和卵细胞相互识别并靠近。" },
            { name: "精卵结合", duration: 3, info: "精子进入卵细胞，两个细胞核逐渐靠近。" },
            { name: "核膜消失", duration: 2, info: "精子和卵细胞的核膜消失，染色体释放。" },
            { name: "染色体联合", duration: 3, info: "父源和母源染色体在受精卵中配对，恢复二倍体状态。" },
            { name: "受精卵形成", duration: 2, info: "形成含有46条染色体的受精卵，新生命开始。" }
        ];
        
        let stages = overviewStages;
        let stageProgress = 0;
        let stageStartTime = 0;
        
        // 染色体数据
        let chromosomes = [];
        let gametes = [];
        let selectedChromosome = null;
        
        // 交互状态
        let showSpindle = true;
        let showGenes = false;
        let detailedView = true;
        
        // 初始化染色体
        function initChromosomes() {
            chromosomes = [];
            gametes = [];
            
            // 创建23对同源染色体（体细胞）
            for (let i = 0; i < 23; i++) {
                // 父源染色体
                chromosomes.push({
                    id: `p${i}`,
                    type: 'paternal',
                    pairId: i,
                    x: 300 + Math.random() * 400,
                    y: 200 + Math.random() * 100,
                    width: 30,
                    height: 60,
                    replicated: true,
                    chromatids: 2,
                    color: '#2c5aa0',
                    targetX: 0,
                    targetY: 0,
                    moving: false,
                    inGamete: false,
                    crossoverPoints: []
                });
                
                // 母源染色体
                chromosomes.push({
                    id: `m${i}`,
                    type: 'maternal',
                    pairId: i,
                    x: 300 + Math.random() * 400,
                    y: 200 + Math.random() * 100,
                    width: 30,
                    height: 60,
                    replicated: true,
                    chromatids: 2,
                    color: '#a02c6b',
                    targetX: 0,
                    targetY: 0,
                    moving: false,
                    inGamete: false,
                    crossoverPoints: []
                });
            }
            
            updateCounter(46);
        }
        
        // 更新染色体计数器
        function updateCounter(count) {
            counterElement.textContent = count;
            
            // 添加动画效果
            counterElement.style.transform = 'scale(1.2)';
            setTimeout(() => {
                counterElement.style.transform = 'scale(1)';
            }, 300);
        }
        
        // 更新信息面板
        function updateInfoPanel() {
            const stage = stages[currentStage];
            infoTitle.textContent = stage.name;
            infoContent.innerHTML = stage.info;
            
            // 根据阶段添加特定信息
            if (currentModule === 'meiosis') {
                if (currentStage === 1) { // 前期I
                    infoContent.innerHTML += " <span class='highlight'>点击'手动交叉互换'按钮体验重组过程。</span>";
                } else if (currentStage === 8) { // 末期II
                    infoContent.innerHTML += " <span class='highlight'>点击'随机生成配子'按钮观察遗传多样性。</span>";
                }
            }
            
            // 更新进度条
            progressBar.style.width = `${(currentStage / (stages.length - 1)) * 100}%`;
            stageName.textContent = stage.name;
        }
        
        // 绘制染色体
        function drawChromosome(chromo) {
            ctx.save();
            
            if (chromo.inGamete && currentModule === 'fertilization') {
                // 在受精作用中，配子中的染色体较小
                ctx.translate(chromo.x, chromo.y);
                ctx.scale(0.7, 0.7);
            } else {
                ctx.translate(chromo.x, chromo.y);
            }
            
            // 绘制染色体主体
            if (detailedView && chromo.replicated) {
                // 详细视图：X形染色体（两个染色单体）
                ctx.fillStyle = chromo.color;
                
                // 绘制两个染色单体
                ctx.save();
                ctx.rotate(Math.PI / 12); // 轻微旋转
                ctx.fillRect(-chromo.width/2, -chromo.height/2, chromo.width, chromo.height);
                ctx.restore();
                
                ctx.save();
                ctx.rotate(-Math.PI / 12);
                ctx.fillRect(-chromo.width/2, -chromo.height/2, chromo.width, chromo.height);
                ctx.restore();
                
                // 绘制着丝粒
                ctx.fillStyle = '#333';
                ctx.fillRect(-5, -5, 10, 10);
                
                // 如果显示基因位点
                if (showGenes) {
                    ctx.fillStyle = '#FF9800';
                    for (let i = 0; i < 3; i++) {
                        const yPos = -chromo.height/2 + 20 + i * 20;
                        ctx.beginPath();
                        ctx.arc(0, yPos, 3, 0, Math.PI * 2);
                        ctx.fill();
                    }
                }
                
                // 绘制交叉互换点
                if (chromo.crossoverPoints.length > 0) {
                    ctx.fillStyle = '#FF9800';
                    chromo.crossoverPoints.forEach(point => {
                        ctx.beginPath();
                        ctx.arc(0, point, 5, 0, Math.PI * 2);
                        ctx.fill();
                    });
                }
                
            } else {
                // 简化视图：单色条状
                ctx.fillStyle = chromo.color;
                ctx.fillRect(-chromo.width/2, -chromo.height/2, chromo.width, chromo.height);
                
                // 绘制着丝粒
                ctx.fillStyle = '#333';
                ctx.fillRect(-4, -4, 8, 8);
            }
            
            // 如果被选中，绘制高亮边框
            if (selectedChromosome && selectedChromosome.id === chromo.id) {
                ctx.strokeStyle = '#FFEB3B';
                ctx.lineWidth = 3;
                ctx.strokeRect(-chromo.width/2 - 5, -chromo.height/2 - 5, chromo.width + 10, chromo.height + 10);
            }
            
            ctx.restore();
        }
        
        // 绘制细胞
        function drawCell() {
            // 绘制细胞膜
            ctx.strokeStyle = '#999';
            ctx.lineWidth = 2;
            ctx.setLineDash([]);
            
            if (currentModule === 'overview' || currentModule === 'meiosis') {
                if (currentStage >= 4 && currentStage <= 8 && currentModule === 'meiosis') {
                    // 减数分裂后期：绘制两个细胞
                    ctx.beginPath();
                    ctx.arc(250, 250, 120, 0, Math.PI * 2);
                    ctx.stroke();
                    
                    ctx.beginPath();
                    ctx.arc(750, 250, 120, 0, Math.PI * 2);
                    ctx.stroke();
                    
                    if (currentStage >= 6) {
                        // 减数分裂II：绘制四个细胞
                        ctx.beginPath();
                        ctx.arc(200, 200, 80, 0, Math.PI * 2);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.arc(300, 300, 80, 0, Math.PI * 2);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.arc(700, 200, 80, 0, Math.PI * 2);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.arc(800, 300, 80, 0, Math.PI * 2);
                        ctx.stroke();
                    }
                } else {
                    // 单个细胞
                    ctx.beginPath();
                    ctx.arc(500, 250, 180, 0, Math.PI * 2);
                    ctx.stroke();
                }
            } else if (currentModule === 'fertilization') {
                // 受精作用：绘制两个配子细胞
                ctx.beginPath();
                ctx.arc(350, 250, 80, 0, Math.PI * 2);
                ctx.stroke();
                ctx.fillStyle = 'rgba(90, 140, 208, 0.1)';
                ctx.fill();
                
                ctx.beginPath();
                ctx.arc(650, 250, 80, 0, Math.PI * 2);
                ctx.stroke();
                ctx.fillStyle = 'rgba(208, 90, 148, 0.1)';
                ctx.fill();
                
                if (currentStage >= 3) {
                    // 绘制融合后的受精卵
                    ctx.beginPath();
                    ctx.arc(500, 250, 120, 0, Math.PI * 2);
                    ctx.stroke();
                    ctx.fillStyle = 'rgba(76, 175, 80, 0.1)';
                    ctx.fill();
                }
            }
            
            // 绘制纺锤体
            if (showSpindle && (currentModule === 'meiosis' || currentModule === 'overview')) {
                if (currentStage === 2 || currentStage === 3 || currentStage === 6 || currentStage === 7) {
                    ctx.strokeStyle = '#CCCCCC';
                    ctx.lineWidth = 2;
                    ctx.setLineDash([5, 5]);
                    
                    const centerX = currentStage >= 4 && currentStage <= 8 ? (currentStage >= 6 ? [200, 300, 700, 800] : [250, 750]) : [500];
                    
                    if (Array.isArray(centerX)) {
                        centerX.forEach(x => {
                            const y = x === 200 || x === 700 ? 200 : 300;
                            ctx.beginPath();
                            ctx.moveTo(x, y - 100);
                            ctx.lineTo(x, y + 100);
                            ctx.stroke();
                            
                            ctx.beginPath();
                            ctx.moveTo(x - 80, y - 60);
                            ctx.lineTo(x + 80, y - 60);
                            ctx.stroke();
                            
                            ctx.beginPath();
                            ctx.moveTo(x - 80, y + 60);
                            ctx.lineTo(x + 80, y + 60);
                            ctx.stroke();
                        });
                    } else {
                        ctx.beginPath();
                        ctx.moveTo(centerX, 100);
                        ctx.lineTo(centerX, 400);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.moveTo(centerX - 150, 150);
                        ctx.lineTo(centerX + 150, 150);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.moveTo(centerX - 150, 350);
                        ctx.lineTo(centerX + 150, 350);
                        ctx.stroke();
                    }
                    ctx.setLineDash([]);
                }
            }
        }
        
        // 绘制配子
        function drawGametes() {
            if (gametes.length === 0) return;
            
            ctx.fillStyle = 'rgba(44, 90, 160, 0.8)';
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            
            gametes.forEach((gamete, index) => {
                const x = 150 + index * 200;
                const y = 400;
                
                // 绘制配子细胞
                ctx.beginPath();
                ctx.arc(x, y, 40, 0, Math.PI * 2);
                ctx.stroke();
                
                // 绘制配子中的染色体
                gamete.chromosomes.forEach((chromo, i) => {
                    ctx.save();
                    ctx.translate(x - 20 + (i % 3) * 20, y - 10 + Math.floor(i / 3) * 20);
                    
                    ctx.fillStyle = chromo.type === 'paternal' ? '#2c5aa0' : '#a02c6b';
                    ctx.fillRect(-5, -8, 10, 16);
                    
                    ctx.restore();
                });
                
                // 显示配子编号
                ctx.fillText(`配子 ${index + 1}`, x, y + 60);
                ctx.fillText(`${gamete.chromosomes.length}条染色体`, x, y + 80);
            });
        }
        
        // 更新染色体位置（动画）
        function updateChromosomes(deltaTime) {
            if (!isPlaying) return;
            
            stageProgress += deltaTime / 1000; // 转换为秒
            
            const stage = stages[currentStage];
            const progress = Math.min(stageProgress / stage.duration, 1);
            
            // 根据当前模块和阶段更新染色体位置
            switch(currentModule) {
                case 'overview':
                    updateOverviewPositions(progress);
                    break;
                case 'meiosis':
                    updateMeiosisPositions(progress);
                    break;
                case 'fertilization':
                    updateFertilizationPositions(progress);
                    break;
            }
            
            // 如果当前阶段完成，进入下一阶段
            if (progress >= 1) {
                nextStage();
            }
        }
        
        // 更新概览模块的染色体位置
        function updateOverviewPositions(progress) {
            switch(currentStage) {
                case 0: // 体细胞
                    chromosomes.forEach((chromo, i) => {
                        const angle = (i / chromosomes.length) * Math.PI * 2;
                        const radius = 120;
                        chromo.x = 500 + Math.cos(angle) * radius;
                        chromo.y = 250 + Math.sin(angle) * radius;
                    });
                    break;
                    
                case 1: // 减数分裂
                    if (progress < 0.5) {
                        // 减数分裂I：同源染色体分离
                        chromosomes.forEach((chromo, i) => {
                            const targetX = chromo.type === 'paternal' ? 300 : 700;
                            const targetY = 250 + (i % 10) * 20 - 100;
                            chromo.x += (targetX - chromo.x) * 0.05;
                            chromo.y += (targetY - chromo.y) * 0.05;
                        });
                        
                        if (progress > 0.3 && progress < 0.4) {
                            updateCounter(23);
                        }
                    } else {
                        // 减数分裂II：姐妹染色单体分离
                        chromosomes.forEach((chromo, i) => {
                            const baseX = chromo.type === 'paternal' ? 300 : 700;
                            const quadrant = Math.floor(i / 6) % 4;
                            let targetX, targetY;
                            
                            switch(quadrant) {
                                case 0: targetX = baseX - 50; targetY = 200; break;
                                case 1: targetX = baseX + 50; targetY = 200; break;
                                case 2: targetX = baseX - 50; targetY = 300; break;
                                case 3: targetX = baseX + 50; targetY = 300; break;
                            }
                            
                            chromo.x += (targetX - chromo.x) * 0.05;
                            chromo.y += (targetY - chromo.y) * 0.05;
                        });
                    }
                    break;
                    
                case 2: // 配子
                    // 配子中的染色体聚集
                    chromosomes.forEach((chromo, i) => {
                        const gameteIndex = Math.floor(i / 23);
                        const x = 150 + gameteIndex * 200;
                        const y = 400;
                        
                        chromo.x += (x - chromo.x) * 0.05;
                        chromo.y += (y - chromo.y) * 0.05;
                        chromo.inGamete = true;
                    });
                    break;
                    
                case 3: // 受精作用
                    // 配子向中心移动
                    chromosomes.forEach((chromo, i) => {
                        const isPaternal = chromo.type === 'paternal';
                        const targetX = isPaternal ? 400 : 600;
                        const targetY = 250;
                        
                        chromo.x += (targetX - chromo.x) * 0.05;
                        chromo.y += (targetY - chromo.y) * 0.05;
                    });
                    break;
                    
                case 4: // 新个体
                    // 染色体分散在受精卵中
                    chromosomes.forEach((chromo, i) => {
                        const angle = (i / chromosomes.length) * Math.PI * 2;
                        const radius = 80;
                        chromo.x = 500 + Math.cos(angle) * radius;
                        chromo.y = 250 + Math.sin(angle) * radius;
                        chromo.inGamete = false;
                    });
                    updateCounter(46);
                    break;
            }
        }
        
        // 更新减数分裂模块的染色体位置
        function updateMeiosisPositions(progress) {
            // 根据减数分裂阶段更新位置
            // 这里简化实现，实际应根据每个阶段的具体生物学过程
            chromosomes.forEach((chromo, i) => {
                let targetX, targetY;
                
                switch(currentStage) {
                    case 0: // 间期
                        targetX = 500 + (i % 10) * 30 - 150;
                        targetY = 250 + Math.floor(i / 10) * 30 - 75;
                        break;
                        
                    case 1: // 前期I - 同源染色体配对
                        const pairX = 500 + (chromo.pairId % 8) * 40 - 160;
                        const pairY = 250 + Math.floor(chromo.pairId / 8) * 40 - 80;
                        targetX = pairX + (chromo.type === 'paternal' ? -15 : 15);
                        targetY = pairY;
                        break;
                        
                    case 2: // 中期I - 排列在赤道板
                        targetX = 500;
                        targetY = 250 + chromo.pairId * 8 - 92;
                        break;
                        
                    case 3: // 后期I - 同源染色体分离
                        targetX = chromo.type === 'paternal' ?
350 : 650;
                        targetY = 250 + (chromo.pairId % 12) * 15 - 90;
                        break;
                        
                    case 4: // 末期I - 形成两个细胞
                        targetX = chromo.type === 'paternal' ? 250 : 750;
                        targetY = 250 + (chromo.pairId % 12) * 15 - 90;
                        break;
                        
                    case 5: // 前期II
                        targetX = chromo.type === 'paternal' ? 250 : 750;
                        targetY = 250 + (chromo.pairId % 12) * 15 - 90;
                        break;
                        
                    case 6: // 中期II
                        const cellOffset = chromo.type === 'paternal' ? 0 : 500;
                        const cellIndex = chromo.pairId % 2;
                        targetX = cellOffset + (cellIndex === 0 ? 200 : 300);
                        targetY = cellIndex === 0 ? 200 : 300;
                        break;
                        
                    case 7: // 后期II - 姐妹染色单体分离
                        const baseCell = chromo.type === 'paternal' ? 0 : 500;
                        const chromoIndex = chromo.pairId % 4;
                        switch(chromoIndex) {
                            case 0: targetX = baseCell + 180; targetY = 180; break;
                            case 1: targetX = baseCell + 220; targetY = 180; break;
                            case 2: targetX = baseCell + 180; targetY = 320; break;
                            case 3: targetX = baseCell + 220; targetY = 320; break;
                        }
                        break;
                        
                    case 8: // 末期II - 四个配子
                        const gameteGroup = chromo.type === 'paternal' ? 0 : 2;
                        const gametePos = chromo.pairId % 4;
                        switch(gameteGroup + (gametePos % 2)) {
                            case 0: targetX = 200; targetY = 200; break;
                            case 1: targetX = 300; targetY = 300; break;
                            case 2: targetX = 700; targetY = 200; break;
                            case 3: targetX = 800; targetY = 300; break;
                        }
                        chromo.inGamete = true;
                        break;
                }
                
                if (targetX !== undefined && targetY !== undefined) {
                    chromo.x += (targetX - chromo.x) * 0.05;
                    chromo.y += (targetY - chromo.y) * 0.05;
                }
            });
            
            // 更新染色体计数器
            if (currentStage === 3 && progress > 0.5) {
                updateCounter(23); // 后期I染色体数目减半
            }
        }
        
        // 更新受精作用模块的染色体位置
        function updateFertilizationPositions(progress) {
            switch(currentStage) {
                case 0: // 配子相遇
                    chromosomes.forEach((chromo, i) => {
                        const isPaternal = chromo.type === 'paternal';
                        const baseX = isPaternal ? 350 : 650;
                        const baseY = 250;
                        const angle = (i / 23) * Math.PI * 2;
                        const radius = 50;
                        
                        chromo.x = baseX + Math.cos(angle) * radius;
                        chromo.y = baseY + Math.sin(angle) * radius;
                        chromo.inGamete = true;
                    });
                    updateCounter(23);
                    break;
                    
                case 1: // 精卵结合
                    chromosomes.forEach((chromo, i) => {
                        const isPaternal = chromo.type === 'paternal';
                        const targetX = isPaternal ? 450 : 550;
                        const targetY = 250;
                        
                        chromo.x += (targetX - chromo.x) * 0.05;
                        chromo.y += (targetY - chromo.y) * 0.05;
                    });
                    break;
                    
                case 2: // 核膜消失
                    chromosomes.forEach((chromo, i) => {
                        const angle = (i / chromosomes.length) * Math.PI * 2;
                        const radius = 80;
                        chromo.x = 500 + Math.cos(angle) * radius;
                        chromo.y = 250 + Math.sin(angle) * radius;
                    });
                    break;
                    
                case 3: // 染色体联合
                    chromosomes.forEach((chromo, i) => {
                        // 同源染色体配对
                        const pairId = chromo.pairId;
                        const isPaternal = chromo.type === 'paternal';
                        const pairX = 500 + (pairId % 8) * 30 - 120;
                        const pairY = 250 + Math.floor(pairId / 8) * 30 - 60;
                        
                        const targetX = pairX + (isPaternal ? -12 : 12);
                        const targetY = pairY;
                        
                        chromo.x += (targetX - chromo.x) * 0.05;
                        chromo.y += (targetY - chromo.y) * 0.05;
                        chromo.inGamete = false;
                    });
                    break;
                    
                case 4: // 受精卵形成
                    chromosomes.forEach((chromo, i) => {
                        const angle = (i / chromosomes.length) * Math.PI * 2;
                        const radius = 60;
                        const targetX = 500 + Math.cos(angle) * radius;
                        const targetY = 250 + Math.sin(angle) * radius;
                        
                        chromo.x += (targetX - chromo.x) * 0.05;
                        chromo.y += (targetY - chromo.y) * 0.05;
                    });
                    updateCounter(46);
                    break;
            }
        }
        
        // 主动画循环
        function animate(timestamp) {
            if (!lastTime) lastTime = timestamp;
            const deltaTime = timestamp - lastTime;
            lastTime = timestamp;
            
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 更新和绘制
            updateChromosomes(deltaTime);
            drawCell();
            
            // 绘制染色体
            chromosomes.forEach(chromo => {
                if (!chromo.inGamete || currentModule === 'fertilization') {
                    drawChromosome(chromo);
                }
            });
            
            // 绘制配子（如果需要）
            if (currentModule === 'overview' && currentStage === 2) {
                drawGametes();
            }
            
            // 继续动画循环
            if (isPlaying || animationId) {
                animationId = requestAnimationFrame(animate);
            }
        }
        
        // 切换到下一阶段
        function nextStage() {
            if (currentStage < stages.length - 1) {
                currentStage++;
                stageProgress = 0;
                updateInfoPanel();
                
                // 检查是否需要弹出测验
                if (currentModule === 'meiosis' && currentStage === 3) {
                    setTimeout(() => showQuiz("同源染色体分离发生在哪一次分裂？", [
                        "减数分裂I",
                        "减数分裂II", 
                        "有丝分裂",
                        "两次分裂都会发生"
                    ], 0), 500);
                }
            } else if (isPlaying) {
                // 如果是自动播放，循环回到第一阶段
                currentStage = 0;
                stageProgress = 0;
                updateInfoPanel();
            }
        }
        
        // 切换到上一阶段
        function prevStage() {
            if (currentStage > 0) {
                currentStage--;
                stageProgress = 0;
                updateInfoPanel();
            }
        }
        
        // 切换模块
        function switchModule(moduleName) {
            currentModule = moduleName;
            currentStage = 0;
            stageProgress = 0;
            
            // 更新标签状态
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.toggle('active', tab.dataset.module === moduleName);
            });
            
            // 设置对应的阶段数据
            switch(moduleName) {
                case 'overview':
                    stages = overviewStages;
                    initChromosomes();
                    break;
                case 'meiosis':
                    stages = meiosisStages;
                    initChromosomes();
                    break;
                case 'fertilization':
                    stages = fertilizationStages;
                    initChromosomes();
                    break;
            }
            
            // 更新按钮状态
            document.getElementById('crossoverBtn').style.display = 
                moduleName === 'meiosis' ? 'flex' : 'none';
            document.getElementById('generateGameteBtn').style.display = 
                moduleName === 'meiosis' ? 'flex' : 'none';
            
            updateInfoPanel();
            
            // 如果正在播放，重新开始动画
            if (isPlaying) {
                playAnimation();
            }
        }
        
        // 播放动画
        function playAnimation() {
            if (!isPlaying) {
                isPlaying = true;
                document.getElementById('playBtn').innerHTML = '<span>▶</span> 播放中...';
                if (!animationId) {
                    lastTime = 0;
                    animationId = requestAnimationFrame(animate);
                }
            }
        }
        
        // 暂停动画
        function pauseAnimation() {
            isPlaying = false;
            document.getElementById('playBtn').innerHTML = '<span>▶</span> 播放';
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
        }
        
        // 重置动画
        function resetAnimation() {
            currentStage = 0;
            stageProgress = 0;
            initChromosomes();
            updateInfoPanel();
            
            if (isPlaying) {
                pauseAnimation();
                playAnimation();
            }
        }
        
        // 执行交叉互换
        function performCrossover() {
            if (currentModule !== 'meiosis' || currentStage !== 1) {
                alert("请在减数分裂的'前期 I'阶段进行交叉互换操作。");
                return;
            }
            
            // 随机选择一对同源染色体进行交叉互换
            const pairId = Math.floor(Math.random() * 23);
            const paternal = chromosomes.find(c => c.type === 'paternal' && c.pairId === pairId);
            const maternal = chromosomes.find(c => c.type === 'maternal' && c.pairId === pairId);
            
            if (paternal && maternal) {
                // 添加交叉互换点
                paternal.crossoverPoints.push(20);
                maternal.crossoverPoints.push(-20);
                
                // 改变颜色表示重组
                paternal.color = '#5a8cd0';
                maternal.color = '#d05a94';
                
                // 显示信息
                infoContent.innerHTML = `第${pairId + 1}对同源染色体发生了交叉互换！非姐妹染色单体间交换了片段，增加了遗传多样性。`;
                
                // 添加视觉效果
                setTimeout(() => {
                    paternal.color = 'linear-gradient(45deg, #2c5aa0 50%, #a02c6b 50%)';
                    maternal.color = 'linear-gradient(45deg, #a02c6b 50%, #2c5aa0 50%)';
                }, 500);
            }
        }
        
        // 随机生成配子
        function generateRandomGamete() {
            if (currentModule !== 'meiosis' || currentStage < 8) {
                alert("请在减数分裂完成后生成配子。");
                return;
            }
            
            // 创建一个随机配子
            const gamete = {
                id: gametes.length + 1,
                chromosomes: []
            };
            
            // 从每对同源染色体中随机选择一个
            for (let i = 0; i < 23; i++) {
                const isPaternal = Math.random() > 0.5;
                const original = chromosomes.find(c => c.pairId === i && c.type === (isPaternal ? 'paternal' : 'maternal'));
                
                if (original) {
                    gamete.chromosomes.push({
                        ...original,
                        id: `g${gametes.length}_${i}`,
                        x: 150 + gametes.length * 200,
                        y: 400
                    });
                }
            }
            
            gametes.push(gamete);
            
            // 限制最多显示4个配子
            if (gametes.length > 4) {
                gametes.shift();
            }
            
            // 显示信息
            infoContent.innerHTML = `生成了新的配子！由于非同源染色体的自由组合，每个配子的染色体组成都不同。这增加了遗传多样性。<br>已生成 ${gametes.length} 个配子示例。`;
        }
        
        // 显示测验
        function showQuiz(question, options, correctIndex) {
            quizQuestion.textContent = question;
            quizOptions.innerHTML = '';
            
            options.forEach((option, index) => {
                const optionElement = document.createElement('div');
                optionElement.className = 'quiz-option';
                optionElement.textContent = option;
                optionElement.dataset.correct = index === correctIndex;
                
                optionElement.addEventListener('click', function() {
                    const isCorrect = this.dataset.correct === 'true';
                    
                    // 显示正确/错误反馈
                    document.querySelectorAll('.quiz-option').forEach(opt => {
                        opt.classList.remove('correct', 'incorrect');
                        if (opt.dataset.correct === 'true') {
                            opt.classList.add('correct');
                        } else if (opt === this && !isCorrect) {
                            opt.classList.add('incorrect');
                        }
                    });
                    
                    if (isCorrect) {
                        this.classList.add('correct');
                        infoContent.innerHTML = "<span style='color:#4CAF50;'>✓ 回答正确！</span> 同源染色体分离发生在减数分裂I，这是染色体数目减半的关键步骤。";
                    }
                });
                
                quizOptions.appendChild(optionElement);
            });
            
            quizPopup.style.display = 'block';
        }
        
        // 初始化事件监听器
        function initEventListeners() {
            // 模块标签切换
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', () => {
                    switchModule(tab.dataset.module);
                });
            });
            
            // 控制按钮
            document.getElementById('playBtn').addEventListener('click', playAnimation);
            document.getElementById('pauseBtn').addEventListener('click', pauseAnimation);
            document.getElementById('resetBtn').addEventListener('click', resetAnimation);
            document.getElementById('prevBtn').addEventListener('click', prevStage);
            document.getElementById('nextBtn').addEventListener('click', nextStage);
            
            // 交互按钮
            document.getElementById('crossoverBtn').addEventListener('click', performCrossover);
            document.getElementById('generateGameteBtn').addEventListener('click', generateRandomGamete);
            
            // 视觉辅助开关
            document.getElementById('spindleToggle').addEventListener('change', function() {
                showSpindle = this.checked;
            });
            
            document.getElementById('geneToggle').addEventListener('change', function() {
                showGenes = this.checked;
            });
            
            document.getElementById('detailedViewToggle').addEventListener('change', function() {
                detailedView = this.checked;
            });
            
            // 测验关闭按钮
            document.getElementById('closeQuiz').addEventListener('click', function() {
                quizPopup.style.display = 'none';
            });
            
            // 点击染色体选择
            canvas.addEventListener('click', function(event) {
                const rect = canvas.getBoundingClientRect();
                const x = event.clientX - rect.left;
                const y = event.clientY - rect.top;
                
                // 查找点击的染色体
                for (const chromo of chromosomes) {
                    const dx = x - chromo.x;
                    const dy = y - chromo.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 40) {
                        selectedChromosome = chromo;
                        
                        // 显示染色体信息
                        const typeText = chromo.type === 'paternal' ? '父源' : '母源';
                        infoTitle.textContent = `染色体信息 (${typeText})`;
                        infoContent.innerHTML = `
                            <strong>染色体对:</strong> 第${chromo.pairId + 1}对<br>
                            <strong>来源:</strong> ${typeText}染色体<br>
                            <strong>状态:</strong> ${chromo.replicated ? '已复制（两个染色单体）' : '未复制'}<br>
                            <strong>位置:</strong> 细胞${chromo.inGamete ? '配子中' : '核内'}<br>
                            ${chromo.crossoverPoints.length > 0 ? '<strong>特征:</strong> 已发生交叉互换' : ''}
                        `;
                        return;
                    }
                }
                
                // 如果点击空白处，取消选择
                selectedChromosome = null;
            });
            
            // 键盘控制
            document.addEventListener('keydown', function(event) {
                switch(event.key) {
                    case ' ':
                        event.preventDefault();
                        if (isPlaying) pauseAnimation();
                        else playAnimation();
                        break;
                    case 'ArrowLeft':
                        event.preventDefault();
                        prevStage();
                        break;
                    case 'ArrowRight':
                        event.preventDefault();
                        nextStage();
                        break;
                    case 'r':
                    case 'R':
                        resetAnimation();
                        break;
                }
            });
        }
        
        // 初始化函数
        function init() {
            initChromosomes();
            initEventListeners();
            updateInfoPanel();
            
            // 开始动画
            playAnimation();
        }
        
        // 页面加载完成后初始化
        window.addEventListener('load', init);
    </script>
</body>
</html>


### 3. 过程输出

### 3. 交互式教学动画使用指南

欢迎使用《减数分裂与受精作用》交互式教学动画！本指南将帮助您充分利用这一精心设计的教学工具，深入理解生命遗传的核心过程。

#### 一、 功能说明

本动画是一个基于HTML5 Canvas开发的交互式学习环境，旨在通过动态可视化、交互操作和即时反馈，将抽象的生物学概念转化为直观、生动的学习体验。它完整呈现了从体细胞到配子形成，再到受精作用恢复染色体数目的生命循环，特别聚焦于**染色体行为**这一核心主线。

#### 二、 主要功能

1.  **模块化学习路径**
    *   **生命循环概览**：快速了解从“46条→23条→46条”的完整染色体数目变化周期。
    *   **减数分裂详解**：分步深入减数分裂I和II的九个阶段，观察每个阶段的染色体关键行为。
    *   **受精作用**：专门展示精卵结合、核融合及染色体配对恢复二倍体的过程。

2.  **智能动画控制**
    *   **播放/暂停/重置**：掌控整体动画节奏。
    *   **上一步/下一步**：精细控制，逐步学习每个分裂阶段，适合难点反复观摩。
    *   **阶段进度条**：清晰显示当前学习进度。

3.  **探索式交互操作**
    *   **点击染色体**：点击任意染色体，将高亮显示并弹出详细信息窗口，了解其来源（父源/母源）和状态。
    *   **手动交叉互换**（仅在减数分裂-前期I）：点击按钮，随机触发一对同源染色体的非姐妹染色单体间片段交换，直观展示遗传重组的物理基础。
    *   **随机生成配子**（在减数分裂完成后）：模拟“非同源染色体自由组合”的随机性，每次点击都会生成一个染色体组成不同的配子，生动诠释遗传多样性的来源。

4.  **认知辅助工具**
    *   **实时染色体计数器**：始终显示当前细胞中的染色体数目，强化“数目变化”这一核心概念。
    *   **动态信息面板**：随动画进程同步更新，提供当前阶段的专业文字解说。
    *   **视觉辅助开关**：可独立控制“纺锤体显示”、“基因位点显示”和“染色体视图（简略/详细）”的开关，帮助聚焦学习重点。
    *   **智能迷你测验**：在关键学习节点（如同源染色体分离后）自动弹出选择题，提供即时学习反馈。

#### 三、 设计特色

1.  **科学的视觉编码**：
    *   **父源染色体**采用**深蓝色系**，**母源染色体**采用**红紫色系**，对比鲜明且和谐。
    *   发生交叉互换后，染色体颜色变为**混合渐变**，直观体现遗传物质的交换。
    *   “X”形染色体设计准确表示复制后包含两个姐妹染色单体的状态。

2.  **符合认知规律的教学设计**：
    *   **从宏观到微观**：先呈现完整循环建立整体框架，再深入具体过程。
    *   **分解复杂过程**：将连续的减数分裂分解为可暂停、可重复的独立阶段。
    *   **多重感官刺激**：结合平滑动画、颜色高亮、文字提示和交互反馈，促进深度理解。

3.  **友好的用户体验**：
    *   界面布局清晰，功能分区明确。
    *   提供键盘快捷键（空格键播放/暂停，左右箭头切换阶段），操作便捷。
    *   响应式设计，适应不同屏幕尺寸。

#### 四、 教学要点

本动画特别适合用于理解和强化以下核心知识与难点：

1.  **染色体数目变化轨迹**：紧盯右上角的计数器，明确“减半”（减数分裂I后期）和“恢复”（受精作用）的具体时刻。
2.  **减数分裂I与II的核心区别**：
    *   **分离对象**：减数分裂I分离的是**同源染色体**；减数分裂II分离的是**姐妹染色单体**。
    *   **遗传学意义**：I实现了染色体数目减半和遗传重组（交叉互换+自由组合）；II类似于有丝分裂，保证配子获得单套遗传物质。
3.  **遗传多样性的来源**：
    *   **交叉互换**：在“前期I”使用“手动交叉互换”功能，观察非姐妹染色单体间的片段交换。
    *   **自由组合**：在生成配子后，多次点击“随机生成配子”，观察染色体组合的随机性。
4.  **受精作用的本质**：不仅是两个细胞的结合，更是**两个单倍体细胞核的融合**，使染色体数目恢复为二倍体，保证了物种遗传的稳定性。

#### 五、 使用建议

1.  **初次学习者**：
    *   建议从“生命循环概览”模块开始，完整观看1-2遍，建立“46→23→46”的宏观概念。
    *   进入“减数分裂详解”模块，使用“下一步”按钮**逐步学习**，结合信息面板的文字说明，仔细观察每个阶段染色体的形态、位置和行为。
    *   积极使用交互功能：点击染色体查看详情，在前期I尝试“交叉互换”，在完成后“生成配子”。

2.  **复习与深化者**：
    *   直接进入“减数分裂详解”模块，利用“上一步/下一步”功能**针对性地复习薄弱环节**（如联会、中期I排列方式、分离过程）。
    *   关闭“纺锤体”等视觉辅助，尝试回忆并描述染色体行为，再打开验证。
    *   认真完成弹出的测验题，检验理解程度。

3.  **教师教学辅助**：
    *   可在课堂讲解时，分阶段播放动画，作为动态板书。
    *   针对“交叉互换”和“自由组合”两大抽象概念，引导学生操作交互功能，开展探究式讨论。
    *   利用“随机生成配子”功能，直观展示孟德尔遗传定律的细胞学基础。

我们希望这个交互式动画能成为您探索生命奥秘的得力助手。请尽情点击、探索和发现，祝您学习愉快！