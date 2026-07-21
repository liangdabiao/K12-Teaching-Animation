# 需求：冒泡排序（相邻比较+交换，像气泡上升）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为编程初学者或数据结构与算法的入门者。他们可能对抽象的排序算法感到困惑，需要直观、动态的视觉辅助来理解其工作原理。
2.  **核心需求**：
    *   **理解过程**：用户需要清晰地看到冒泡排序“相邻比较”和“交换”这两个核心操作的每一步，理解“气泡”（较大/较小值）如何一步步“上升”到正确位置。
    *   **掌握规律**：用户需要观察到每一轮排序后，序列中“已排序区”（有序部分）和“未排序区”的动态变化，理解算法如何逐步缩小问题规模。
    *   **控制与探索**：用户需要能够控制动画的速度，暂停以观察细节，并能手动输入不同的初始数据序列，以验证对算法的理解。
    *   **降低认知负荷**：将抽象的代码逻辑（如嵌套循环、索引操作）转化为直观的、有明确状态的视觉元素和动画。

#### 教学设计思路
1.  **核心概念分解**：
    *   **相邻比较**：将算法中的 `if (arr[j] > arr[j+1])` 可视化。
    *   **交换**：将数据交换的过程可视化，强调这是算法改变序列顺序的唯一方式。
    *   **气泡上升**：通过高亮和移动动画，体现较大值（以升序排序为例）像气泡一样向右/向上移动的过程。
    *   **轮次与边界**：明确区分每一轮（`i`循环）和每一轮内的逐个比较（`j`循环），并动态显示当前未排序区的边界。
2.  **遵循认知规律**：
    *   **从具体到抽象**：先展示完整的、生动的排序动画，再逐步关联到伪代码或关键代码行。
    *   **引导注意力**：使用颜色、高亮和慢速动画引导用户关注当前正在进行的比较和交换操作。
    *   **提供即时反馈**：在用户交互（如点击“下一步”）时，界面元素（如数字、箭头、说明文字）同步更新，强化操作与结果的联系。
3.  **交互设计**：
    *   **分步控制**：提供“播放/暂停”、“下一步”、“上一步”、“重置”按钮，让用户能按自己的节奏学习。
    *   **参数调节**：允许用户调整动画速度，并输入自定义的数字序列。
    *   **多视图关联**：将“动画视图”（柱状图或带数字的圆圈）与“伪代码视图”或“状态说明视图”并列，并用高亮同步两者，帮助用户在直观操作和抽象逻辑之间建立联系。
4.  **视觉呈现**：
    *   **主视图**：使用**垂直柱状图**来代表数据。柱子的高度对应数值大小，直观易懂。
    *   **状态色码**：
        *   **默认色**：未参与当前操作的柱子。
        *   **比较色**：高亮当前正在比较的两个相邻柱子。
        *   **交换色**：当需要交换时，高亮这两个柱子，并用平滑的动画交换它们的位置。
        *   **已排序色**：每一轮结束后，固定在正确位置上的柱子（即本轮“冒”到顶端的元素）标记为已排序状态，颜色区别于未排序部分。
    *   **辅助视觉元素**：
        *   在正在比较的两个柱子之间显示一个比较符号（如 `> ?` 或 `< ?`）。
        *   在交换时，可以显示交换箭头或轨迹。
        *   用一个明显的标记或分隔线来指示当前未排序区的边界。

#### 配色方案选择
选择对比清晰、符合教育场景且对色盲友好的配色方案：
*   **背景**：浅灰色（`#f5f5f5`）或白色，保持干净，减少干扰。
*   **数据柱默认色**：中性蓝色（`#4A90E2`），平和且专业。
*   **比较状态色**：温和的黄色（`#FFD700`），表示“注意，正在检查”。
*   **交换状态色**：橙色（`#FF7F50`），表示“正在发生改变”。
*   **已排序状态色**：绿色（`#2E8B57`），表示“已完成，位置正确”。
*   **文本与边框**：深灰色（`#333333`），确保可读性。
*   **高亮/强调色**：红色（`#DC143C`），用于关键提示或错误状态。

#### 交互功能列表
1.  **动画控制区**：
    *   `播放 / 暂停` 按钮：开始或暂停连续动画。
    *   `下一步` 按钮：手动单步执行一次比较或交换操作。
    *   `上一步` 按钮：回退到上一个操作步骤（可选，用于深入分析）。
    *   `重置` 按钮：恢复初始无序状态。
2.  **参数控制区**：
    *   `速度调节滑块`：控制动画播放的快慢。
    *   `数据输入框`：允许用户输入一组以逗号分隔的数字（如 `5, 3, 8, 1, 2`）。
    *   `随机生成` 按钮：随机生成一组新数据。
3.  **信息展示区**：
    *   `算法状态说明`：用文字描述当前步骤（例如：“正在比较第3和第4个元素...”、“交换 8 和 1”、“第2轮结束，最大值8已就位”）。
    *   `伪代码高亮面板`：显示冒泡排序的伪代码或简化代码，并高亮当前执行到的行。
    *   `统计信息`：显示当前已进行的比较次数、交换次数和已完成的轮次。
4.  **可视化主区**：
    *   动态柱状图，根据算法状态应用上述配色方案。
    *   清晰标注当前比较对、交换动画和已排序区域。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>冒泡排序算法可视化</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #4A90E2;
        }
        
        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #7f8c8d;
            font-size: 1.1rem;
        }
        
        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .visualization-section {
            flex: 1;
            min-width: 300px;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        }
        
        .controls-section {
            flex: 1;
            min-width: 300px;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        }
        
        .section-title {
            color: #4A90E2;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        
        #canvas-container {
            width: 100%;
            height: 300px;
            position: relative;
            margin-bottom: 20px;
        }
        
        canvas {
            display: block;
            background-color: white;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        
        .status-display {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #4A90E2;
            margin-bottom: 20px;
        }
        
        .status-text {
            font-size: 1.1rem;
            font-weight: 500;
        }
        
        .stats {
            display: flex;
            justify-content: space-around;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: bold;
            color: #2E8B57;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #7f8c8d;
        }
        
        .controls {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }
        
        button {
            padding: 12px 15px;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1rem;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        #play-btn {
            background-color: #2E8B57;
            color: white;
        }
        
        #pause-btn {
            background-color: #FFD700;
            color: #333;
        }
        
        #next-btn {
            background-color: #4A90E2;
            color: white;
        }
        
        #reset-btn {
            background-color: #7f8c8d;
            color: white;
        }
        
        .speed-control {
            margin-bottom: 25px;
        }
        
        .speed-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }
        
        input[type="range"] {
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: #ddd;
            outline: none;
        }
        
        .data-control {
            margin-bottom: 25px;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        input[type="text"] {
            flex: 1;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
        }
        
        #random-btn {
            background-color: #FF7F50;
            color: white;
        }
        
        #apply-btn {
            background-color: #4A90E2;
            color: white;
        }
        
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eee;
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
        
        .code-section {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            margin-top: 20px;
        }
        
        .code-container {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Consolas', 'Monaco', monospace;
            overflow-x: auto;
            line-height: 1.5;
            margin-top: 15px;
        }
        
        .code-line {
            padding: 2px 0;
        }
        
        .code-line.highlighted {
            background-color: #34495e;
            border-left: 4px solid #FFD700;
            padding-left: 10px;
        }
        
        .explanation {
            margin-top: 30px;
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        }
        
        .explanation h3 {
            color: #4A90E2;
            margin-bottom: 15px;
        }
        
        .explanation ul {
            padding-left: 20px;
            margin-bottom: 15px;
        }
        
        .explanation li {
            margin-bottom: 8px;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #7f8c8d;
            font-size: 0.9rem;
        }
        
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            
            .controls {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>冒泡排序算法可视化</h1>
        <p class="subtitle">相邻比较 + 交换，像气泡一样上升</p>
    </header>
    
    <div class="container">
        <section class="visualization-section">
            <h2 class="section-title">排序过程可视化</h2>
            
            <div id="canvas-container">
                <canvas id="sorting-canvas" width="800" height="300"></canvas>
            </div>
            
            <div class="status-display">
                <p class="status-text" id="status-text">点击"播放"开始排序动画</p>
            </div>
            
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-value" id="comparison-count">0</div>
                    <div class="stat-label">比较次数</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="swap-count">0</div>
                    <div class="stat-label">交换次数</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value" id="pass-count">0</div>
                    <div class="stat-label">已完成轮次</div>
                </div>
            </div>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #4A90E2;"></div>
                    <span>默认（未排序）</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #FFD700;"></div>
                    <span>正在比较</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #FF7F50;"></div>
                    <span>正在交换</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #2E8B57;"></div>
                    <span>已排序</span>
                </div>
            </div>
        </section>
        
        <section class="controls-section">
            <h2 class="section-title">控制面板</h2>
            
            <div class="controls">
                <button id="play-btn">▶ 播放</button>
                <button id="pause-btn">⏸ 暂停</button>
                <button id="next-btn">⏭ 下一步</button>
                <button id="reset-btn">↺ 重置</button>
            </div>
            
            <div class="speed-control">
                <div class="speed-label">
                    <span>动画速度</span>
                    <span id="speed-value">中速</span>
                </div>
                <input type="range" id="speed-slider" min="1" max="10" value="5">
            </div>
            
            <div class="data-control">
                <h3 class="section-title">数据设置</h3>
                <div class="input-group">
                    <input type="text" id="data-input" value="5, 3, 8, 1, 6, 9, 2, 7, 4">
                    <button id="apply-btn">应用</button>
                </div>
                <button id="random-btn">🎲 随机生成数据</button>
            </div>
        </section>
    </div>
    
    <section class="code-section">
        <h2 class="section-title">算法伪代码</h2>
        <div class="code-container">
            <div class="code-line">function bubbleSort(arr) {</div>
            <div class="code-line" id="line1">  let n = arr.length;</div>
            <div class="code-line" id="line2">  for (let i = 0; i < n-1; i++) {</div>
            <div class="code-line" id="line3">    for (let j = 0; j < n-i-1; j++) {</div>
            <div class="code-line" id="line4">      // 比较相邻元素</div>
            <div class="code-line" id="line5">      if (arr[j] > arr[j+1]) {</div>
            <div class="code-line" id="line6">        // 交换元素</div>
            <div class="code-line" id="line7">        swap(arr[j], arr[j+1]);</div>
            <div class="code-line" id="line8">      }</div>
            <div class="code-line" id="line9">    }</div>
            <div class="code-line" id="line10">    // 第i轮结束，arr[n-i-1]已就位</div>
            <div class="code-line" id="line11">  }</div>
            <div class="code-line" id="line12">}</div>
        </div>
    </section>
    
    <section class="explanation">
        <h3>冒泡排序算法说明</h3>
        <ul>
            <li><strong>核心思想</strong>：重复遍历要排序的数列，一次比较两个相邻元素，如果它们的顺序错误就把它们交换过来。</li>
            <li><strong>算法步骤</strong>：
                <ol>
                    <li>从第一个元素开始，比较相邻的两个元素。</li>
                    <li>如果第一个比第二个大（升序排序），就交换它们。</li>
                    <li>对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。这样一轮结束后，最大的元素会"冒泡"到数列的末端。</li>
                    <li>针对所有的元素重复以上的步骤，除了已经排序好的元素。</li>
                    <li>重复步骤1~4，直到排序完成。</li>
                </ol>
            </li>
            <li><strong>时间复杂度</strong>：平均和最坏情况都是O(n²)，最好情况（已排序）是O(n)。</li>
            <li><strong>空间复杂度</strong>：O(1)，是原地排序算法。</li>
            <li><strong>稳定性</strong>：稳定排序算法，相等元素的相对位置不会改变。</li>
        </ul>
        <p><strong>观察提示</strong>：注意观察每一轮结束后，最大的元素如何像"气泡"一样上升到正确位置，以及已排序区域如何逐渐扩大。</p>
    </section>
    
    <footer>
        <p>冒泡排序算法可视化 | 设计用于教学演示 | 使用HTML5 Canvas实现</p>
    </footer>

    <script>
        // 全局变量
        let data = [5, 3, 8, 1, 6, 9, 2, 7, 4];
        let originalData = [...data];
        let canvas, ctx;
        let animationId = null;
        let isPlaying = false;
        let speed = 5; // 1-10，值越大速度越快
        let currentStep = 0;
        let totalSteps = 0;
        
        // 算法状态变量
        let i = 0; // 外层循环索引
        let j = 0; // 内层循环索引
        let n = data.length;
        let comparisons = 0;
        let swaps = 0;
        let passes = 0;
        let isComparing = false;
        let isSwapping = false;
        let swapIndex = -1;
        let sortedIndices = new Set();
        
        // 颜色定义
        const colors = {
            default: '#4A90E2',
            comparing: '#FFD700',
            swapping: '#FF7F50',
            sorted: '#2E8B57',
            text: '#333333',
            background: '#f5f5f5',
            canvasBg: '#FFFFFF'
        };
        
        // 初始化Canvas
        function initCanvas() {
            canvas = document.getElementById('sorting-canvas');
            ctx = canvas.getContext('2d');
            
            // 设置Canvas尺寸为容器尺寸
            const container = document.getElementById('canvas-container');
            canvas.width = container.clientWidth;
            canvas.height = container.clientHeight;
            
            drawBars();
        }
        
        // 绘制柱状图
        function drawBars() {
            const width = canvas.width;
            const height = canvas.height;
            const barCount = data.length;
            const barWidth = Math.min(50, (width - 20) / barCount);
            const maxValue = Math.max(...data);
            const spacing = 5;
            
            // 清空画布
            ctx.clearRect(0, 0, width, height);
            
            // 绘制背景
            ctx.fillStyle = colors.canvasBg;
            ctx.fillRect(0, 0, width, height);
            
            // 绘制每个柱子
            for (let idx = 0; idx < barCount; idx++) {
                const barHeight = (data[idx] / maxValue) * (height - 80);
                const x = (width - (barCount * (barWidth + spacing))) / 2 + idx * (barWidth + spacing);
                const y = height - 60 - barHeight;
                
                // 选择颜色
                let color = colors.default;
                
                if (sortedIndices.has(idx)) {
                    color = colors.sorted;
                } else if (isSwapping && (idx === j || idx === j + 1)) {
                    color = colors.swapping;
                } else if (isComparing && (idx === j || idx === j + 1)) {
                    color = colors.comparing;
                }
                
                // 绘制柱子
                ctx.fillStyle = color;
                ctx.fillRect(x, y, barWidth, barHeight);
                
                // 绘制柱子边框
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 1;
                ctx.strokeRect(x, y, barWidth, barHeight);
                
                // 绘制数值
                ctx.fillStyle = colors.text;
                ctx.font = 'bold 16px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(data[idx], x + barWidth / 2, y - 10);
                
                // 绘制索引
                ctx.fillStyle = '#7f8c8d';
                ctx.font = '14px Arial';
                ctx.fillText(`[${idx}]`, x + barWidth / 2, height - 30);
                
                // 如果是正在比较的元素，绘制比较符号
                if (isComparing && (idx === j || idx === j + 1)) {
                    ctx.fillStyle = '#DC143C';
                    ctx.font = 'bold 20px Arial';
                    
                    if (idx === j) {
                        ctx.fillText("←", x + barWidth / 2, y - 40);
                    } else {
                        ctx.fillText("→", x + barWidth / 2, y - 40);
                    }
                    
                    // 在两者之间绘制比较符号
                    if (idx === j) {
                        const midX = x + barWidth + spacing / 2;
                        ctx.fillText(data[j] > data[j+1] ? ">" : "≤", midX, height - 80);
                    }
                }
            }
            
            // 绘制已排序区域指示线
            if (sortedIndices.size > 0) {
                const sortedCount = sortedIndices.size;
                const xPos = (width - (barCount * (barWidth + spacing))) / 2 + 
                            (barCount - sortedCount) * (barWidth + spacing) - spacing/2;
                
                ctx.strokeStyle = '#2E8B57';
                ctx.lineWidth = 3;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(xPos, 20);
                ctx.lineTo(xPos, height - 40);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // 添加标签
                ctx.fillStyle = '#2E8B57';
                ctx.font = 'bold 14px Arial';
                ctx.fillText("已排序区", xPos + 10, 30);
            }
            
            // 更新状态文本
            updateStatusText();
        }
        
        // 更新状态文本
        function updateStatusText() {
            let statusText = "";
            
            if (isComparing) {
                statusText = `正在比较第 ${j} 个元素(${data[j]}) 和第 ${j+1} 个元素(${data[j+1]})`;
                if (data[j] > data[j+1]) {
                    statusText += ` → ${data[j]} > ${data[j+1]}，需要交换`;
                } else {
                    statusText += ` → ${data[j]} ≤ ${data[j+1]}，无需交换`;
                }
            } else if (isSwapping) {
                statusText = `正在交换第 ${j} 个元素(${data[j+1]}) 和第 ${j+1} 个元素(${data[j]})`;
            } else if (passes === n - 1) {
                statusText = `排序完成！总共进行了 ${comparisons} 次比较和 ${swaps} 次交换`;
            } else if (j === n - i - 1) {
                statusText = `第 ${passes} 轮结束，元素 ${data[n - passes - 1]} 已就位`;
            } else if (!isPlaying && currentStep === 0) {
                statusText = "点击'播放'开始排序动画";
            } else {
                statusText = `第 ${passes} 轮，第 ${j+1}/${n-passes-1} 次比较`;
            }
            
            document.getElementById('status-text').textContent = statusText;
            
            // 更新统计信息
            document.getElementById('comparison-count').textContent = comparisons;
            document.getElementById('swap-count').textContent = swaps;
            document.getElementById('pass-count').textContent = passes;
            
            // 更新代码高亮
            updateCodeHighlight();
        }
        
        // 更新代码高亮
        function updateCodeHighlight() {
            // 清除所有高亮
            for (let lineNum = 1; lineNum <= 12; lineNum++) {
                document.getElementById(`line${lineNum}`).classList.remove('highlighted');
            }
            
            // 根据当前状态高亮对应代码行
            if (passes === n - 1) {
                // 排序完成，高亮最后一行
                document.getElementById('line12').classList.add('highlighted');
            } else if (j === n - i - 1) {
                // 一轮结束
                document.getElementById('line10').classList.add('highlighted');
            } else if (isSwapping) {
                // 正在交换
                document.getElementById('line7').classList.add('highlighted');
            } else if (isComparing) {
                // 正在比较
                if (data[j] > data[j+1]) {
                    document.getElementById('line5').classList.add('highlighted');
                } else {
                    document.getElementById('line8').classList.add('highlighted');
                }
            } else if (j < n - i - 1) {
                // 内层循环
                document.getElementById('line3').classList.add('highlighted');
            } else {
                // 外层循环
                document.getElementById('line2').classList.add('highlighted');
            }
        }
        
        // 执行一步排序
        function step() {
            if (passes >= n - 1) {
                // 排序已完成
                isPlaying = false;
                document.getElementById('play-btn').textContent = "▶ 播放";
                return;
            }
            
            currentStep++;
            
            if (j < n - i - 1) {
                // 执行比较
                isComparing = true;
                isSwapping = false;
                comparisons++;
                
                drawBars();
                
                // 延迟后决定是否交换
                setTimeout(() => {
                    if (data[j] > data[j + 1]) {
                        // 需要交换
                        isComparing = false;
                        isSwapping = true;
                        swapIndex = j;
                        
                        // 执行交换
                        [data[j], data[j + 1]] = [data[j + 1], data[j]];
                        swaps++;
                        
                        drawBars();
                        
                        // 交换完成后，准备下一次比较
                        setTimeout(() => {
                            isSwapping = false;
                            j++;
                            if (isPlaying) {
                                setTimeout(step, 1000 / speed);
                            }
                        }, 800 / speed);
                    } else {
                        // 不需要交换，直接进行下一次比较
                        isComparing = false;
                        j++;
                        if (isPlaying) {
                            setTimeout(step, 800 / speed);
                        }
                    }
                }, 800 / speed);
            } else {
                // 一轮结束
                sortedIndices.add(n - passes - 1);
                passes++;
                i++;
                j = 0;
                
                if (isPlaying) {
                    setTimeout(step, 1000 / speed);
                }
            }
            
            drawBars();
        }
        
        // 开始/暂停动画
        function togglePlay() {
            if (passes >= n - 1) {
                reset();
                return;
            }
            
            if (isPlaying) {
                // 暂停
                isPlaying = false;
                document.getElementById('play-btn').textContent = "▶ 播放";
            } else {
                // 开始
                isPlaying = true;
                document.getElementById('play-btn').textContent = "⏸ 暂停";
                step();
            }
        }
        
        // 下一步
        function nextStep() {
            if (passes >= n - 1) return;
            
            if (isPlaying) {
                isPlaying = false;
                document.getElementById('play-btn').textContent = "▶ 播放";
            }
            
            step();
        }
        
        // 重置
        function reset() {
            // 停止动画
            if (animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
            
            // 重置状态
            data = [...originalData];
            i = 0;
            j = 0;
            n = data.length;
            comparisons = 0;
            swaps = 0;
            passes = 0;
            isComparing = false;
            isSwapping = false;
            swapIndex = -1;
            sortedIndices.clear();
            isPlaying = false;
            currentStep = 0;
            
            // 更新按钮状态
            document.getElementById('play-btn').textContent = "▶ 播放";
            
            // 重新绘制
            drawBars();
        }
        
        // 应用新数据
        function applyData() {
            const input = document.getElementById('data-input').value;
            const newData = input.split(',').map(num => parseInt(num.trim())).filter(num => !isNaN(num));
            
            if (newData.length < 2) {
                alert("请输入至少2个有效的数字，用逗号分隔");
                return;
            }
            
            if (newData.length > 15) {
                alert("为了可视化效果，请不要超过15个数字");
                return;
            }
            
            originalData = [...newData];
            reset();
        }
        
        // 生成随机数据
        function generateRandomData() {
            const count = Math.floor(Math.random() * 8) + 5; // 5-12个数字
            const newData = [];
            
            for (let i = 0; i < count; i++) {
                newData.push(Math.floor(Math.random() * 20) + 1);
            }
            
            document.getElementById('data-input').value = newData.join(', ');
            originalData = [...newData];
            reset();
        }
        
        // 更新速度
        function updateSpeed() {
            const slider = document.getElementById('speed-slider');
            speed = parseInt(slider.value);
            
            const speedValue = document.getElementById('speed-value');
            if (speed <= 3) {
                speedValue.textContent = "慢速";
            } else if (speed <= 7) {
                speedValue.textContent = "中速";
            } else {
                speedValue.textContent = "快速";
            }
        }
        
        // 窗口大小改变时调整Canvas
        window.addEventListener('resize', () => {
            initCanvas();
        });
        
        // 初始化
        document.addEventListener('DOMContentLoaded', () => {
            initCanvas();
            
            // 事件监听
            document.getElementById('play-btn').addEventListener('click', togglePlay);
            document.getElementById('pause-btn').addEventListener('click', () => {
                if (isPlaying) {
                    isPlaying = false;
                    document.getElementById('play-btn').textContent = "▶ 播放";
                }
            });
            document.getElementById('next-btn').addEventListener('click', nextStep);
            document.getElementById('reset-btn').addEventListener('click', reset);
            document.getElementById('apply-btn').addEventListener('click', applyData);
            document.getElementById('random-btn').addEventListener('click', generateRandomData);
            document.getElementById('speed-slider').addEventListener('input', updateSpeed);
            
            // 初始化速度显示
            updateSpeed();
        });
    </script>
</body>
</html>
```

### 3. 过程输出

### 3. 使用指南

## 冒泡排序交互式教学动画使用指南

欢迎使用这款精心设计的冒泡排序算法可视化工具！本指南将帮助您充分利用这个交互式动画，深入理解冒泡排序的核心原理和运作机制。

---

### 一、功能说明

本动画将抽象的冒泡排序算法转化为直观的视觉体验，通过**动态柱状图**、**实时状态反馈**和**交互式控制**，让您能够：
- **观察**算法的每一步执行过程
- **理解**相邻比较和元素交换的核心操作
- **掌握**算法的时间复杂度和空间特性
- **探索**不同数据集的排序表现

### 二、主要功能区域

#### 1. 可视化主区（左侧）
- **动态柱状图**：每个柱子的高度代表数值大小，颜色表示当前状态
- **实时状态显示**：用文字描述当前正在进行的操作
- **统计面板**：实时显示比较次数、交换次数和已完成轮次
- **图例说明**：解释四种颜色状态的含义

#### 2. 控制面板（右侧）
- **动画控制**：
  - **播放/暂停**：开始或暂停连续动画
  - **下一步**：手动执行单步操作（推荐初学者使用）
  - **重置**：恢复初始状态
- **速度调节**：通过滑块控制动画播放速度（慢速-中速-快速）
- **数据管理**：
  - 输入自定义数据（用逗号分隔，如：`9,2,5,1,8`）
  - 应用新数据
  - 随机生成数据（5-12个随机数）

#### 3. 算法伪代码区
- 显示冒泡排序的标准伪代码
- **实时高亮**：当前执行的代码行会突出显示
- 帮助您在直观操作和抽象逻辑之间建立联系

#### 4. 算法说明区
- 详细解释冒泡排序的核心思想、步骤和特性
- 提供时间复杂度、空间复杂度和稳定性分析
- 包含观察提示，指导您关注关键现象

### 三、设计特色

#### 1. 多感官学习体验
- **视觉编码**：四种颜色清晰区分不同状态
  - 蓝色：默认/未排序
  - 黄色：正在比较
  - 橙色：正在交换
  - 绿色：已排序
- **动态反馈**：箭头、比较符号、分隔线等辅助视觉元素
- **同步显示**：可视化、状态文字和伪代码三者同步更新

#### 2. 渐进式学习支持
- **分步控制**：支持连续播放和单步执行
- **速度调节**：可根据理解程度调整节奏
- **可逆操作**：重置功能允许反复练习

#### 3. 认知负荷优化
- 关键信息突出显示
- 复杂操作分解为简单步骤
- 抽象概念与具体示例相结合

### 四、教学要点与观察指导

#### 核心概念观察点：

1. **"气泡上升"现象**
   - 注意观察每一轮结束后，**最大的元素如何"冒"到最右侧**
   - 已排序区域（绿色柱子）如何从右向左逐渐扩大

2. **相邻比较与交换**
   - 关注**黄色高亮**的两个相邻柱子
   - 观察比较符号（> 或 ≤）如何决定是否需要交换
   - 注意**橙色高亮**的交换过程，理解元素位置的改变

3. **算法效率体现**
   - 观察统计面板：比较次数和交换次数的增长
   - 注意已排序的元素不再参与后续比较
   - 思考：为什么冒泡排序在最好情况下也需要O(n²)次比较？

#### 推荐学习路径：

1. **初次接触**：
   - 使用默认数据，点击"播放"观看完整排序过程
   - 注意观察颜色变化和元素移动规律

2. **深入理解**：
   - 切换到"慢速"，使用"下一步"按钮单步执行
   - 同时观察柱状图变化、状态文字和伪代码高亮
   - 回答：为什么这一轮需要交换？为什么这一轮不需要交换？

3. **探索验证**：
   - 输入已排序的数据（如：`1,2,3,4,5`）
   - 观察算法在最好情况下的表现
   - 输入逆序数据（如：`9,8,7,6,5`）
   - 观察算法在最坏情况下的表现

4. **巩固应用**：
   - 随机生成数据，尝试预测排序过程
   - 记录比较次数和交换次数，验证算法复杂度

### 五、使用建议

#### 给学习者的建议：
1. **先观后析**：先完整观看几遍动画，建立整体印象，再深入分析细节
2. **手眼脑并用**：一边操作，一边观察，一边思考
3. **主动提问**：在观察过程中，主动问自己"为什么"：
   - 为什么这个元素要交换？
   - 为什么这一轮比较次数减少了？
   - 如果数据不同，算法表现会有什么变化？
4. **联系实际**：将可视化过程与代码实现联系起来，理解每个视觉变化对应的代码操作

#### 给教师/教学者的建议：
1. **课堂演示**：
   - 使用大屏幕展示，引导学生集体观察
   - 在关键步骤暂停，提问引导学生思考
   - 对比不同数据集的排序过程，讨论算法特性

2. **练习设计**：
   - 让学生预测特定数据集的排序过程
   - 设计数据让学生发现算法的边界情况
   - 引导学生从可视化理解过渡到代码实现

3. **评估工具**：
   - 观察学生能否正确解释每个步骤
   - 检查学生能否将视觉过程转化为算法描述
   - 评估学生对算法时间复杂度的直观理解

#### 技术提示：
1. 推荐使用Chrome、Firefox或Edge等现代浏览器
2. 屏幕分辨率建议在1366×768以上，以获得最佳视觉效果
3. 如果动画卡顿，可适当降低速度或减少数据量

---

### 开始您的探索之旅吧！

现在，您已经掌握了这个教学工具的所有功能。建议您：

1. 点击"播放"按钮，感受冒泡排序的完整过程
2. 尝试"下一步"单步执行，仔细观察每个细节
3. 输入自己的数据，验证您的理解
4. 对照伪代码，思考每个视觉变化对应的程序逻辑

记住：**理解算法最好的方式不是记忆，而是观察和思考**。这个工具为您提供了观察的"显微镜"和思考的"脚手架"。祝您在算法学习的道路上收获满满！

如有任何问题或建议，欢迎反馈。让我们一起让算法学习变得更加生动有趣！