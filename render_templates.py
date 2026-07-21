#!/usr/bin/env python3
"""渲染所有未替换的模板文件，将 %(title)s %(css)s %(desc)s %(legend)s 替换为实际内容"""
import os, re, glob

BASE = r'd:\K12-Teaching-Animation'

# 学科主题色配置
SUBJECT_THEMES = {
    '信息技术': {'primary': '#6C5CE7', 'secondary': '#a29bfe', 'bg': '#0a0a1a', 'accent': '#fd79a8'},
    '化学':     {'primary': '#e84393', 'secondary': '#fd79a8', 'bg': '#1a0a15', 'accent': '#fdcb6e'},
    '物理':     {'primary': '#0984e3', 'secondary': '#74b9ff', 'bg': '#0a1520', 'accent': '#00cec9'},
    '生物':     {'primary': '#00b894', 'secondary': '#55efc4', 'bg': '#0a1a10', 'accent': '#ffeaa7'},
}

# 各文件的具体描述和图例
CONTENT = {
    # ===== 信息技术 =====
    'AVL树四种旋转': {
        'desc': 'AVL树通过LL、RR、LR、RL四种旋转维持平衡。每次插入或删除后，从失衡节点向上回溯，根据左右子树高度差选择对应旋转方式，确保树高始终为O(log n)。',
        'legend': '<span class="li"><b style="color:#6C5CE7">■</b> 失衡节点</span><span class="li"><b style="color:#00cec9">■</b> 旋转中心</span><span class="li"><b style="color:#fdcb6e">■</b> 子树移动</span>'
    },
    '哈希表解决冲突': {
        'desc': '哈希表通过哈希函数将键映射到数组索引。当两个键映射到同一位置时产生冲突。拉链法用链表存储同位置元素；开放定址法按线性探测、二次探测等方式寻找空位。',
        'legend': '<span class="li"><b style="color:#6C5CE7">■</b> 键值对</span><span class="li"><b style="color:#e17055">■</b> 冲突位置</span><span class="li"><b style="color:#00cec9">■</b> 解决后</span>'
    },
    '链表的插入删除': {
        'desc': '链表通过指针将节点串联。插入时修改前后节点指针指向新节点；删除时跳过被删节点，将其前驱直接连到后继。单向、双向、循环链表各有不同的指针操作方式。',
        'legend': '<span class="li"><b style="color:#6C5CE7">■</b> 节点</span><span class="li"><b style="color:#00cec9">■</b> 新插入</span><span class="li"><b style="color:#e17055">■</b> 待删除</span><span class="li">→ 指针方向</span>'
    },
    '二叉搜索树': {
        'desc': '二叉搜索树(BST)满足：左子树所有节点值 < 根节点值 < 右子树所有节点值。查找、插入、删除平均O(log n)。删除节点时需处理叶子、单子、双子三种情况，双子节点用后继替代。',
        'legend': '<span class="li"><b style="color:#6C5CE7">■</b> 当前节点</span><span class="li"><b style="color:#00cec9">■</b> 查找路径</span><span class="li"><b style="color:#e17055">■</b> 删除节点</span>'
    },
    # ===== 化学 =====
    '反应速率和活化能': {
        'desc': '化学反应速率取决于反应物分子的有效碰撞频率。只有能量超过活化能的碰撞才能打断旧键、形成新键。温度升高使分子运动加快，有效碰撞增多；催化剂降低活化能门槛。',
        'legend': '<span class="li"><b style="color:#e84393">●</b> 反应物分子</span><span class="li"><b style="color:#fdcb6e">●</b> 活化分子</span><span class="li"><b style="color:#00cec9">●</b> 生成物</span>'
    },
    '实验室制取二氧化碳': {
        'desc': '实验室用大理石(CaCO₃)与稀盐酸(HCl)反应制取CO₂。微观上，H⁺攻击CaCO₃晶格，Ca²⁺溶出，CO₃²⁻分解为CO₂分子和H₂O。CO₂分子从液面逸出。',
        'legend': '<span class="li"><b style="color:#e84393">●</b> CaCO₃</span><span class="li"><b style="color:#0984e3">●</b> HCl</span><span class="li"><b style="color:#636e72">●</b> CO₂↑</span><span class="li"><b style="color:#00cec9">●</b> H₂O</span>'
    },
    '浓硫酸稀释': {
        'desc': '浓硫酸稀释时释放大量热量。必须将浓硫酸沿容器壁缓慢注入水中并不断搅拌，绝不能将水倒入浓硫酸中——否则水浮在酸面上剧烈沸腾喷溅，极其危险。',
        'legend': '<span class="li"><b style="color:#e84393">●</b> H₂SO₄分子</span><span class="li"><b style="color:#0984e3">●</b> H₂O分子</span><span class="li"><b style="color:#fdcb6e">⚡</b> 放热</span>'
    },
    '电解饱和食盐水': {
        'desc': '电解饱和食盐水时，阳极Cl⁻失电子生成Cl₂↑，阴极H₂O得电子生成H₂↑和NaOH。微观上，电场驱动离子定向移动，电极表面发生氧化还原反应。这是氯碱工业的基础。',
        'legend': '<span class="li"><b style="color:#00b894">●</b> Na⁺</span><span class="li"><b style="color:#e84393">●</b> Cl⁻</span><span class="li"><b style="color:#fdcb6e">↑</b> Cl₂/H₂</span><span class="li"><b style="color:#0984e3">●</b> H₂O</span>'
    },
    '钠与水反应': {
        'desc': '钠与水剧烈反应：2Na + 2H₂O → 2NaOH + H₂↑。微观上，Na原子失去最外层电子成为Na⁺，水分子中H⁺获得电子成为H原子，两个H原子结合为H₂分子。反应放热使钠熔化成银白色小球。',
        'legend': '<span class="li"><b style="color:#e84393">●</b> Na原子</span><span class="li"><b style="color:#0984e3">●</b> H₂O</span><span class="li"><b style="color:#fdcb6e">↑</b> H₂</span><span class="li"><b style="color:#00cec9">●</b> Na⁺/OH⁻</span>'
    },
    # ===== 物理 =====
    '内能改变': {
        'desc': '改变物体内能有两种方式：做功（如压缩气体、摩擦生热）和热传递（传导、对流、辐射）。微观上，做功是宏观力使分子动能改变，热传递是分子间碰撞传递动能。两者在改变内能上等效。',
        'legend': '<span class="li"><b style="color:#0984e3">●</b> 分子</span><span class="li"><b style="color:#e17055">→</b> 做功</span><span class="li"><b style="color:#fdcb6e">↔</b> 热传递</span>'
    },
    '分子运动论': {
        'desc': '分子动理论三大要点：①物质由大量分子组成，分子间有空隙；②分子做永不停息的无规则运动（布朗运动、扩散现象）；③分子间存在引力和斥力，统称为分子力。温度越高，分子运动越剧烈。',
        'legend': '<span class="li"><b style="color:#0984e3">●</b> 分子</span><span class="li"><b style="color:#e17055">~</b> 布朗运动轨迹</span><span class="li"><b style="color:#00cec9">↔</b> 分子力</span>'
    },
    '凸透镜成像全过程': {
        'desc': '凸透镜成像规律：u>2f成缩小倒立实像；u=2f成等大倒立实像；f<u<2f成放大倒立实像；u=f不成像；u<f成放大正立虚像。物距连续变化时，像的大小和位置也随之连续变化。',
        'legend': '<span class="li"><b style="color:#fdcb6e">|</b> 焦点F</span><span class="li"><b style="color:#e17055">↑</b> 物体</span><span class="li"><b style="color:#00cec9">↑</b> 像</span><span class="li">— 光线路径</span>'
    },
    '电磁感应中的动生电动势': {
        'desc': '导体在磁场中切割磁感线运动时，导体内自由电荷受洛伦兹力而定向移动，产生动生电动势。若构成回路则产生感应电流。方向由右手定则判定。感生电动势则由变化磁场产生的涡旋电场驱动电荷运动。',
        'legend': '<span class="li"><b style="color:#0984e3">→</b> 磁场B</span><span class="li"><b style="color:#e17055">→</b> 导体运动v</span><span class="li"><b style="color:#fdcb6e">⊕</b> 感应电流方向</span>'
    },
    '电磁波的电场与磁场': {
        'desc': '电磁波由相互垂直的电场E和磁场B组成，两者均垂直于传播方向。振荡电荷产生变化的电场，变化的电场又产生变化的磁场，如此交替向外传播，速度为光速c=3×10⁸ m/s。',
        'legend': '<span class="li"><b style="color:#e17055">↕</b> 电场E</span><span class="li"><b style="color:#0984e3">↔</b> 磁场B</span><span class="li"><b style="color:#00cec9">→</b> 传播方向</span>'
    },
    '简谐运动的波形图': {
        'desc': '简谐运动的位移-时间图像是正弦曲线。圆周运动的投影即为简谐运动。两个同频率简谐运动的相位差决定了它们是同相、反相还是正交，这在波的干涉中有重要应用。',
        'legend': '<span class="li"><b style="color:#0984e3">●</b> 参考圆上的点</span><span class="li"><b style="color:#e17055">—</b> 投影轨迹</span><span class="li"><b style="color:#fdcb6e">~</b> 正弦波形</span>'
    },
    'α粒子散射实验': {
        'desc': '卢瑟福用α粒子轰击金箔，发现绝大多数α粒子直线穿过，少数大角度偏转，极少数甚至反弹。这说明原子内部大部分是空的，正电荷和质量集中在极小的原子核中，从而推翻了枣糕模型，建立了核式结构模型。',
        'legend': '<span class="li"><b style="color:#fdcb6e">●</b> α粒子</span><span class="li"><b style="color:#e17055">●</b> 原子核</span><span class="li"><b style="color:#0984e3">○</b> 金原子</span>'
    },
    '链式核反应': {
        'desc': '铀-235吸收一个中子后裂变为两个中等质量的核，同时释放2-3个中子和大量能量。这些中子又可以引发更多铀核裂变，形成链式反应。核电站用控制棒吸收多余中子使反应可控；原子弹则让反应不可控地进行。',
        'legend': '<span class="li"><b style="color:#0984e3">●</b> 中子</span><span class="li"><b style="color:#e17055">●</b> 铀核</span><span class="li"><b style="color:#fdcb6e">✦</b> 裂变产物</span><span class="li"><b style="color:#00cec9">↑</b> 能量释放</span>'
    },
    '行星运动': {
        'desc': '开普勒三定律：①行星绕太阳运动的轨道是椭圆，太阳在焦点上；②行星与太阳连线在相等时间内扫过相等面积（近日点速度快）；③轨道半长轴的三次方与周期的平方之比为常数。万有引力是这一切的根本原因。',
        'legend': '<span class="li"><b style="color:#fdcb6e">●</b> 太阳</span><span class="li"><b style="color:#0984e3">●</b> 行星</span><span class="li">— 椭圆轨道</span><span class="li"><b style="color:#e17055">→</b> 引力方向</span>'
    },
    # ===== 生物 =====
    '人体内环境与稳态': {
        'desc': '内环境由血浆、组织液和淋巴组成，是细胞与外界环境进行物质交换的媒介。稳态通过神经-体液-免疫调节网络维持：血糖调节（胰岛素/胰高血糖素）、体温调节（产热/散热平衡）、水盐平衡（抗利尿激素）。',
        'legend': '<span class="li"><b style="color:#e17055">●</b> 血糖</span><span class="li"><b style="color:#0984e3">●</b> 胰岛素</span><span class="li"><b style="color:#00b894">●</b> 正常范围</span>'
    },
    '中心法则完整流程': {
        'desc': '中心法则描述遗传信息的传递方向：DNA复制→转录→mRNA加工（加帽加尾、剪接）→翻译→蛋白质折叠修饰。某些病毒还有RNA逆转录和RNA复制。这是分子生物学的核心框架。',
        'legend': '<span class="li"><b style="color:#0984e3">═</b> DNA</span><span class="li"><b style="color:#00b894">─</b> mRNA</span><span class="li"><b style="color:#e17055">●</b> 核糖体</span><span class="li"><b style="color:#fdcb6e">◆</b> 氨基酸</span>'
    },
    '从DNA到蛋白质': {
        'desc': '基因表达分两步：①转录——RNA聚合酶以DNA一条链为模板合成mRNA；②翻译——mRNA进入细胞质，核糖体读取密码子，tRNA携带对应氨基酸，按A-U、G-C配对原则依次连接成多肽链。',
        'legend': '<span class="li"><b style="color:#0984e3">═</b> DNA双链</span><span class="li"><b style="color:#00b894">─</b> mRNA</span><span class="li"><b style="color:#e17055">▲</b> tRNA</span><span class="li"><b style="color:#fdcb6e">●</b> 氨基酸</span>'
    },
    '显微镜观察细胞': {
        'desc': '光学显微镜下观察口腔上皮细胞、草履虫、洋葱表皮细胞。操作要点：先低倍后高倍、调粗准焦螺旋再调细准焦螺旋。真实视野灰暗、对焦困难，动画可展示高清染色效果。',
        'legend': '<span class="li"><b style="color:#00b894">●</b> 细胞核</span><span class="li"><b style="color:#0984e3">○</b> 细胞膜</span><span class="li"><b style="color:#e17055">░</b> 细胞质</span>'
    },
    '基因工程全过程': {
        'desc': '基因工程五步：①用限制酶剪切目的基因和载体DNA；②用DNA连接酶将目的基因插入载体构建重组DNA；③将重组DNA导入受体细胞（转化）；④筛选含目的基因的受体细胞并培养表达；⑤获得转基因产物。',
        'legend': '<span class="li"><b style="color:#00b894">═</b> 目的基因</span><span class="li"><b style="color:#0984e3">○</b> 载体</span><span class="li"><b style="color:#e17055">✂</b> 限制酶</span><span class="li"><b style="color:#fdcb6e">●</b> 受体细胞</span>'
    },
    '生态系统碳循环': {
        'desc': '碳在生物圈中循环：大气CO₂→光合作用→有机物→呼吸作用/分解→CO₂。人类活动（化石燃料燃烧、毁林）打破了碳循环平衡，导致大气CO₂浓度持续上升，引发全球变暖。',
        'legend': '<span class="li"><b style="color:#636e72">●</b> CO₂</span><span class="li"><b style="color:#00b894">●</b> 光合作用</span><span class="li"><b style="color:#e17055">●</b> 呼吸/燃烧</span><span class="li"><b style="color:#0984e3">●</b> 海洋吸收</span>'
    },
    '神经调节反射弧': {
        'desc': '反射弧是神经调节的结构基础：感受器→传入神经→神经中枢（突触传递）→传出神经→效应器。兴奋在神经纤维上以电信号传导，在突触处通过神经递质化学传递，速度较慢（突触延搁）。',
        'legend': '<span class="li"><b style="color:#fdcb6e">●</b> 感受器</span><span class="li"><b style="color:#0984e3">→</b> 电信号</span><span class="li"><b style="color:#e17055">●</b> 突触</span><span class="li"><b style="color:#00b894">●</b> 效应器</span>'
    },
    '细胞呼吸三阶段': {
        'desc': '有氧呼吸三阶段：①糖酵解（细胞质基质）：葡萄糖分解为丙酮酸，产2ATP；②丙酮酸氧化（线粒体基质）：丙酮酸脱羧生成乙酰CoA，产2ATP；③电子传递链（线粒体内膜）：[H]与O₂结合生成水，产约32ATP。总计约36ATP。',
        'legend': '<span class="li"><b style="color:#00b894">●</b> 糖酵解</span><span class="li"><b style="color:#0984e3">●</b> 丙酮酸氧化</span><span class="li"><b style="color:#6c5ce7">●</b> 电子传递链</span><span class="li"><b style="color:#fdcb6e">⚡</b> ATP</span>'
    },
    '群落演替过程': {
        'desc': '群落演替是从简单到复杂的群落变化过程。初生演替：裸岩→地衣→苔藓→草本→灌木→森林，需数百年。次生演替：火灾/砍伐后从土壤开始恢复，速度更快。人类活动可改变演替的方向和速度。',
        'legend': '<span class="li"><b style="color:#636e72">░</b> 裸地</span><span class="li"><b style="color:#00b894">●</b> 草本</span><span class="li"><b style="color:#2d3436">▲</b> 灌木</span><span class="li"><b style="color:#00b894">🌲</b> 森林</span>'
    },
}

CSS_TEMPLATE = '''
* { margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI','Microsoft YaHei',sans-serif; }
body { background:linear-gradient(135deg,{bg} 0%,#0a0a1a 100%); color:#e0e0e0; min-height:100vh; padding:20px; display:flex; flex-direction:column; align-items:center; }
.topbar { width:100%; max-width:1200px; display:flex; align-items:center; gap:15px; margin-bottom:20px; padding:15px 20px; background:rgba(255,255,255,0.05); border-radius:12px; border:1px solid rgba(255,255,255,0.1); }
.topbar .back { color:{primary}; text-decoration:none; font-weight:600; white-space:nowrap; }
.topbar .back:hover { text-decoration:underline; }
.topbar .title { color:#fff; font-size:1.5rem; font-weight:bold; }
main { display:flex; flex-wrap:wrap; gap:20px; max-width:1200px; width:100%; }
.stage { flex:1; min-width:500px; background:rgba(0,0,0,0.3); border-radius:15px; padding:15px; border:1px solid rgba(255,255,255,0.1); }
.stage canvas { width:100%; display:block; border-radius:10px; background:rgba(0,0,0,0.5); }
.panel { width:320px; background:rgba(255,255,255,0.05); border-radius:15px; padding:20px; border:1px solid rgba(255,255,255,0.1); }
.panel h2 { color:{primary}; margin-bottom:15px; font-size:1.3rem; border-bottom:2px solid rgba(255,255,255,0.1); padding-bottom:8px; }
.panel p { line-height:1.7; font-size:0.95rem; color:#ccc; }
.legend { margin-top:15px; display:flex; flex-wrap:wrap; gap:10px; }
.legend .li { display:flex; align-items:center; gap:5px; font-size:0.85rem; color:#aaa; }
.controls { max-width:1200px; width:100%; display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-top:20px; padding:15px 20px; background:rgba(255,255,255,0.05); border-radius:12px; }
.controls button { padding:10px 18px; border:none; border-radius:8px; cursor:pointer; font-weight:600; transition:all 0.2s; background:rgba(255,255,255,0.1); color:#e0e0e0; }
.controls button:hover { background:rgba(255,255,255,0.2); transform:translateY(-1px); }
.controls button.primary { background:{primary}; color:white; }
.controls button.primary:hover { filter:brightness(1.2); }
.controls label { color:#aaa; display:flex; align-items:center; gap:8px; }
.controls input[type="range"] { width:100px; }
.controls .status { color:{secondary}; font-weight:600; margin-left:auto; }
@media(max-width:900px) { main{flex-direction:column;} .stage,.panel{width:100%;min-width:unset;} }
'''

def get_subject(filepath):
    rel = os.path.relpath(filepath, BASE)
    return rel.split(os.sep)[0]

def get_dirname(filepath):
    return os.path.basename(os.path.dirname(filepath))

def find_content(dirname):
    """根据目录名匹配内容描述"""
    for key, val in CONTENT.items():
        if key in dirname:
            return val
    return None

def render_file(filepath):
    subject = get_subject(filepath)
    dirname = get_dirname(filepath)
    theme = SUBJECT_THEMES.get(subject, SUBJECT_THEMES['物理'])
    content = find_content(dirname)
    
    # 从目录名提取标题（去掉括号中的补充说明）
    title = dirname
    # 清理标题
    title = re.sub(r'[（(].*?[）)]', '', title).strip()
    if not title:
        title = dirname
    
    if content:
        desc = content['desc']
        legend = content['legend']
    else:
        desc = f'本动画演示了{title}的过程和原理，通过交互式可视化帮助理解核心概念。'
        legend = f'<span class="li"><b style="color:{theme["primary"]}">●</b> 主要元素</span>'
    
    css = CSS_TEMPLATE.replace('{bg}', theme['bg']).replace('{primary}', theme['primary']).replace('{secondary}', theme['secondary'])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('%(title)s', title)
    html = html.replace('%(css)s', css)
    html = html.replace('%(desc)s', desc)
    html = html.replace('%(legend)s', legend)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'  OK: {dirname}')

def main():
    count = 0
    for root, dirs, files in os.walk(BASE):
        if '.workbuddy' in root:
            continue
        for fname in files:
            if fname == 'index.html':
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()
                if '%(title)s' in text:
                    render_file(fpath)
                    count += 1
    print(f'\n共渲染 {count} 个文件')

if __name__ == '__main__':
    main()
