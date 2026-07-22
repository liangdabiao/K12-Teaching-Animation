# K12 教学动画项目 — 长期约定

## 浏览器测试硬性约束（最高优先级，2026-07-22 用户明确）
- **禁止安装、禁止使用 Playwright 与 Chrome 做渲染抽查。**
- 浏览器实渲抽查一律改用 **MCP**（agent-browser / 浏览器 MCP 工具）。
- 前期曾在隔离工作区安装过 Playwright+Chromium 并跑通 12/12，但该方案已被用户废止，后续不得复用。

## 动画页统一外壳规范
- 深色主题 CSS 变量；`<header class="topbar">` 含 `← 返回学科目录` 链接（指向 `../学科/index.html`）。
- `<canvas id="cv">` + `<aside class="panel">`（教学面板）+ `.controls`（播放/重置/步进/调速）。
- JS 契约：`sceneInit / sceneReset / sceneUpdate(dt) / sceneDraw / sceneStep(d)`，`STEPS` 步骤数组，`wireExtra` 绑定额外控件；`window.showTip` 由外壳注入（替代 alert）。
- 不引用任何外部 CDN，纯离线可开。

## 索引页与 guide.md 范式
- 学科 index.html：分类 `section` + 卡片网格；新增动画须挂接对应学科 index 并更新顶部统计数；根 index.html 同步更新学科计数与总计数。
- guide.md：采用「需求 + 专业思考 + HTML_CODE」三段式。

## 课程补充进度
- `补充.md` 已过时：其列"缺失"话题（物理力学/化学初中基础/生物必修一/信息二进制HTTPS）大多已存在，照抄会大量重复。
- 真实高优先级缺口约 60+（物理15/化学20/生物14/信息19）。
- **首批均衡 14 个（用户已确认）**：物理3（比热容、热机四冲程、声音三特性）、化学3（金属活动性顺序、酸的共性、同分异构体）、生物4（ATP、细胞癌变、质壁分离、PCR）、信息4（线段树、并查集、编辑距离、进程与线程）。
- **第二批 53 个（2026-07-21 补齐）**：物理12/化学16/生物10/信息15，复用 `gen_supplement.py` 的 `build_html/build_guide`（生成器在 `C:\Users\49707\AppData\Local\Temp\gen_batch2.py`）。文件夹名含 `/` 的 3 个（I=Q/t、R=ρL/S、L/g）已改用全角 `／` 避免 NTFS 嵌套。补齐后全库 284 页；索引统计已对齐：物理76/化学74/生物65/信息69，根总数284。
- **全库校验 harness**：`C:\Users\49707\AppData\Local\Temp\validate_batch2.js`（Node `vm` + mock DOM/Canvas 桩，拼接多 `<script>` 块）。最新结果 PASS=279/FAIL=3/标记=0；53 个 batch2 全过。3 个失败均为既有旧文件潜在 bug（酸碱中和 TDZ、兴奋传导 classList、细胞呼吸 Stop 未定义），按红线未擅改，待确认修复。
