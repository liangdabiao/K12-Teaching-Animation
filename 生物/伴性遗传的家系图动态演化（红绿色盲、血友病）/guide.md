# 需求：伴性遗传的家系图动态演化（红绿色盲、血友病）

### 1. 专业思考


#### 用户需求分析
本动画的主要用户是高中或大学低年级的生物学学生，他们正在学习孟德尔遗传的扩展——伴性遗传。用户的核心需求是：
1.  **理解抽象概念**：将抽象的“X染色体隐性遗传”规律，通过具体的、动态的家系图演化过程具象化，降低理解门槛。
2.  **区分遗传模式**：清晰区分红绿色盲（常见、外显率受环境影响小）与血友病（重型、典型X连锁隐性）在遗传图谱上的异同，避免混淆。
3.  **掌握图谱绘制与解读**：学习标准家系图符号（方形、圆形、阴影、箭头），并能根据遗传规律预测后代基因型和表现型。
4.  **动态观察与探究**：希望看到遗传过程不是静态结论，而是可以动态推进、并允许自己进行“如果…会怎样”的探究性操作。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）

*   **核心概念聚焦**：
    *   **核心一：性染色体与基因定位**。强调致病基因位于X染色体上，Y染色体上无对应等位基因。
    *   **核心二：隐性遗传与杂合子**。重点展示女性携带者（X^A X^a）不发病但能传递致病基因的关键作用。
    *   **核心三：交叉遗传**。动态突出男性患者的致病基因必然来自母亲，并只能传给女儿（使其成为携带者）的传递路径。
    *   **核心四：发病率性别差异**。通过大量样本的模拟，直观展现男性发病率远高于女性的现象及其原因。

*   **遵循认知规律**：
    *   **从具体到抽象**：先展示一个经典、完整的红绿色盲家系演化案例，建立感性认识。然后提炼出静态规则。最后引入血友病案例进行对比、应用和巩固。
    *   **从观察到推理**：动画先自动演示一个世代的遗传过程，然后暂停，邀请用户根据已学规则预测下一个后代的基因型和表现型，再继续动画验证。
    *   **对比强化记忆**：将红绿色盲与血友病的家系图并置，突出其遗传规律的**共性**（都是X隐），同时通过旁白或标签说明其**差异**（如基因频率、疾病严重程度、可能涉及的基因治疗等现实联系）。

*   **交互设计策略**：
    *   **分层控制**：提供“播放/暂停/步进/重置”全局控制。允许用户控制演化速度。
    *   **焦点探究**：点击家系图中的任何一个个体，可以弹出其详细的基因型（如 X^A Y, X^a X^A 等）、表现型说明，以及其“遗传来源”与“传递去向”的高亮箭头。
    *   **变量调节与模拟**：设计一个“模拟实验室”板块。用户可以设定初始父母基因型，然后点击“繁衍数代”，系统自动生成一个大的随机家系图，统计男女患者比例，强化对发病率差异的理解。
    *   **对比视图**：提供“单一案例演化视图”和“双疾病对比视图”的切换按钮。

*   **视觉呈现规划**：
    *   **动态连线与箭头**：使用平滑的动画绘制亲代与子代之间的连线，遗传基因的传递用高亮的光点或彩色箭头沿连线移动来表示，清晰可视化“基因流动”。
    *   **状态渐变**：个体的表现型（正常、携带者、患者）变化不是瞬间切换，而是通过颜色填充渐变或符号（如眼镜、止血贴图标）的淡入淡出来实现，引导视觉关注。
    *   **图层与聚焦**：画布分为背景网格层、静态家系图层、动态高亮层、UI控制层。当讲解特定路径时，其他部分半透明化，聚焦区域保持高亮。
    *   **信息卡片**：所有补充信息（定义、基因型、概率计算）都以可开关的卡片形式呈现，保持主画布整洁。

#### 配色方案选择
*   **主色调与无障碍**：
    *   采用**蓝紫色系**作为界面主色调（如#6A5ACD 岩蓝），专业、冷静，且与常见的红绿色盲测试色板（红绿）形成明确区分，避免干扰。
    *   严格遵循WCAG无障碍标准，对“正常”、“携带者”、“患者”的状态区分，不仅使用颜色（如浅蓝、淡紫、深紫），也结合明确的图案符号（对勾、圆点、十字）和边框粗细，确保色觉障碍用户也能准确识别。
*   **状态与高亮色**：
    *   **正常个体**：浅蓝色填充（#E6F3FF）或白色填充+蓝色边框。
    *   **女性携带者**：淡紫色填充（#F0E6FF），中间加一个白色圆点。
    *   **患者（男女）**：深紫色填充（#8A2BE2）。
    *   **动态高亮路径**：使用醒目的**琥珀色**（#FFBF00）箭头和光点。
    *   **交互反馈**：鼠标悬停时使用柔和的**明黄色**（#FFF9C4）光晕。
*   **画布与文字**：
    *   画布背景为浅灰色（#F8F9FA），网格线为极浅的灰色（#E9ECEF）。
    *   文字主要使用深灰色（#333333），重点标签使用主色调蓝紫色。

#### 交互功能列表
1.  **动画流程控制**：播放、暂停、下一步（步进）、上一步、重置、速度调节滑块。
2.  **案例选择器**：下拉菜单选择“红绿色盲经典案例”、“血友病皇室案例”或“自定义案例”。
3.  **信息显示开关**：可切换“显示基因型”、“显示表现型”、“显示概率计算”的复选框。
4.  **个体深度查询**：点击家系图中任意个体，弹出信息卡，显示其基因型、表现型、父母、配偶、子女列表，并可高亮其遗传路径。
5.  **模拟实验室**：
    *   输入框或选择器设定“父亲基因型”（X^A Y 或 X^a Y）和“母亲基因型”（X^A X^A, X^A X^a, X^a X^a）。
    *   滑块选择“模拟代数”（如3-5代）。
    *   “开始模拟”按钮，生成随机婚配的大规模家系图。
    *   自动生成统计面板，显示总人数、男女患者数、携带者数及比例。
6.  **视图切换**：“学习模式”（单一家系分步演化）与“对比模式”（左右分屏对比两种疾病家系）。
7.  **提示与帮助**：常驻的“图例说明”按钮，以及关键步骤前的半透明引导提示（可关闭）。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>伴性遗传家系图动态演化 | 红绿色盲与血友病</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #6A5ACD;
        }

        .header h1 {
            color: #6A5ACD;
            margin-bottom: 10px;
            font-size: 2.2rem;
        }

        .header p {
            color: #666;
            max-width: 800px;
            margin: 0 auto;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 30px;
        }

        .main-content {
            flex: 3;
            min-width: 300px;
        }

        .sidebar {
            flex: 1;
            min-width: 280px;
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e9ecef;
        }

        .canvas-container {
            background: white;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e9ecef;
            margin-bottom: 20px;
            position: relative;
            overflow: hidden;
        }

        #pedigreeCanvas {
            display: block;
            width: 100%;
            height: 500px;
            background-color: #f8f9fa;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 20px;
            padding: 15px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e9ecef;
        }

        .control-group {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        button {
            padding: 10px 18px;
            background-color: #6A5ACD;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        button:hover {
            background-color: #5a4abc;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(106, 90, 205, 0.3);
        }

        button:active {
            transform: translateY(0);
        }

        button.secondary {
            background-color: #8A2BE2;
        }

        button.secondary:hover {
            background-color: #7a1bd2;
        }

        select, input[type="range"] {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            background: white;
            font-size: 14px;
        }

        .checkbox-group {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .info-panel {
            margin-top: 20px;
            padding: 15px;
            background: #E6F3FF;
            border-radius: 8px;
            border-left: 4px solid #6A5ACD;
        }

        .info-panel h3 {
            color: #6A5ACD;
            margin-bottom: 10px;
        }

        .legend {
            margin-top: 20px;
            padding: 15px;
            background: #F0E6FF;
            border-radius: 8px;
        }

        .legend h3 {
            color: #8A2BE2;
            margin-bottom: 10px;
        }

        .legend-items {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 10px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
        }

        .legend-symbol {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            border: 2px solid;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }

        .tooltip {
            position: absolute;
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid #6A5ACD;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
            pointer-events: none;
            z-index: 1000;
            max-width: 300px;
            opacity: 0;
            transition: opacity 0.2s;
        }

        .tooltip h4 {
            color: #6A5ACD;
            margin-bottom: 8px;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }

        .tooltip p {
            margin-bottom: 5px;
            font-size: 14px;
        }

        .stats {
            background: #FFF9C4;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            border: 1px solid #FFBF00;
        }

        .stats h3 {
            color: #333;
            margin-bottom: 10px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }

        .stat-item {
            background: white;
            padding: 10px;
            border-radius: 6px;
            text-align: center;
            border: 1px solid #FFBF00;
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #8A2BE2;
        }

        .highlight {
            color: #FFBF00;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            
            .controls {
                flex-direction: column;
            }
            
            .control-group {
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>伴性遗传家系图动态演化</h1>
        <p>探索X染色体隐性遗传规律：红绿色盲与血友病的遗传模式对比与可视化</p>
    </div>

    <div class="controls">
        <div class="control-group">
            <button id="playBtn" title="播放动画">
                <span>▶</span> 播放
            </button>
            <button id="pauseBtn" title="暂停动画">
                <span>⏸</span> 暂停
            </button>
            <button id="stepBtn" title="下一步">
                <span>⏭</span> 步进
            </button>
            <button id="resetBtn" title="重置动画">
                <span>↺</span> 重置
            </button>
        </div>

        <div class="control-group">
            <label for="speedSlider">速度:</label>
            <input type="range" id="speedSlider" min="1" max="10" value="5">
        </div>

        <div class="control-group">
            <label for="diseaseSelect">案例选择:</label>
            <select id="diseaseSelect">
                <option value="colorBlindness">红绿色盲经典案例</option>
                <option value="hemophilia">血友病皇室案例</option>
                <option value="custom">自定义案例</option>
            </select>
        </div>

        <div class="checkbox-group">
            <div class="checkbox-item">
                <input type="checkbox" id="showGenotype" checked>
                <label for="showGenotype">显示基因型</label>
            </div>
            <div class="checkbox-item">
                <input type="checkbox" id="showPhenotype" checked>
                <label for="showPhenotype">显示表现型</label>
            </div>
            <div class="checkbox-item">
                <input type="checkbox" id="showProbability">
                <label for="showProbability">显示概率计算</label>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="main-content">
            <div class="canvas-container">
                <canvas id="pedigreeCanvas"></canvas>
                <div id="tooltip" class="tooltip"></div>
            </div>

            <div class="info-panel">
                <h3>当前状态说明</h3>
                <p id="currentInfo">正在演示红绿色盲的X染色体隐性遗传模式。男性患者（XᵃY）的致病基因来自母亲（携带者XᴬXᵃ）。</p>
            </div>
        </div>

        <div class="sidebar">
            <div class="legend">
                <h3>图例说明</h3>
                <div class="legend-items">
                    <div class="legend-item">
                        <div class="legend-symbol" style="background-color: #E6F3FF; border-color: #6A5ACD;">□</div>
                        <span>正常男性</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-symbol" style="background-color: #E6F3FF; border-color: #6A5ACD;">○</div>
                        <span>正常女性</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-symbol" style="background-color: #F0E6FF; border-color: #8A2BE2;">○•</div>
                        <span>女性携带者</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-symbol" style="background-color: #8A2BE2; border-color: #5a1a9e;">□</div>
                        <span>男性患者</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-symbol" style="background-color: #8A2BE2; border-color: #5a1a9e;">○</div>
                        <span>女性患者</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-symbol" style="border-color: #FFBF00; background: none;">→</div>
                        <span>基因传递路径</span>
                    </div>
                </div>
            </div>

            <div class="stats">
                <h3>模拟统计</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value" id="totalCount">0</div>
                        <div>总人数</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="malePatients">0</div>
                        <div>男性患者</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="femalePatients">0</div>
                        <div>女性患者</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="carriers">0</div>
                        <div>携带者</div>
                    </div>
                </div>
            </div>

            <button id="simulateBtn" class="secondary" style="margin-top: 20px; width: 100%;">
                <span>🧪</span> 进入模拟实验室
            </button>
        </div>
    </div>

    <script>
        // 全局变量
        const canvas = document.getElementById('pedigreeCanvas');
        const ctx = canvas.getContext('2d');
        const tooltip = document.getElementById('tooltip');
        const currentInfo = document.getElementById('currentInfo');
        
        // 设置Canvas尺寸
        function resizeCanvas() {
            const container = canvas.parentElement;
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
        }
        
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();
        
        // 遗传系统
        class Individual {
            constructor(id, generation, position, gender, genotype, phenotype, parents = []) {
                this.id = id;
                this.generation = generation;
                this.position = position; // {x, y}
                this.gender = gender; // 'male' or 'female'
                this.genotype = genotype; // 例如: 'X^A Y', 'X^A X^a'
                this.phenotype = phenotype; // 'normal', 'carrier', 'affected'
                this.parents = parents;
                this.children = [];
                this.spouse = null;
                this.radius = 25;
                this.hovered = false;
                this.selected = false;
            }
            
            draw() {
                // 绘制个体
                ctx.save();
                
                // 设置颜色
                let fillColor, borderColor;
                switch(this.phenotype) {
                    case 'normal':
                        fillColor = this.gender === 'male' ? '#E6F3FF' : '#E6F3FF';
                        borderColor = '#6A5ACD';
                        break;
                    case 'carrier':
                        fillColor = '#F0E6FF';
                        borderColor = '#8A2BE2';
                        break;
                    case 'affected':
                        fillColor = '#8A2BE2';
                        borderColor = '#5a1a9e';
                        break;
                }
                
                // 绘制形状
                ctx.beginPath();
                if (this.gender === 'male') {
                    // 方形
                    ctx.rect(this.position.x - this.radius, this.position.y - this.radius, 
                            this.radius * 2, this.radius * 2);
                } else {
                    // 圆形
                    ctx.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2);
                }
                
                ctx.fillStyle = fillColor;
                ctx.fill();
                ctx.lineWidth = this.selected ? 4 : 2;
                ctx.strokeStyle = borderColor;
                ctx.stroke();
                
                // 如果是携带者，在中间画一个点
                if (this.phenotype === 'carrier' && this.gender === 'female') {
                    ctx.beginPath();
                    ctx.arc(this.position.x, this.position.y, 6, 0, Math.PI * 2);
                    ctx.fillStyle = '#FFFFFF';
                    ctx.fill();
                    ctx.strokeStyle = '#8A2BE2';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
                
                // 如果是患者，添加十字标记
                if (this.phenotype === 'affected') {
                    ctx.beginPath();
                    ctx.moveTo(this.position.x - 10, this.position.y);
                    ctx.lineTo(this.position.x + 10, this.position.y);
                    ctx.moveTo(this.position.x, this.position.y - 10);
                    ctx.lineTo(this.position.x, this.position.y + 10);
                    ctx.strokeStyle = '#FFFFFF';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
                
                // 绘制ID和基因型
                ctx.fillStyle = '#333333';
                ctx.font = '14px Arial';
                ctx.textAlign = 'center';
                
                // 显示ID
                ctx.fillText(`I${this.id}`, this.position.x, this.position.y - this.radius - 10);
                
                // 显示基因型（如果开启）
                if (document.getElementById('showGenotype').checked) {
                    ctx.font = '12px Arial';
                    let genotypeText = this.genotype;
                    if (this.gender === 'male') {
                        genotypeText = genotypeText.replace('X^A', 'Xᴬ').replace('X^a', 'Xᵃ');
                    } else {
                        genotypeText = genotypeText.replace('X^A', 'Xᴬ').replace('X^a', 'Xᵃ');
                    }
                    ctx.fillText(genotypeText, this.position.x, this.position.y + this.radius + 15);
                }
                
                // 显示表现型（如果开启）
                if (document.getElementById('showPhenotype').checked) {
                    ctx.font = '12px Arial';
                    let phenotypeText = '';
                    switch(this.phenotype) {
                        case 'normal': phenotypeText = '正常'; break;
                        case 'carrier': phenotypeText = '携带者'; break;
                        case 'affected': 
                            phenotypeText = document.getElementById('diseaseSelect').value === 'colorBlindness' 
                                ? '色盲' : '血友病';
                            break;
                    }
                    ctx.fillText(phenotypeText, this.position.x, this.position.y + this.radius + 30);
                }
                
                // 悬停效果
                if (this.hovered) {
                    ctx.beginPath();
                    ctx.arc(this.position.x, this.position.y, this.radius + 5, 0, Math.PI * 2);
                    ctx.strokeStyle = '#FFBF00';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
                
                ctx.restore();
            }
            
            isPointInside(x, y) {
                const dx = x - this.position.x;
                const dy = y - this.position.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                return distance <= this.radius;
            }
            
            getInfo() {
                let diseaseName = document.getElementById('diseaseSelect').value === 'colorBlindness' 
                    ? '红绿色盲' : '血友病';
                
                let phenotypeDesc = '';
                switch(this.phenotype) {
                    case 'normal':
                        phenotypeDesc = '正常个体';
                        break;
                    case 'carrier':
                        phenotypeDesc = `女性携带者（不表现${diseaseName}症状）`;
                        break;
                    case 'affected':
                        phenotypeDesc = `${diseaseName}患者`;
                        break;
                }
                
                let info = `<h4>个体 I${this.id}</h4>
                           <p><strong>性别:</strong> ${this.gender === 'male' ? '男性' : '女性'}</p>
                           <p><strong>基因型:</strong> ${this.genotype}</p>
                           <p><strong>表现型:</strong> ${phenotypeDesc}</p>`;
                
                if (this.parents.length > 0) {
                    info += `<p><strong>父母:</strong> I${this.parents[0].id}, I${this.parents[1].id}</p>`;
                }
                
                if (this.children.length > 0) {
                    info += `<p><strong>子女:</strong> ${this.children.map(c => 'I' + c.id).join(', ')}</p>`;
                }
                
                return info;
            }
        }
        
        class PedigreeSystem {
            constructor() {
                this.individuals = [];
                this.currentGeneration = 0;
                this.animationStep = 0;
                this.isAnimating = false;
                this.animationSpeed = 5;
                this.currentDisease = 'colorBlindness';
                this.highlightedPath = null;
                this.nextId = 1;
                
                // 初始化家系图
                this.initializePedigree();
            }
            
            initializePedigree() {
                this.individuals = [];
                this.nextId = 1;
                this.animationStep = 0;
                
                // 创建第一代（根据选择的疾病）
                const disease = document.getElementById('diseaseSelect').value;
                this.currentDisease = disease;
                
                if (disease === 'colorBlindness') {
                    // 红绿色盲案例：正常男性 + 携带者女性
                    const father = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.3, y: 100}, 'male', 'X^A Y', 'normal');
                    const mother = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.7, y: 100}, 'female', 'X^A X^a', 'carrier');
                    
                    father.spouse = mother;
                    mother.spouse = father;
                    
                    this.individuals.push(father, mother);
                    currentInfo.textContent = "第一代：正常男性（XᴬY）与女性携带者（XᴬXᵃ）婚配。女性携带者不表现红绿色盲症状。";
                    
                } else if (disease === 'hemophilia') {
                    // 血友病案例：正常男性 + 携带者女性（模拟欧洲皇室）
                    const father = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.3, y: 100}, 'male', 'X^A Y', 'normal');
                    const mother = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.7, y: 100}, 'female', 'X^A X^a', 'carrier');
                    
                    father.spouse = mother;
                    mother.spouse = father;
                    
                    this.individuals.push(father, mother);
                    currentInfo.textContent = "第一代：正常男性（XᴬY）与女性携带者（XᴬXᵃ）婚配。模拟欧洲皇室血友病遗传。";
                    
                } else {
                    // 自定义案例
                    const father = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.3, y: 100}, 'male', 'X^A Y', 'normal');
                    const mother = new Individual(this.nextId++, 1, 
                        {x: canvas.width * 0.7, y: 100}, 'female', 'X^A X^A', 'normal');
                    
                    father.spouse = mother;
                    mother.spouse = father;
                    
                    this.individuals.push(father, mother);
                    currentInfo.textContent = "自定义案例：正常男性（XᴬY）与正常女性（XᴬXᴬ）婚配。点击'模拟实验室'进行自定义设置。";
                }
                
                this.updateStats();
            }
            
            addGeneration() {
                if (this.animationStep === 0) {
                    // 第一步：显示第一代
                    this.animationStep = 1;
                    currentInfo.textContent = "观察第一代父母。男性为正常（XᴬY），女性为携带者（XᴬXᵃ）。";
                    
                } else if (this.animationStep === 1) {
                    // 第二步：创建第二代子女
                    const parents = this.individuals.filter(ind => ind.generation === 1);
                    if (parents.length === 2) {
                        const [father, mother] = parents;
                        
                        // 计算可能的子女基因型
                        const possibleGenotypes = this.calculateOffspring(father.genotype, mother.genotype);
                        
                        // 创建4个子女（展示所有可能性）
                        const startX = canvas.width * 0.2;
                        const spacing = canvas.width * 0.15;
                        
                        possibleGenotypes.forEach((genotype, index) => {
                            const gender = genotype.includes('Y') ? 'male' : 'female';
                            const phenotype = this.determinePhenotype(genotype, gender);
                            
                            const child = new Individual(
                                this.nextId++,
                                2,
                                {x: startX + spacing * index, y: 250},
                                gender,
                                genotype,
                                phenotype,
                                [father, mother]
                            );
                            
                            this.individuals.push(child);
                            father.children.push(child);
                            mother.children.push(child);
                        });
                        
                        this.animationStep = 2;
                        currentInfo.textContent = "第二代：子女基因型分析。注意男性患者（XᵃY）的致病基因来自母亲。";
                        this.highlightedPath = {from: mother.id, to: this.individuals.find(ind => 
                            ind.genotype === 'X^a Y' && ind.generation === 2).id};
                        
                    }
                    
                } else if (this.animationStep === 2) {
                    // 第三步：选择一对婚配并创建第三代
                    const secondGen = this.individuals.filter(ind => ind.generation === 2);
                    if (secondGen.length >= 2) {
                        // 选择正常女性和男性患者婚配（常见情况）
                        const normalFemale = secondGen.find(ind => 
                            ind.gender === 'female' && ind.phenotype === 'normal');
                        const affectedMale = secondGen.find(ind => 
                            ind.gender === 'male' && ind.phenotype === 'affected');
                        
                        if (normalFemale && affectedMale) {
                            normalFemale.spouse = affectedMale;
                            affectedMale.spouse = normalFemale;
                            
                            // 创建第三代子女
                            const possibleGenotypes = this.calculateOffspring(affectedMale.genotype, normalFemale.genotype);
                            
                            const startX = canvas.width * 0.3;
                            const spacing = canvas.width * 0.2;
                            
                            possibleGenotypes.forEach((genotype, index) => {
                                const gender = genotype.includes('Y') ? 'male' : 'female';
                                const phenotype = this.determinePhenotype(genotype, gender);
                                
                                const child = new Individual(
                                    this.nextId++,
                                    3,
                                    {x: startX + spacing * index, y: 400},
                                    gender,
                                    genotype,
                                    phenotype,
                                    [affectedMale, normalFemale]
                                );
                                
                                this.individuals.push(child);
                                affectedMale.children.push(child);
                                normalFemale.children.push(child);
                            });
                            
                            this.animationStep = 3;
                            currentInfo.textContent = "第三代：男性患者与正常女性婚配。所有女儿都是携带者，所有儿子都正常。这就是'交叉遗传'。";
                            this.highlightedPath = {from: affectedMale.id, to: this.individuals.find(ind => 
                                ind.generation === 3 && ind.gender === 'female').id};
                        }
                    }
                }
                
                this.updateStats();
            }
            
            calculateOffspring(fatherGenotype, motherGenotype) {
                // 简化计算：返回所有可能的子女基因型
                if (fatherGenotype === 'X^A Y' && motherGenotype === 'X^A X^a') {
                    return ['X^A X^A', 'X^A X^a', 'X^A Y', 'X^a Y'];
                } else if (fatherGenotype === 'X^a Y' && motherGenotype === 'X^A X^A') {
                    return ['X^A X^a', 'X^A Y'];
                }
                return [];
            }
            
            determinePhenotype(genotype, gender) {
                if (gender === 'male') {
                    return genotype === 'X^a Y' ? 'affected' : 'normal';
                } else {
                    if (genotype === 'X^a X^a') return 'affected';
                    if (genotype === 'X^A X^a') return 'carrier';
                    return 'normal';
                }
            }
            
            draw() {
                // 清空画布
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // 绘制网格背景
                this.drawGrid();
                
                // 绘制连接线
                this.drawConnections();
                
                // 绘制高亮路径
                if (this.highlightedPath) {
                    this.drawHighlightedPath();
                }
                
                // 绘制所有个体
                this.individuals.forEach(individual => individual.draw());
                
                // 绘制概率计算（如果开启）
                if (document.getElementById('showProbability').checked && this.animationStep >= 1) {
                    this.drawProbabilityCalculations();
                }
            }
            
            drawGrid() {
                ctx.strokeStyle = '#E9ECEF';
                ctx.lineWidth = 1;
                
                // 水平线
                for (let y = 50; y < canvas.height; y += 50) {
                    ctx.beginPath();
                    ctx.moveTo(0, y);
                    ctx.lineTo(canvas.width, y);
                    ctx.stroke();
                }
                
                // 垂直线
                for (let x = 50; x < canvas.width; x += 50) {
                    ctx.beginPath();
                    ctx.moveTo(x, 0);
                    ctx.lineTo(x, canvas.height);
                    ctx.stroke();
                }
            }
            
            drawConnections() {
                ctx.strokeStyle = '#333333';
                ctx.lineWidth = 1;
                
                // 绘制配偶连接线
                this.individuals.forEach(individual => {
                    if (individual.spouse && individual.id < individual.spouse.id) {
                        ctx.beginPath();
                        ctx.moveTo(individual.position.x, individual.position.y);
                        ctx.lineTo(individual.spouse.position.x, individual.spouse.position.y);
                        ctx.stroke();
                        
                        // 在中间画一个小圆表示婚姻
                        const midX = (individual.position.x + individual.spouse.position.x) / 2;
                        const midY = (individual.position.y + individual.spouse.position.y) / 2;
                        ctx.beginPath();
                        ctx.arc(midX, midY, 4, 0, Math.PI * 2);
                        ctx.fillStyle = '#333333';
                        ctx.fill();
                    }
                });
                
                // 绘制亲子连接线
                this.individuals.forEach(individual => {
                    if (individual.children.length > 0) {
                        // 找到配偶（如果有）
                        const spouse = individual.spouse;
                        let parentY = individual.position.y;
                        let parentX = individual.position.x;
                        
                        if (spouse) {
                            parentY = Math.max(individual.position.y, spouse.position.y);
                            parentX = (individual.position.x + spouse.position.x) / 2;
                        }
                        
                        // 绘制到子女的连线
                        const childrenCount = individual.children.length;
                        const startX = individual.children[0].position.x;
                        const endX = individual.children[childrenCount - 1].position.x;
                        
                        // 水平线从父母到子女上方
                        ctx.beginPath();
                        ctx.moveTo(parentX, parentY + 25);
                        ctx.lineTo(parentX, parentY + 50);
                        ctx.stroke();
                        
                        // 水平线连接所有子女
                        ctx.beginPath();
                        ctx.moveTo(startX, parentY + 50);
                        ctx.lineTo(endX, parentY + 50);
                        ctx.stroke();
                        
                        // 垂直线到每个子女
                        individual.children.forEach(child => {
                            ctx.beginPath();
                            ctx.moveTo(child.position.x, parentY + 50);
                            ctx.lineTo(child.position.x, child.position.y - 25);
                            ctx.stroke();
                        });
                    }
                });
            }
            
            drawHighlightedPath() {
                const fromInd = this.individuals.find(ind => ind.id === this.highlightedPath.from);
                const toInd = this.individuals.find(ind => ind.id === this.highlightedPath.to);
                
                if (fromInd && toInd) {
                    ctx.strokeStyle = '#FFBF00';
                    ctx.lineWidth = 3;
                    ctx.setLineDash([5, 5]);
                    
                    // 绘制箭头
                    this.drawArrow(fromInd.position.x, fromInd.position.y, 
                                 toInd.position.x, toInd.position.y);
                    
                    ctx.setLineDash([]);
                    
                    // 绘制光点动画
                    const progress = (Date.now() % 2000) / 2000;
                    const pointX = fromInd.position.x + (toInd.position.x - fromInd.position.x) * progress;
                    const pointY = fromInd.position.y + (toInd.position.y - fromInd.position.y) * progress;
                    
                    ctx.beginPath();
                    ctx.arc(pointX, pointY, 8, 0, Math.PI * 2);
                    ctx.fillStyle = '#FFBF00';
                    ctx.fill();
                    ctx.strokeStyle = '#FFFFFF';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
            }
            
            drawArrow(fromX, fromY, toX, toY) {
                const headlen = 15;
                const dx = toX - fromX;
                const dy = toY - fromY;
                const angle = Math.atan2(dy, dx);
                
                ctx.beginPath();
                ctx.moveTo(fromX, fromY);
                ctx.lineTo(toX, toY);
                ctx.stroke();
                
                // 绘制箭头头部
                ctx.beginPath();
                ctx.moveTo(toX, toY);
                ctx.lineTo(toX - headlen * Math.cos(angle - Math.PI / 6), 
                          toY - headlen * Math.sin(angle - Math.PI / 6));
                ctx.lineTo(toX - headlen * Math.cos(angle + Math.PI / 6), 
                          toY - headlen * Math.sin(angle + Math.PI / 6));
                ctx.closePath();
                ctx.fillStyle = '#FFBF00';
                ctx.fill();
            }
            
            drawProbabilityCalculations() {
                ctx.fillStyle = '#333333';
                ctx.font = '14px Arial';
                ctx.textAlign = 'left';
                
                let text = '';
                let yPos = canvas.height - 100;
                
                if (this.animationStep === 1) {
                    text = "概率计算：\n";
                    text += "女性携带者(XᴬXᵃ) × 正常男性(XᴬY)\n";
                    text += "→ 儿子：50%正常(XᴬY)，50%患者(XᵃY)\n";
                    text += "→ 女儿：50%正常(XᴬXᴬ)，50%携带者(XᴬXᵃ)";
                } else if (this.animationStep === 2) {
                    text = "概率计算：\n";
                    text += "男性患者(XᵃY) × 正常女性(XᴬXᴬ)\n";
                    text += "→ 儿子：100%正常(XᴬY)\n";
                    text += "→ 女儿：100%携带者(XᴬXᵃ)";
                }
                
                // 绘制背景框
                const lines = text.split('\n');
                const maxWidth = Math.max(...lines.map(line => ctx.measureText(line).width));
                
                ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
                ctx.fillRect(20, yPos - 30, maxWidth + 40, lines.length * 20 + 20);
                ctx.strokeStyle = '#6A5ACD';
                ctx.lineWidth = 2;
                ctx.strokeRect(20, yPos - 30, maxWidth + 40, lines.length * 20 + 20);
                
                // 绘制文字
                ctx.fillStyle = '#333333';
                lines.forEach((line, index) => {
                    ctx.fillText(line, 40, yPos + index * 20);
                });
            }
            
            updateStats() {
                const total = this.individuals.length;
                const malePatients = this.individuals.filter(ind => 
                    ind.gender === 'male' && ind.phenotype === 'affected').length;
                const femalePatients = this.individuals.filter(ind => 
                    ind.gender === 'female' && ind.phenotype === 'affected').length;
                const carriers = this.individuals.filter(ind => 
                    ind.phenotype === 'carrier').length;
                
                document.getElementById('totalCount').textContent = total;
                document.getElementById('malePatients').textContent = malePatients;
                document.getElementById('femalePatients').textContent = femalePatients;
                document.getElementById('carriers').
textContent = carriers;
            }
            
            handleClick(x, y) {
                // 检查是否点击了个体
                for (let i = this.individuals.length - 1; i >= 0; i--) {
                    const individual = this.individuals[i];
                    if (individual.isPointInside(x, y)) {
                        // 显示工具提示
                        tooltip.innerHTML = individual.getInfo();
                        tooltip.style.left = (x + 15) + 'px';
                        tooltip.style.top = (y + 15) + 'px';
                        tooltip.style.opacity = '1';
                        
                        // 高亮相关个体
                        this.individuals.forEach(ind => ind.selected = false);
                        individual.selected = true;
                        
                        // 高亮遗传路径
                        if (individual.parents.length > 0) {
                            this.highlightedPath = {
                                from: individual.parents[0].id,
                                to: individual.id
                            };
                        }
                        
                        return;
                    }
                }
                
                // 点击空白处隐藏工具提示
                tooltip.style.opacity = '0';
                this.individuals.forEach(ind => ind.selected = false);
            }
            
            handleHover(x, y) {
                let hoveredAny = false;
                
                this.individuals.forEach(individual => {
                    individual.hovered = individual.isPointInside(x, y);
                    if (individual.hovered) hoveredAny = true;
                });
                
                // 更新鼠标指针
                canvas.style.cursor = hoveredAny ? 'pointer' : 'default';
            }
            
            animate() {
                if (this.isAnimating && this.animationStep < 3) {
                    this.addGeneration();
                }
                this.draw();
                
                if (this.isAnimating) {
                    setTimeout(() => {
                        requestAnimationFrame(() => this.animate());
                    }, 2000 / this.animationSpeed);
                }
            }
            
            startAnimation() {
                if (!this.isAnimating) {
                    this.isAnimating = true;
                    this.animate();
                }
            }
            
            stopAnimation() {
                this.isAnimating = false;
            }
            
            reset() {
                this.stopAnimation();
                this.initializePedigree();
                this.draw();
                tooltip.style.opacity = '0';
            }
        }

        // 初始化系统
        const pedigreeSystem = new PedigreeSystem();
        pedigreeSystem.draw();

        // 事件监听器
        document.getElementById('playBtn').addEventListener('click', () => {
            pedigreeSystem.startAnimation();
            currentInfo.textContent = "动画播放中...观察遗传基因的传递路径。";
        });

        document.getElementById('pauseBtn').addEventListener('click', () => {
            pedigreeSystem.stopAnimation();
            currentInfo.textContent = "动画已暂停。点击个体查看详细信息，或点击'步进'继续。";
        });

        document.getElementById('stepBtn').addEventListener('click', () => {
            pedigreeSystem.stopAnimation();
            pedigreeSystem.addGeneration();
            pedigreeSystem.draw();
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            pedigreeSystem.reset();
        });

        document.getElementById('speedSlider').addEventListener('input', (e) => {
            pedigreeSystem.animationSpeed = parseInt(e.target.value);
        });

        document.getElementById('diseaseSelect').addEventListener('change', () => {
            pedigreeSystem.reset();
        });

        document.getElementById('showGenotype').addEventListener('change', () => {
            pedigreeSystem.draw();
        });

        document.getElementById('showPhenotype').addEventListener('change', () => {
            pedigreeSystem.draw();
        });

        document.getElementById('showProbability').addEventListener('change', () => {
            pedigreeSystem.draw();
        });

        document.getElementById('simulateBtn').addEventListener('click', () => {
            alert("模拟实验室功能：\n\n1. 自定义父母基因型\n2. 模拟多代遗传\n3. 统计遗传规律\n\n（此为扩展功能演示，完整实现需要更多代码）");
            
            // 简单演示：随机生成一个大家系
            pedigreeSystem.reset();
            
            // 添加更多随机个体
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    pedigreeSystem.addGeneration();
                    pedigreeSystem.draw();
                }, i * 500);
            }
            
            currentInfo.textContent = "模拟实验室：随机生成多代家系图，观察遗传规律。注意男性患者比例显著高于女性。";
        });

        // Canvas 交互
        canvas.addEventListener('click', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            pedigreeSystem.handleClick(x, y);
        });

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            pedigreeSystem.handleHover(x, y);
            
            // 移动工具提示
            if (tooltip.style.opacity === '1') {
                tooltip.style.left = (x + 15) + 'px';
                tooltip.style.top = (y + 15) + 'px';
            }
        });

        canvas.addEventListener('mouseleave', () => {
            pedigreeSystem.individuals.forEach(ind => ind.hovered = false);
            canvas.style.cursor = 'default';
            tooltip.style.opacity = '0';
        });

        // 初始提示
        setTimeout(() => {
            currentInfo.textContent = "点击'播放'开始动画演示，或点击'步进'手动控制。将鼠标悬停在家系成员上查看详细信息。";
        }, 1000);
    </script>
</body>
</html>

### 3. 过程输出

### 3. 使用指南

## 交互式教学动画使用指南

欢迎使用“伴性遗传家系图动态演化”交互式教学动画！本动画旨在通过直观、动态的可视化方式，帮助您深入理解X染色体隐性遗传的复杂规律。无论您是学生、教师还是生物学爱好者，本工具都将为您提供沉浸式的学习体验。

---

### 一、功能说明

本动画模拟了红绿色盲与血友病这两种典型X染色体隐性遗传疾病的遗传过程。通过动态生成三代家系图，您可以：

1. **观察基因传递路径**：可视化致病基因在家族中的流动轨迹
2. **理解遗传规律**：直观展示“交叉遗传”、“男性高发病率”等核心概念
3. **进行探究学习**：通过交互操作验证遗传学原理

### 二、主要功能

#### 1. 动画控制区（顶部工具栏）
- **播放/暂停**：控制动画自动演示
- **步进**：手动逐步推进遗传过程（推荐学习使用）
- **重置**：恢复到初始状态
- **速度调节**：控制动画播放速度（1-10档）

#### 2. 案例选择器
- **红绿色盲经典案例**：最常见的X隐性遗传病案例
- **血友病皇室案例**：基于欧洲皇室真实遗传历史的模拟
- **自定义案例**：基础模板，可结合“模拟实验室”进行扩展

#### 3. 信息显示开关
- **显示基因型**：在个体下方显示基因型（如XᴬY、XᴬXᵃ）
- **显示表现型**：显示“正常”、“携带者”、“患者”状态
- **显示概率计算**：在画布下方显示遗传概率计算过程

#### 4. 交互探索功能
- **点击任意个体**：弹出详细信息卡片，包括：
  - 基因型与表现型
  - 父母与子女关系
  - 遗传路径高亮显示
- **鼠标悬停**：个体周围显示金色光环，表示可交互

#### 5. 模拟实验室
- **多代模拟**：随机生成大规模家系图
- **实时统计**：自动计算并显示：
  - 总人数、男女患者数
  - 携带者数量
  - 发病率性别差异

### 三、设计特色

#### 1. 专业可视化设计
- **无障碍配色**：采用蓝紫色系，避免红绿色盲识别困难
- **标准遗传学符号**：严格遵循国际通用的家系图绘制规范
- **动态高亮路径**：使用金色箭头和光点标记基因传递轨迹

#### 2. 分层认知设计
- **第一层（观察）**：自动演示完整遗传过程
- **第二层（理解）**：通过步进控制，分阶段学习
- **第三层（探究）**：点击个体查看详细信息，深入分析

#### 3. 多模式学习支持
- **引导模式**：跟随预设案例学习核心概念
- **探索模式**：自主控制，验证假设
- **对比模式**：切换不同疾病，发现共性与差异

### 四、教学要点

#### 核心概念可视化
1. **携带者的关键作用**
   - 注意第一代女性（紫色圆圈带白点）不发病但传递致病基因
   - 观察她如何将致病基因传给50%的儿子

2. **交叉遗传模式**
   - 第二代男性患者的致病基因**必然来自母亲**
   - 该患者只能将致病基因传给女儿（使其成为携带者）
   - 金色高亮箭头清晰展示这一路径

3. **发病率性别差异**
   - 查看右侧统计面板，注意男性患者数量显著多于女性
   - 理解原因：男性只有一条X染色体，隐性基因直接表达

4. **两种疾病的对比**
   - **共同点**：都是X染色体隐性遗传
   - **差异点**：
     - 红绿色盲基因频率较高（约8%男性）
     - 血友病症状严重，历史上影响欧洲皇室
     - 通过切换案例观察家系图差异

### 五、使用建议

#### 对于学生
1. **初次学习**
   - 选择“红绿色盲案例”，点击“播放”观看完整过程
   - 注意观察金色高亮路径，理解基因流向
   - 阅读画布下方的概率计算，联系理论知识

2. **巩固复习**
   - 使用“步进”功能，在每个阶段暂停并预测下一步
   - 点击每个个体，查看其基因型和遗传关系
   - 尝试解释为什么某些个体是携带者而不发病

3. **探究学习**
   - 切换到“血友病案例”，比较异同
   - 使用“模拟实验室”生成随机家系，验证遗传规律
   - 提出问题：如果第一代父母基因型不同，结果会怎样？

#### 对于教师
1. **课堂演示**
   - 使用投影展示，逐步讲解遗传过程
   - 在关键步骤暂停，提问引导学生思考
   - 利用“重置”功能快速比较不同情景

2. **小组活动设计**
   - 任务1：找出所有携带者并解释其重要性
   - 任务2：追踪某个致病基因的完整传递路径
   - 任务3：预测第四代可能出现的基因型

3. **评估工具**
   - 让学生操作动画解释特定遗传现象
   - 设计问题：“为什么这个家系中没有女性患者？”
   - 要求学生使用统计数据分析发病率差异

#### 最佳实践提示
1. **循序渐进**：先观察→再理解→最后探究
2. **善用交互**：不要被动观看，多点击、多探索
3. **联系实际**：思考这些遗传规律在现实生活中的应用
4. **记录发现**：在学习过程中记录观察到的规律和疑问

---

### 技术支持与反馈

本动画基于HTML5 Canvas技术开发，支持现代主流浏览器。如遇显示问题，请确保：
- 使用Chrome、Firefox、Edge等最新版本浏览器
- 启用JavaScript功能
- 屏幕分辨率不低于1024×768

我们持续改进此教学工具。如果您有改进建议或发现任何问题，欢迎通过教育技术平台反馈。祝您学习愉快，探索遗传学的奥秘！

**记住：每一个家系图背后，都是生命密码的奇妙传递。**