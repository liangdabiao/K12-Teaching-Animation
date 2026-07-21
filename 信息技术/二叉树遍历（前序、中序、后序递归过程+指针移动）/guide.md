# 需求：二叉树遍历（前序、中序、后序递归过程+指针移动）

### 1. 专业思考


#### 用户需求分析
1.  **目标用户**：主要为学习数据结构与算法的计算机专业学生或自学者。他们已具备二叉树的基本概念，但难以直观理解递归遍历过程中程序执行栈、节点访问顺序和指针移动的协同关系。
2.  **核心痛点**：
    *   **递归过程抽象**：递归的“调用-返回”机制和隐式的系统栈难以可视化，导致学生只能死记硬背遍历顺序。
    *   **指针状态模糊**：在递归的不同阶段（进入左子树、返回、访问节点、进入右子树），当前“指针”或“执行位置”指向哪里，容易混淆。
    *   **三者对比困难**：前序、中序、后序的代码差异微小，但过程截然不同，需要并排对比才能深刻理解其本质区别。
3.  **学习目标**：通过动画，用户应能清晰说出三种遍历的节点访问序列，并能逐步解释递归在每一节点上的具体操作（访问、向左递归、向右递归）及其顺序。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）
1.  **核心概念解构**：
    *   将一次递归调用分解为几个关键“动作”：`访问节点（V）`、`向左递归（L）`、`向右递归（R）`。
    *   三种遍历的本质是这三个动作的执行顺序不同：
        *   前序：`V -> L -> R`
        *   中序：`L -> V -> R`
        *   后序：`L -> R -> V`
    *   “指针移动”实质是当前递归调用所关注的节点，以及程序执行流的跳转。

2.  **遵循认知规律**：
    *   **从具体到抽象**：先展示一棵具体的二叉树，然后通过高亮和动画展示遍历过程。
    *   **分步与连贯结合**：提供“单步执行”让用户控制节奏，观察每一步细节；同时提供“连续播放”以形成整体流程观。
    *   **对比学习**：并排展示三种遍历的动画，突出相同树结构下访问顺序的差异。

3.  **交互设计**：
    *   **双重视角同步**：
        *   **树视图**：高亮当前节点，显示访问结果序列。
        *   **代码视图**：高亮当前正在执行的代码行（`visit`， `traverse(left)`， `traverse(right)`）。
        *   **栈视图**：可视化递归调用栈，显示每个栈帧对应的节点和返回地址（即将执行的动作：V， L， R）。
    *   **进程控制**：提供播放/暂停、下一步、上一步、重置控件。
    *   **模式选择**：允许用户单独学习一种遍历，或并排对比三种遍历。

4.  **视觉呈现**：
    *   **树结构**：节点清晰，连线分明。当前节点用醒目的颜色（如橙色）高亮。
    *   **状态编码**：
        *   **已访问**：节点变为另一种颜色（如绿色）并伴随“已访问”标记。
        *   **访问序列**：在独立区域动态添加节点值，形成访问顺序列表。
    *   **指针/执行位置**：在树视图上，用一个明显的指示器（如三角形箭头）指向“当前节点”。在代码视图，高亮当前行。
    *   **递归栈**：用堆叠的方块表示栈帧，从上到下模拟栈的增长与收缩。每个方块内写明节点值和待执行动作。

#### 配色方案选择
*   **背景与画布**：浅灰色（`#f5f5f5`）或白色背景，确保清晰度。
*   **二叉树**：
    *   节点默认：白色填充，深灰色边框（`#333`），黑色文字。
    *   当前节点：橙色填充（`#FFA726`），强调醒目。
    *   已访问节点：浅绿色填充（`#C8E6C9`），表示完成状态。
*   **代码高亮**：当前执行行用浅橙色背景（`#FFF3E0`）高亮。
*   **递归栈**：
    *   栈帧：不同深浅的蓝色系（如 `#E3F2FD`, `#BBDEFB`, `#90CAF9`），表示层级。
    *   文字：深蓝色（`#1565C0`）。
*   **访问序列**：中性深灰色（`#424242`）区域，文字黑色。
*   **按钮与控件**：采用扁平化设计，主色调蓝色（`#2196F3`），悬停时加深。
*   **对比模式边框**：为三种遍历的视图区域添加细微的边框色（如前序浅红、中序浅蓝、后序浅紫）以示区分。

#### 交互功能列表
1.  **树结构控制**：
    *   预设二叉树示例选择器（如：完整二叉树、斜树、普通树）。
    *   （可选）简单的手动构建/编辑树节点功能。
2.  **遍历模式选择**：
    *   单选按钮：前序、中序、后序。
    *   “对比模式”复选框：开启后，并排显示三种遍历的动画。
3.  **动画控制面板**：
    *   `开始 / 暂停` 按钮。
    *   `下一步` 按钮：单步执行下一个动作（访问、进入左递归、进入右递归、返回）。
    *   `上一步` 按钮：回退到上一个状态。
    *   `重置` 按钮：恢复到初始状态。
    *   动画速度滑块。
4.  **同步视图显示**：
    *   **主树视图**：动态高亮节点，显示指针。
    *   **代码面板**：根据所选遍历类型显示对应伪代码，并高亮执行行。
    *   **递归栈面板**：动态展示调用栈的压栈与弹栈过程。
    *   **访问序列面板**：实时显示已访问的节点值序列。
5.  **状态提示**：在控制面板附近用文字简要描述当前执行的动作（例如：“访问节点 A”、“递归调用进入左子树 B”、“从节点 C 返回”）。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>二叉树遍历递归过程可视化</title>
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
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #2196F3;
        }

        h1 {
            color: #1565C0;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .main-content {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .control-panel {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            align-items: center;
        }

        .control-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .control-group h3 {
            color: #2196F3;
            font-size: 1em;
            margin-bottom: 5px;
        }

        .tree-selector, .traversal-selector {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 8px 16px;
            background-color: #E3F2FD;
            border: 1px solid #BBDEFB;
            border-radius: 6px;
            cursor: pointer;
            color: #1565C0;
            font-weight: 500;
            transition: all 0.2s;
        }

        .btn:hover {
            background-color: #BBDEFB;
            transform: translateY(-2px);
        }

        .btn.active {
            background-color: #2196F3;
            color: white;
            border-color: #1976D2;
        }

        .animation-controls {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .speed-control {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .speed-slider {
            width: 120px;
        }

        .status-display {
            background-color: #FFF3E0;
            padding: 12px 20px;
            border-radius: 8px;
            border-left: 4px solid #FFA726;
            font-weight: 500;
            color: #333;
            min-height: 50px;
            display: flex;
            align-items: center;
        }

        .visualization-area {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }

        .tree-section {
            flex: 1;
            min-width: 300px;
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            display: flex;
            flex-direction: column;
        }

        .tree-section h2 {
            color: #2196F3;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #E0E0E0;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .tree-section h2 .color-indicator {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }

        .preorder .color-indicator { background-color: #FFCDD2; }
        .inorder .color-indicator { background-color: #C8E6C9; }
        .postorder .color-indicator { background-color: #BBDEFB; }

        .tree-container {
            flex: 1;
            position: relative;
            min-height: 300px;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            overflow: auto;
            background-color: #fafafa;
        }

        .code-container, .stack-container, .sequence-container {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
            border: 1px solid #E0E0E0;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
            line-height: 1.5;
            overflow: auto;
        }

        .code-line {
            padding: 4px 8px;
            margin: 2px 0;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        .code-line.highlighted {
            background-color: #FFF3E0;
            font-weight: bold;
        }

        .stack-visualization {
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
            gap: 5px;
            min-height: 150px;
        }

        .stack-frame {
            background-color: #E3F2FD;
            border: 2px solid #BBDEFB;
            border-radius: 6px;
            padding: 10px 15px;
            width: 80%;
            text-align: center;
            font-weight: 500;
            color: #1565C0;
            transition: all 0.3s;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .stack-frame.active {
            background-color: #BBDEFB;
            border-color: #2196F3;
            transform: scale(1.05);
        }

        .sequence-visualization {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            min-height: 60px;
        }

        .sequence-node {
            background-color: #C8E6C9;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #2E7D32;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.3s;
        }

        .sequence-node.new {
            background-color: #81C784;
            transform: scale(1.1);
        }

        .legend {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9em;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }

        .node-default { background-color: white; border: 2px solid #333; }
        .node-current { background-color: #FFA726; }
        .node-visited { background-color: #C8E6C9; }

        @media (max-width: 1200px) {
            .visualization-area {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🌳 二叉树遍历递归过程可视化</h1>
            <p class="subtitle">前序、中序、后序遍历的递归过程、指针移动与调用栈可视化</p>
        </header>

        <div class="main-content">
            <div class="control-panel">
                <div class="control-group">
                    <h3>二叉树结构</h3>
                    <div class="tree-selector">
                        <button class="btn active" data-tree="balanced">平衡二叉树</button>
                        <button class="btn" data-tree="left-skewed">左斜树</button>
                        <button class="btn" data-tree="right-skewed">右斜树</button>
                        <button class="btn" data-tree="custom">普通二叉树</button>
                    </div>
                </div>

                <div class="control-group">
                    <h3>遍历模式</h3>
                    <div class="traversal-selector">
                        <button class="btn active" data-traversal="preorder">前序遍历 (V→L→R)</button>
                        <button class="btn" data-traversal="inorder">中序遍历 (L→V→R)</button>
                        <button class="btn" data-traversal="postorder">后序遍历 (L→R→V)</button>
                        <label style="display: flex; align-items: center; gap: 8px; margin-left: 10px;">
                            <input type="checkbox" id="compare-mode"> 对比模式
                        </label>
                    </div>
                </div>

                <div class="control-group animation-controls">
                    <h3>动画控制</h3>
                    <div style="display: flex; gap: 10px;">
                        <button class="btn" id="start-pause">▶️ 开始</button>
                        <button class="btn" id="next-step">⏭️ 下一步</button>
                        <button class="btn" id="prev-step">⏮️ 上一步</button>
                        <button class="btn" id="reset">🔄 重置</button>
                    </div>
                    <div class="speed-control">
                        <span>速度:</span>
                        <input type="range" min="1" max="10" value="5" class="speed-slider" id="speed-slider">
                        <span id="speed-value">中速</span>
                    </div>
                </div>
            </div>

            <div class="status-display" id="status-display">
                请选择遍历模式并点击"开始"按钮启动动画。
            </div>

            <div class="visualization-area" id="visualization-area">
                <!-- 前序遍历视图 -->
                <div class="tree-section preorder" id="preorder-section">
                    <h2><span class="color-indicator"></span>前序遍历 (V→L→R)</h2>
                    <div class="tree-container" id="preorder-tree">
                        <canvas id="preorder-canvas" width="600" height="300"></canvas>
                    </div>
                    <div class="code-container" id="preorder-code">
                        <div class="code-line">function preorder(node) {</div>
                        <div class="code-line">    if (node == null) return;</div>
                        <div class="code-line">    visit(node);           // V</div>
                        <div class="code-line">    preorder(node.left);  // L</div>
                        <div class="code-line">    preorder(node.right); // R</div>
                        <div class="code-line">}</div>
                    </div>
                    <div class="stack-container">
                        <h3>递归调用栈</h3>
                        <div class="stack-visualization" id="preorder-stack"></div>
                    </div>
                    <div class="sequence-container">
                        <h3>访问序列</h3>
                        <div class="sequence-visualization" id="preorder-sequence"></div>
                    </div>
                </div>

                <!-- 中序遍历视图 -->
                <div class="tree-section inorder" id="inorder-section" style="display: none;">
                    <h2><span class="color-indicator"></span>中序遍历 (L→V→R)</h2>
                    <div class="tree-container" id="inorder-tree">
                        <canvas id="inorder-canvas" width="600" height="300"></canvas>
                    </div>
                    <div class="code-container" id="inorder-code">
                        <div class="code-line">function inorder(node) {</div>
                        <div class="code-line">    if (node == null) return;</div>
                        <div class="code-line">    inorder(node.left);   // L</div>
                        <div class="code-line">    visit(node);          // V</div>
                        <div class="code-line">    inorder(node.right);  // R</div>
                        <div class="code-line">}</div>
                    </div>
                    <div class="stack-container">
                        <h3>递归调用栈</h3>
                        <div class="stack-visualization" id="inorder-stack"></div>
                    </div>
                    <div class="sequence-container">
                        <h3>访问序列</h3>
                        <div class="sequence-visualization" id="inorder-sequence"></div>
                    </div>
                </div>

                <!-- 后序遍历视图 -->
                <div class="tree-section postorder" id="postorder-section" style="display: none;">
                    <h2><span class="color-indicator"></span>后序遍历 (L→R→V)</h2>
                    <div class="tree-container" id="postorder-tree">
                        <canvas id="postorder-canvas" width="600" height="300"></canvas>
                    </div>
                    <div class="code-container" id="postorder-code">
                        <div class="code-line">function postorder(node) {</div>
                        <div class="code-line">    if (node == null) return;</div>
                        <div class="code-line">    postorder(node.left);  // L</div>
                        <div class="code-line">    postorder(node.right); // R</div>
                        <div class="code-line">    visit(node);           // V</div>
                        <div class="code-line">}</div>
                    </div>
                    <div class="stack-container">
                        <h3>递归调用栈</h3>
                        <div class="stack-visualization" id="postorder-stack"></div>
                    </div>
                    <div class="sequence-container">
                        <h3>访问序列</h3>
                        <div class="sequence-visualization" id="postorder-sequence"></div>
                    </div>
                </div>
            </div>

            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color node-default"></div>
                    <span>未访问节点</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color node-current"></div>
                    <span>当前节点</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color node-visited"></div>
                    <span>已访问节点</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #FFF3E0;"></div>
                    <span>当前执行代码行</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #BBDEFB;"></div>
                    <span>活动栈帧</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 二叉树节点类
        class TreeNode {
            constructor(value, x, y) {
                this.value = value;
                this.left = null;
                this.right = null;
                this.x = x;
                this.y = y;
                this.radius = 25;
                this.state = 'default'; // 'default', 'current', 'visited'
            }
        }

        // 遍历状态类
        class TraversalState {
            constructor(type) {
                this.type = type; // 'preorder', 'inorder', 'postorder'
                this.currentNode = null;
                this.callStack = [];
                this.visitedSequence = [];
                this.isAnimating = false;
                this.speed = 500; // 毫秒
                this.stepIndex = 0;
                this.traversalSteps = [];
                this.codeLines = [];
                this.initCodeLines();
            }

            initCodeLines() {
                if (this.type === 'preorder') {
                    this.codeLines = [2, 3, 4, 5, 6];
                } else if (this.type === 'inorder') {
                    this.codeLines = [2, 3, 4, 5, 6];
                } else if (this.type === 'postorder') {
                    this.codeLines = [2, 3, 4, 5, 6];
                }
            }

            reset() {
                this.currentNode = null;
                this.callStack = [];
                this.visitedSequence = [];
                this.isAnimating = false;
                this.stepIndex = 0;
                this.traversalSteps = [];
            }

            generateSteps(node) {
                this.traversalSteps = [];
                this._generateStepsRecursive(node, []);
                return this.traversalSteps;
            }

            _generateStepsRecursive(node, stack) {
                if (!node) {
                    this.traversalSteps.push({
                        action: 'return',
                        node: null,
                        stack: [...stack],
                        codeLine: 2
                    });
                    return;
                }

                // 根据遍历类型生成不同的步骤序列
                if (this.type === 'preorder') {
                    // 前序: V -> L -> R
                    this.traversalSteps.push({
                        action: 'enter',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'V'}],
                        codeLine: 2
                    });
                    
                    this.traversalSteps.push({
                        action: 'visit',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'L'}],
                        codeLine: 3
                    });
                    
                    this._generateStepsRecursive(node.left, [...stack, {node: node, nextAction: 'R'}]);
                    
                    this.traversalSteps.push({
                        action: 'enter_right',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'R'}],
                        codeLine: 5
                    });
                    
                    this._generateStepsRecursive(node.right, [...stack]);
                    
                    this.traversalSteps.push({
                        action: 'return',
                        node: node,
                        stack: [...stack],
                        codeLine: 6
                    });
                } else if (this.type === 'inorder') {
                    // 中序: L -> V -> R
                    this.traversalSteps.push({
                        action: 'enter',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'L'}],
                        codeLine: 2
                    });
                    
                    this._generateStepsRecursive(node.left, [...stack, {node: node, nextAction: 'V'}]);
                    
                    this.traversalSteps.push({
                        action: 'visit',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'R'}],
                        codeLine: 4
                    });
                    
                    this.traversalSteps.push({
                        action: 'enter_right',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'R'}],
                        codeLine: 5
                    });
                    
                    this._generateStepsRecursive(node.right, [...stack]);
                    
                    this.traversalSteps.push({
                        action: 'return',
                        node: node,
                        stack: [...stack],
                        codeLine: 6
                    });
                } else if (this.type === 'postorder') {
                    // 后序: L -> R -> V
                    this.traversalSteps.push({
                        action: 'enter',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'L'}],
                        codeLine: 2
                    });
                    
                    this._generateStepsRecursive(node.left, [...stack, {node: node, nextAction: 'R'}]);
                    
                    this.traversalSteps.push({
                        action: 'enter_right',
                        node: node,
                        stack: [...stack, {node: node, nextAction: 'R'}],
                        codeLine: 4
                    });
                    
                    this._generateStepsRecursive(node.right, [...stack, {node: node, nextAction: 'V'}]);
                    
                    this.traversalSteps.push({
                        action: 'visit',
                        node: node,
                        stack: [...stack],
                        codeLine: 5
                    });
                    
                    this.traversalSteps.push({
                        action: 'return',
                        node: node,
                        stack: [...stack],
                        codeLine: 6
                    });
                }
            }

            getCurrentStep() {
                if (this.stepIndex < this.traversalSteps.length) {
                    return this.traversalSteps[this.stepIndex];
                }
                return null;
            }

            nextStep() {
                if (this.stepIndex < this.traversalSteps.length) {
                    const step = this.traversalSteps[this.stepIndex];
                    this.stepIndex++;
                    
                    // 更新状态
                    if (step.action === 'visit') {
                        this.visitedSequence.push(step.node.value);
                        step.node.state = 'visited';
                    } else if (step.action === 'enter' || step.action === 'enter_right') {
                        this.currentNode = step.node;
                        step.node.state = 'current';
                    } else if (step.action === 'return') {
                        if (this.currentNode) {
                            this.currentNode.state = 'visited';
                        }
                        this.currentNode = null;
                    }
                    
                    this.callStack = step.stack;
                    return step;
                }
                return null;
            }

            prevStep() {
                if (this.stepIndex > 0) {
                    this.stepIndex--;
                    const step = this.traversalSteps[this.stepIndex];
                    
                    // 回退状态
                    if (step.action === 'visit') {
                        this.visitedSequence.pop();
                        step.node.state = 'default';
                    } else if (step.action === 'enter' || step.action === 'enter_right') {
                        step.node.state = 'default';
                        this.currentNode = null;
                    } else if (step.action === 'return') {
                        // 查找前一个节点
                        if (this.stepIndex > 0) {
                            const prevStep = this.traversalSteps[this.stepIndex - 1];
                            if (prevStep.node) {
                                this.currentNode = prevStep.node;
                                this.currentNode.state = 'current';
                            }
                        }
                    }
                    
                    // 更新调用栈
                    if (this.stepIndex > 0) {
                        this.callStack = this.traversalSteps[this.stepIndex - 1].stack;
                    } else {
                        this.callStack = [];
                    }
                    
                    return step;
                }
                return null;
            }
        }

        // 主应用类
        class BinaryTreeVisualizer {
            constructor() {
                this.treeRoot = null;
                this.traversalStates = {
                    preorder: new TraversalState('preorder'),
                    inorder: new TraversalState('inorder'),
                    postorder: new TraversalState('postorder')
                };
                this.currentTraversal = 'preorder';
                this.compareMode = false;
                this.animationInterval = null;
                this.speed = 5;
                
                this.initTree();
                this.initEventListeners();
                this.render();
            }

            initTree() {
                // 创建平衡二叉树
                this.createBalancedTree();
            }

            createBalancedTree() {
                // 创建节点
                const root = new TreeNode('A', 300, 50);
                const b = new TreeNode('B', 200, 120);
                const c = new TreeNode('C', 400, 120);
                const d = new TreeNode('D', 150, 190);
                const e = new TreeNode('E', 250, 190);
                const f = new TreeNode('F', 350, 190);
                const g = new TreeNode('G', 450, 190);
                
                // 构建树结构
                root.left = b;
                root.right = c;
                b.left = d;
                b.right = e;
                c.left = f;
                c.right = g;
                
                this.treeRoot = root;
                this.resetAllTraversals();
            }

            createLeftSkewedTree() {
                const root = new TreeNode('A', 400, 50);
                const b = new TreeNode('B', 350, 120);
                const c = new TreeNode('C', 300, 190);
                const d = new TreeNode('D', 250, 260);
                
                root.left = b;
                b.left = c;
                c.left = d;
                
                this.treeRoot = root;
                this.resetAllTraversals();
            }

            createRightSkewedTree() {
                const root = new TreeNode('A', 200, 50);
                const b = new TreeNode('B', 250, 120);
                const c = new TreeNode('C', 300, 190);
                const d = new TreeNode('D', 350, 260);
                
                root.right = b;
                b.right = c;
                c.right = d;
                
                this.treeRoot = root;
                this.resetAllTraversals();
            }

            createCustomTree() {
                const root = new TreeNode('A', 300, 50);
                const b = new TreeNode('B', 200, 120);
                const c = new TreeNode('C', 400, 120);
                const d = new TreeNode('D', 150, 190);
                const e = new TreeNode('E', 350, 190);
                const f = new TreeNode('F', 450, 190);
                
                root.left = b;
                root.right = c;
                b.left = d;
                c.left = e;
                c.right = f;
                
                this.treeRoot = root;
                this.resetAllTraversals();
            }

            resetAllTraversals() {
                // 重置所有节点状态
                this.resetNodeStates(this.treeRoot);
                
                // 重置所有遍历状态
                Object.values(this.traversalStates).forEach(state => {
                    state.reset();
                    state.generateSteps(this.treeRoot);
                });
            }

            resetNodeStates(node) {
                if (!node) return;
                node.state = 'default';
                this.resetNodeStates(node.left);
                this.resetNodeStates(node.right);
            }

            initEventListeners() {
                // 树结构选择
                document.querySelectorAll('.tree-selector .btn').forEach(btn => {
                    btn.addEventListener('click', () => {
                        document.querySelectorAll('.tree-selector .btn').forEach(b => b.classList.remove('active'));
                        btn.classList.add('active');
                        
                        const treeType = btn.dataset.tree;
                        if (treeType === 'balanced') {
                            this.createBalancedTree();
                        } else if (treeType === 'left-skewed') {
                            this.createLeftSkewedTree();
                        } else if (treeType === 'right-skewed') {
                            this.createRightSkewedTree();
                        } else if (treeType === 'custom') {
                            this.createCustomTree();
                        }
                        
                        this.render();
                    });
                });

                // 遍历模式选择
                document.querySelectorAll('.traversal-selector .btn[data-traversal]').forEach(btn => {
                    btn.addEventListener('click', () => {
                        document.querySelectorAll('.traversal-selector .btn[data-traversal]').forEach(b => b.classList.remove('active'));
                        btn.classList.add('active');
                        
                        this.currentTraversal = btn.dataset.traversal;
                        this.updateViewVisibility();
                        this.render();
                    });
                });

                // 对比模式切换
                document.getElementById('compare-mode').addEventListener('change', (e) => {
                    this.compareMode = e.target.checked;
                    this.updateViewVisibility();
                    this.render();
                });

                // 动画控制
                document.getElementById('start-pause').addEventListener('click', () => {
                    this.toggleAnimation();
                });

                document.getElementById('next-step').addEventListener('click', () => {
                    this.stopAnimation();
                    this.nextStep();
                });

                document.getElementById('prev-step').addEventListener('click', () => {
                    this.stopAnimation();
                    this.prevStep();
                });

                document.getElementById('reset').addEventListener('click', () => {
                    this.stopAnimation();
                    this.resetAllTraversals();
                    this.render();
                });

                // 速度控制
                document.getElementById('speed-slider').addEventListener('input', (e) => {
                    this.speed = parseInt(e.target.value);
                    document.getElementById('speed-value').textContent = 
                        this.speed <= 3 ? '慢速' : this.speed <= 7 ? '中速' : '快速';
                    
                    if (this.animationInterval) {
                        this.stopAnimation();
                        this.startAnimation();
                    }
                });
            }

            updateViewVisibility() {
                const preorderSection = document.getElementById('preorder-section');
                const inorderSection = document.getElementById('inorder-section');
                const postorderSection = document.getElementById('postorder-section');
                const visualizationArea = document.getElementById('visualization-area');
                
                if (this.compareMode) {
                    // 对比模式：显示所有三个视图
                    preorderSection.style.display = 'flex';
                    inorderSection.style.display = 'flex';
                    postorderSection.style.display = 'flex';
                    visualizationArea.style.flexDirection = 'row';
                } else {
                    // 单视图模式：只显示当前选择的遍历
                    preorderSection.style.display = this.currentTraversal === 'preorder' ? 'flex' : 'none';
                    inorderSection.style.display = this.currentTraversal === 'inorder' ? 'flex' : 'none';
                    postorderSection.style.display = this.currentTraversal === 'postorder' ? 'flex' : 'none';
                    visualizationArea.style.flexDirection = 'column';
                }
            }

            toggleAnimation() {
                const btn = document.getElementById('start-pause');
                if (this.animationInterval) {
                    this.stopAnimation();
                    btn.innerHTML = '▶️ 继续';
                } else {
                    this.startAnimation();
                    btn.innerHTML = '⏸️ 暂停';
                }
            }

            startAnimation() {
                this.stopAnimation();
                
                const interval = 1100 - (this.speed * 100); // 速度映射：1=1000ms, 10=100ms
                this.animationInterval = setInterval(() => {
                    if (!this.nextStep()) {
                        this.stopAnimation();
                        document.getElementById('start-pause').innerHTML = '▶️ 开始';
                    }
                }, interval);
            }

            stopAnimation() {
                if (this.animationInterval) {
                    clearInterval(this.animationInterval);
                    this.animationInterval = null;
                }
            }

            nextStep() {
                let stepPerformed = false;
                
                if (this.compareMode) {
                    // 对比模式下，所有遍历同时前进
                    Object.values(this.traversalStates).forEach(state => {
                        if (state.nextStep()) {
                            stepPerformed = true;
                        }
                    });
                } else {
                    // 单视图模式下，只前进当前遍历
                    const state = this.traversalStates[this.currentTraversal];
                    if (state.nextStep()) {
                        stepPerformed = true;
                    }
                }
                
                if (stepPerformed) {
                    this.render();
                    this.updateStatus();
                }
                
                return stepPerformed;
            }

            prevStep() {
                let stepPerformed = false;
                
                if (this.compareMode) {
                    // 对比模式下，所有遍历同时回退
                    Object.values(this.traversalStates).forEach(state => {
                        if (state.prevStep()) {
                            stepPerformed = true;
                        }
                    });
                } else {
                    // 单视图模式下，只回退当前遍历
                    const state = this.traversalStates[this.currentTraversal];
                    if (state.prevStep()) {
                        stepPerformed = true;
                    }
                }
                
                if (stepPerformed) {
                    this.render();
                    this.updateStatus();
                }
            }

            updateStatus() {
                const statusDisplay = document.getElementById('status-display');
                let statusText = '';
                
                if (this.compareMode) {
                    statusText = '对比模式：三种遍历同步进行中...';
                } else {
                    const state = this.traversalStates[this.currentTraversal];
                    const step = state.getCurrentStep();
                    
                    if (step) {
                        const actionMap = {
                            'enter': '进入节点',
                            'visit': '访问节点',
                            'enter_right': '进入右子树',
                            'return': '返回'
                        };
                        
                        const nodeName = step.node ? step.node.value : 'null';
                        statusText = `${actionMap[step.action]} ${nodeName}`;
                        
                        if (step.action === 'visit') {
                            statusText += ` (已访问节点: ${state.visitedSequence.join(' → ')})`;
                        }
                    } else {
                        statusText = '遍历完成！';
                    }
                }
                
                statusDisplay.textContent = statusText;
            }

            drawTree(canvasId, traversalType) {
                const canvas = document.getElementById(canvasId);
                const ctx = canvas.getContext('2d');
                const state = this.traversalStates[traversalType];
                
                // 清除画布
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // 绘制树
                this.drawTreeRecursive(ctx, this.treeRoot, state);
                
                // 绘制当前节点指针
                if (state.currentNode) {
                    this.drawPointer(ctx, state.currentNode);
                }
            }

            drawTreeRecursive(ctx, node, state) {
                if (!node) return;
                
                // 绘制连线
                if (node.left) {
                    ctx.beginPath();
                    ctx.moveTo(node.x, node.y + node.radius);
                    ctx.lineTo(node.left.x, node.left.y - node.left.radius);
                    ctx.strokeStyle = '#666';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
                
                if (node.right) {
                    ctx.beginPath();
                    ctx.moveTo(node.x, node.y + node.radius);
                    ctx.lineTo(node.right.x, node.right.y - node.right.radius);
                    ctx.strokeStyle = '#666';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }
                
                // 绘制子节点
                this.drawTreeRecursive(ctx, node.left, state);
                this.drawTreeRecursive(ctx, node.right, state);
                
                // 绘制当前节点
                this.drawNode(ctx, node, state);
            }

            drawNode(ctx, node, state) {
                // 设置节点颜色
                let fillColor = '#FFFFFF';
                if (node.state === 'current') {
                    fillColor = '#FFA726';
                } else if (node.state === 'visited') {
                    fillColor = '#C8E6C9';
                }
                
                // 绘制节点圆
                ctx.beginPath();
                ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
                ctx.fillStyle = fillColor;
                ctx.fill();
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // 绘制节点值
                ctx.fillStyle = '#000';
                ctx.font = 'bold 16px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(node.value, node.x, node.y);
            }

            drawPointer(ctx, node) {
                // 绘制指向当前节点的三角形指针
                ctx.beginPath();
                ctx.moveTo(node.x, node.y - node.radius - 15);
                ctx.lineTo(node.x - 10, node.y - node.radius - 5);
                ctx.lineTo(node.x + 10, node.y - node.radius - 5);
                ctx.closePath();
                ctx.fillStyle = '#FF5722';
                ctx.fill();
                
                // 添加指针动画效果
                ctx.beginPath();
                ctx.arc(node.x, node.y - node.radius - 10, 3, 0, Math.PI * 2);
                ctx.fillStyle = '#FFF';
                ctx.fill();
            }

            updateCodeHighlight(traversalType) {
                const state = this.traversalStates[traversalType];
                const step = state.getCurrentStep();
                const codeContainer = document.getElementById(`${traversalType}-code`);
                
                // 清除所有高亮
                codeContainer.querySelectorAll('.code-line').forEach(line => {
                    line.classList.remove('highlighted');
                });
                
                // 高亮当前代码行
                if (step && step.codeLine
) {
                    const lines = codeContainer.querySelectorAll('.code-line');
                    if (step.codeLine - 1 < lines.length) {
                        lines[step.codeLine - 1].classList.add('highlighted');
                    }
                }
            }

            updateStackVisualization(traversalType) {
                const state = this.traversalStates[traversalType];
                const stackContainer = document.getElementById(`${traversalType}-stack`);
                
                // 清空栈显示
                stackContainer.innerHTML = '';
                
                // 显示栈帧（从栈底到栈顶）
                const stackFrames = [...state.callStack].reverse();
                
                stackFrames.forEach((frame, index) => {
                    const frameElement = document.createElement('div');
                    frameElement.className = 'stack-frame';
                    
                    // 最后一个栈帧是活动的
                    if (index === 0) {
                        frameElement.classList.add('active');
                    }
                    
                    frameElement.textContent = `${frame.node.value} (下一步: ${frame.nextAction})`;
                    stackContainer.appendChild(frameElement);
                });
                
                // 如果栈为空，显示提示
                if (stackFrames.length === 0) {
                    const emptyFrame = document.createElement('div');
                    emptyFrame.className = 'stack-frame';
                    emptyFrame.textContent = '调用栈为空';
                    stackContainer.appendChild(emptyFrame);
                }
            }

            updateSequenceVisualization(traversalType) {
                const state = this.traversalStates[traversalType];
                const sequenceContainer = document.getElementById(`${traversalType}-sequence`);
                
                // 清空序列显示
                sequenceContainer.innerHTML = '';
                
                // 显示访问序列
                state.visitedSequence.forEach((value, index) => {
                    const nodeElement = document.createElement('div');
                    nodeElement.className = 'sequence-node';
                    
                    // 最后一个节点是新访问的
                    if (index === state.visitedSequence.length - 1) {
                        nodeElement.classList.add('new');
                    }
                    
                    nodeElement.textContent = value;
                    sequenceContainer.appendChild(nodeElement);
                    
                    // 添加箭头（除了最后一个）
                    if (index < state.visitedSequence.length - 1) {
                        const arrow = document.createElement('span');
                        arrow.textContent = '→';
                        arrow.style.color = '#666';
                        arrow.style.margin = '0 5px';
                        sequenceContainer.appendChild(arrow);
                    }
                });
                
                // 如果序列为空，显示提示
                if (state.visitedSequence.length === 0) {
                    const emptyText = document.createElement('div');
                    emptyText.textContent = '尚未访问任何节点';
                    emptyText.style.color = '#999';
                    emptyText.style.fontStyle = 'italic';
                    sequenceContainer.appendChild(emptyText);
                }
            }

            render() {
                // 更新所有视图
                const traversals = this.compareMode ? 
                    ['preorder', 'inorder', 'postorder'] : 
                    [this.currentTraversal];
                
                traversals.forEach(traversalType => {
                    // 绘制树
                    this.drawTree(`${traversalType}-canvas`, traversalType);
                    
                    // 更新代码高亮
                    this.updateCodeHighlight(traversalType);
                    
                    // 更新栈可视化
                    this.updateStackVisualization(traversalType);
                    
                    // 更新序列可视化
                    this.updateSequenceVisualization(traversalType);
                });
                
                // 更新状态显示
                this.updateStatus();
            }
        }

        // 页面加载完成后初始化应用
        document.addEventListener('DOMContentLoaded', () => {
            const visualizer = new BinaryTreeVisualizer();
            
            // 初始渲染
            visualizer.render();
            
            // 将visualizer暴露给全局，便于调试
            window.visualizer = visualizer;
        });
    </script>
</body>
</html>


### 3. 过程输出

### 3. 使用指南

## 🌳 二叉树遍历递归过程可视化 - 交互式教学动画使用指南

欢迎使用“二叉树遍历递归过程可视化”教学动画！本工具旨在通过直观、动态的方式，帮助您深入理解二叉树前序、中序、后序遍历的递归过程、指针移动与调用栈机制。

---

### 📋 功能说明

本动画将抽象的递归遍历过程分解为可视化的四个核心组件：
1. **树结构视图**：实时显示二叉树，动态高亮当前节点
2. **代码执行视图**：同步高亮正在执行的代码行
3. **递归调用栈视图**：可视化展示递归调用的压栈与弹栈过程
4. **访问序列视图**：实时记录并显示节点访问顺序

### 🎯 主要功能

#### 1. **树结构选择**
- **平衡二叉树**：标准对称结构，适合基础学习
- **左斜树**：所有节点只有左子树，展示极端情况
- **右斜树**：所有节点只有右子树，展示极端情况
- **普通二叉树**：非对称结构，模拟实际应用场景

#### 2. **遍历模式**
- **前序遍历 (V→L→R)**：先访问根节点，再遍历左右子树
- **中序遍历 (L→V→R)**：先遍历左子树，再访问根节点，最后遍历右子树
- **后序遍历 (L→R→V)**：先遍历左右子树，最后访问根节点
- **对比模式**：同时展示三种遍历过程，直观比较差异

#### 3. **动画控制**
- **开始/暂停**：启动或暂停动画播放
- **下一步**：单步执行下一个动作（进入节点、访问节点、进入右子树、返回）
- **上一步**：回退到上一个状态
- **重置**：恢复到初始状态
- **速度调节**：从慢速到快速（1-10档）

### ✨ 设计特色

#### 1. **双重视角同步**
- **视觉同步**：树视图中的节点高亮与代码视图中的行高亮完全同步
- **状态同步**：当前节点、调用栈、访问序列三者状态实时一致

#### 2. **递归过程透明化**
- **调用栈可视化**：将隐式的系统调用栈显式展示为堆叠的方块
- **执行状态标记**：每个栈帧显示“下一步动作”（V/L/R），明确程序执行位置

#### 3. **认知友好的视觉编码**
- **颜色语义化**：
  - 🟠 橙色：当前节点（正在处理）
  - 🟢 浅绿：已访问节点（已完成）
  - ⬜ 白色：未访问节点（待处理）
  - 🟦 蓝色高亮：活动栈帧
  - 🟡 浅黄高亮：当前执行代码行

#### 4. **灵活的学习模式**
- **单步学习模式**：适合初次学习者，可控制节奏仔细观察每一步
- **连续播放模式**：适合复习巩固，形成整体流程认知
- **对比学习模式**：适合深入理解三种遍历的本质差异

### 🧠 教学要点

#### 核心概念解析
1. **递归的本质**：每次递归调用对应一个栈帧的压入，返回对应栈帧的弹出
2. **三种遍历的区别**：
   - **前序**：到达节点立即访问（V在L、R之前）
   - **中序**：从左子树返回后访问（V在L之后、R之前）
   - **后序**：从右子树返回后访问（V在L、R之后）
3. **“指针”的含义**：动画中的“指针”代表当前递归调用关注的节点，即程序执行流的位置

#### 关键观察点
1. **栈帧生命周期**：注意栈帧何时压入（进入递归）、何时弹出（返回）
2. **节点状态转换**：观察节点如何从“未访问”→“当前”→“已访问”
3. **代码执行顺序**：对照代码高亮，理解不同遍历的执行路径差异
4. **访问序列生成**：注意访问序列与节点访问动作的对应关系

### 💡 使用建议

#### 学习路径建议
1. **第一阶段：基础认知**
   - 选择“平衡二叉树”和“前序遍历”
   - 使用“单步模式”，仔细观察每一步的变化
   - 重点关注：节点状态变化、调用栈变化、代码执行位置

2. **第二阶段：对比理解**
   - 开启“对比模式”，观察三种遍历的差异
   - 注意相同节点在不同遍历中的访问时机
   - 思考：为什么访问顺序不同？代码差异在哪里？

3. **第三阶段：深入探究**
   - 尝试不同的树结构（特别是斜树）
   - 观察极端情况下的遍历过程
   - 思考：树的结构如何影响遍历效率？

4. **第四阶段：自我测试**
   - 关闭动画，手动推导遍历序列
   - 再用动画验证自己的推导
   - 尝试解释每一步的栈状态变化

#### 教学应用建议
- **课堂演示**：使用“连续播放”模式进行整体流程演示
- **小组讨论**：使用“单步模式”，在关键步骤暂停，引导学生预测下一步
- **课后练习**：让学生使用不同树结构和遍历模式，记录观察结果
- **概念强化**：重点讲解“对比模式”下的差异，强化三种遍历的本质区别

#### 调试与探索
- 如果对某一步不理解，使用“上一步”功能回退重新观察
- 调整动画速度，找到最适合自己认知节奏的速度
- 在不同树结构间切换，观察相同遍历算法在不同结构上的表现

---

### 🚀 开始探索吧！

现在，您已经掌握了本教学动画的所有功能。建议您：

1. 从“平衡二叉树”和“前序遍历”开始
2. 点击“下一步”按钮，仔细观察每一步的变化
3. 当您熟悉基本流程后，尝试其他树结构和遍历模式
4. 最后开启“对比模式”，体验三种遍历的同步展示

通过这个交互式动画，您将能够：
- ✅ 直观理解递归遍历的执行过程
- ✅ 清晰分辨三种遍历的本质差异
- ✅ 掌握调用栈在递归中的作用
- ✅ 建立二叉树遍历的完整心智模型

祝您学习愉快，探索成功！ 🌟

> **提示**：本工具完全在浏览器中运行，无需安装任何插件。建议使用Chrome、Firefox或Edge等现代浏览器以获得最佳体验。