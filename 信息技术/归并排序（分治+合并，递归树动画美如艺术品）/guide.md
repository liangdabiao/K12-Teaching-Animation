# 需求：归并排序（分治+合并，递归树动画美如艺术品）

### 1. 专业思考


#### 用户需求分析
1.  **核心目标用户**：学习数据结构与算法的学生（大学或自学者），以及希望直观理解归并排序原理的编程爱好者。
2.  **核心需求**：
    *   **理解分治思想**：清晰地看到“分”与“治”（合）两个截然不同的阶段。
    *   **可视化递归过程**：理解递归如何将大问题分解为小问题，以及递归调用栈的展开与回归。
    *   **掌握合并过程**：直观地看到两个有序子数组合并成一个有序数组的**比较与移动**细节。
    *   **感受算法美感与效率**：通过动画节奏和视觉设计，体会归并排序O(n log n)时间复杂度的由来及其“稳定排序”的特性。
3.  **潜在痛点**：
    *   对递归的抽象性感到困惑。
    *   不理解合并步骤为何是线性的，以及它如何保证正确性。
    *   难以在脑中构建递归树和整个排序过程的动态图景。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）

*   **核心概念拆解**：
    1.  **分治策略**：将大数组递归地**一分为二**，直到子数组长度为1（自然有序）。
    2.  **递归树**：展示分解过程的树状结构，体现log n的深度。
    3.  **合并操作**：核心教学点。强调“两个有序数组”的**指针比较**、**较小值选取**和**放入新数组**三个步骤。
    4.  **递归返回**：合并后的有序数组向上返回，作为上一层的子问题解。

*   **认知规律遵循**：
    *   **从具体到抽象**：先展示完整的动画，再允许用户分步控制，最后可探索递归细节。
    *   **双重编码**：将算法逻辑（文本、代码高亮）与视觉动画（图形移动、颜色变化、路径指示）紧密结合，强化记忆。
    *   **渐进式呈现**：初始时隐藏复杂信息（如递归栈），在用户熟悉基本流程后，可开启高级视图。

*   **交互设计**：
    *   **分层控制**：提供“播放/暂停”、“下一步/上一步”按钮，让用户能以自己的节奏学习。
    *   **焦点引导**：在每一步，通过高亮、放大或脉动效果，突出当前正在操作的元素（如被分割的数组、正在比较的两个数字、被选中的数字）。
    *   **探索式学习**：
        *   允许用户输入自定义数据。
        *   提供“高亮递归路径”或“显示递归调用栈”的开关，帮助理解递归流程。
        *   在递归树视图和数组视图之间建立视觉连接（如连线、同步高亮）。

*   **视觉呈现**：
    *   **双视图并列**：
        *   **左视图（过程视图）**：以水平条形图或带数字的圆球表示数组元素，主要展示分割与合并的具体操作。
        *   **右视图（结构视图）**：绘制一棵**递归树**，动态生长，展示“分”的层级和“合”的向上返回。这是体现“美如艺术品”的关键。
    *   **动画设计**：
        *   **“分”的动画**：数组被一道柔和的光线或动画效果“切开”，并向左右轻轻分离，移动到递归树的子节点位置。
        *   **“合”的动画**：为两个待合并的子数组设置两个颜色区（如浅蓝、浅粉）。比较时，候选数字高亮（如黄色）。被选中的数字优雅地“飞”入上方父节点的数组中，飞行轨迹可带尾迹。合并完成后，颜色区融合。
        *   **递归树动画**：节点随递归调用动态创建和展开。合并时，从子节点到父节点有光流或连线高亮，表示结果返回。

#### 配色方案选择
选择柔和、清晰、富有科技感且利于区分不同状态的配色。

*   **主色调**：
    *   **背景**：深空蓝（`#0f172a`）或浅灰色（`#f8fafc`），营造专注、清晰的画布。
    *   **数据结构**：
        *   未排序数字：中性白色（`#ffffff`）带深色边框。
        *   有序子数组区域：使用低饱和度的相邻色（如合并时的浅蓝 `#93c5fd` 和浅粉 `#f9a8d4`），区分同时又不刺眼。
*   **状态色**：
    *   **高亮/当前操作**：明黄色（`#fde047`）或荧光绿（`#86efac`），吸引注意力。
    *   **比较元素**：橙色（`#fb923c`），表示正在评估。
    *   **已排序/已完成部分**：稳定的绿色（`#4ade80`）或淡青色（`#5eead4`），传达“完成”和“正确”的感觉。
    *   **递归树节点**：节点边框用主色，激活时填充半透明亮色。
*   **动效与轨迹**：使用半透明的光效颜色（如高亮蓝 `#60a5fa`，透明度0.7）来绘制飞行轨迹或连接线。

#### 交互功能列表
1.  **核心控制面板**：
    *   播放/暂停
    *   下一步 (Step)
    *   上一步 (Prev)
    *   重置 (Reset)
2.  **数据输入区**：
    *   预设示例按钮（如：随机数组、逆序数组、部分有序数组）
    *   自定义输入框（允许用户输入逗号分隔的数字）
3.  **视图控制开关**：
    *   `显示递归树` 开关：控制右侧递归树视图的显示/隐藏。
    *   `高亮递归路径` 开关：在递归树上高亮显示当前活跃的调用路径。
    *   `显示代码联动` 开关：在动画旁显示伪代码，并高亮当前执行的代码行。
    *   `动画速度` 滑块：控制动画播放的快慢。
4.  **信息显示面板**：
    *   当前步骤说明（如：“正在分割左半部分 [0, 3]”、“合并 [1, 3] 和 [4, 6]”）。
    *   关键变量状态（如：当前子数组索引 `left, mid, right`）。
    *   步骤计数器。
5.  **可视化元素交互**：
    *   鼠标悬停在递归树节点上时，显示该节点对应的子数组范围和内容。
    *   在过程视图中，悬停在数字上可显示其索引和值。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>归并排序可视化 - 分治的艺术</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background-color: #0f172a;
            color: #e2e8f0;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            max-width: 800px;
        }

        h1 {
            color: #5eead4;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(94, 234, 212, 0.3);
        }

        .subtitle {
            color: #94a3b8;
            font-size: 1.1rem;
            margin-bottom: 20px;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            max-width: 1400px;
            width: 100%;
            justify-content: center;
        }

        .panel {
            background: rgba(30, 41, 59, 0.8);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(94, 234, 212, 0.1);
        }

        .left-panel {
            flex: 1;
            min-width: 500px;
            max-width: 700px;
        }

        .right-panel {
            flex: 1;
            min-width: 500px;
            max-width: 600px;
        }

        .panel-title {
            color: #5eead4;
            font-size: 1.5rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid rgba(94, 234, 212, 0.3);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .panel-title i {
            font-size: 1.2rem;
        }

        .canvas-container {
            position: relative;
            width: 100%;
            height: 400px;
            background: rgba(15, 23, 42, 0.5);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 1px solid rgba(148, 163, 184, 0.2);
        }

        canvas {
            display: block;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 25px;
            padding: 20px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 10px;
            align-items: center;
        }

        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #5eead4, #2dd4bf);
            color: #0f172a;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(94, 234, 212, 0.4);
        }

        .btn-secondary {
            background: rgba(148, 163, 184, 0.2);
            color: #e2e8f0;
        }

        .btn-secondary:hover {
            background: rgba(148, 163, 184, 0.3);
            transform: translateY(-2px);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none !important;
            box-shadow: none !important;
        }

        .input-section {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 25px;
            padding: 20px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 10px;
        }

        .input-group {
            flex: 1;
            min-width: 200px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #94a3b8;
            font-weight: 500;
        }

        input, select {
            width: 100%;
            padding: 12px;
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(94, 234, 212, 0.3);
            border-radius: 8px;
            color: #e2e8f0;
            font-size: 1rem;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #5eead4;
            box-shadow: 0 0 0 2px rgba(94, 234, 212, 0.2);
        }

        .toggle-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }

        .toggle-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 12px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .toggle-item:hover {
            background: rgba(15, 23, 42, 0.8);
        }

        .toggle-item input {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }

        .info-panel {
            background: rgba(15, 23, 42, 0.6);
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
        }

        .info-item {
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
        }

        .info-item:last-child {
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }

        .info-label {
            color: #94a3b8;
            font-size: 0.9rem;
            margin-bottom: 5px;
        }

        .info-value {
            color: #e2e8f0;
            font-size: 1.1rem;
            font-weight: 600;
        }

        .status-highlight {
            color: #fde047;
            font-weight: 700;
        }

        .color-legend {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
        }

        .color-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
        }

        .color-box {
            width: 16px;
            height: 16px;
            border-radius: 4px;
        }

        .color-default { background-color: #ffffff; border: 1px solid #64748b; }
        .color-compare { background-color: #fb923c; }
        .color-selected { background-color: #fde047; }
        .color-left { background-color: #93c5fd; }
        .color-right { background-color: #f9a8d4; }
        .color-sorted { background-color: #4ade80; }

        .pseudocode {
            background: rgba(15, 23, 42, 0.8);
            border-radius: 10px;
            padding: 20px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9rem;
            line-height: 1.6;
            margin-top: 20px;
            max-height: 300px;
            overflow-y: auto;
        }

        .code-line {
            padding: 5px 10px;
            border-radius: 5px;
            margin-bottom: 2px;
            transition: background 0.3s ease;
        }

        .code-line.active {
            background: rgba(94, 234, 212, 0.2);
            color: #5eead4;
            font-weight: 600;
        }

        .code-line.comment {
            color: #94a3b8;
            font-style: italic;
        }

        .code-line.keyword {
            color: #f472b6;
        }

        .code-line.function {
            color: #60a5fa;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
            color: #64748b;
            font-size: 0.9rem;
            padding: 20px;
            max-width: 800px;
        }

        @media (max-width: 1100px) {
            .container {
                flex-direction: column;
                align-items: center;
            }
            
            .left-panel, .right-panel {
                min-width: 90%;
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>归并排序可视化</h1>
        <div class="subtitle">分治策略 · 递归之美 · 合并艺术</div>
    </div>

    <div class="container">
        <!-- 左面板：数组操作视图 -->
        <div class="panel left-panel">
            <div class="panel-title">
                <span>📊 数组操作视图</span>
            </div>
            
            <div class="canvas-container">
                <canvas id="arrayCanvas" width="650" height="400"></canvas>
            </div>
            
            <div class="controls">
                <button id="playBtn" class="btn btn-primary">
                    <span>▶️ 播放</span>
                </button>
                <button id="pauseBtn" class="btn btn-secondary">
                    <span>⏸️ 暂停</span>
                </button>
                <button id="stepBtn" class="btn btn-secondary">
                    <span>⏭️ 下一步</span>
                </button>
                <button id="prevBtn" class="btn btn-secondary">
                    <span>⏮️ 上一步</span>
                </button>
                <button id="resetBtn" class="btn btn-secondary">
                    <span>🔄 重置</span>
                </button>
                
                <div style="flex: 1; min-width: 150px;">
                    <label for="speedSlider">动画速度</label>
                    <input type="range" id="speedSlider" min="1" max="10" value="5">
                </div>
            </div>
            
            <div class="input-section">
                <div class="input-group">
                    <label for="arrayInput">自定义数组（逗号分隔）</label>
                    <input type="text" id="arrayInput" value="38, 27, 43, 3, 9, 82, 10">
                </div>
                
                <div class="input-group">
                    <label for="presetSelect">预设示例</label>
                    <select id="presetSelect">
                        <option value="custom">自定义</option>
                        <option value="random">随机数组</option>
                        <option value="reverse">逆序数组</option>
                        <option value="nearly">基本有序数组</option>
                        <option value="small">小型数组</option>
                    </select>
                </div>
            </div>
            
            <div class="info-panel">
                <div class="info-item">
                    <div class="info-label">当前操作</div>
                    <div id="currentOperation" class="info-value">等待开始...</div>
                </div>
                
                <div class="info-item">
                    <div class="info-label">当前子数组范围</div>
                    <div id="currentRange" class="info-value">-</div>
                </div>
                
                <div class="info-item">
                    <div class="info-label">步骤计数</div>
                    <div id="stepCount" class="info-value">0</div>
                </div>
                
                <div class="color-legend">
                    <div class="color-item">
                        <div class="color-box color-default"></div>
                        <span>默认元素</span>
                    </div>
                    <div class="color-item">
                        <div class="color-box color-compare"></div>
                        <span>比较中</span>
                    </div>
                    <div class="color-item">
                        <div class="color-box color-selected"></div>
                        <span>已选中</span>
                    </div>
                    <div class="color-item">
                        <div class="color-box color-left"></div>
                        <span>左子数组</span>
                    </div>
                    <div class="color-item">
                        <div class="color-box color-right"></div>
                        <span>右子数组</span>
                    </div>
                    <div class="color-item">
                        <div class="color-box color-sorted"></div>
                        <span>已排序</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 右面板：递归树视图 -->
        <div class="panel right-panel">
            <div class="panel-title">
                <span>🌳 递归树视图</span>
            </div>
            
            <div class="canvas-container">
                <canvas id="treeCanvas" width="550" height="400"></canvas>
            </div>
            
            <div class="toggle-section">
                <div class="toggle-item">
                    <input type="checkbox" id="showTreeToggle" checked>
                    <label for="showTreeToggle">显示递归树</label>
                </div>
                
                <div class="toggle-item">
                    <input type="checkbox" id="highlightPathToggle" checked>
                    <label for="highlightPathToggle">高亮递归路径</label>
                </div>
                
                <div class="toggle-item">
                    <input type="checkbox" id="showCodeToggle" checked>
                    <label for="showCodeToggle">显示代码联动</label>
                </div>
            </div>
            
            <div id="pseudocodePanel" class="pseudocode">
                <div class="code-line comment">// 归并排序主函数</div>
                <div id="codeLine1" class="code-line">function mergeSort(arr, left, right) {</div>
                <div id="codeLine2" class="code-line">  if (left < right) {</div>
                <div id="codeLine3" class="code-line">    let mid = Math.floor((left + right) / 2);</div>
                <div id="codeLine4" class="code-line">    mergeSort(arr, left, mid);      // 递归排序左半部分</div>
                <div id="codeLine5" class="code-line">    mergeSort(arr, mid + 1, right); // 递归排序右半部分</div>
                <div id="codeLine6" class="code-line">    merge(arr, left, mid, right);   // 合并两个有序数组</div>
                <div id="codeLine7" class="code-line">  }</div>
                <div id="codeLine8" class="code-line">}</div>
                <div class="code-line comment" style="margin-top: 15px;">// 合并函数</div>
                <div id="codeLine9" class="code-line">function merge(arr, left, mid, right) {</div>
                <div id="codeLine10" class="code-line">  let temp = [];</div>
                <div id="codeLine11" class="code-line">  let i = left, j = mid + 1;</div>
                <div id="codeLine12" class="code-line">  while (i <= mid && j <= right) {</div>
                <div id="codeLine13" class="code-line">    if (arr[i] <= arr[j]) {</div>
                <div id="codeLine14" class="code-line">      temp.push(arr[i]); i++;</div>
                <div id="codeLine15" class="code-line">    } else {</div>
                <div id="codeLine16" class="code-line">      temp.push(arr[j]); j++;</div>
                <div id="codeLine17" class="code-line">    }</div>
                <div id="codeLine18" class="code-line">  }</div>
                <div id="codeLine19" class="code-line">  while (i <= mid) { temp.push(arr[i]); i++; }</div>
                <div id="codeLine20" class="code-line">  while (j <= right) { temp.push(arr[j]); j++; }</div>
                <div id="codeLine21" class="code-line">  for (let k = left; k <= right; k++) {</div>
                <div id="codeLine22" class="code-line">    arr[k] = temp[k - left];</div>
                <div id="codeLine23" class="code-line">  }</div>
                <div id="codeLine24" class="code-line">}</div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>归并排序是一种采用分治策略的稳定排序算法，时间复杂度为 O(n log n)。通过递归地将数组分解，然后合并有序子数组，最终完成排序。</p>
        <p style="margin-top: 10px;">交互式教学动画 © 2023 | 设计灵感：熊猫老师</p>
    </div>

    <script>
        // 全局变量
        let originalArray = [38, 27, 43, 3, 9, 82, 10];
        let currentArray = [...originalArray];
        let animationSteps = [];
        let currentStep = 0;
        let isPlaying = false;
        let animationSpeed = 5;
        let animationInterval;
        
        // 配置选项
        let showTree = true;
        let highlightPath = true;
        let showCode = true;
        
        // 获取DOM元素
        const arrayCanvas = document.getElementById('arrayCanvas');
        const treeCanvas = document.getElementById('treeCanvas');
        const arrayCtx = arrayCanvas.getContext('2d');
        const treeCtx = treeCanvas.getContext('2d');
        
        // 获取控制元素
        const playBtn = document.getElementById('playBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const stepBtn = document.getElementById('stepBtn');
        const prevBtn = document.getElementById('prevBtn');
        const resetBtn = document.getElementById('resetBtn');
        const speedSlider = document.getElementById('speedSlider');
        const arrayInput = document.getElementById('arrayInput');
        const presetSelect = document.getElementById('presetSelect');
        
        // 获取信息显示元素
        const currentOperation = document.getElementById('currentOperation');
        const currentRange = document.getElementById('currentRange');
        const stepCount = document.getElementById('stepCount');
        
        // 获取切换开关
        const showTreeToggle = document.getElementById('showTreeToggle');
        const highlightPathToggle = document.getElementById('highlightPathToggle');
        const showCodeToggle = document.getElementById('showCodeToggle');
        
        // 获取代码行元素
        const codeLines = {};
        for (let i = 1; i <= 24; i++) {
            codeLines[i] = document.getElementById(`codeLine${i}`);
        }
        
        // 归并排序算法实现（生成动画步骤）
        function generateMergeSortSteps(arr) {
            const steps = [];
            const tempArray = [...arr];
            
            function mergeSort(arr, left, right, depth, path) {
                const stepId = steps.length;
                steps.push({
                    type: 'enter',
                    left, right, depth, path,
                    stepId,
                    operation: `进入归并排序: [${left}, ${right}]`
                });
                
                if (left < right) {
                    const mid = Math.floor((left + right) / 2);
                    
                    // 递归左半部分
                    const leftPath = [...path, 'L'];
                    mergeSort(arr, left, mid, depth + 1, leftPath);
                    
                    // 递归右半部分
                    const rightPath = [...path, 'R'];
                    mergeSort(arr, mid + 1, right, depth + 1, rightPath);
                    
                    // 合并
                    merge(arr, left, mid, right, depth, path);
                } else {
                    steps.push({
                        type: 'base',
                        left, right, depth, path,
                        stepId: steps.length,
                        operation: `基本情况: 单个元素 [${left}]`
                    });
                }
                
                steps.push({
                    type: 'exit',
                    left, right, depth, path,
                    stepId: steps.length,
                    operation: `退出归并排序: [${left}, ${right}]`
                });
            }
            
            function merge(arr, left, mid, right, depth, path) {
                const temp = [];
                let i = left;
                let j = mid + 1;
                let k = 0;
                
                steps.push({
                    type: 'merge_start',
                    left, mid, right, depth, path,
                    stepId: steps.length,
                    operation: `开始合并: [${left}, ${mid}] 和 [${mid+1}, ${right}]`
                });
                
                // 比较并合并
                while (i <= mid && j <= right) {
                    steps.push({
                        type: 'compare',
                        left, mid, right, i, j, depth, path,
                        stepId: steps.length,
                        operation: `比较: arr[${i}]=${arr[i]} 和 arr[${j}]=${arr[j]}`
                    });
                    
                    if (arr[i] <= arr[j]) {
                        steps.push({
                            type: 'select_left',
                            left, mid, right, i, j, depth, path,
                            stepId: steps.length,
                            operation: `选择左元素: arr[${i}]=${arr[i]}`
                        });
                        temp[k++] = arr[i++];
                    } else {
                        steps.push({
                            type: 'select_right',
                            left, mid, right, i, j, depth, path,
                            stepId: steps.length,
                            operation: `选择右元素: arr[${j}]=${arr[j]}`
                        });
                        temp[k++] = arr[j++];
                    }
                }
                
                // 复制剩余元素
                while (i <= mid) {
                    steps.push({
                        type: 'copy_left',
                        left, mid, right, i, depth, path,
                        stepId: steps.length,
                        operation: `复制左剩余元素: arr[${i}]=${arr[i]}`
                    });
                    temp[k++] = arr[i++];
                }
                
                while (j <= right) {
                    steps.push({
                        type: 'copy_right',
                        left, mid, right, j, depth, path,
                        stepId: steps.length,
                        operation: `复制右剩余元素: arr[${j}]=${arr[j]}`
                    });
                    temp[k++] = arr[j++];
                }
                
                // 复制回原数组
                for (let t = 0; t < k; t++) {
                    arr[left + t] = temp[t];
                    steps.push({
                        type: 'copy_back',
                        left, mid, right, index: left + t, value: temp[t], depth, path,
                        stepId: steps.length,
                        operation: `复制回原数组: arr[${left + t}] = ${temp[t]}`
                    });
                }
                
                steps.push({
                    type: 'merge_end',
                    left, mid, right, depth, path,
                    stepId: steps.length,
                    operation: `合并完成: [${left}, ${right}] 已排序`
                });
            }
            
            mergeSort(tempArray, 0, tempArray.length - 1, 0, ['ROOT']);
            return steps;
        }
        
        // 绘制数组视图
        function drawArrayView(step) {
            const canvas = arrayCanvas;
            const ctx = arrayCtx;
            const width = canvas.width;
            const height = canvas.height;
            
            // 清除画布
            ctx.clearRect(0, 0, width, height);
            
            // 绘制背景
            ctx.fillStyle = 'rgba(15, 23, 42, 0.5)';
            ctx.fillRect(0, 0, width, height);
            
            // 如果没有步骤，绘制初始数组
            if (!step) {
                drawArray(currentArray, 0, currentArray.length - 1, 'default');
                return;
            }
            
            // 根据步骤类型绘制
            const { type, left, right, mid, i, j, index, value, depth, path } = step;
            
            switch (type) {
                case 'enter':
                case 'exit':
                case 'base':
                    drawArray(currentArray, left, right, 'highlight_range');
                    break;
                    
                case 'merge_start':
                    drawArray(currentArray, left, mid, 'left_array');
                    drawArray(currentArray, mid + 1, right, 'right_array');
                    break;
                    
                case 'compare':
                    drawArray(currentArray, left, mid, 'left_array');
                    drawArray(currentArray, mid + 1, right, 'right_array');
                    drawArrayElement(i, 'compare');
                    drawArrayElement(j, 'compare');
                    break;
                    
                case 'select_left':
                    drawArray(currentArray, left, mid, 'left_array');
                    drawArray(currentArray, mid + 1, right, 'right_array');
                    drawArrayElement(i, 'selected');
                    break;
                    
                case 'select_right':
                    drawArray(currentArray, left, mid, 'left_array');
                    drawArray(currentArray, mid + 1, right, 'right_array');
                    drawArrayElement(j, 'selected');
                    break;
                    
                case 'copy_back':
                    // 更新数组值
                    if (index >= 0 && index < currentArray.length) {
                        currentArray[index] = value;
                    }
                    drawArray(currentArray, left, right, 'sorted');
                    drawArrayElement(index, 'selected');
                    break;
                    
                default:
                    drawArray(currentArray, 0, currentArray.length - 1, 'default');
            }
            
            // 绘制当前操作信息
            if (step.operation) {
                ctx.fillStyle = '#5eead4';
                ctx.font = '16px "Segoe UI", sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(step.operation, width / 2, 30);
            }
        }
        
        // 绘制数组
        function drawArray(arr, start, end, style) {
            const canvas = arrayCanvas;
            const ctx = arrayCtx;
            const width = canvas.width;
            const height = canvas.height;
            
            const totalElements = arr.length;
            const barWidth = (width - 100) / totalElements;
            const maxBarHeight = height - 100;
            const maxValue = Math.max(...arr);
            
            // 确定颜色
            let fillColor, borderColor;
            switch (style) {
                case 'highlight_range':
                    fillColor = 'rgba(253, 224, 71, 0.3)';
                    borderColor = '#fde047';
                    break;
                case 'left_array':
                    fillColor = 'rgba(147, 197, 253, 0.3)';
                    borderColor = '#93c5fd';
                    break;
                case 'right_array':
                    fillColor = 'rgba(249, 168, 212, 0.3)';
                    borderColor = '#f9a8d4';
                    break;
                case 'sorted':
                    fillColor = 'rgba(74, 222, 128, 0.3)';
                    borderColor = '#4ade80';
                    break;
                default:
                    fillColor = 'rgba(255, 255, 255, 0.1)';
                    borderColor = '#64748b';
            }
            
            // 绘制数组元素
            for (let idx = 0; idx < arr.length; idx++) {
                const x = 50 + idx * barWidth;
                const barHeight = (arr[idx] / maxValue) * maxBarHeight;
                const y = height - 50 - barHeight;
                
                // 如果元素在指定范围内，使用特殊样式
                if (idx >= start && idx <= end) {
                    ctx.fillStyle = fillColor;
                    ctx.fillRect(x, y, barWidth - 2, barHeight);
                    
                    ctx.strokeStyle = borderColor;
                    ctx.lineWidth = 2;
                    ctx.strokeRect(x, y, barWidth - 2, barHeight);
                } else {
                    // 默认样式
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
                    ctx.fillRect(x, y, barWidth - 2, barHeight);
                    
                    ctx.strokeStyle = '#64748b';
                    ctx.lineWidth = 1;
                    ctx.strokeRect(x, y, barWidth - 2, barHeight);
                }
                
                // 绘制数值
                ctx.fillStyle = '#e2e8f0';
                ctx.font = '14px "Segoe UI", sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(arr[idx], x + (barWidth - 2) / 2, y - 10);
                
                // 绘制索引
                ctx.fillStyle = '#94a3b8';
                ctx.font = '12px "Segoe UI", sans-serif';
                ctx.fillText(idx, x + (barWidth - 2) / 2, height - 25);
            }
        }
        
        // 绘制单个数组元素（高亮）
        function drawArrayElement(index, style) {
            const canvas = arrayCanvas;
            const ctx = arrayCtx;
            const width = canvas.width;
            const height = canvas.height;
            
            const totalElements = currentArray.length;
            const barWidth = (width - 100) / totalElements;
            const maxBarHeight = height - 100;
            const maxValue = Math.max(...currentArray);
            
            const x = 50 + index * barWidth;
            const barHeight = (currentArray[index] / maxValue) * maxBarHeight;
            const y = height - 50 - barHeight;
            
            // 确定颜色
            let fillColor, borderColor;
            switch (style) {
                case 'compare':
                    fillColor = 'rgba(251, 146, 60, 0.7)';
                    borderColor = '#fb923c';
                    break;
                case 'selected':
                    fillColor = 'rgba(253, 224, 71, 0.7)';
                    borderColor = '#fde047';
                    break;
                default:
                    return;
            }
            
            // 绘制高亮元素
            ctx.fillStyle = fillColor;
            ctx.fillRect(x - 2, y - 2, barWidth + 2, barHeight + 4);
            
            ctx.strokeStyle = borderColor;
            ctx.lineWidth = 3;
            ctx.strokeRect(x - 2, y - 2, barWidth + 2, barHeight + 4);
            
            // 重新绘制数值（确保在顶部）
            ctx.fillStyle = '#0f172a';
            ctx.font = 'bold 14px "Segoe UI", sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(currentArray[index], x + (barWidth - 2) / 2, y - 10);
        }
        
        // 绘制递归树
        function drawTreeView(step) {
            if (!showTree) return;
            
            const canvas = treeCanvas;
            const ctx = treeCtx;
            const width = canvas.width;
            const height = canvas.height;
            
            // 清除画布
            ctx.clearRect(0, 0, width, height);
            
            // 绘制背景
            ctx.fillStyle = 'rgba(15, 23, 42, 0.5)';
            ctx.fillRect(0, 0, width, height);
            
            // 如果没有步骤，绘制空树
            if (!step) {
                ctx.fillStyle = '#5eead4';
                ctx.font = '18px "Segoe UI", sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('点击"播放"开始可视化递归树', width / 2, height / 2);
                return;
            }
            
            // 绘制递归树
            const { depth, path, left, right, type } = step;
            
            // 计算节点位置
            const maxDepth = 5;
            const nodeRadius = 20;
            const levelHeight = 70;
            
            // 绘制所有历史节点
            for (let i = 0; i <= currentStep; i++) {
                const stepInfo = animationSteps[i];
                if (!stepInfo || !stepInfo.path) continue;
                
                // 计算节点位置
                const nodeDepth = stepInfo.depth;
                const pathStr = stepInfo.path.join('');
                
                // 计算水平位置（基于路径）
                let position = 0.5; // 根节点在中间
                for (let j = 1; j < stepInfo.path.length; j++) {
                    const direction = stepInfo.path[j];
                    const offset = Math.pow(0.5, j + 1);
                    position += direction === 'L' ? -offset : offset;
                }
                
                const x = 50 + position * (width - 100);
                const y = 50 + nodeDepth * levelHeight;
                
                // 确定节点颜色
                let nodeColor = '#334155';
                let borderColor = '#64748b';
                let textColor = '#e2e8f0';
                
                // 高亮当前路径
                if (highlightPath && isPathPrefix(stepInfo.path, path)) {
                    nodeColor = 'rgba(94, 234, 212, 0.3)';
                    borderColor = '#5eead4';
                }
                
                // 当前节点特殊高亮
                if (i === currentStep) {
                    nodeColor = 'rgba(253, 224, 71, 0.5)';
                    borderColor = '#fde047';
                }
                
                // 绘制节点
                ctx.beginPath();
                ctx.arc(x, y, nodeRadius, 0, Math.PI * 2);
                ctx.fillStyle = nodeColor;
                ctx.fill();
                ctx.strokeStyle = borderColor;
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // 绘制节点文本
                ctx.fillStyle = textColor;
                ctx.font = '12px "Segoe UI", sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                
                let displayText = '';
                if (stepInfo.type === 'base') {
                    displayText = `[${left}]`;
                } else if (stepInfo.left !== undefined && stepInfo.right !== undefined) {
                    displayText = `[${stepInfo.left},${stepInfo.right}]`;
                } else {
                    displayText = pathStr.substring(0, 4) + (pathStr.length > 4 ? '...' : '');
                }
                
                ctx.fillText(displayText, x, y);
                
                // 绘制连接线（连接到父节点）
                if (stepInfo.path.length > 1) {
                    const parentPath = stepInfo.path.slice(0, -1);
                    const parentStep = findStepByPath(parentPath);
                    
                    if (parentStep) {
                        // 计算父节点位置
                        let parentPosition = 0.5;
                        for (let j = 1; j < parentPath.length; j++) {
                            const direction = parentPath[j];
                            const offset = Math.pow(0.5, j + 1);
                            parentPosition
+= direction === 'L' ? -offset : offset;
                        }
                        
                        const parentX = 50 + parentPosition * (width - 100);
                        const parentY = 50 + parentStep.depth * levelHeight;
                        
                        // 绘制连接线
                        ctx.beginPath();
                        ctx.moveTo(parentX, parentY + nodeRadius);
                        ctx.lineTo(x, y - nodeRadius);
                        ctx.strokeStyle = highlightPath && isPathPrefix(parentPath, path) ? '#5eead4' : '#475569';
                        ctx.lineWidth = 1.5;
                        ctx.stroke();
                    }
                }
            }
            
            // 绘制当前操作信息
            if (step.operation) {
                ctx.fillStyle = '#5eead4';
                ctx.font = '16px "Segoe UI", sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(step.operation, width / 2, height - 20);
            }
        }
        
        // 辅助函数：检查路径前缀
        function isPathPrefix(prefix, fullPath) {
            if (prefix.length > fullPath.length) return false;
            for (let i = 0; i < prefix.length; i++) {
                if (prefix[i] !== fullPath[i]) return false;
            }
            return true;
        }
        
        // 辅助函数：根据路径查找步骤
        function findStepByPath(path) {
            for (let i = currentStep; i >= 0; i--) {
                if (animationSteps[i] && 
                    animationSteps[i].path.length === path.length &&
                    animationSteps[i].path.every((val, idx) => val === path[idx])) {
                    return animationSteps[i];
                }
            }
            return null;
        }
        
        // 更新代码高亮
        function updateCodeHighlight(step) {
            if (!showCode) {
                // 清除所有高亮
                for (let i = 1; i <= 24; i++) {
                    codeLines[i].classList.remove('active');
                }
                return;
            }
            
            // 清除所有高亮
            for (let i = 1; i <= 24; i++) {
                codeLines[i].classList.remove('active');
            }
            
            if (!step) return;
            
            // 根据步骤类型高亮对应代码行
            const { type } = step;
            
            switch (type) {
                case 'enter':
                    codeLines[1].classList.add('active');
                    codeLines[2].classList.add('active');
                    break;
                    
                case 'base':
                    codeLines[7].classList.add('active');
                    break;
                    
                case 'merge_start':
                    codeLines[6].classList.add('active');
                    codeLines[9].classList.add('active');
                    break;
                    
                case 'compare':
                    codeLines[12].classList.add('active');
                    codeLines[13].classList.add('active');
                    break;
                    
                case 'select_left':
                    codeLines[14].classList.add('active');
                    break;
                    
                case 'select_right':
                    codeLines[16].classList.add('active');
                    break;
                    
                case 'copy_left':
                case 'copy_right':
                    codeLines[19].classList.add('active');
                    codeLines[20].classList.add('active');
                    break;
                    
                case 'copy_back':
                    codeLines[21].classList.add('active');
                    codeLines[22].classList.add('active');
                    break;
                    
                case 'merge_end':
                    codeLines[23].classList.add('active');
                    codeLines[24].classList.add('active');
                    break;
                    
                case 'exit':
                    codeLines[8].classList.add('active');
                    break;
            }
        }
        
        // 更新信息面板
        function updateInfoPanel(step) {
            if (!step) {
                currentOperation.textContent = '等待开始...';
                currentRange.textContent = '-';
                stepCount.textContent = '0';
                return;
            }
            
            currentOperation.textContent = step.operation;
            stepCount.textContent = currentStep + 1;
            
            if (step.left !== undefined && step.right !== undefined) {
                currentRange.textContent = `[${step.left}, ${step.right}]`;
            } else {
                currentRange.textContent = '-';
            }
        }
        
        // 执行一步动画
        function executeStep(stepIndex) {
            if (stepIndex < 0 || stepIndex >= animationSteps.length) return;
            
            currentStep = stepIndex;
            const step = animationSteps[stepIndex];
            
            // 更新数组状态（对于copy_back步骤）
            if (step.type === 'copy_back' && step.index !== undefined && step.value !== undefined) {
                currentArray[step.index] = step.value;
            }
            
            // 更新显示
            drawArrayView(step);
            drawTreeView(step);
            updateCodeHighlight(step);
            updateInfoPanel(step);
            
            // 更新按钮状态
            updateButtonStates();
        }
        
        // 下一步
        function nextStep() {
            if (currentStep < animationSteps.length - 1) {
                executeStep(currentStep + 1);
            } else {
                pauseAnimation();
            }
        }
        
        // 上一步
        function prevStep() {
            if (currentStep > 0) {
                // 需要重新计算数组状态
                resetArrayState();
                for (let i = 0; i < currentStep - 1; i++) {
                    const step = animationSteps[i];
                    if (step.type === 'copy_back' && step.index !== undefined && step.value !== undefined) {
                        currentArray[step.index] = step.value;
                    }
                }
                executeStep(currentStep - 1);
            }
        }
        
        // 重置数组状态
        function resetArrayState() {
            currentArray = [...originalArray];
        }
        
        // 播放动画
        function playAnimation() {
            if (isPlaying) return;
            
            isPlaying = true;
            updateButtonStates();
            
            animationInterval = setInterval(() => {
                if (currentStep < animationSteps.length - 1) {
                    nextStep();
                } else {
                    pauseAnimation();
                }
            }, 1000 / animationSpeed);
        }
        
        // 暂停动画
        function pauseAnimation() {
            isPlaying = false;
            clearInterval(animationInterval);
            updateButtonStates();
        }
        
        // 重置动画
        function resetAnimation() {
            pauseAnimation();
            currentStep = 0;
            resetArrayState();
            drawArrayView(null);
            drawTreeView(null);
            updateCodeHighlight(null);
            updateInfoPanel(null);
            updateButtonStates();
        }
        
        // 更新按钮状态
        function updateButtonStates() {
            playBtn.disabled = isPlaying || currentStep >= animationSteps.length - 1;
            pauseBtn.disabled = !isPlaying;
            stepBtn.disabled = isPlaying || currentStep >= animationSteps.length - 1;
            prevBtn.disabled = isPlaying || currentStep <= 0;
        }
        
        // 生成随机数组
        function generateRandomArray(size = 8) {
            const arr = [];
            for (let i = 0; i < size; i++) {
                arr.push(Math.floor(Math.random() * 90) + 10);
            }
            return arr;
        }
        
        // 生成逆序数组
        function generateReverseArray(size = 8) {
            const arr = [];
            for (let i = size; i > 0; i--) {
                arr.push(i * 10);
            }
            return arr;
        }
        
        // 生成基本有序数组
        function generateNearlySortedArray(size = 8) {
            const arr = [];
            for (let i = 0; i < size; i++) {
                arr.push((i + 1) * 10);
            }
            // 交换几对元素
            for (let i = 0; i < 2; i++) {
                const idx1 = Math.floor(Math.random() * size);
                const idx2 = Math.floor(Math.random() * size);
                [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
            }
            return arr;
        }
        
        // 初始化
        function init() {
            // 生成初始动画步骤
            animationSteps = generateMergeSortSteps(originalArray);
            
            // 绘制初始状态
            drawArrayView(null);
            drawTreeView(null);
            updateCodeHighlight(null);
            updateInfoPanel(null);
            updateButtonStates();
            
            // 事件监听器
            playBtn.addEventListener('click', playAnimation);
            pauseBtn.addEventListener('click', pauseAnimation);
            stepBtn.addEventListener('click', nextStep);
            prevBtn.addEventListener('click', prevStep);
            resetBtn.addEventListener('click', resetAnimation);
            
            speedSlider.addEventListener('input', function() {
                animationSpeed = parseInt(this.value);
                if (isPlaying) {
                    pauseAnimation();
                    playAnimation();
                }
            });
            
            arrayInput.addEventListener('change', function() {
                const input = this.value.trim();
                if (input) {
                    const newArray = input.split(',').map(num => parseInt(num.trim())).filter(num => !isNaN(num));
                    if (newArray.length > 0) {
                        originalArray = newArray;
                        resetAnimation();
                        animationSteps = generateMergeSortSteps(originalArray);
                        presetSelect.value = 'custom';
                    }
                }
            });
            
            presetSelect.addEventListener('change', function() {
                const preset = this.value;
                
                switch (preset) {
                    case 'random':
                        originalArray = generateRandomArray();
                        break;
                    case 'reverse':
                        originalArray = generateReverseArray();
                        break;
                    case 'nearly':
                        originalArray = generateNearlySortedArray();
                        break;
                    case 'small':
                        originalArray = [5, 2, 8, 1];
                        break;
                    case 'custom':
                        return; // 保持当前数组
                }
                
                arrayInput.value = originalArray.join(', ');
                resetAnimation();
                animationSteps = generateMergeSortSteps(originalArray);
            });
            
            showTreeToggle.addEventListener('change', function() {
                showTree = this.checked;
                drawTreeView(animationSteps[currentStep]);
            });
            
            highlightPathToggle.addEventListener('change', function() {
                highlightPath = this.checked;
                drawTreeView(animationSteps[currentStep]);
            });
            
            showCodeToggle.addEventListener('change', function() {
                showCode = this.checked;
                updateCodeHighlight(animationSteps[currentStep]);
            });
            
            // 初始生成步骤
            resetAnimation();
        }
        
        // 页面加载完成后初始化
        window.addEventListener('load', init);
    </script>
</body>
</html>


### 3. 过程输出


## 《归并排序交互式教学动画使用指南》

欢迎使用归并排序交互式教学动画！本工具旨在通过可视化方式，帮助您直观理解归并排序算法的核心思想、分治策略和递归过程。无论您是算法初学者还是希望深化理解的进阶学习者，本动画都将为您提供独特的视觉学习体验。

---

### 一、功能说明

本动画采用**双视图并行设计**，同步展示归并排序的两个关键维度：

1. **数组操作视图（左面板）**：动态展示数组元素的分割、比较、选择和合并过程
2. **递归树视图（右面板）**：可视化展示递归调用的层级结构和执行路径

通过这两个视图的协同展示，您将能够：
- 直观看到算法在“微观”（元素操作）和“宏观”（递归结构）层面的执行过程
- 理解分治策略如何将大问题分解为小问题
- 掌握合并操作如何将有序子数组合并为完整有序数组

---

### 二、主要功能

#### 1. 动画控制功能
- **播放/暂停**：连续播放整个排序过程
- **下一步/上一步**：单步执行，精细控制学习节奏
- **重置**：恢复到初始状态
- **速度调节**：通过滑块调整动画播放速度（1-10档）

#### 2. 数据输入功能
- **自定义数组**：输入任意逗号分隔的数字序列
- **预设示例**：
  - 随机数组：生成随机数据
  - 逆序数组：展示最坏情况
  - 基本有序数组：展示最佳情况
  - 小型数组：简化学习难度

#### 3. 视图控制功能
- **显示递归树开关**：控制右侧递归树视图的显示/隐藏
- **高亮递归路径开关**：在递归树中高亮显示当前执行路径
- **显示代码联动开关**：同步高亮当前执行的伪代码行

#### 4. 信息显示功能
- 实时显示当前操作说明
- 显示当前处理的子数组范围
- 步骤计数器
- 颜色图例说明

---

### 三、设计特色

#### 1. 视觉编码系统
我们设计了精心的颜色编码系统，帮助您快速识别不同状态：
- **白色**：默认元素状态
- **橙色**：正在比较的元素
- **黄色**：已选中的元素（将被移动）
- **浅蓝色**：左子数组区域
- **浅粉色**：右子数组区域
- **绿色**：已排序完成的区域

#### 2. 递归树艺术化呈现
递归树不仅是数据结构，更是算法美学的体现：
- 节点动态生长，反映递归深度
- 路径高亮显示当前调用栈
- 父子节点连线展示递归关系
- 节点标签显示处理的数组范围

#### 3. 多模态学习支持
- **视觉**：动画、颜色、形状
- **文本**：操作说明、伪代码
- **交互**：手动控制、参数调整
- **结构**：双视图对比、层次展示

---

### 四、教学要点

#### 1. 核心概念可视化
- **分治策略**：观察数组如何被递归地一分为二
- **递归基线**：理解当子数组长度为1时停止递归
- **合并操作**：重点学习两个有序数组的合并算法
  - 双指针比较
  - 较小值选择
  - 临时数组使用
  - 结果复制回原数组

#### 2. 算法复杂度直观理解
- **时间复杂度 O(n log n)**：
  - 递归树深度 ≈ log₂n（观察右侧树的高度）
  - 每层合并总工作量 ≈ n（观察左侧合并操作）
- **空间复杂度 O(n)**：观察临时数组的使用

#### 3. 递归执行流程
- **递归展开**：从上到下，不断分解问题
- **递归返回**：从下到上，逐层合并结果
- **调用栈**：通过高亮路径理解递归调用顺序

#### 4. 稳定排序特性
观察算法如何保持相等元素的相对顺序（在比较时使用≤而非<）

---

### 五、使用建议

#### 1. 初学者学习路径
1. **整体观察**：先播放完整动画，了解整体流程
2. **分步学习**：使用“下一步”功能，仔细研究每个步骤
3. **重点突破**：在合并操作步骤暂停，理解比较和选择过程
4. **更换数据**：尝试不同输入数据，观察算法行为变化
5. **关闭辅助**：尝试关闭代码高亮，仅通过动画理解算法

#### 2. 进阶学习建议
1. **递归深度分析**：观察不同规模数据的递归树深度变化
2. **最坏/最好情况**：比较逆序数组和有序数组的执行差异
3. **手动预测**：在下一步之前，尝试预测算法将执行什么操作
4. **算法对比**：在心中与本动画对比其他排序算法（如快速排序）

#### 3. 教学场景应用
- **课堂演示**：教师可使用本动画进行算法原理讲解
- **自主学习**：学生可按照自己的节奏探索算法细节
- **小组讨论**：围绕动画中的特定步骤进行深入讨论
- **作业辅助**：帮助学生验证对算法过程的理解

#### 4. 最佳实践提示
- **从简单开始**：先使用小型数组（如4个元素）
- **关注颜色变化**：颜色是理解状态转换的关键线索
- **利用双视图**：同时观察数组操作和递归树变化
- **控制节奏**：复杂步骤放慢速度，简单步骤加快速度
- **反复观看**：多次观看同一过程，加深理解

---

### 六、技术说明

1. **浏览器兼容性**：建议使用最新版本的Chrome、Firefox或Edge
2. **性能优化**：数组大小建议在20个元素以内以获得最佳视觉效果
3. **响应式设计**：支持不同屏幕尺寸，在移动设备上建议横屏使用

---

### 结语

归并排序不仅是高效的排序算法，更是分治策略的经典范例。通过本交互式动画，我们希望您不仅能掌握算法的实现细节，更能欣赏到算法设计中蕴含的数学美和结构美。

**学习建议**：算法学习如同欣赏艺术品——第一次看整体，第二次看细节，第三次看结构，第四次看思想。愿您在本动画的陪伴下，享受算法学习的每一刻！

如有任何问题或建议，欢迎反馈。祝您学习愉快！

---
*设计灵感：熊猫老师 | 交互式教学动画 © 2023*