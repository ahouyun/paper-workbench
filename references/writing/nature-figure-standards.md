# Nature 图表标准

## 核心原则

### 1. 信息层次 (Information Hierarchy)

**三级结构**：
- **主信息 (Level 1)**：图表要传达的核心信息
- **次信息 (Level 2)**：支持核心信息的细节
- **细节 (Level 3)**：补充说明，不干扰主要信息

**设计原则**：
- 一个图表一个核心信息
- 视觉焦点引导到主信息
- 避免信息过载

### 2. 自包含性 (Self-Containment)

**要求**：
- 图表应能独立理解
- 图注包含足够信息
- 不依赖正文解释

**图注结构**：
```
Fig. 1 | [标题] [简短描述]
[a-d] [各子图说明] [关键观察] [统计信息]
```

### 3. 色盲友好 (Color-Blind Friendly)

**推荐调色板**：
- 8 色调色板：#0072B2, #D55E00, #009E73, #CC79A7, #F0E442, #56B4E9, #E69F00, #000000
- 避免红绿同时使用
- 使用形状和纹理区分

---

## 图表类型

### 1. 核心发现图 (Main Finding)

**位置**：Figure 1

**功能**：展示论文最重要的发现

**设计**：
- 清晰的视觉层次
- 突出核心结果
- 简洁明了

**示例**：
- 实验结果对比
- 关键现象展示
- 核心机制图解

### 2. 机制图 (Mechanism)

**位置**：Figure 2-3

**功能**：解释背后的机制或原理

**设计**：
- 流程清晰
- 标注完整
- 逻辑连贯

**示例**：
- 信号通路
- 分子机制
- 算法流程

### 3. 验证图 (Validation)

**位置**：Figure 3-4

**功能**：验证核心发现的可靠性

**设计**：
- 多角度验证
- 统计信息完整
- 对照清晰

**示例**：
- 多组实验验证
- 不同条件测试
- 交叉验证结果

### 4. 应用图 (Application)

**位置**：Figure 4-5

**功能**：展示实际应用价值

**设计**：
- 应用场景明确
- 效果对比清晰
- 实用性强

**示例**：
- 实际案例展示
- 性能对比
- 应用效果

---

## 图表设计规范

### 1. 尺寸规范

**单栏图**：
- 宽度：89 mm (3.5 in)
- 高度：根据内容调整

**双栏图**：
- 宽度：183 mm (7.2 in)
- 高度：根据内容调整

**多面板图**：
- 面板间距：2-3 mm
- 标签字号：≥8 pt
- 坐标轴字号：≥6 pt

### 2. 字体规范

**推荐字体**：
- Arial (首选)
- Helvetica
- sans-serif 系列

**字号要求**：
- 图注：≥8 pt
- 坐标轴标签：≥6 pt
- 刻度标签：≥5 pt
- 内部标注：≥6 pt

### 3. 颜色规范

**调色板选择**：
```python
# Nature 推荐 8 色调色板
colors = [
    '#0072B2',  # 蓝
    '#D55E00',  # 橙
    '#009E73',  # 绿
    '#CC79A7',  # 粉
    '#F0E442',  # 黄
    '#56B4E9',  # 浅蓝
    '#E69F00',  # 深橙
    '#000000',  # 黑
]
```

**使用原则**：
- 避免红绿同时使用
- 使用形状和纹理辅助区分
- 背景色：白色或浅灰

### 4. 线条规范

**线条宽度**：
- 主要线条：1-1.5 pt
- 次要线条：0.5-1 pt
- 坐标轴：0.5-1 pt

**线条样式**：
- 实线：主要数据
- 虚线：参考线或次要数据
- 点线：趋势线

---

## matplotlib 配置

### rcParams 设置

```python
import matplotlib.pyplot as plt

# Nature 标准配置
plt.rcParams.update({
    # 字体
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans'],
    'svg.fonttype': 'none',  # 文本保持为文本节点
    
    # 字号
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    
    # 图形尺寸
    'figure.figsize': (7.2, 4.5),  # 双栏图默认尺寸
    'figure.dpi': 300,
    
    # 坐标轴
    'axes.linewidth': 0.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    
    # 刻度
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    
    # 图例
    'legend.frameon': False,
    'legend.borderpad': 0.3,
    
    # 保存
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})
```

### 输出格式

**首选格式**：
- SVG：矢量图，可编辑
- PDF：矢量图，通用
- EPS：矢量图，LaTeX 兼容

**备用格式**：
- PNG：300 dpi（彩图），600 dpi（线条图）
- TIFF：300 dpi，LZW 压缩

---

## 多面板图设计

### 布局原则

1. **逻辑分组**：相关面板放在一起
2. **视觉平衡**：避免某侧过重
3. **标签统一**：a, b, c, d 标签
4. **比例协调**：面板大小匹配重要性

### 常见布局

**2x2 布局**：
```
[a] [b]
[c] [d]
```

**1x3 布局**：
```
[a] [b] [c]
```

**混合布局**：
```
[a] [b]
[c] [d] [e]
```

### 面板间距

- 面板间距：2-3 mm
- 标签位置：左上角
- 标签字号：≥8 pt

---

## 图注写作

### 图注结构

```
Fig. 1 | [主标题]
[简短描述，1-2句]
[a] [子图a说明] [关键观察] [统计信息]
[b] [子图b说明] [关键观察] [统计信息]
[c] [子图c说明] [关键观察] [统计信息]
```

### 写作原则

1. **自包含**：不依赖正文
2. **简洁**：每句 ≤25 词
3. **具体**：包含关键数据
4. **清晰**：逻辑结构明确

### 示例

```
Fig. 1 | HT1 overexpression improves heat tolerance in rice.
a, Survival rates of wild-type (WT) and HT1-overexpressing (HT1-OE) plants 
   after heat stress (42°C, 3 days). n = 30 plants per genotype. 
   **P < 0.01, two-tailed t-test.
b, Relative expression of heat-shock genes in WT and HT1-OE plants. 
   Error bars, s.e.m. (n = 3 biological replicates).
c, Yield performance under control and heat stress conditions. 
   HT1-OE shows 30% higher yield under heat stress (P = 0.003).
```

---

## 常见错误

### 1. 信息过载

**问题**：一个图表包含太多信息

**解决**：
- 拆分为多个图表
- 突出核心信息
- 简化细节

### 2. 颜色问题

**问题**：红绿同时使用，色盲不友好

**解决**：
- 使用推荐调色板
- 辅以形状和纹理
- 测试色盲可读性

### 3. 字体过小

**问题**：图表中的文字难以辨认

**解决**：
- 字号 ≥6 pt
- 使用无衬线字体
- 高分辨率输出

### 4. 图注不完整

**问题**：图注信息不足，无法独立理解

**解决**：
- 包含完整信息
- 标注统计方法
- 说明样本量

---

## 自检清单

### 设计检查

- [ ] 信息层次清晰
- [ ] 一个图表一个核心信息
- [ ] 视觉焦点明确
- [ ] 避免信息过载

### 格式检查

- [ ] 尺寸符合规范
- [ ] 字体字号正确
- [ ] 颜色色盲友好
- [ ] 线条规范统一

### 内容检查

- [ ] 图注自包含
- [ ] 统计信息完整
- [ ] 标签清晰
- [ ] 逻辑连贯

### 输出检查

- [ ] 矢量图优先
- [ ] 分辨率足够
- [ ] 格式正确
- [ ] 命名规范
