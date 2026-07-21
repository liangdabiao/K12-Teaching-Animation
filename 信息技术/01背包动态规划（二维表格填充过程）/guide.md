# 需求：01背包动态规划（二维表格填充过程）

### 1. 专业思考


#### 用户需求分析
目标用户是学习算法设计与分析、数据结构或准备技术面试的学生和开发者。他们对动态规划的基本概念有一定了解，但可能对“01背包”问题的状态转移和表格填充过程感到抽象和困惑。

*   **核心痛点**：
    1.  **过程抽象**：难以将递推公式 `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])` 与二维表格中每个单元格的填充过程直观对应。
    2.  **状态依赖不清晰**：不理解为什么当前单元格 `dp[i][j]` 的值只依赖于其“正上方”和“左上方”的单元格。
    3.  **最优子结构理解困难**：无法可视化“选择”与“不选择”当前物品时，如何利用之前子问题的解来构造当前最优解。
    4.  **缺乏主动探索**：被动观看静态图表或代码，无法通过交互来验证自己的理解或观察不同输入下的动态过程。

*   **核心需求**：用户需要一个**可视化、可交互、分步演示**的工具，将抽象的递推过程转化为具象的、有因果联系的动画，从而内化01背包动态规划的核心思想。

#### 教学设计思路（核心概念、认知规律、交互设计、视觉呈现）

1.  **核心概念聚焦**：
    *   **状态定义**：`dp[i][j]` 表示“考虑前 `i` 件物品，在背包容量为 `j` 时所能获得的最大价值”。
    *   **状态转移**：对于每个物品（第 `i` 个），在每种容量（`j`）下，做出“不放入”或“放入”的决策，并选取价值最大者。
    *   **表格填充顺序**：强调自底向上、从左到右、逐行（或逐列）的填充逻辑，体现动态规划的“填表”特性。

2.  **遵循认知规律**：
    *   **从具体到抽象**：先展示一个具体的背包问题实例（例如：4件物品，背包容量为8），用动画演示完整填充过程，再引导用户总结出通用公式。
    *   **分步分解**：将一次完整的填充分解为多个可暂停、可回退的“原子步骤”：`高亮当前待填单元格` -> `计算“不放入”选项的值（查看上方单元格）` -> `计算“放入”选项的值（查看左上方单元格并计算）` -> `比较并确定最大值` -> `填入结果并显示决策`。
    *   **突出焦点与关联**：在每一步，通过高亮、箭头、连线等视觉手段，清晰指示“当前计算单元格”与它所依赖的“上方”和“左上方”单元格之间的关系。

3.  **交互设计**：
    *   **控制层**：提供明确的播放控制（播放/暂停、上一步/下一步、重置）和速度调节。
    *   **探索层**：
        *   允许用户点击表格中的任意**已填充**单元格，回溯展示该单元格值是如何计算出来的（即重现其决策过程）。
        *   允许用户修改问题实例（物品数量、容量、单个物品的重量和价值），然后重新运行动画，观察表格变化，深化理解。
    *   **反馈层**：在动画过程中，在表格旁或下方用清晰的文字描述当前步骤在发生什么（例如：“正在计算`dp[2][5]`：比较不放入物品2的价值`dp[1][5]=6`，与放入物品2的价值`dp[1][5-3]+4=0+4=4`，最大值为6，因此`dp[2][5]=6`”）。

4.  **视觉呈现**：
    *   **主场景**：一个大型的、清晰的二维表格占据视觉中心。行代表物品（`i`，0到n），列代表背包容量（`j`，0到C）。第0行和第0列作为基础情况（值为0）预先填充。
    *   **视觉编码**：
        *   **当前焦点单元格**：用醒目的彩色边框（如亮蓝色）高亮。
        *   **依赖单元格**（上方和左上方）：用不同的颜色（如浅灰色）高亮，并用箭头从它们指向当前单元格。
        *   **决策路径**：“不放入”选项的箭头用一种颜色（如橙色），“放入”选项用另一种颜色（如绿色）。最终选择的决策路径可以更粗或闪烁强调。
        *   **单元格内部**：显示最终的最大价值数值。可以考虑在角落用小图标或颜色块表示该单元格的决策（例如：↑ 代表不放入，↖ 代表放入）。
    *   **辅助信息面板**：
        *   **物品列表**：以一个小表格形式列出所有物品的编号、重量、价值。
        *   **状态说明区**：用文字动态描述当前计算步骤。
        *   **控制面板**：放置所有交互控件。

#### 配色方案选择
*   **主色调**：选择一种专业、清晰、对视力友好的配色。例如，使用深蓝色（`#2c3e50`）作为背景或标题色，白色（`#ffffff`）作为表格背景。
*   **功能色**：
    *   **当前单元格**：亮蓝色边框（`#3498db`）。
    *   **依赖单元格（参考单元格）**：浅灰色背景（`#ecf0f1`）。
    *   **“不放入”决策路径/箭头**：温和的橙色（`#e67e22`）。
    *   **“放入”决策路径/箭头**：清新的绿色（`#2ecc71`）。
    *   **最终最优解追踪**：醒目的黄色高亮（`#f1c40f`），用于在表格填充完成后，从右下角回溯到左上角，标记出被选中的物品。
*   **文字色**：主要文字使用深灰色（`#2c3e50`），说明文字使用中灰色（`#7f8c8d`）。
*   **原则**：确保颜色对比度符合可访问性标准，且颜色使用一致，符合用户的心智模型。

#### 交互功能列表
1.  **动画控制**：
    *   `开始 / 暂停`：开始或暂停自动播放填充动画。
    *   `下一步`：手动前进到下一个计算步骤（一个单元格的完整决策过程或一个子步骤）。
    *   `上一步`：回退到上一个步骤。
    *   `重置`：清空表格（除第0行/列），回到初始状态。
    *   `动画速度调节滑块`：控制自动播放的速度。
2.  **实例配置**（可选但推荐）：
    *   `物品数量`输入框。
    *   `背包容量`输入框。
    *   `物品重量/价值`输入表格（可编辑）。
    *   `应用新实例`按钮：根据新输入重新初始化并开始动画。
3.  **表格交互**：
    *   `单元格点击探查`：点击任意已填充的单元格，触发一个“回溯”动画，展示该单元格值的来源和计算过程。
4.  **视图与信息**：
    *   `显示/隐藏决策路径`：切换是否显示箭头。
    *   `显示/隐藏详细计算过程`：在状态说明区显示或隐藏每一步的详细计算文本。
    *   `高亮最优解路径`：在表格填充完成后，提供一个按钮，用于高亮显示从`dp[n][C]`回溯到`dp[0][0]`的路径，直观展示哪些物品被最终选中。
5.  **响应式布局**：确保动画在桌面和较大平板设备上均有良好的显示效果。

### 2. HTML_CODE


```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01背包动态规划 - 二维表格填充过程可视化</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #2c3e50;
            line-height: 1.6;
            padding: 20px;
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #3498db;
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 2.2rem;
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

        .left-panel {
            flex: 1;
            min-width: 300px;
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        }

        .right-panel {
            flex: 2;
            min-width: 500px;
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        }

        .panel-title {
            color: #3498db;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ecf0f1;
            font-size: 1.4rem;
        }

        .problem-config {
            margin-bottom: 25px;
        }

        .config-item {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #2c3e50;
        }

        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #3498db;
        }

        .items-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        .items-table th, .items-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }

        .items-table th {
            background-color: #f2f6fa;
            font-weight: 600;
        }

        .items-table input {
            width: 80px;
            text-align: center;
            padding: 5px;
        }

        .control-panel {
            margin-top: 30px;
        }

        .control-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-primary {
            background-color: #3498db;
            color: white;
        }

        .btn-primary:hover {
            background-color: #2980b9;
        }

        .btn-secondary {
            background-color: #2ecc71;
            color: white;
        }

        .btn-secondary:hover {
            background-color: #27ae60;
        }

        .btn-warning {
            background-color: #e67e22;
            color: white;
        }

        .btn-warning:hover {
            background-color: #d35400;
        }

        .btn-danger {
            background-color: #e74c3c;
            color: white;
        }

        .btn-danger:hover {
            background-color: #c0392b;
        }

        .speed-control {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-top: 15px;
        }

        .speed-slider {
            flex: 1;
        }

        .visualization-container {
            position: relative;
            width: 100%;
            height: 500px;
            border: 1px solid #ecf0f1;
            border-radius: 5px;
            overflow: auto;
            background-color: white;
        }

        #animationCanvas {
            display: block;
        }

        .status-panel {
            margin-top: 25px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }

        .status-title {
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }

        #statusText {
            min-height: 80px;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            border: 1px solid #ecf0f1;
            font-size: 1rem;
            line-height: 1.5;
            color: #2c3e50;
        }

        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #ecf0f1;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 3px;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        @media (max-width: 1100px) {
            .container {
                flex-direction: column;
            }
            
            .left-panel, .right-panel {
                min-width: 100%;
            }
            
            .visualization-container {
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>01背包动态规划 - 二维表格填充过程可视化</h1>
        <p class="subtitle">通过交互式动画理解状态转移方程与表格填充过程</p>
    </div>

    <div class="container">
        <div class="left-panel">
            <h2 class="panel-title">问题配置</h2>
            
            <div class="problem-config">
                <div class="config-item">
                    <label for="capacity">背包容量 (C):</label>
                    <input type="number" id="capacity" min="1" max="20" value="8">
                </div>
                
                <div class="config-item">
                    <label for="itemCount">物品数量 (n):</label>
                    <input type="number" id="itemCount" min="1" max="8" value="4">
                </div>
                
                <div class="config-item">
                    <label>物品列表 (重量 w, 价值 v):</label>
                    <table class="items-table" id="itemsTable">
                        <thead>
                            <tr>
                                <th>物品 i</th>
                                <th>重量 w</th>
                                <th>价值 v</th>
                            </tr>
                        </thead>
                        <tbody id="itemsBody">
                            <!-- 动态生成 -->
                        </tbody>
                    </table>
                </div>
                
                <button id="applyConfig" class="btn-secondary">应用配置</button>
            </div>
            
            <div class="control-panel">
                <h2 class="panel-title">动画控制</h2>
                
                <div class="control-buttons">
                    <button id="startBtn" class="btn-primary">▶ 开始</button>
                    <button id="pauseBtn" class="btn-warning">⏸ 暂停</button>
                    <button id="nextStepBtn" class="btn-secondary">⏭ 下一步</button>
                    <button id="prevStepBtn" class="btn-secondary">⏮ 上一步</button>
                    <button id="resetBtn" class="btn-danger">↺ 重置</button>
                </div>
                
                <div class="speed-control">
                    <span>动画速度:</span>
                    <input type="range" id="speedSlider" class="speed-slider" min="1" max="10" value="5">
                    <span id="speedValue">中速</span>
                </div>
                
                <div class="control-buttons" style="margin-top: 20px;">
                    <button id="showPathBtn" class="btn-secondary">🔍 显示最优解路径</button>
                    <button id="toggleArrowsBtn" class="btn-secondary">↕️ 切换箭头显示</button>
                </div>
            </div>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #3498db;"></div>
                    <span>当前单元格</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #ecf0f1;"></div>
                    <span>依赖单元格</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #e67e22;"></div>
                    <span>不放入决策</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #2ecc71;"></div>
                    <span>放入决策</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background-color: #f1c40f;"></div>
                    <span>最优解路径</span>
                </div>
            </div>
        </div>
        
        <div class="right-panel">
            <h2 class="panel-title">动态规划表格可视化</h2>
            
            <div class="visualization-container">
                <canvas id="animationCanvas"></canvas>
            </div>
            
            <div class="status-panel">
                <div class="status-title">当前状态说明</div>
                <div id="statusText">
                    点击"开始"按钮启动动画，或点击"下一步"手动前进。动画将展示二维DP表格的填充过程。
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>01背包动态规划可视化教学工具 | 状态转移方程: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])</p>
        <p>点击表格中的单元格可以查看其计算过程</p>
    </div>

    <script>
        // 全局变量
        let canvas, ctx;
        let capacity = 8;
        let itemCount = 4;
        let items = [
            { weight: 2, value: 3 },
            { weight: 3, value: 4 },
            { weight: 4, value: 5 },
            { weight: 5, value: 8 }
        ];
        
        // DP表格数据
        let dp = [];
        let decisions = []; // 记录每个单元格的决策: 0=不放入, 1=放入
        
        // 动画状态
        let animationState = {
            isPlaying: false,
            currentStep: 0,
            totalSteps: 0,
            speed: 300, // 毫秒
            showArrows: true,
            showOptimalPath: false
        };
        
        // 当前高亮的单元格
        let highlightedCell = { i: -1, j: -1 };
        let dependentCells = [];
        
        // 动画步骤队列
        let animationSteps = [];
        
        // 画布尺寸
        const cellSize = 60;
        const headerSize = 40;
        const arrowLength = 25;
        
        // 初始化函数
        function init() {
            canvas = document.getElementById('animationCanvas');
            ctx = canvas.getContext('2d');
            
            // 初始化物品表格
            initItemsTable();
            
            // 初始化DP表格
            initDPTable();
            
            // 生成动画步骤
            generateAnimationSteps();
            
            // 设置事件监听器
            setupEventListeners();
            
            // 初始绘制
            resizeCanvas();
            drawTable();
            
            // 更新状态文本
            updateStatusText("初始化完成。点击'开始'按钮启动动画。");
        }
        
        // 初始化物品表格
        function initItemsTable() {
            const itemsBody = document.getElementById('itemsBody');
            itemsBody.innerHTML = '';
            
            for (let i = 0; i < itemCount; i++) {
                const row = document.createElement('tr');
                
                // 物品编号
                const idCell = document.createElement('td');
                idCell.textContent = i + 1;
                row.appendChild(idCell);
                
                // 重量输入
                const weightCell = document.createElement('td');
                const weightInput = document.createElement('input');
                weightInput.type = 'number';
                weightInput.min = '1';
                weightInput.max = '10';
                weightInput.value = items[i] ? items[i].weight : Math.floor(Math.random() * 5) + 1;
                weightCell.appendChild(weightInput);
                row.appendChild(weightCell);
                
                // 价值输入
                const valueCell = document.createElement('td');
                const valueInput = document.createElement('input');
                valueInput.type = 'number';
                valueInput.min = '1';
                valueInput.max = '20';
                valueInput.value = items[i] ? items[i].value : Math.floor(Math.random() * 10) + 1;
                valueCell.appendChild(valueInput);
                row.appendChild(valueCell);
                
                itemsBody.appendChild(row);
            }
        }
        
        // 初始化DP表格
        function initDPTable() {
            // 重置DP表格
            dp = [];
            decisions = [];
            
            // 初始化第一行（没有物品）和第一列（容量为0）
            for (let i = 0; i <= itemCount; i++) {
                dp[i] = [];
                decisions[i] = [];
                for (let j = 0; j <= capacity; j++) {
                    if (i === 0 || j === 0) {
                        dp[i][j] = 0;
                        decisions[i][j] = -1; // -1表示基础情况
                    } else {
                        dp[i][j] = -1; // -1表示未计算
                        decisions[i][j] = -1;
                    }
                }
            }
            
            // 重置动画状态
            animationState.currentStep = 0;
            highlightedCell = { i: -1, j: -1 };
            dependentCells = [];
        }
        
        // 生成动画步骤
        function generateAnimationSteps() {
            animationSteps = [];
            
            // 为每个需要计算的单元格生成步骤
            for (let i = 1; i <= itemCount; i++) {
                for (let j = 1; j <= capacity; j++) {
                    // 步骤1: 高亮当前单元格
                    animationSteps.push({
                        type: 'highlight',
                        i: i,
                        j: j,
                        description: `准备计算 dp[${i}][${j}]：考虑前${i}个物品，背包容量为${j}`
                    });
                    
                    // 步骤2: 计算不放入的情况（查看上方单元格）
                    animationSteps.push({
                        type: 'calc_no_take',
                        i: i,
                        j: j,
                        description: `选项1：不放入物品${i}，价值为 dp[${i-1}][${j}] = ${dp[i-1][j]}`
                    });
                    
                    // 步骤3: 计算放入的情况（查看左上方单元格）
                    if (j >= items[i-1].weight) {
                        animationSteps.push({
                            type: 'calc_take',
                            i: i,
                            j: j,
                            description: `选项2：放入物品${i}，价值为 dp[${i-1}][${j-items[i-1].weight}] + v[${i}] = ${dp[i-1][j-items[i-1].weight]} + ${items[i-1].value} = ${dp[i-1][j-items[i-1].weight] + items[i-1].value}`
                        });
                    } else {
                        animationSteps.push({
                            type: 'calc_take_invalid',
                            i: i,
                            j: j,
                            description: `选项2：无法放入物品${i}，因为物品重量${items[i-1].weight} > 当前容量${j}`
                        });
                    }
                    
                    // 步骤4: 比较并填入结果
                    animationSteps.push({
                        type: 'fill',
                        i: i,
                        j: j,
                        description: `比较两个选项，选择最大值填入 dp[${i}][${j}]`
                    });
                }
            }
            
            animationState.totalSteps = animationSteps.length;
        }
        
        // 执行下一步动画
        function nextStep() {
            if (animationState.currentStep >= animationSteps.length) {
                animationState.isPlaying = false;
                updateStatusText("表格填充完成！点击'显示最优解路径'查看最终结果。");
                document.getElementById('startBtn').textContent = "▶ 开始";
                return;
            }
            
            const step = animationSteps[animationState.currentStep];
            
            // 根据步骤类型执行相应操作
            switch (step.type) {
                case 'highlight':
                    highlightedCell = { i: step.i, j: step.j };
                    dependentCells = [];
                    break;
                    
                case 'calc_no_take':
                    dependentCells = [{ i: step.i-1, j: step.j, type: 'no_take' }];
                    break;
                    
                case 'calc_take':
                    dependentCells = [
                        { i: step.i-1, j: step.j, type: 'no_take' },
                        { i: step.i-1, j: step.j - items[step.i-1].weight, type: 'take' }
                    ];
                    break;
                    
                case 'calc_take_invalid':
                    dependentCells = [{ i: step.i-1, j: step.j, type: 'no_take' }];
                    break;
                    
                case 'fill':
                    // 实际计算DP值
                    calculateDPCell(step.i, step.j);
                    highlightedCell = { i: -1, j: -1 };
                    dependentCells = [];
                    break;
            }
            
            // 更新状态文本
            updateStatusText(step.description);
            
            // 重绘表格
            drawTable();
            
            // 前进到下一步
            animationState.currentStep++;
            
            // 如果动画正在播放，安排下一步
            if (animationState.isPlaying) {
                setTimeout(nextStep, animationState.speed);
            }
        }
        
        // 执行上一步动画
        function prevStep() {
            if (animationState.currentStep <= 0) return;
            
            // 后退一步
            animationState.currentStep--;
            
            // 如果当前步骤是fill类型，需要清除DP值
            const step = animationSteps[animationState.currentStep];
            if (step.type === 'fill') {
                dp[step.i][step.j] = -1;
                decisions[step.i][step.j] = -1;
            }
            
            // 计算前一步的状态
            if (animationState.currentStep > 0) {
                const prevStep = animationSteps[animationState.currentStep - 1];
                
                switch (prevStep.type) {
                    case 'highlight':
                        highlightedCell = { i: prevStep.i, j: prevStep.j };
                        dependentCells = [];
                        break;
                        
                    case 'calc_no_take':
                        highlightedCell = { i: prevStep.i, j: prevStep.j };
                        dependentCells = [{ i: prevStep.i-1, j: prevStep.j, type: 'no_take' }];
                        break;
                        
                    case 'calc_take':
                        highlightedCell = { i: prevStep.i, j: prevStep.j };
                        dependentCells = [
                            { i: prevStep.i-1, j: prevStep.j, type: 'no_take' },
                            { i: prevStep.i-1, j: prevStep.j - items[prevStep.i-1].weight, type: 'take' }
                        ];
                        break;
                        
                    case 'calc_take_invalid':
                        highlightedCell = { i: prevStep.i, j: prevStep.j };
                        dependentCells = [{ i: prevStep.i-1, j: prevStep.j, type: 'no_take' }];
                        break;
                        
                    default:
                        highlightedCell = { i: -1, j: -1 };
                        dependentCells = [];
                }
                
                updateStatusText(prevStep.description);
            } else {
                highlightedCell = { i: -1, j: -1 };
                dependentCells = [];
                updateStatusText("已回到第一步。");
            }
            
            // 重绘表格
            drawTable();
        }
        
        // 计算DP单元格的值
        function calculateDPCell(i, j) {
            // 不放入当前物品
            const noTakeValue = dp[i-1][j];
            
            // 放入当前物品（如果可能）
            let takeValue = -1;
            if (j >= items[i-1].weight) {
                takeValue = dp[i-1][j - items[i-1].weight] + items[i-1].value;
            }
            
            // 选择较大值
            if (takeValue > noTakeValue) {
                dp[i][j] = takeValue;
                decisions[i][j] = 1; // 放入
            } else {
                dp[i][j] = noTakeValue;
                decisions[i][j] = 0; // 不放入
            }
        }
        
        // 绘制表格
        function drawTable() {
            // 清除画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 计算表格尺寸
            const tableWidth = (capacity + 1) * cellSize;
            const tableHeight = (itemCount + 1) * cellSize;
            
            // 绘制列标题（背包容量）
            ctx.fillStyle = '#2c3e50';
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            
            for (let j = 0; j <= capacity; j++) {
                const x = headerSize + j * cellSize + cellSize / 2;
                const y = headerSize / 2;
                ctx.fillText(`容量=${j}`, x, y);
            }
            
            // 绘制行标题（物品）
            for (let i = 0; i <= itemCount; i++) {
                const x = headerSize / 2;
                const y = headerSize + i * cellSize + cellSize / 2;
                
                if (i === 0) {
                    ctx.fillText('物品/容量', x, y);
                } else {
                    ctx.fillText(`前${i}个物品`, x, y);
                }
            }
            
            // 绘制表格单元格
            for (let i = 0; i <= itemCount; i++) {
                for (let j = 0; j <= capacity; j++) {
                    const x = headerSize + j * cellSize;
                    const y = headerSize + i * cellSize;
                    
                    // 检查是否为高亮单元格
                    let isHighlighted = (i === highlightedCell.i && j === highlightedCell.j);
                    let isDependent = dependentCells.some(cell => cell.i === i && cell.j === j);
                    
                    // 设置单元格背景色
                    if (isHighlighted) {
                        ctx.fillStyle = 'rgba(52, 152, 219, 0.2)';
                        ctx.fillRect(x, y, cellSize, cellSize);
                        
                        // 绘制高亮边框
                        ctx.strokeStyle = '#3498db';
                        ctx.lineWidth = 3;
                        ctx.strokeRect(x, y, cellSize, cellSize);
                    } else if (isDependent) {
                        ctx.fillStyle = '#ecf0f1';
                        ctx.fillRect(x, y, cellSize, cellSize);
                    }
                    
                    // 绘制单元格边框
                    ctx.strokeStyle = '#bdc3c7';
                    ctx.lineWidth = 1;
                    ctx.strokeRect(x, y, cellSize, cellSize);
                    
                    // 绘制单元格内容
                    ctx.fillStyle = '#2c3e50';
                    ctx.font = '16px Arial';
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    
                    const centerX = x + cellSize / 2;
                    const centerY = y + cellSize / 2;
                    
                    if (dp[i][j] >= 0) {
                        // 已计算的单元格
                        ctx.fillText(dp[i][j], centerX, centerY);
                        
                        // 绘制决策指示器
                        if (decisions[i][j] === 0) {
                            // 不放入
                            ctx.fillStyle = '#e67e22';
                            ctx.fillText('↑', centerX + 20, centerY - 20);
                        } else if (decisions[i][j] === 1) {
                            // 放入
                            ctx.fillStyle = '#2ecc71';
                            ctx.fillText('↖', centerX + 20, centerY - 20);
                        }
                    } else if (i === 0 || j === 0) {
                        // 基础情况
                        ctx.fillText('0', centerX, centerY);
                    } else {
                        // 未计算的单元格
                        ctx.fillStyle = '#95a5a6';
                        ctx.fillText('?', centerX, centerY);
                    }
                }
            }
            
            // 绘制箭头（如果启用）
            if (animationState.showArrows && dependentCells.length > 0) {
                drawArrows();
            }
            
            // 绘制最优解路径（如果启用）
            if (animationState.showOptimalPath) {
                drawOptimalPath();
            }
        }
        
        // 绘制箭头
        function drawArrows() {
            const currentX = headerSize + highlightedCell.j * cellSize + cellSize / 2;
            const currentY = headerSize + highlightedCell.i * cellSize + cellSize / 2;
            
            dependentCells.forEach(depCell => {
                const depX = headerSize + depCell.j * cellSize + cellSize / 2;
                const depY = headerSize + depCell.i * cellSize + cellSize / 2;
                
                // 设置箭头颜色
                if (depCell.type === 'no_take') {
                    ctx.strokeStyle = '#e67e22';
                    ctx.fillStyle = '#e67e22';
                } else {
                    ctx.strokeStyle = '#2ecc71';
                    ctx.fillStyle = '#2ecc71';
                }
                
                ctx.lineWidth = 2;
                
                // 计算箭头方向
                const dx = currentX - depX;
                const dy = currentY - depY;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                // 如果距离太短，不绘制箭头
                if (distance < cellSize / 2) return;
                
                // 计算起点和终点（从依赖单元格边缘开始）
                const startX = depX + (dx / distance) * (cellSize / 2);
                const startY = depY + (dy / distance) * (cellSize / 2);
                const endX = currentX - (dx / distance) * (cellSize / 2);
                const endY = currentY - (dy / distance) * (cellSize / 2);
                
                // 绘制箭头线
                ctx.beginPath();
                ctx.moveTo(startX, startY);
                ctx.lineTo(endX, endY);
                ctx.stroke();
                
                // 绘制箭头头部
                const angle = Math.atan2(dy, dx);
                ctx.beginPath();
                ctx.moveTo(endX, endY);
                ctx.lineTo(
                    endX - arrowLength * Math.cos(angle - Math.PI / 6),
                    endY - arrowLength * Math.sin(angle - Math.PI / 6)
                );
                ctx.lineTo(
                    endX - arrowLength * Math.cos(angle + Math.PI / 6),
                    endY - arrowLength * Math.sin(angle + Math.PI / 6)
                );
                ctx.closePath();
                ctx.fill();
            });
        }
        
        // 绘制最优解路径
        function drawOptimalPath() {
            // 从右下角开始回溯
            let i = itemCount;
            let j = capacity;
            let path = [];
            
            while (i > 0 && j > 0) {
                path.push({ i: i, j: j });
                
                if (decisions[i][j] === 0) {
                    // 不放入，向上移动
                    i--;
                } else if (decisions[i][j] === 1) {
                    // 放入，向左上方移动
                    j -= items[i-1].weight;
                    i--;
                } else {
                    break;
                }
            }
            
            // 绘制路径
            ctx.strokeStyle = '#f1c40f';
            ctx.lineWidth = 3;
            ctx.setLineDash([5, 5]);
            
            ctx.beginPath();
            
            // 按顺序连接路径点
            for (let k = 0; k < path.length; k++) {
                const cell = path[k];
                const x = headerSize + cell.j * cellSize + cellSize / 2;
                const y = headerSize + cell.i * cellSize + cellSize / 2;
                
                if (k === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            }
            
            ctx.stroke();
            ctx.setLineDash([]);
            
            // 高亮路径上的单元格
            path.forEach(cell => {
                const x = headerSize + cell.j * cellSize;
                const y = headerSize + cell.i * cellSize;
                
                ctx.fillStyle = 'rgba(241, 196, 15, 0.3)';
                ctx.fillRect(x, y, cellSize, cellSize);
                
                ctx.strokeStyle = '#f1c40f';
                ctx.lineWidth = 2;
                ctx.strokeRect(x, y, cellSize, cellSize);
            });
        }
        
        // 更新状态文本
        function updateStatusText(text) {
            document.getElementById('statusText').textContent = text;
        }
        
        // 调整画布大小
        function resizeCanvas() {
            const container = document.querySelector('.visualization-container');
            const width = container.clientWidth;
            const height = container.clientHeight;
            
            canvas.width = width;
            canvas.height = height;
        }
        
        // 处理画布点击事件（探查单元格）
        function handleCanvasClick(event) {
            const rect = canvas.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            
            // 计算点击的单元格
            const j = Math.floor((x - headerSize) / cellSize);
            const i = Math.floor((y - headerSize) / cellSize);
            
            // 检查点击是否在有效范围内
            if (i >= 1 && i <= itemCount && j >= 1 && j <= capacity && dp[i][j] >= 0) {
                // 显示该单元格的计算过程
                showCellCalculation(i, j);
            }
        }
        
        // 显示单元格的计算过程
        function showCellCalculation(i, j) {
            // 高亮当前单元格
            highlightedCell = { i: i, j: j };
            
            // 设置依赖单元格
            dependentCells = [{ i: i-1, j: j, type: 'no_take' }];
            
            if (j >= items[i-1].weight) {
                dependentCells.push({ i: i-1, j: j - items[i-1].weight, type: 'take' });
            }
            
            // 更新状态文本
            let description = `单元格 dp[${i}][${j}] = ${dp[i][j]} 的计算过程：\n`;
            description += `• 不放入物品${i}: dp[${i-1}][${j}] = ${dp[i-1][j]}\n`;
            
            if (j >= items[i-1].weight) {
                description += `• 放入物品${i}: dp[${i-1}][${j-items[i-1].weight}] + v[${i}] = ${dp[i-1][j-items[i-1].weight]} + ${items[i-1].value} = ${dp[i-1][j-items[i-1].weight] + items[i-1].value}\n`;
            } else {
                description += `• 无法放入物品${i} (重量${items[i-1].weight} > 容量${j})\n`;
            }
            
            description += `• 最大值为 ${dp[i][j]}`;
            
            if (decisions[i][j] === 0) {
                description += `，决策为不放入物品${i}`;
            } else {
                description += `，决策为放入物品${i}`;
            }
            
            updateStatusText(description);
            
            // 重绘表格
            drawTable();
        }
        
        // 应用新配置
        function applyNewConfig() {
            // 获取新配置
            capacity = parseInt(document.getElementById('capacity').value);
            itemCount = parseInt(document.getElementById('itemCount').value);
            
            // 获取物品数据
            items = [];
            const inputs = document.querySelectorAll('#itemsBody input');
            
            for (let i = 0; i < itemCount; i++) {
                const weight = parseInt(inputs[i * 2].value);
                const value = parseInt(inputs[i * 2 + 1].value);
                items.push({ weight, value });
            }
            
            // 重新初始化
            initDPTable();
            generateAnimationSteps();
            resizeCanvas();
            drawTable();
            
            // 更新状态
            animationState.isPlaying = false;
            document.getElementById('startBtn').textContent = "▶ 开始";
            animationState.showOptimalPath = false;
            
            updateStatusText(`已应用新配置：${itemCount}个物品，背包容量${capacity}。点击"开始"按钮启动动画。`);
        }
        
        // 设置事件监听器
        function setupEventListeners() {
            // 控制按钮
            document.getElementById('startBtn').addEventListener('click', function() {
                if (!animationState.isPlaying) {
                    animationState.isPlaying = true;
                    this.textContent = "⏸ 暂停";
                    nextStep();
                }
            });
            
            document.getElementById('pauseBtn').addEventListener('click', function() {
                animationState.isPlaying = false;
                document.getElementById('startBtn').textContent = "▶ 开始";
            });
            
            document.getElementById('nextStepBtn').addEventListener('click', function() {
                animationState.isPlaying = false;
                document.getElementById('startBtn').textContent = "▶ 开始";
                nextStep();
            });
            
            document.getElementById('prevStepBtn').addEventListener('click', function() {
                animationState.isPlaying = false;
                document.getElementById('startBtn').textContent = "▶ 开始";
                prevStep();
            });
            
            document.getElementById('resetBtn').addEventListener('click', function() {
                animationState.isPlaying = false;
                document.getElementById('startBtn').textContent = "▶ 开始";
                animationState.currentStep = 0;
                animationState.showOptimalPath = false;
                initDPTable();
                drawTable();
                updateStatusText("已重置。点击'开始'按钮重新启动动画。");
            });
            
            // 速度控制
            document.getElementById
('speedSlider').addEventListener('input', function() {
                const speed = parseInt(this.value);
                animationState.speed = 550 - (speed * 50); // 速度值从500ms到50ms
                
                const speedText = ['极慢', '很慢', '慢', '较慢', '中速', '较快', '快', '很快', '极快', '最快'];
                document.getElementById('speedValue').textContent = speedText[speed - 1];
            });
            
            // 应用配置按钮
            document.getElementById('applyConfig').addEventListener('click', applyNewConfig);
            
            // 物品数量变化时更新物品表格
            document.getElementById('itemCount').addEventListener('change', function() {
                itemCount = parseInt(this.value);
                initItemsTable();
            });
            
            // 显示最优解路径按钮
            document.getElementById('showPathBtn').addEventListener('click', function() {
                // 检查表格是否已完全填充
                let isComplete = true;
                for (let i = 1; i <= itemCount; i++) {
                    for (let j = 1; j <= capacity; j++) {
                        if (dp[i][j] < 0) {
                            isComplete = false;
                            break;
                        }
                    }
                    if (!isComplete) break;
                }
                
                if (!isComplete) {
                    updateStatusText("表格尚未完全填充，无法显示最优解路径。请先完成表格填充。");
                    return;
                }
                
                animationState.showOptimalPath = !animationState.showOptimalPath;
                this.textContent = animationState.showOptimalPath ? "🔍 隐藏最优解路径" : "🔍 显示最优解路径";
                
                if (animationState.showOptimalPath) {
                    // 计算并显示最优解
                    let i = itemCount;
                    let j = capacity;
                    let selectedItems = [];
                    let totalValue = dp[itemCount][capacity];
                    let totalWeight = 0;
                    
                    while (i > 0 && j > 0) {
                        if (decisions[i][j] === 1) {
                            selectedItems.push(i);
                            totalWeight += items[i-1].weight;
                            j -= items[i-1].weight;
                        }
                        i--;
                    }
                    
                    selectedItems.reverse();
                    
                    let pathDescription = `最优解：最大价值 = ${totalValue}\n`;
                    pathDescription += `选中物品：${selectedItems.length > 0 ? selectedItems.join(', ') : '无'}\n`;
                    pathDescription += `总重量：${totalWeight} (容量：${capacity})`;
                    
                    updateStatusText(pathDescription);
                }
                
                drawTable();
            });
            
            // 切换箭头显示按钮
            document.getElementById('toggleArrowsBtn').addEventListener('click', function() {
                animationState.showArrows = !animationState.showArrows;
                this.textContent = animationState.showArrows ? "↕️ 隐藏箭头" : "↕️ 显示箭头";
                drawTable();
            });
            
            // 画布点击事件
            canvas.addEventListener('click', handleCanvasClick);
            
            // 窗口大小变化时调整画布
            window.addEventListener('resize', function() {
                resizeCanvas();
                drawTable();
            });
        }
        
        // 页面加载完成后初始化
        window.addEventListener('load', init);
    </script>
</body>
</html>


### 3. 过程输出

### 3. 使用指南

## 01背包动态规划交互式教学动画使用指南

欢迎使用“01背包动态规划-二维表格填充过程可视化”教学动画！本工具旨在通过直观、交互的方式，帮助您深入理解动态规划解决01背包问题的核心思想与实现过程。无论您是算法初学者还是希望巩固知识的开发者，本工具都将为您提供独特的学习体验。

---

### 🎯 功能说明

本动画将抽象的01背包动态规划算法转化为可视化的二维表格填充过程，让您能够：
- **直观观察**状态转移方程的每一步计算
- **清晰理解**每个单元格值如何由其依赖的单元格决定
- **主动探索**不同问题实例下的表格变化
- **深入掌握**最优子结构和重叠子问题的本质

### 🚀 主要功能

#### 1. **动画控制区**
- **开始/暂停**：控制动画的自动播放与暂停
- **上一步/下一步**：手动控制动画进度，仔细查看每个计算步骤
- **重置**：清空表格，回到初始状态
- **速度调节**：通过滑块控制动画播放速度（从“极慢”到“最快”）

#### 2. **问题配置区**
- **背包容量**：设置背包的最大承重（1-20）
- **物品数量**：设置物品的总数（1-8）
- **物品详情表**：为每个物品设置重量和价值
- **应用配置**：应用新的问题实例，重新开始动画

#### 3. **可视化交互区**
- **表格探查**：点击任意已填充的单元格，查看该单元格的详细计算过程
- **箭头显示**：切换显示/隐藏单元格间的依赖关系箭头
- **最优解路径**：在表格完全填充后，高亮显示从最终结果回溯到起点的最优选择路径

### ✨ 设计特色

#### 1. **渐进式教学**
动画将每个单元格的计算分解为四个清晰步骤：
1. **高亮当前单元格**：明确当前计算目标
2. **计算“不放入”选项**：查看正上方单元格
3. **计算“放入”选项**：查看左上方单元格（如果容量允许）
4. **比较并填入结果**：选择最大值，记录决策

#### 2. **多感官学习**
- **视觉编码**：不同颜色代表不同状态（当前单元格、依赖单元格、决策类型）
- **动态关联**：箭头清晰指示单元格间的依赖关系
- **实时反馈**：状态面板详细描述当前步骤的计算逻辑

#### 3. **探索式学习**
- 支持自定义问题实例，观察不同输入下的表格变化
- 允许回溯任意单元格的计算过程
- 提供最优解路径的可视化追踪

### 📚 教学要点

#### 核心概念可视化
1. **状态定义** `dp[i][j]`
   - 行索引 `i`：考虑前 i 个物品
   - 列索引 `j`：当前背包容量
   - 单元格值：在当前条件下的最大价值

2. **状态转移方程**
   ```
   dp[i][j] = max(
       dp[i-1][j],                     // 不放入物品 i
       dp[i-1][j-w[i]] + v[i]          // 放入物品 i（如果容量允许）
   )
   ```
   - 动画将抽象的公式转化为具体的视觉操作
   - 清晰展示“不放入”和“放入”两种决策的比较过程

3. **填表顺序**
   - 自底向上：从基础情况（i=0或j=0）开始
   - 逐行计算：确保计算当前单元格时，依赖的单元格已计算完成
   - 动画严格按照算法执行顺序填充表格

#### 关键观察点
- **基础情况**：第0行（无物品）和第0列（容量为0）的值均为0
- **依赖关系**：每个单元格只依赖于其**正上方**和**左上方**的单元格
- **决策记录**：每个单元格不仅存储最大价值，还记录达到该价值的决策（放入/不放入）
- **最优解回溯**：从右下角 `dp[n][C]` 开始，根据决策记录反向追踪，得到具体物品选择方案

### 💡 使用建议

#### 给初学者的学习路径
1. **第一次使用**
   - 保持默认配置，点击“开始”观看完整动画
   - 观察表格如何从左上角逐步填充到右下角
   - 注意状态面板的文字描述，理解每一步在做什么

2. **深入理解**
   - 使用“上一步/下一步”手动控制，仔细查看每个单元格的计算细节
   - 点击已填充的单元格，查看其计算过程
   - 开启“箭头显示”，观察单元格间的依赖关系

3. **主动探索**
   - 修改物品的重量和价值，观察表格如何变化
   - 尝试极端情况：所有物品都很重、所有物品价值都很高
   - 点击“显示最优解路径”，理解如何从表格中提取最终答案

#### 给教师的课堂应用建议
1. **演示阶段**
   - 使用默认实例完整演示一次填表过程
   - 重点讲解状态转移方程的视觉对应关系
   - 强调“不放入”和“放入”两种决策的对比

2. **互动阶段**
   - 让学生预测下一个单元格的值，然后播放动画验证
   - 提出“如果修改某个物品的重量，哪个区域会受影响？”等问题
   - 引导学生发现规律：为什么某些单元格的值与其上方单元格相同？

3. **巩固阶段**
   - 让学生自行设计问题实例，观察表格变化
   - 讨论不同问题规模下的表格特点
   - 引导学生总结动态规划解决01背包问题的通用模式

#### 高效学习技巧
1. **边看边想**
   - 在动画播放前，尝试自己推导下一个单元格的值
   - 对比自己的推导与动画展示的结果
   - 如果不一致，仔细分析差异原因

2. **多次重复**
   - 第一次：整体观看，了解流程
   - 第二次：关注细节，理解每个计算步骤
   - 第三次：关闭状态描述，尝试自己解释动画

3. **联系实际**
   - 将表格中的数值与实际问题对应
   - 思考：为什么 `dp[2][5]` 的值是6？这在实际中意味着什么？
   - 理解：表格不仅存储结果，还隐含了达到该结果的决策历史

### 🔧 技术提示

- **响应式设计**：工具适应不同屏幕尺寸，但在较大屏幕上体验更佳
- **性能优化**：问题规模限制在合理范围内，确保动画流畅
- **颜色编码**：所有颜色选择均考虑色觉障碍用户的可访问性
- **交互反馈**：所有操作都有明确的视觉或文字反馈

---

### 🎓 学习目标达成

通过本工具的学习，您将能够：
- ✅ 准确解释01背包问题的动态规划解法
- ✅ 手动绘制并填充二维DP表格
- ✅ 理解状态转移方程的每个部分在实际计算中的对应
- ✅ 从填充完成的表格中回溯出最优解
- ✅ 将01背包的解法思路迁移到其他动态规划问题

**开始您的探索之旅吧！点击“开始”按钮，让抽象的算法在您眼前“活”起来。** 🚀

---

*本工具由教育技术专家设计，旨在通过可视化降低算法学习门槛。如果您有任何反馈或建议，欢迎与我们分享！*