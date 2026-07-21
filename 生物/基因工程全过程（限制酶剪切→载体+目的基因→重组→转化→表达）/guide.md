# 需求：基因工程全过程（限制酶剪切→载体+目的基因→重组→转化→表达）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为高中或大学低年级的生物学学生。他们具备基础的生物学知识（如DNA、酶、细胞），但对基因工程这一具体、流程化的技术缺乏直观、动态的理解。
2.  **核心需求**：用户需要清晰地理解基因工程从“剪切”到“表达”的完整、连续的操作流程，而不仅仅是记忆零散的步骤名称。他们需要看到分子层面的动态交互，理解每一步的“目的”和“原理”。
3.  **痛点与挑战**：
    *   **抽象性**：DNA、酶、质粒等分子尺度的事物难以想象。
    *   **流程复杂性**：步骤多，且每一步的输入和输出产物是下一步的起点，容易混淆。
    *   **术语障碍**：限制酶、粘性末端、重组质粒、转化等术语缺乏直观对应物。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）
1.  **核心概念聚焦**：
    *   **核心流程**：剪切 → 连接 → 运载 → 进入 → 生产。
    *   **关键角色**：**目的基因**（要搬运的货物）、**限制酶**（分子剪刀）、**质粒载体**（分子货车）、**DNA连接酶**（分子胶水）、**宿主细胞**（工厂）。
    *   **核心原理**：碱基互补配对（粘性末端连接）、质粒的自我复制与表达特性。

2.  **认知规律遵循**：
    *   **从宏观到微观**：开场可展示一个宏观比喻（如“改造一个细胞工厂”），再迅速切入分子视图。
    *   **分步讲解，串联成线**：将全过程分解为5个清晰的步骤模块。每个模块遵循“展示操作 → 解释原理 → 明确结果”的逻辑。
    *   **可视化类比**：使用强烈的视觉隐喻（剪刀、胶水、货车、钥匙孔、工厂）来映射抽象概念，降低认知负荷。
    *   **主动建构**：通过交互，让用户亲自“操作”关键步骤（如选择限制酶剪切位点、拖动基因进行连接），加深理解。

3.  **交互设计策略**：
    *   **流程导航**：顶部或侧边设置清晰的进度条或步骤按钮，允许用户随时跳转、回顾，掌控学习节奏。
    *   **步骤内交互**：
        *   **剪切**：让用户点击“施加限制酶”，观看DNA和质粒被剪开的动画。
        *   **连接**：让用户将剪下的“目的基因”拖拽到“切开质粒”的对应末端，触发连接酶进行粘合。
        *   **转化与表达**：提供“播放/暂停”控制，观察重组质粒进入细胞及蛋白质合成的动态过程。
    *   **信息分层**：默认界面简洁，点击关键对象（如酶、质粒）可弹出详细说明卡片，满足不同深度学习需求。

4.  **视觉呈现规划**：
    *   **主视角**：采用横屏2.5D等距视角或俯视视角，营造一个清晰的“分子操作台”场景。
    *   **角色设计**：
        *   **DNA/基因**：双螺旋结构简化成彩色条带，不同基因用不同颜色区分。
        *   **酶与蛋白质**：设计成具有特征形状的卡通化形象（如限制酶像剪刀，连接酶像胶水瓶），增强识别度。
        *   **质粒**：环形DNA，设计得像一个带“标记”（如抗性基因、启动子区域）的圆形手环或方向盘。
        *   **细胞**：一个柔和的囊状结构，膜上有孔洞。
    *   **动画风格**：平滑、拟人化的关键帧动画，配合粒子效果（如碱基对连接时的闪光）来强调关键动作。

#### 配色方案选择
*   **主色调**：采用**科技蓝**与**生命绿**的搭配。蓝色代表精准、科技（酶、工具），绿色代表生命、DNA、细胞。
*   **角色配色**：
    *   **目的基因**：使用醒目的**暖色（如亮橙/洋红）**，使其在画面中始终成为视觉焦点。
    *   **质粒载体**：使用**浅蓝色或灰色**作为基底，其上的关键区域（如抗性基因、多克隆位点）用不同颜色高亮。
    *   **限制酶/连接酶**：分别用**红色（警示/剪切）** 和**黄色（粘合/连接）**。
    *   **细胞与背景**：细胞膜用浅灰色半透明，内部细胞质为极浅的米黄或淡蓝。背景为柔和的深蓝灰或白色，确保前景物体突出。
*   **状态色**：未激活元素为灰阶，可交互元素有颜色外发光，已完成步骤在进度条上显示为绿色。

#### 交互功能列表
1.  **全局控制**：
    *   步骤进度条（点击跳转）
    *   播放/暂停/重置动画按钮
    *   声音开关
    *   显示/隐藏术语标签开关
2.  **步骤一：限制酶剪切**：
    *   点击“添加限制酶”按钮，触发动画。
    *   可点击不同的“限制酶”图标，观察其对DNA序列的不同剪切效果（展示特异性）。
    *   高亮显示产生的“粘性末端”序列。
3.  **步骤二：载体准备**：
    *   展示质粒结构图，点击可了解各部分功能（启动子、抗性基因等）。
    *   同样使用限制酶剪切质粒，动画强调产生与目的基因匹配的末端。
4.  **步骤三：重组连接**：
    *   **核心交互**：将目的基因片段拖拽至切开的质粒缺口处。
    *   当末端匹配正确时，自动触发“DNA连接酶”进行连接，并有效果音和视觉反馈。
    *   连接错误时（末端不匹配），基因弹回原位。
5.  **步骤四：转化**：
    *   点击“开始转化”按钮。
    *   动画展示重组质粒与宿主细胞（如大肠杆菌）混合，通过热激或电击法进入细胞。
    *   可切换视图，展示细胞内部视角：质粒进入细胞质。
6.  **步骤五：筛选与表达**：
    *   **筛选**：展示在含抗生素的培养基上，只有含抗性基因（来自质粒）的细胞存活。
    *   **表达**：动画展示质粒上的目的基因被转录为mRNA，再在核糖体上翻译成蛋白质（一串小球链）。
    *   最终，画面定格在宿主细胞“工厂”大量生产目的蛋白质（如胰岛素）的示意图。
7.  **辅助学习功能**：
    *   点击任何生物分子（DNA、酶、质粒）弹出详细说明卡片。
    *   关键步骤配有简短的文字解说字幕。
    *   流程结束后，提供“总览模式”，以一张信息图快速回顾全流程。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>基因工程全过程交互教学动画</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0a192f 0%, #1a365d 100%);
            color: #e6f1ff;
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
            background: rgba(16, 42, 88, 0.7);
            border-radius: 15px;
            border: 1px solid rgba(64, 156, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 30, 60, 0.3);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #64ffda, #4cc9f0);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 2px 10px rgba(100, 255, 218, 0.2);
        }
        
        .subtitle {
            font-size: 1.1rem;
            color: #a8b2d1;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .main-content {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }
        
        .control-panel {
            background: rgba(16, 42, 88, 0.8);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(64, 156, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 30, 60, 0.3);
        }
        
        .steps-nav {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .step-btn {
            flex: 1;
            min-width: 120px;
            padding: 12px 15px;
            background: rgba(30, 60, 114, 0.7);
            border: 1px solid rgba(64, 156, 255, 0.3);
            border-radius: 10px;
            color: #ccd6f6;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        .step-btn:hover {
            background: rgba(64, 156, 255, 0.2);
            transform: translateY(-2px);
        }
        
        .step-btn.active {
            background: linear-gradient(90deg, #1e7a5e, #2a9d8f);
            color: white;
            border-color: #64ffda;
            box-shadow: 0 0 15px rgba(100, 255, 218, 0.3);
        }
        
        .step-btn.completed {
            background: rgba(42, 157, 143, 0.3);
            border-color: #2a9d8f;
        }
        
        .animation-controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }
        
        .control-btn {
            padding: 10px 25px;
            background: rgba(30, 60, 114, 0.9);
            border: 1px solid rgba(64, 156, 255, 0.5);
            border-radius: 8px;
            color: #e6f1ff;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .control-btn:hover {
            background: rgba(64, 156, 255, 0.3);
            transform: translateY(-2px);
        }
        
        .control-btn.primary {
            background: linear-gradient(90deg, #1e7a5e, #2a9d8f);
            border-color: #64ffda;
        }
        
        .content-area {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }
        
        .animation-container {
            background: rgba(10, 25, 47, 0.9);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(64, 156, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 30, 60, 0.3);
            min-height: 500px;
            position: relative;
            overflow: hidden;
        }
        
        #animationCanvas {
            width: 100%;
            height: 100%;
            display: block;
            border-radius: 10px;
        }
        
        .info-panel {
            background: rgba(16, 42, 88, 0.8);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(64, 156, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 30, 60, 0.3);
        }
        
        .step-info {
            display: none;
        }
        
        .step-info.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .step-title {
            font-size: 1.8rem;
            margin-bottom: 15px;
            color: #64ffda;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .step-icon {
            width: 40px;
            height: 40px;
            background: rgba(100, 255, 218, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
        }
        
        .step-description {
            font-size: 1.1rem;
            line-height: 1.7;
            color: #a8b2d1;
            margin-bottom: 20px;
        }
        
        .key-terms {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }
        
        .term {
            padding: 8px 15px;
            background: rgba(30, 60, 114, 0.7);
            border-radius: 20px;
            font-size: 0.9rem;
            color: #ccd6f6;
            border: 1px solid rgba(64, 156, 255, 0.3);
            cursor: help;
            transition: all 0.3s ease;
        }
        
        .term:hover {
            background: rgba(64, 156, 255, 0.2);
            transform: translateY(-2px);
        }
        
        .interaction-hint {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(16, 42, 88, 0.9);
            padding: 10px 20px;
            border-radius: 20px;
            color: #64ffda;
            font-size: 0.9rem;
            border: 1px solid rgba(100, 255, 218, 0.3);
            display: flex;
            align-items: center;
            gap: 8px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(100, 255, 218, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(100, 255, 218, 0); }
            100% { box-shadow: 0 0 0 0 rgba(100, 255, 218, 0); }
        }
        
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(64, 156, 255, 0.2);
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
            border-radius: 4px;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #8892b0;
            font-size: 0.9rem;
            border-top: 1px solid rgba(64, 156, 255, 0.2);
        }
        
        @media (max-width: 768px) {
            .steps-nav {
                flex-direction: column;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .animation-container {
                min-height: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>基因工程全过程交互教学动画</h1>
            <p class="subtitle">探索从限制酶剪切到基因表达的完整流程：剪切 → 连接 → 重组 → 转化 → 表达。通过交互式动画直观理解分子生物学核心技术。</p>
        </header>
        
        <div class="main-content">
            <div class="control-panel">
                <div class="steps-nav">
                    <button class="step-btn active" data-step="1">1. 限制酶剪切</button>
                    <button class="step-btn" data-step="2">2. 载体准备</button>
                    <button class="step-btn" data-step="3">3. 重组连接</button>
                    <button class="step-btn" data-step="4">4. 转化</button>
                    <button class="step-btn" data-step="5">5. 表达与筛选</button>
                </div>
                
                <div class="animation-controls">
                    <button class="control-btn" id="prevBtn">上一步</button>
                    <button class="control-btn primary" id="playBtn">播放动画</button>
                    <button class="control-btn" id="resetBtn">重置</button>
                    <button class="control-btn" id="nextBtn">下一步</button>
                </div>
            </div>
            
            <div class="content-area">
                <div class="animation-container">
                    <canvas id="animationCanvas" width="1100" height="500"></canvas>
                    <div class="interaction-hint" id="hintText">
                        <span>💡</span> 点击"播放动画"按钮开始学习
                    </div>
                </div>
                
                <div class="info-panel">
                    <div class="step-info active" id="step1-info">
                        <h2 class="step-title"><span class="step-icon">✂️</span> 步骤1: 限制酶剪切</h2>
                        <p class="step-description">
                            限制性内切酶是基因工程的"分子剪刀"，能识别DNA分子上特定的核苷酸序列并在特定位点切割DNA。
                            本步骤展示限制酶EcoRI识别"GAATTC"序列并在G和A之间切割，产生具有粘性末端的DNA片段。
                        </p>
                        <div class="key-terms">
                            <div class="term" title="能识别特定DNA序列并在特定位点切割的酶">限制性内切酶</div>
                            <div class="term" title="限制酶识别和切割的特定DNA序列">识别序列</div>
                            <div class="term" title="DNA切割后产生的单链末端，能通过碱基互补配对连接">粘性末端</div>
                            <div class="term" title="被切割出来的目标DNA片段">目的基因</div>
                        </div>
                    </div>
                    
                    <div class="step-info" id="step2-info">
                        <h2 class="step-title"><span class="step-icon">🚚</span> 步骤2: 载体准备</h2>
                        <p class="step-description">
                            质粒是基因工程的"分子货车"，是能自我复制的小型环状DNA分子。
                            使用相同的限制酶切割质粒DNA，使其产生与目的基因匹配的粘性末端，为连接做好准备。
                        </p>
                        <div class="key-terms">
                            <div class="term" title="用于携带外源基因进入宿主细胞的DNA分子">载体</div>
                            <div class="term" title="细菌中天然存在的小型环状DNA分子">质粒</div>
                            <div class="term" title="质粒上含有多个限制酶切位点的区域">多克隆位点</div>
                            <div class="term" title="使宿主细胞具有抗生素抗性的基因">抗性基因</div>
                        </div>
                    </div>
                    
                    <div class="step-info" id="step3-info">
                        <h2 class="step-title"><span class="step-icon">🔗</span> 步骤3: 重组连接</h2>
                        <p class="step-description">
                            DNA连接酶是"分子胶水"，能将DNA片段共价连接起来。
                            目的基因与质粒载体通过互补的粘性末端结合，在DNA连接酶的作用下形成磷酸二酯键，产生重组DNA分子。
                        </p>
                        <div class="key-terms">
                            <div class="term" title="催化DNA片段连接的酶">DNA连接酶</div>
                            <div class="term" title="将目的基因插入载体后形成的DNA分子">重组DNA</div>
                            <div class="term" title="重组后的质粒分子">重组质粒</div>
                            <div class="term" title="DNA分子中连接核苷酸的化学键">磷酸二酯键</div>
                        </div>
                    </div>
                    
                    <div class="step-info" id="step4-info">
                        <h2 class="step-title"><span class="step-icon">🦠</span> 步骤4: 转化</h2>
                        <p class="step-description">
                            将重组质粒导入宿主细胞（如大肠杆菌）的过程称为转化。
                            常用方法包括热激法和电击法，使细胞膜暂时出现孔洞，允许质粒进入细胞内部。
                        </p>
                        <div class="key-terms">
                            <div class="term" title="将外源DNA导入宿主细胞的过程">转化</div>
                            <div class="term" title="接受外源DNA的细胞">宿主细胞</div>
                            <div class="term" title="通过温度变化使细胞膜通透性增加的方法">热激法</div>
                            <div class="term" title="通过电脉冲使细胞膜形成临时孔洞的方法">电击法</div>
                        </div>
                    </div>
                    
                    <div class="step-info" id="step5-info">
                        <h2 class="step-title"><span class="step-icon">🏭</span> 步骤5: 表达与筛选</h2>
                        <p class="step-description">
                            成功转化的细胞在含有抗生素的培养基上生长，只有含有抗性基因的细胞才能存活。
                            目的基因在宿主细胞内转录和翻译，合成目标蛋白质（如胰岛素），实现基因的表达。
                        </p>
                        <div class="key-terms">
                            <div class="term" title="基因信息转化为蛋白质的过程">基因表达</div>
                            <div class="term" title="从DNA合成RNA的过程">转录</div>
                            <div class="term" title="从RNA合成蛋白质的过程">翻译</div>
                            <div class="term" title="用于筛选转化成功细胞的物质">抗生素筛选</div>
                        </div>
                    </div>
                    
                    <div class="legend">
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ff6b6b;"></div>
                            <span>限制酶 (分子剪刀)</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ffa726;"></div>
                            <span>目的基因</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #4ecdc4;"></div>
                            <span>质粒载体</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #ffe66d;"></div>
                            <span>DNA连接酶 (分子胶水)</span>
                        </div>
                        <div class="legend-item">
                            <div class="legend-color" style="background-color: #95e1d3;"></div>
                            <span>宿主细胞</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <footer>
            <p>基因工程交互教学动画 | 设计原理：限制酶剪切 → 载体+目的基因 → 重组 → 转化 → 表达</p>
            <p>© 2023 教育技术演示 | 用于教学目的</p>
        </footer>
    </div>

    <script>
        // 全局变量
        const canvas = document.getElementById('animationCanvas');
        const ctx = canvas.getContext('2d');
        const stepButtons = document.querySelectorAll('.step-btn');
        const stepInfos = document.querySelectorAll('.step-info');
        const playBtn = document.getElementById('playBtn');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const resetBtn = document.getElementById('resetBtn');
        const hintText = document.getElementById('hintText');
        
        let currentStep = 1;
        let animationPlaying = false;
        let animationFrameId = null;
        let animationTime = 0;
        
        // 动画对象定义
        const animationObjects = {
            // 步骤1: 限制酶剪切
            dna: {
                x: 200, y: 250, width: 400, height: 30,
                segments: 8, color: '#4a4a4a',
                cutPosition: 4, // 第4段被切割
                isCut: false,
                stickyEnds: []
            },
            restrictionEnzyme: {
                x: 150, y: 150, width: 40, height: 40,
                color: '#ff6b6b', targetX: 350, targetY: 250,
                isMoving: false, hasCut: false
            },
            targetGene: {
                x: 0, y: 0, width: 100, height: 30,
                color: '#ffa726', isVisible: false,
                isDraggable: false, isDragging: false
            },
            
            // 步骤2: 载体准备
            plasmid: {
                x: 700, y: 250, radius: 60, color: '#4ecdc4',
                isCut: false, cutAngle: Math.PI/4,
                markerGenes: [
                    {angle: 0, label: "启动子", color: "#ff9e80"},
                    {angle: Math.PI, label: "抗性基因", color: "#80deea"}
                ]
            },
            
            // 步骤3: 重组连接
            ligase: {
                x: 500, y: 100, width: 40, height: 40,
                color: '#ffe66d', isVisible: false,
                isMoving: false
            },
            recombinantPlasmid: {
                x: 700, y: 250, radius: 60, color: '#4ecdc4',
                geneInserted: false, geneColor: '#ffa726',
                isVisible: false
            },
            
            // 步骤4: 转化
            hostCell: {
                x: 550, y: 250, radius: 120, color: '#95e1d3',
                membraneWidth: 5, isVisible: false,
                plasmidsInside: []
            },
            
            // 步骤5: 表达与筛选
            proteinFactory: {
                x: 550, y: 250, radius: 100, color: '#95e1d3',
                isVisible: false, proteins: []
            },
            antibiotics: {
                x: 300, y: 400, width: 600, height: 50,
                color: 'rgba(255, 107, 107, 0.3)', isVisible: false
            }
        };
        
        // 初始化
        function init() {
            // 设置Canvas尺寸
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);
            
            // 事件监听器
            stepButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const step = parseInt(btn.dataset.step);
                    goToStep(step);
                });
            });
            
            playBtn.addEventListener('click', toggleAnimation);
            prevBtn.addEventListener('click', () => goToStep(currentStep - 1));
            nextBtn.addEventListener('click', () => goToStep(currentStep + 1));
            resetBtn.addEventListener('click', resetAnimation);
            
            // 鼠标事件用于拖拽交互
            canvas.addEventListener('mousedown', handleMouseDown);
            canvas.addEventListener('mousemove', handleMouseMove);
            canvas.addEventListener('mouseup', handleMouseUp);
            
            // 开始动画循环
            animate();
        }
        
        // 调整Canvas尺寸
        function resizeCanvas() {
            const container = canvas.parentElement;
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
        }
        
        // 转到指定步骤
        function goToStep(step) {
            if (step < 1 || step > 5) return;
            
            // 更新当前步骤
            currentStep = step;
            
            // 更新步骤按钮状态
            stepButtons.forEach((btn, index) => {
                const btnStep = index + 1;
                btn.classList.remove('active');
                if (btnStep === step) {
                    btn.classList.add('active');
                }
                if (btnStep < step) {
                    btn.classList.add('completed');
                } else {
                    btn.classList.remove('completed');
                }
            });
            
            // 更新信息面板
            stepInfos.forEach(info => {
                info.classList.remove('active');
            });
            document.getElementById(`step${step}-info`).classList.add('active');
            
            // 重置动画状态
            resetAnimationState();
            animationTime = 0;
            
            // 更新提示文本
            updateHintText();
        }
        
        // 重置动画状态
        function resetAnimationState() {
            // 重置所有对象状态
            animationObjects.dna.isCut = false;
            animationObjects.dna.stickyEnds = [];
            animationObjects.restrictionEnzyme.isMoving = false;
            animationObjects.restrictionEnzyme.hasCut = false;
            animationObjects.restrictionEnzyme.x = 150;
            animationObjects.restrictionEnzyme.y = 150;
            
            animationObjects.targetGene.isVisible = false;
            animationObjects.targetGene.isDraggable = false;
            animationObjects.targetGene.x = 0;
            animationObjects.targetGene.y = 0;
            
            animationObjects.plasmid.isCut = false;
            animationObjects.ligase.isVisible = false;
            animationObjects.ligase.isMoving = false;
            animationObjects.recombinantPlasmid.isVisible = false;
            animationObjects.recombinantPlasmid.geneInserted = false;
            
            animationObjects.hostCell.isVisible = false;
            animationObjects.hostCell.plasmidsInside = [];
            
            animationObjects.proteinFactory.isVisible = false;
            animationObjects.proteinFactory.proteins = [];
            animationObjects.antibiotics.isVisible = false;
            
            animationPlaying = false;
            playBtn.textContent = '播放动画';
            
            if (animationFrameId) {
                cancelAnimationFrame(animationFrameId);
                animationFrameId = null;
            }
        }
        
        // 切换动画播放状态
        function toggleAnimation() {
            animationPlaying = !animationPlaying;
            playBtn.textContent = animationPlaying ? '暂停动画' : '播放动画';
            
            if (animationPlaying) {
                hintText.style.display = 'none';
                startAnimation();
            }
        }
        
        // 开始动画
        function startAnimation() {
            if (animationFrameId) return;
            
            function animateStep() {
                animationTime += 0.016; // 约60fps
                
                // 根据当前步骤执行动画
                switch(currentStep) {
                    case 1:
                        animateStep1();
                        break;
                    case 2:
                        animateStep2();
                        break;
                    case 3:
                        animateStep3();
                        break;
                    case 4:
                        animateStep4();
                        break;
                    case 5:
                        animateStep5();
                        break;
                }
                
                // 绘制当前帧
                draw();
                
                if (animationPlaying) {
                    animationFrameId = requestAnimationFrame(animateStep);
                } else {
                    animationFrameId = null;
                }
            }
            
            animateStep();
        }
        
        // 步骤1动画：限制酶剪切
        function animateStep1() {
            const dna = animationObjects.dna;
            const enzyme = animationObjects.restrictionEnzyme;
            const gene = animationObjects.targetGene;
            
            // 第一阶段：酶移动到DNA
            if (animationTime < 2 && !enzyme.hasCut) {
                enzyme.isMoving = true;
                const progress = animationTime / 2;
                enzyme.x = 150 + (350 - 150) * progress;
                enzyme.y = 150 + (250 - 150) * progress;
            }
            
            // 第二阶段：切割DNA
            if (animationTime >= 2 && animationTime < 3 && !enzyme.hasCut) {
                dna.isCut = true;
                enzyme.hasCut = true;
                
                // 创建粘性末端
                dna.stickyEnds = [
                    {x: dna.x + dna.width/2 - 20, y: dna.y - 15, sequence: 'AATT'},
                    {x: dna.x + dna.width/2 + 20, y: dna.y - 15, sequence: 'TTAA'}
                ];
                
                // 设置目的基因位置
                gene.x = dna.x + dna.width/2 - 50;
                gene.y = dna.y;
                gene.isVisible = true;
            }
            
            // 第三阶段：酶离开，基因可拖拽
            if (animationTime >= 3 && animationTime < 4) {
                enzyme.isMoving = true;
                const progress = (animationTime - 3) / 1;
                enzyme.x = 350 + (150 - 350) * progress;
                enzyme.y = 250 + (150 - 250) * progress;
            }
            
            if (animationTime >= 4) {
                enzyme.isMoving = false;
                gene.isDraggable = true;
                
                // 自动进入下一步
                if (animationTime > 6) {
                    goToStep(2);
                    animationTime = 0;
                }
            }
        }
        
        // 步骤2动画：载体准备
        function animateStep2() {
            const plasmid = animationObjects.plasmid;
            const enzyme = animationObjects.restrictionEnzyme;
            
            // 重置酶位置
            if (animationTime < 0.5) {
                enzyme.x = 550;
                enzyme.y = 150;
                enzyme.hasCut = false;
            }
            
            // 酶移动到质粒
            if (animationTime >= 0.5 && animationTime < 1.5 && !enzyme.hasCut) {
                enzyme.isMoving = true;
                const progress = (animationTime - 0.5) / 1;
                enzyme.x = 550 + (700 - 550) * progress;
                enzyme.y = 150 + (250 - 150) * progress;
            }
            
            // 切割质粒
            if (animationTime >= 1.5 && animationTime < 2.5 && !enzyme.hasCut) {
                plasmid.isCut = true;
                enzyme.hasCut = true;
            }
            
            // 酶离开
            if (animationTime >= 2.5 && animationTime < 3.5) {
                enzyme.isMoving = true;
                const progress = (animationTime - 2.5) / 1;
                enzyme.x = 700 + (550 - 700) * progress;
                enzyme.y = 250 + (150 - 250) * progress;
            }
            
            if (animationTime >= 3.5) {
                enzyme.isMoving = false;
                
                // 自动进入下一步
                if (animationTime > 5) {
                    goToStep(3);
                    animationTime = 0;
                }
            }
        }
        
        // 步骤3动画：重组连接
        function animateStep3() {
            const gene = animationObjects.targetGene;
            const plasmid = animationObjects.plasmid;
            const ligase = animationObjects.ligase;
            const recombinant = animationObjects.recombinantPlasmid;
            
            // 显示连接酶
            if (animationTime < 1) {
                ligase.isVisible = true;
                ligase.x = 500;
                ligase.y = 100;
            }
            
            // 如果基因已连接到质粒
            if (gene.isDragging === false && gene.x > 650 && gene.x < 750 && gene.y > 200 && gene.y < 300) {
                gene.x = plasmid.x;
                gene.y = plasmid.y;
                gene.isDraggable = false;
                gene.isVisible = false;
                
                // 连接酶移动到连接位置
                if (animationTime >= 1 && animationTime < 2) {
                    ligase.isMoving = true;
                    const progress = (animationTime - 1) / 1;
                    ligase.x = 500 + (700 - 500) * progress;
                    ligase.y = 100 + (250 - 100) * progress;
                }
                
                // 显示重组质粒
                if (animationTime >= 2) {
                    recombinant.isVisible = true;
                    recombinant.geneInserted = true;
                    plasmid.isCut = false;
                    
                    // 自动进入下一步
                    if (animationTime > 4) {
                        goToStep(4);
                        animationTime = 0;
                    }
                }
            }
        }
        
        // 步骤4动画：转化
        function animateStep4() {
            const hostCell = animationObjects.hostCell;
            const recombinant = animationObjects.recombinantPlasmid;
            
            // 显示宿主细胞
            if (animationTime < 1) {
                hostCell.isVisible = true;
            }
            
            // 重组质粒移动到细胞
            if (animationTime >= 1 && animationTime < 3) {
                const progress = (animationTime - 1) / 2;
                recombinant.x = 700 + (550 - 700) * progress;
                recombinant.y = 250 + (250 - 250) * progress;
                
                // 当质粒接近细胞时，添加到内部
                if (progress > 0.8 && hostCell.plasmidsInside.length === 0) {
                    hostCell.plasmidsInside.push({x: 550, y: 250, radius: 20});
                    recombinant.isVisible = false;
                }
            }
            
            // 自动进入下一步
            if (animationTime > 4) {
                goToStep(5);
                animationTime = 0;
            }
        }
        
        // 步骤5动画：表达与筛选
        function animateStep5() {
            const proteinFactory = animationObjects.proteinFactory;
            const antibiotics = animationObjects.antibiotics;
            
            // 显示蛋白质工厂和抗生素
            if (animationTime < 1) {
                proteinFactory.isVisible = true;
                antibiotics.isVisible = true;
            }
            
            // 生成蛋白质
            if (animationTime >= 1 && animationTime < 6) {
                // 每0.5秒生成一个蛋白质
                if (Math.floor(animationTime * 2) > proteinFactory.proteins.length) {
                    const angle = Math.random() * Math.PI * 2;
                    const distance = 80 + Math.random() * 40;
                    proteinFactory.proteins.push({
                        x: proteinFactory.x + Math.cos(angle) * distance,
                        y: proteinFactory.y + Math.sin(angle) * distance,
                        size: 5 + Math.random() * 10,
                        color: '#ffa726'
                    });
                }
            }
            
            // 限制蛋白质数量
            if (proteinFactory.proteins.length > 20) {
                proteinFactory.proteins.shift();
            }
        }
        
        // 绘制函数
        function draw() {
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景
            drawBackground();
            
            // 根据当前步骤绘制
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
                case 5:
                    drawStep5();
                    break;
            }
        }
        
        // 绘制背景
        function drawBackground() {
            // 渐变背景
            const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
            gradient.addColorStop(0, '#0a192f');
            gradient.addColorStop(1, '#1a365d');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 网格线
            ctx.strokeStyle = 'rgba(100, 255, 218, 0.05)';
            ctx.lineWidth = 1;
            
            for (let x = 0; x < canvas.width; x += 50) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();
            }
            
            for (let y = 0; y < canvas.height; y += 50) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();
            }
            
            // 当前步骤标题
            ctx.fillStyle = '#64ffda';
            ctx.font = 'bold 24px "Segoe UI"';
            ctx.textAlign = 'center';
            const stepTitles = ['', '限制酶剪切', '载体准备', '重组连接', '转化', '表达与筛选'];
            ctx.fillText(`步骤 ${currentStep}: ${stepTitles[currentStep]}`, canvas.width/2, 40);
        }
        
        // 绘制步骤1
        function drawStep1() {
            const dna = animationObjects.dna;
            const enzyme = animationObjects.restrictionEnzyme;
            const gene = animationObjects.targetGene;
            
            // 绘制DNA
            ctx.fillStyle = dna.color;
            const segmentWidth = dna.width / dna.segments;
            
            for (let i = 0; i < dna.segments; i++) {
                // 如果DNA被切割且这是切割点，跳过绘制
                if (dna.isCut && i === dna.cutPosition) {
                    continue;
                }
                
                const x = dna.x + i * segmentWidth;
                ctx.fillRect(x, dna.y, segmentWidth - 2, dna.height);
                
                // 绘制DNA双螺旋效果
                ctx.strokeStyle = '#64ffda';
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.moveTo(x, dna.y);
                ctx.lineTo(x, dna.y + dna.height);
                ctx.stroke();
            }
            
            // 绘制粘性末端
            if (dna.stickyEnds.length > 0) {
                ctx.fillStyle = '#ffa726';
                ctx.font = '
'bold 14px "Segoe UI"';
                ctx.textAlign = 'center';
                
                dna.stickyEnds.forEach(end => {
                    // 绘制末端形状
                    ctx.beginPath();
                    ctx.moveTo(end.x, end.y);
                    ctx.lineTo(end.x + 20, end.y + 15);
                    ctx.lineTo(end.x + 20, end.y - 15);
                    ctx.closePath();
                    ctx.fill();
                    
                    // 绘制序列文本
                    ctx.fillStyle = '#ffffff';
                    ctx.fillText(end.sequence, end.x + 10, end.y + 5);
                    ctx.fillStyle = '#ffa726';
                });
            }
            
            // 绘制限制酶
            ctx.fillStyle = enzyme.color;
            ctx.beginPath();
            ctx.arc(enzyme.x, enzyme.y, enzyme.width/2, 0, Math.PI * 2);
            ctx.fill();
            
            // 绘制剪刀图标
            ctx.fillStyle = '#ffffff';
            ctx.font = '20px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('✂️', enzyme.x, enzyme.y);
            
            // 绘制酶标签
            ctx.fillStyle = '#ff6b6b';
            ctx.font = 'bold 14px "Segoe UI"';
            ctx.fillText('限制酶', enzyme.x, enzyme.y + 30);
            
            // 绘制目的基因（如果可见）
            if (gene.isVisible) {
                ctx.fillStyle = gene.color;
                ctx.fillRect(gene.x, gene.y, gene.width, gene.height);
                
                // 基因标签
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('目的基因', gene.x + gene.width/2, gene.y - 10);
                
                // 如果可拖拽，添加发光效果
                if (gene.isDraggable) {
                    ctx.shadowColor = gene.color;
                    ctx.shadowBlur = 15;
                    ctx.fillRect(gene.x, gene.y, gene.width, gene.height);
                    ctx.shadowBlur = 0;
                }
            }
            
            // 绘制连接线（如果酶在移动）
            if (enzyme.isMoving && animationTime < 2) {
                ctx.strokeStyle = 'rgba(255, 107, 107, 0.5)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(150, 150);
                ctx.lineTo(350, 250);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // 绘制步骤2
        function drawStep2() {
            const plasmid = animationObjects.plasmid;
            const enzyme = animationObjects.restrictionEnzyme;
            
            // 绘制质粒
            ctx.fillStyle = plasmid.color;
            ctx.beginPath();
            ctx.arc(plasmid.x, plasmid.y, plasmid.radius, 0, Math.PI * 2);
            ctx.fill();
            
            // 绘制质粒切口
            if (plasmid.isCut) {
                ctx.strokeStyle = '#ff6b6b';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(plasmid.x, plasmid.y, plasmid.radius, plasmid.cutAngle - 0.2, plasmid.cutAngle + 0.2);
                ctx.stroke();
                
                // 绘制粘性末端
                ctx.fillStyle = '#ffa726';
                const end1X = plasmid.x + Math.cos(plasmid.cutAngle) * plasmid.radius;
                const end1Y = plasmid.y + Math.sin(plasmid.cutAngle) * plasmid.radius;
                
                ctx.beginPath();
                ctx.moveTo(end1X, end1Y);
                ctx.lineTo(end1X + 15, end1Y + 10);
                ctx.lineTo(end1X + 15, end1Y - 10);
                ctx.closePath();
                ctx.fill();
                
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 12px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('AATT', end1X + 8, end1Y + 3);
            }
            
            // 绘制质粒标记基因
            plasmid.markerGenes.forEach(gene => {
                const geneX = plasmid.x + Math.cos(gene.angle) * (plasmid.radius - 10);
                const geneY = plasmid.y + Math.sin(gene.angle) * (plasmid.radius - 10);
                
                ctx.fillStyle = gene.color;
                ctx.beginPath();
                ctx.arc(geneX, geneY, 8, 0, Math.PI * 2);
                ctx.fill();
                
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 10px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText(gene.label, geneX, geneY + 15);
            });
            
            // 绘制质粒标签
            ctx.fillStyle = '#4ecdc4';
            ctx.font = 'bold 16px "Segoe UI"';
            ctx.textAlign = 'center';
            ctx.fillText('质粒载体', plasmid.x, plasmid.y + plasmid.radius + 25);
            
            // 绘制限制酶
            ctx.fillStyle = enzyme.color;
            ctx.beginPath();
            ctx.arc(enzyme.x, enzyme.y, enzyme.width/2, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.fillStyle = '#ffffff';
            ctx.font = '20px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('✂️', enzyme.x, enzyme.y);
            
            // 绘制连接线
            if (enzyme.isMoving && animationTime > 0.5 && animationTime < 1.5) {
                ctx.strokeStyle = 'rgba(255, 107, 107, 0.5)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(550, 150);
                ctx.lineTo(700, 250);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // 绘制步骤3
        function drawStep3() {
            const gene = animationObjects.targetGene;
            const plasmid = animationObjects.plasmid;
            const ligase = animationObjects.ligase;
            const recombinant = animationObjects.recombinantPlasmid;
            
            // 绘制质粒（如果未重组）
            if (!recombinant.isVisible) {
                ctx.fillStyle = plasmid.color;
                ctx.beginPath();
                ctx.arc(plasmid.x, plasmid.y, plasmid.radius, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制切口
                if (plasmid.isCut) {
                    ctx.strokeStyle = '#ff6b6b';
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.arc(plasmid.x, plasmid.y, plasmid.radius, plasmid.cutAngle - 0.2, plasmid.cutAngle + 0.2);
                    ctx.stroke();
                }
                
                // 绘制质粒标签
                ctx.fillStyle = '#4ecdc4';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('切开的质粒', plasmid.x, plasmid.y + plasmid.radius + 25);
            }
            
            // 绘制目的基因
            if (gene.isVisible) {
                ctx.fillStyle = gene.color;
                ctx.fillRect(gene.x, gene.y, gene.width, gene.height);
                
                // 基因标签
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('目的基因', gene.x + gene.width/2, gene.y - 10);
                
                // 如果可拖拽，添加发光效果
                if (gene.isDraggable) {
                    ctx.shadowColor = gene.color;
                    ctx.shadowBlur = 15;
                    ctx.fillRect(gene.x, gene.y, gene.width, gene.height);
                    ctx.shadowBlur = 0;
                }
            }
            
            // 绘制连接酶
            if (ligase.isVisible) {
                ctx.fillStyle = ligase.color;
                ctx.beginPath();
                ctx.arc(ligase.x, ligase.y, ligase.width/2, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制胶水图标
                ctx.fillStyle = '#ffffff';
                ctx.font = '20px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('🔗', ligase.x, ligase.y);
                
                // 酶标签
                ctx.fillStyle = '#ffe66d';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.fillText('DNA连接酶', ligase.x, ligase.y + 30);
            }
            
            // 绘制重组质粒
            if (recombinant.isVisible) {
                ctx.fillStyle = recombinant.color;
                ctx.beginPath();
                ctx.arc(recombinant.x, recombinant.y, recombinant.radius, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制插入的基因
                if (recombinant.geneInserted) {
                    ctx.fillStyle = recombinant.geneColor;
                    const insertWidth = recombinant.radius * 0.6;
                    const insertHeight = 15;
                    ctx.fillRect(
                        recombinant.x - insertWidth/2,
                        recombinant.y - insertHeight/2,
                        insertWidth,
                        insertHeight
                    );
                    
                    // 基因标签
                    ctx.fillStyle = '#ffffff';
                    ctx.font = 'bold 12px "Segoe UI"';
                    ctx.textAlign = 'center';
                    ctx.fillText('目的基因', recombinant.x, recombinant.y - recombinant.radius - 10);
                }
                
                // 重组质粒标签
                ctx.fillStyle = '#4ecdc4';
                ctx.font = 'bold 16px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('重组质粒', recombinant.x, recombinant.y + recombinant.radius + 25);
            }
            
            // 绘制连接线
            if (ligase.isMoving && animationTime > 1 && animationTime < 2) {
                ctx.strokeStyle = 'rgba(255, 230, 109, 0.5)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(500, 100);
                ctx.lineTo(700, 250);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // 绘制步骤4
        function drawStep4() {
            const hostCell = animationObjects.hostCell;
            const recombinant = animationObjects.recombinantPlasmid;
            
            // 绘制宿主细胞
            if (hostCell.isVisible) {
                // 细胞膜
                ctx.strokeStyle = hostCell.color;
                ctx.lineWidth = hostCell.membraneWidth;
                ctx.beginPath();
                ctx.arc(hostCell.x, hostCell.y, hostCell.radius, 0, Math.PI * 2);
                ctx.stroke();
                
                // 细胞质
                ctx.fillStyle = 'rgba(149, 225, 211, 0.2)';
                ctx.beginPath();
                ctx.arc(hostCell.x, hostCell.y, hostCell.radius - hostCell.membraneWidth, 0, Math.PI * 2);
                ctx.fill();
                
                // 细胞标签
                ctx.fillStyle = '#95e1d3';
                ctx.font = 'bold 16px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('宿主细胞', hostCell.x, hostCell.y + hostCell.radius + 30);
            }
            
            // 绘制重组质粒
            if (recombinant.isVisible) {
                ctx.fillStyle = recombinant.color;
                ctx.beginPath();
                ctx.arc(recombinant.x, recombinant.y, recombinant.radius, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制插入的基因
                ctx.fillStyle = recombinant.geneColor;
                const insertWidth = recombinant.radius * 0.6;
                const insertHeight = 12;
                ctx.fillRect(
                    recombinant.x - insertWidth/2,
                    recombinant.y - insertHeight/2,
                    insertWidth,
                    insertHeight
                );
            }
            
            // 绘制细胞内的质粒
            hostCell.plasmidsInside.forEach(plasmid => {
                ctx.fillStyle = '#4ecdc4';
                ctx.beginPath();
                ctx.arc(plasmid.x, plasmid.y, plasmid.radius, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制插入的基因
                ctx.fillStyle = '#ffa726';
                const insertWidth = plasmid.radius * 0.8;
                const insertHeight = 8;
                ctx.fillRect(
                    plasmid.x - insertWidth/2,
                    plasmid.y - insertHeight/2,
                    insertWidth,
                    insertHeight
                );
            });
            
            // 绘制转化路径
            if (recombinant.isVisible && recombinant.x > 600) {
                ctx.strokeStyle = 'rgba(78, 205, 196, 0.5)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(700, 250);
                ctx.lineTo(550, 250);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // 绘制步骤5
        function drawStep5() {
            const proteinFactory = animationObjects.proteinFactory;
            const antibiotics = animationObjects.antibiotics;
            
            // 绘制蛋白质工厂（细胞）
            if (proteinFactory.isVisible) {
                // 细胞膜
                ctx.strokeStyle = proteinFactory.color;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(proteinFactory.x, proteinFactory.y, proteinFactory.radius, 0, Math.PI * 2);
                ctx.stroke();
                
                // 细胞质
                ctx.fillStyle = 'rgba(149, 225, 211, 0.3)';
                ctx.beginPath();
                ctx.arc(proteinFactory.x, proteinFactory.y, proteinFactory.radius - 3, 0, Math.PI * 2);
                ctx.fill();
                
                // 工厂标签
                ctx.fillStyle = '#95e1d3';
                ctx.font = 'bold 16px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('蛋白质工厂', proteinFactory.x, proteinFactory.y + proteinFactory.radius + 30);
                
                // 绘制内部质粒
                ctx.fillStyle = '#4ecdc4';
                ctx.beginPath();
                ctx.arc(proteinFactory.x, proteinFactory.y, 20, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制基因
                ctx.fillStyle = '#ffa726';
                ctx.fillRect(proteinFactory.x - 15, proteinFactory.y - 5, 30, 10);
                
                // 绘制核糖体
                ctx.fillStyle = '#ff9e80';
                ctx.beginPath();
                ctx.arc(proteinFactory.x + 30, proteinFactory.y - 20, 8, 0, Math.PI * 2);
                ctx.fill();
                
                ctx.fillStyle = '#ffffff';
                ctx.font = '12px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('●', proteinFactory.x + 30, proteinFactory.y - 20);
            }
            
            // 绘制蛋白质
            proteinFactory.proteins.forEach(protein => {
                ctx.fillStyle = protein.color;
                ctx.beginPath();
                ctx.arc(protein.x, protein.y, protein.size, 0, Math.PI * 2);
                ctx.fill();
                
                // 蛋白质标签
                if (proteinFactory.proteins.length < 10) {
                    ctx.fillStyle = '#ffffff';
                    ctx.font = '10px "Segoe UI"';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillText('蛋白', protein.x, protein.y);
                }
            });
            
            // 绘制抗生素培养基
            if (antibiotics.isVisible) {
                ctx.fillStyle = antibiotics.color;
                ctx.fillRect(antibiotics.x, antibiotics.y, antibiotics.width, antibiotics.height);
                
                // 培养基标签
                ctx.fillStyle = '#ff6b6b';
                ctx.font = 'bold 16px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('抗生素培养基', antibiotics.x + antibiotics.width/2, antibiotics.y - 10);
                
                // 绘制存活的细胞
                ctx.fillStyle = '#95e1d3';
                ctx.beginPath();
                ctx.arc(antibiotics.x + antibiotics.width/2, antibiotics.y + antibiotics.height/2, 25, 0, Math.PI * 2);
                ctx.fill();
                
                // 绘制细胞内的质粒
                ctx.fillStyle = '#4ecdc4';
                ctx.beginPath();
                ctx.arc(antibiotics.x + antibiotics.width/2, antibiotics.y + antibiotics.height/2, 8, 0, Math.PI * 2);
                ctx.fill();
                
                // 存活标签
                ctx.fillStyle = '#2a9d8f';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.fillText('存活细胞', antibiotics.x + antibiotics.width/2, antibiotics.y + antibiotics.height + 25);
            }
            
            // 绘制表达箭头
            if (animationTime > 1) {
                ctx.strokeStyle = '#64ffda';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 3]);
                ctx.beginPath();
                ctx.moveTo(proteinFactory.x + 50, proteinFactory.y);
                ctx.lineTo(proteinFactory.x + 150, proteinFactory.y);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // 箭头头
                ctx.fillStyle = '#64ffda';
                ctx.beginPath();
                ctx.moveTo(proteinFactory.x + 150, proteinFactory.y);
                ctx.lineTo(proteinFactory.x + 140, proteinFactory.y - 5);
                ctx.lineTo(proteinFactory.x + 140, proteinFactory.y + 5);
                ctx.closePath();
                ctx.fill();
                
                // 表达标签
                ctx.fillStyle = '#64ffda';
                ctx.font = 'bold 14px "Segoe UI"';
                ctx.textAlign = 'center';
                ctx.fillText('基因表达 → 蛋白质合成', proteinFactory.x + 100, proteinFactory.y - 20);
            }
        }
        
        // 鼠标事件处理
        let mouseX = 0, mouseY = 0;
        let isDragging = false;
        
        function handleMouseDown(e) {
            const rect = canvas.getBoundingClientRect();
            mouseX = e.clientX - rect.left;
            mouseY = e.clientY - rect.top;
            
            // 检查是否点击了目的基因（步骤3）
            if (currentStep === 3 && animationObjects.targetGene.isDraggable) {
                const gene = animationObjects.targetGene;
                if (mouseX > gene.x && mouseX < gene.x + gene.width &&
                    mouseY > gene.y && mouseY < gene.y + gene.height) {
                    isDragging = true;
                    gene.isDragging = true;
                }
            }
        }
        
        function handleMouseMove(e) {
            const rect = canvas.getBoundingClientRect();
            mouseX = e.clientX - rect.left;
            mouseY = e.clientY - rect.top;
            
            // 拖拽目的基因
            if (isDragging && currentStep === 3) {
                const gene = animationObjects.targetGene;
                gene.x = mouseX - gene.width/2;
                gene.y = mouseY - gene.height/2;
            }
        }
        
        function handleMouseUp() {
            if (isDragging && currentStep === 3) {
                const gene = animationObjects.targetGene;
                const plasmid = animationObjects.plasmid;
                
                // 检查是否拖拽到质粒附近
                const distance = Math.sqrt(
                    Math.pow(gene.x + gene.width/2 - plasmid.x, 2) +
                    Math.pow(gene.y + gene.height/2 - plasmid.y, 2)
                );
                
                if (distance < plasmid.radius + 20) {
                    // 基因连接到质粒
                    gene.isDragging = false;
                    gene.x = plasmid.x - gene.width/2;
                    gene.y = plasmid.y - gene.height/2;
                    
                    // 触发连接动画
                    animationObjects.ligase.isVisible = true;
                    animationTime = 1; // 跳到连接动画阶段
                }
            }
            
            isDragging = false;
            if (animationObjects.targetGene) {
                animationObjects.targetGene.isDragging = false;
            }
        }
        
        // 更新提示文本
        function updateHintText() {
            const hints = [
                '',
                '点击"播放动画"观看限制酶剪切DNA的过程',
                '观看质粒载体被相同限制酶剪切的过程',
                '将目的基因拖拽到质粒上进行连接',
                '观看重组质粒进入宿主细胞的过程',
                '观察基因表达和蛋白质合成的过程'
            ];
            
            if (currentStep >= 1 && currentStep <= 5) {
                hintText.innerHTML = `<span>💡</span> ${hints[currentStep]}`;
                hintText.style.display = 'flex';
            }
        }
        
        // 重置动画
        function resetAnimation() {
            resetAnimationState();
            goToStep(1);
            draw();
        }
        
        // 动画循环
        function animate() {
            if (animationPlaying) {
                startAnimation();
            } else {
                draw();
            }
            requestAnimationFrame(animate);
        }
        
        // 初始化应用
        window.addEventListener('load', init);
    </script>
</body>
</html>

### 3. 过程输出


## 交互式教学动画使用指南

欢迎使用“基因工程全过程”交互式教学动画！本指南将帮助您充分利用这一教学工具，获得最佳的学习体验。

---

### 一、功能说明

本动画是一个基于HTML5 Canvas技术开发的交互式教学工具，旨在通过动态可视化方式，生动展示基因工程从“限制酶剪切”到“基因表达”的完整流程。它将抽象的分子生物学概念转化为直观的动画和可操作的交互，特别适合高中及大学低年级生物学课程的教学与自学。

### 二、主要功能

1.  **分步流程学习**：
    *   动画将基因工程全过程清晰地分解为五个核心步骤：**限制酶剪切 → 载体准备 → 重组连接 → 转化 → 表达与筛选**。
    *   用户可通过顶部的导航按钮或控制面板，自由跳转到任意步骤进行学习或复习。

2.  **交互式操作**：
    *   **步骤3（重组连接）** 是本动画的核心交互点。学习者可以**用鼠标拖拽“目的基因”**，将其与“切开的质粒”进行连接，亲身体验DNA重组的操作。
    *   拖拽成功后，系统会自动触发“DNA连接酶”的动画，完成连接过程，给予用户即时的正反馈。

3.  **动画播放与控制**：
    *   每个步骤都配有详细的自动播放动画，演示该步骤的动态过程。
    *   提供**播放/暂停、上一步、下一步、重置**等控制按钮，让学习者完全掌控学习节奏。

4.  **同步知识讲解**：
    *   动画区域右侧设有同步更新的**知识讲解面板**，详细解释当前步骤的原理、关键术语和生物学意义。
    *   关键术语以标签形式呈现，鼠标悬停可查看简要解释。

5.  **视觉化图例**：
    *   界面底部设有**颜色图例**，清晰标注了动画中不同元素（如限制酶、目的基因、质粒等）的颜色编码，帮助用户快速识别。

### 三、设计特色

1.  **专业性与趣味性结合**：
    *   **科学准确性**：严格遵循基因工程的标准操作流程和分子机制（如粘性末端互补配对、DNA连接酶作用等）。
    *   **视觉隐喻**：采用“分子剪刀”（限制酶）、“分子胶水”（DNA连接酶）、“分子货车”（质粒载体）、“细胞工厂”（宿主细胞）等生动比喻，降低理解门槛。

2.  **沉浸式学习环境**：
    *   采用深蓝色科技感背景，营造专注的“分子实验室”氛围。
    *   动画角色设计简洁明了，色彩鲜明，重点突出。

3.  **符合认知规律**：
    *   遵循“分步讲解、串联成线”的原则，将复杂流程拆解为可管理的模块。
    *   每个步骤动画结束后，会**自动过渡到下一步**，帮助学习者建立完整的流程概念。

### 四、教学要点（给教师的建议）

本动画可用于辅助讲解以下核心知识点：

| 步骤 | 核心概念 | 可讨论的问题 |
| :--- | :--- | :--- |
| **1. 限制酶剪切** | 酶的特异性、识别序列、粘性末端 | “为什么选择同一种限制酶来切割目的基因和质粒？” |
| **2. 载体准备** | 质粒的结构与功能（启动子、抗性基因） | “质粒上的‘抗性基因’在后续步骤中起什么作用？” |
| **3. 重组连接** | 碱基互补配对原理、DNA连接酶的作用 | “如果目的基因和质粒的粘性末端不匹配，会发生什么？” |
| **4. 转化** | 宿主细胞、转化方法（热激/电击） | “转化后，是不是所有细胞都成功接收了重组质粒？” |
| **5. 表达与筛选** | 抗生素筛选、基因表达（转录与翻译） | “如何确保我们培养的细胞是成功转化了的？” |

**课堂应用建议**：
*   **引入环节**：播放完整动画，让学生对基因工程流程建立宏观印象。
*   **讲解环节**：分步播放，每播完一步，暂停并利用右侧讲解面板进行深入讨论。
*   **互动环节**：在步骤3，邀请学生上台尝试拖拽连接，并解释其原理。
*   **复习环节**：使用“重置”和导航按钮，快速回顾特定难点步骤。

### 五、使用建议

1.  **首次使用**：建议点击 **“播放动画”** 按钮，从头至尾观看一遍完整流程，建立整体印象。
2.  **自主学习**：利用步骤导航按钮，针对自己薄弱的环节进行反复观看和阅读讲解。
3.  **重点关注交互**：务必亲自体验**步骤3的拖拽操作**，这是理解“重组”概念的关键。
4.  **善用提示**：界面底部的**闪烁提示框**会给出当前步骤的操作指引，请留意查看。
5.  **技术兼容**：本动画基于现代浏览器标准开发，建议在Chrome、Edge、Firefox或Safari的最新版本上使用，以获得最佳效果。

---

**祝您在探索基因工程奥秘的旅程中，收获知识与乐趣！**

> 本工具为教学演示而设计，旨在促进理解。实际基因工程操作更为复杂，请在专业指导下进行。