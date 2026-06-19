# 交通流预测论文可视化模式深度分析

> 基于 STAEformer, PDFormer, DiffSTG, UrbanGPT, UniST, Graph WaveNet, MegaCRN, STID, GAMMA-Net, STM3 等顶级论文（2019-2026）的系统性分析。

---

## 一、Pipeline/Framework 图设计范式

### 1.1 四种主流架构图范式

**范式一：Sequential Block Pipeline（顺序模块流水线）**

以 Graph WaveNet 为代表，最经典的设计：
- 自左向右或自上而下的数据流向
- 分为 Input → Encoding → Processing → Output 四个阶段
- 每个阶段使用彩色矩形块表示不同模块
- 箭头连接各模块表示数据流
- 模块内部或旁边标注 tensor shape

**范式二：Transformer-based Block Design**

以 STAEformer 和 PDFormer 为代表：
- 分层嵌套结构：外层 Pipeline，内层 Attention Mechanism 细节
- 使用虚线框区分不同功能模块（Spatial Attention、Temporal Attention）
- Query/Key/Value 通常使用不同颜色编码
- PDFormer 引入 DTW Matrix 和 Traffic Pattern Set 的热力图可视化

**范式三：Encoder-Decoder with Diffusion**

DiffSTG 的架构图特点：
- Forward Diffusion Process（正向扩散）：从左到右，噪声逐渐增加
  - 渐变色表示噪声程度：深蓝→浅蓝→白色
  - 每步标注时间步 t
- Reverse Denoising Process（反向去噪）：从右到左，逐步恢复
  - 渐变色表示信号恢复：白色→浅绿→深绿
  - 条件箭头从历史观测指向每步去噪
- Conditioning Mechanism：cross-attention 连接历史观测与生成过程

**范式四：LLM-based Framework**

UrbanGPT 和 UniST 代表新兴范式：
- 分层结构：底部 ST-Encoder，中间 MLP 适配器，顶部 LLM 骨干
- ST-Encoder 用蓝色矩形块，LLM 骨干用灰色大矩形（标注如 Vicuna-7B）
- 适配器用橙色小矩形连接，数据流从下到上
- Instruction Tuning 范式：交通数据转换为自然语言指令
- 文本 token 和数值 token 的混合表示

**范式五：Mamba/SSM 架构（2024-2026新兴）**

核心挑战：如何可视化"选择性扫描"机制？

方案一：线性扫描流程图（ST-Mamba 风格）
```
输入序列 → [节点排序] → [线性扫描] → [选择性过滤] → 输出
                ↑
         图拓扑BFS序
```

方案二：多路扫描对比图（STM3 风格）
- 三个并行的扫描路径：空间扫描、时间扫描、联合扫描
- 每个路径用不同颜色表示
- 门控融合用箭头汇聚表示

方案三：GAT+Mamba 交替图（GAMMA-Net 风格）
- 交替排列的 GAT 层（蓝色）和 Mamba 层（橙色）
- 数据流自左向右
- 每层标注 tensor shape 变化

### 1.2 架构图三大布局模式

**模式A：自上而下流水线布局（最常见）**

以 PDFormer（AAAI 2023）为代表：
- 最上方：输入层（带有时空数据图标）
- 中间：多个处理模块纵向堆叠
- 最下方：输出层（预测结果）
- 模块间用箭头连接，箭头粗细表示数据维度变化
- 适用场景：单一流水线式处理架构

**模式B：左右对称/分支布局**

以 STAEformer 为代表：
- 左侧：空间编码分支
- 右侧：时间编码分支
- 中间：融合模块
- 底部：输出层
- 适用场景：双分支编码器架构

**模式C：环形/循环布局**

以 MegaCRN 为代表：
- 中心：核心处理单元（如 GRU cell）
- 环绕：记忆模块、图卷积模块
- 用循环箭头表示迭代过程
- 适用场景：具有迭代/循环结构的模型

### 1.3 模块命名规范

**通用组件：**
- Input Layer / Data Embedding Layer
- Positional Encoding / Spatial Embedding / Temporal Embedding
- Self-Attention / Cross-Attention / Multi-Head Attention
- Feed-Forward Network (FFN)
- Layer Normalization
- Prediction Head / Output Layer

**交通领域特有组件：**
- Spatial Dependency Module / Graph Convolution Layer
- Temporal Dependency Module / Dilated Causal Convolution
- Adaptive Adjacency Matrix / Self-Adaptive Graph
- Traffic Flow Pattern (TFP) Module
- Propagation Delay-Aware Module
- Memory Module / Prototype Memory

**创新点命名特点：**
- STAEformer: "Spatio-Temporal Adaptive Embedding"
- PDFormer: "Propagation Delay-Aware Dynamic Long-Range"
- MegaCRN: "Mega Memory" / "MegaBlock"
- DiffSTG: "Denoising Diffusion" / "Conditional Generation"

### 1.4 模块化封装规范

**子模块封装原则：**
- 每个功能模块用圆角矩形框包裹
- 模块内部用更小的组件表示子结构
- 使用虚线框表示可选/可替换模块
- 所有模块使用相同的圆角半径、阴影效果

**PDFormer 模块设计示例：**
```
┌─────────────────────────────────────┐
│  Historical Spatial-Temporal Block  │
│  ┌───────┐  ┌───────┐  ┌───────┐  │
│  │ Graph │  │  ST   │  │ Delay │  │
│  │ Attn  │→ │Embed  │→ │ Aware │  │
│  └───────┘  └───────┘  └───────┘  │
└─────────────────────────────────────┘
```

### 1.5 箭头样式与数据流

| 箭头类型 | 含义 | 使用场景 |
|---------|------|---------|
| 实线箭头 | 主要数据流 | 模块间连接 |
| 虚线箭头 | 辅助信息流/梯度流 | 残差连接、反馈 |
| 粗箭头 | 关键数据路径 | 核心数据流 |
| 双向箭头 | 交互或注意力机制 | 交叉注意力 |
| 弯曲箭头 | 残差连接或循环连接 | skip connection |

**数据流标注规范：**
- tensor shape：`[B, T, N, D]`（Batch, Time, Nodes, Dimension）
- 数学符号：`⊗` (矩阵乘法)、`⊕` (加法)、`σ` (sigmoid)

### 1.6 避免 AI 生成感的 6 个关键要素

1. **一致性**：所有模块使用相同的圆角半径、阴影效果、线宽
2. **对齐**：严格网格对齐，避免元素偏移
3. **留白**：模块间保持足够间距（至少 8pt）
4. **层次**：用颜色深浅表示层级关系，主次分明
5. **简约**：避免过多装饰（3D、渐变、阴影过度），保持专业感
6. **物理意义**：架构图要有物理/数学动机，不能只是为了好看

---

## 二、配色方案速查

### 2.1 主色调语义映射

| 用途 | 推荐颜色 | 色值 |
|------|---------|------|
| 输入数据/基础模块 | 蓝色系 | #4C78A8, #5B9BD5 |
| 核心创新模块 | 橙色系 | #E8864A, #FFA07A |
| 输出/预测结果 | 绿色系 | #59A14F, #7BC8A4 |
| 注意力机制/特殊组件 | 紫色系 | #9D78B8, #B07AA1 |
| 高亮/本文方法 | 红色系 | #E31A1C |
| 基准方法 | 灰色系 | #797068 |

### 2.2 三套标准配色方案

**方案一：经典学术配色**
```python
classic_academic = {
    'primary_blue': '#4C78A8',
    'secondary_orange': '#E8864A',
    'tertiary_green': '#59A14F',
    'accent_purple': '#9D78B8',
    'highlight_red': '#E31A1C',
    'baseline_gray': '#797068',
}
```

**方案二：色盲友好配色（推荐）**
```python
colorblind_friendly = {
    'blue': '#0072B2',
    'orange': '#E69F00',
    'green': '#009E73',
    'red': '#D55E00',
    'purple': '#CC79A7',
    'cyan': '#56B4E9',
}
```

**方案三：Nature/Science 风格**
```python
nature_style = {
    'red': '#E64B35',
    'blue': '#4DBBD5',
    'green': '#00A087',
    'purple': '#3C5488',
    'orange': '#F39B7F',
    'yellow': '#8491B4',
}
```

### 2.3 学术标准配色扩展

**蓝色系（主要组件）：**
- 深蓝（#003366）：核心模块
- 中蓝（#0066CC）：辅助模块
- 浅蓝（#66B2FF）：输入/输出

**橙色/红色系（强调）：**
- 橙色（#FF8C00）：关键创新点
- 红色（#CC0000）：注意力机制

**绿色系（数据流）：**
- 绿色（#00AA00）：数据流向
- 浅绿（#90EE90）：特征表示

**灰色系（背景/辅助）：**
- 浅灰（#F0F0F0）：背景
- 深灰（#666666）：文本/边框

### 2.4 架构组件配色速查

**Mamba/SSM 架构组件：**

| 组件 | 推荐颜色 | 说明 |
|------|---------|------|
| GNN/GAT 层 | 蓝色系 #4C78A8 | 空间建模 |
| Mamba 层 | 橙色系 #E8864A | 时间建模 |
| 门控融合 | 紫色系 #9D78B8 | 融合机制 |
| 输入/输出 | 绿色系 #59A14F | 数据流 |

**LLM/Foundation Model 架构组件：**

| 组件 | 推荐颜色 | 说明 |
|------|---------|------|
| ST-Encoder | 蓝色系 | 时空编码 |
| LLM 骨干 | 灰色系 #797068 | 冻结的预训练模型 |
| 适配器/投影层 | 橙色系 | 可训练组件 |
| 提示 token | 紫色系 | 任务引导 |
| 输出层 | 绿色系 | 预测结果 |

**各论文配色特点：**

| 论文 | 主色调 | 配色逻辑 |
|------|--------|---------|
| PDFormer | 蓝-橙对比 | 蓝色=空间，橙色=时间 |
| STAEformer | 蓝-橙-紫渐变 | 紫色=蓝+橙融合 |
| UrbanGPT | 蓝紫-橙 | 蓝紫=编码器，橙色=LLM骨干 |
| DiffSTG | 紫-橙渐变 | 紫色=前向，橙色=反向 |
| MegaCRN | 蓝-绿-灰 | 蓝色=GRU，绿色=记忆，灰色=图卷积 |

### 2.5 IEEE 格式配色规范

- 必须支持**黑白打印**可辨识（使用不同纹理/填充模式作为颜色的补充）
- 避免红绿组合（色盲不友好）
- 推荐使用 **ColorBrewer 2.0** 中的 colorblind-safe 调色板
- 热力图推荐使用 **Viridis** 或 **Plasma** colormap
- **避免使用 `jet` 色图**（视觉失真严重）

### 2.6 热力图色图选择

```python
heatmap_colormaps = {
    'attention': 'YlOrRd',
    'correlation': 'RdBu_r',
    'error': 'Reds',
    'flow': 'viridis',
    'speed': 'plasma',
}
```

| 类型 | X轴 | Y轴 | Colormap |
|------|-----|-----|----------|
| 注意力权重热力图 | Key 位置（时间步/空间节点） | Query 位置 | YlOrRd |
| DTW 相似性矩阵 | 传感器编号 | 传感器编号 | RdBu_r |
| 预测误差分布 | 时间（小时） | 传感器/路段编号 | Reds |

---

## 三、结果图（Results Figures）

### 3.1 多步预测折线图

**典型设计：**
- X 轴：时间步（15min, 30min, 60min 或更细粒度）
- Y 轴：预测值（流量/速度）
- 多条线：不同模型的预测结果
- 图例：放在图的外部右侧或下方

**线型规范：**

| 线型 | 用途 |
|------|------|
| 实线 `-` | 本文提出的方法 |
| 虚线 `--` | Baseline 方法 1 |
| 点线 `:` | Baseline 方法 2 |
| 点划线 `-.` | Baseline 方法 3 |

**STID 的结果图特点：**
- 使用 6 个子图（对应 PEMS03, PEMS04, PEMS07, PEMS08, METR-LA, PEMS-BAY）
- 每个子图包含 4-6 条折线（不同模型）
- 真实值用**黑色粗线**表示
- 提出的模型用**红色实线**突出显示

**预测结果对比图规范：**
- Ground Truth：黑色实线，线宽 2pt
- 预测模型：彩色虚线，线宽 1.5pt
- 置信区间：浅色阴影区域

**多步预测子图布局（STAEformer 风格）：**
- 使用 3-4 个子图展示不同预测步长
- 每个子图标题：`Horizon = 15min`, `30min`, `60min`
- 统一 Y 轴范围便于对比
- 用灰色虚线标注预测起始点

### 3.2 消融实验柱状图

**组件消融（Component Ablation）：**
- X 轴：不同组件组合（如 w/o Spatial ID, w/o Temporal ID, Full Model）
- Y 轴：性能指标（MAE, RMSE, MAPE）
- 分组柱状图，每组对应一个数据集
- 完整模型用**深色**突出，消融版本用**浅色**

**样式规范：**
- 柱宽：0.6-0.8，间距：0.2-0.4
- 同一指标用同一颜色
- 误差线：标准差或置信区间
- 用星号标注统计显著性（\*p<0.05, \*\*p<0.01）
- 用虚线标注基线性能
- 在柱顶标注具体数值
- 使用不同纹理区分（斜线、点、纯色）

```python
bar_chart_config = {
    'bar_width': 0.15,
    'group_gap': 0.3,
    'color_full': '#E31A1C',
    'color_ablated': '#B3CDE3',
    'hatch_pattern': '//',  # 黑白打印友好
    'error_bar': True,
    'font_size': 10,
}
```

### 3.3 效率对比图

**效率对比（Efficiency Comparison）：**
- 散点图或气泡图
- X 轴：模型参数量（Parameters）或训练时间
- Y 轴：预测精度（MAE/RMSE）
- 气泡大小：推理速度
- 理想位置：左下角（低参数量 + 高精度）

**参数量-精度散点图（2024新趋势）：**
```python
def plot_efficiency_scatter(models_data):
    """
    models_data: {name: {'params': M, 'mae': X, 'flops': G}}
    """
    fig, ax = plt.subplots(figsize=(5, 4))
    for name, data in models_data.items():
        size = data['flops'] * 10  # 气泡大小表示FLOPs
        ax.scatter(data['params'], data['mae'], s=size, label=name, alpha=0.7)
    ax.set_xlabel('Parameters (M)')
    ax.set_ylabel('MAE (60min)')
    ax.set_xscale('log')
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1))
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('efficiency_scatter.pdf', bbox_inches='tight')
```

**多维效率雷达图（新兴趋势）：**
- 维度：参数量、FLOPs、推理时间、GPU 内存、MAE
- 不同模型用不同颜色
- 面积越小越优

**效率-精度权衡散点图（LightST 风格）：**
- X 轴：推理时间（ms）
- Y 轴：MAE
- 每个点代表一个方法
- 用虚线连接教师模型和学生模型
- 标注速度提升倍数

### 3.4 热力图

**时空热力图设计要素：**
- X 轴：时间（24 小时或 7 天）
- Y 轴：传感器/路段编号
- 颜色条标注数值范围
- 用白色虚线标注特殊事件（如事故）

---

## 四、Case Study Figures（案例研究图）

### 4.1 预测值 vs 真实值对比图

**时间序列对比图设计：**
- X 轴：时间（通常展示 24 小时或一周）
- Y 轴：交通流量/速度值
- **蓝色实线**：真实值（Ground Truth）
- **红色虚线**：预测值（Prediction）
- **灰色阴影区域**：预测不确定性（Confidence Interval）
- **垂直虚线**标记预测起始点

**多传感器对比图：**
- 子图网格展示多个传感器的预测结果
- 按地理位置或传感器编号排列
- 统一的 Y 轴刻度便于横向比较

### 4.2 传感器选择策略

**常见选择标准：**
- **代表性传感器**：选择具有典型交通模式的传感器（如高峰时段流量变化明显的传感器）。STAEformer 选择 METR-LA 中流量波动最大的 3-5 个传感器进行可视化
- **不同区域**：选择来自不同地理区域的传感器，展示模型在不同位置的泛化能力。PDFormer 选择市区、郊区、高速路等不同类型的传感器
- **不同交通模式**：选择具有不同时间模式的传感器（如工作日 vs 周末、高峰 vs 非高峰）。MegaCRN 选择具有明显周期性模式和非周期性模式的传感器各若干个

**具体示例：**
- STAEformer 在 METR-LA 中选择 3 个传感器（ID: 0, 5, 10），分别代表高/中/低流量区域
- PDFormer 在 PEMS04 中选择 4 个传感器，覆盖不同地理位置和交通模式
- Graph WaveNet 在 PEMS-BAY 中选择 6 个传感器，展示自适应图学习的效果

**选择原则：**
- 选择**高流量**和**低流量**传感器对比
- 选择**稳定**和**波动大**的传感器对比
- 选择**模型表现好**和**表现差**的传感器分析原因
- 按地理位置选取代表性传感器

### 4.3 时间段选择

**常见选择标准：**
- **典型工作日**：选择周二至周四，避免周一和周五的特殊模式
- **包含高峰时段**：通常选择包含早高峰（7:00-9:00）和晚高峰（17:00-19:00）的时间段
- **连续时间段**：通常展示 24 小时或 48 小时的连续预测结果
- **特殊事件**：部分论文选择包含交通事故或特殊事件的时间段，展示模型的鲁棒性

**典型时间窗口：**

| 窗口类型 | 时长 | 目的 | 示例 |
|---------|------|------|------|
| 日周期窗口 | 24小时 | 展示完整日周期模式 | STAEformer 展示某天 0:00-24:00 |
| 跨天窗口 | 48小时 | 展示跨天预测效果 | PDFormer 长期预测实验 |
| 高峰聚焦窗口 | 2-3小时 | 聚焦高峰时段表现 | 早高峰 7:00-9:00 |

**其他对比维度：**
- **工作日 vs 周末**对比
- **高峰 vs 低峰**对比
- **正常天气 vs 恶劣天气**对比
- **突发事件**（如事故、施工）期间的表现

---

## 五、Table Patterns（表格模式）

### 5.1 主结果对比表

**标准格式：**
```
| Method | Year | METR-LA          | PEMS-BAY         | PEMS04           | PEMS08           |
|        |      | MAE↓ RMSE↓ MAPE↓ | MAE↓ RMSE↓ MAPE↓ | MAE↓ RMSE↓ MAPE↓ | MAE↓ RMSE↓ MAPE↓ |
|--------|------|------------------|------------------|------------------|------------------|
| DCRNN  | 2018 | ...              | ...              | ...              | ...              |
| STGCN  | 2018 | ...              | ...              | ...              | ...              |
| **Ours** | -- | **best**         | **best**         | **best**         | **best**         |
```

**格式规范：**
- **加粗**表示最优结果
- *斜体*或下划线表示次优结果
- 多列合并表示数据集名称
- 表注说明评估设置（预测步长、评估指标）

### 5.2 消融实验表

```
| Variant           | METR-LA MAE | PEMS-BAY MAE | PEMS04 MAE |
|-------------------|-------------|--------------|------------|
| Full Model        | **2.52**    | **1.52**     | **17.35**  |
| w/o Spatial Attn  | 2.61 (+3.6%)| 1.58 (+3.9%) | 18.12 (+4.4%) |
| w/o Temporal Attn | 2.65 (+5.2%)| 1.61 (+5.9%) | 18.45 (+6.3%) |
| w/o Adaptive Graph| 2.71 (+7.5%)| 1.64 (+7.9%) | 18.78 (+8.2%) |
```

### 5.3 效率对比表

```
| Method      | Params (M) | FLOPs (G) | Inference (ms) | GPU Mem (MB) | MAE (15min) |
|-------------|-----------|-----------|----------------|-------------|-------------|
| STGCN       | 0.5       | 1.2       | 2.3            | 256         | 2.71        |
| GWNet       | 0.8       | 3.5       | 8.7            | 512         | 2.69        |
| STID        | 0.3       | 0.8       | 3.1            | 128         | 2.60        |
| STAEformer  | 12.5      | 45.2      | 25.6           | 2048        | 2.49        |
| **Ours**    | **3.1**   | **8.5**   | **5.2**        | **512**     | **2.52**    |
```

---

## 六、字体、尺寸与标注规范

### 6.1 IEEE 格式字体设置

```python
ieee_font_config = {
    'font_family': 'serif',           # Times New Roman 或 Computer Modern
    'font_size_label': 10,            # 轴标签
    'font_size_title': 11,            # 标题
    'font_size_tick': 8,              # 刻度
    'font_size_legend': 9,            # 图例
    'font_size_annotation': 8,        # 标注
    'font_weight_title': 'bold',
}
```

**图表内文字推荐：**
- LaTeX 文档：Times New Roman 或 Computer Modern
- 图表内文字：Arial 或 Helvetica（无衬线，更清晰）
- 数学公式：CMU Serif 或 STIX

### 6.2 图表尺寸

**单栏图**：宽度 3.5 英寸（8.9cm），高度 2.5-3 英寸
**双栏图**：宽度 7 英寸（17.8cm），高度 3-4 英寸
**子图间距**：水平 0.2-0.3 英寸，垂直 0.2-0.3 英寸

```python
ieee_figure_sizes = {
    'single_column': (3.5, 2.625),    # 单栏宽度（英寸）
    'double_column': (7.16, 4.0),     # 双栏宽度
    'aspect_ratio_4_3': (4.0, 3.0),
    'aspect_ratio_16_9': (6.0, 3.375),
    'square': (3.5, 3.5),
}
```

**常见选择：**
- 架构图：双栏宽度（7.16 英寸），高度根据内容调整
- 结果图：单栏或双栏宽度
- 子图布局：2x2 或 2x3 网格

**坐标轴标注格式**：`变量名 (单位)`，如 `Time (hours)`, `Traffic Flow (vehicles/hour)`
**子图标签**：`(a)`, `(b)`, `(c)`，位置左上角，字号比正文大 2pt

### 6.3 DPI 设置

```python
dpi_settings = {
    'screen': 72,
    'draft': 150,
    'print': 300,        # IEEE 推荐
    'high_quality': 600,
}
```

### 6.4 标注风格规范

**组件标注：**
- 字体：Arial/Helvetica（无衬线）
- 字号：8-10pt
- 位置：组件内部或上方
- 格式：加粗组件名称，普通字体描述参数

**数据维度标注：**
- 在箭头旁标注张量形状：`(B, T, N, D)`
- 使用灰色小字
- 斜体表示可变维度

**公式/符号：**
- 使用斜体数学符号
- 关键操作用粗体：**Attention**, **GCN**
- 参数用等宽字体：`d_model=64`

---

## 七、Python 绘图代码模板

### 7.1 IEEE 学术风格设置

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

def set_ieee_style():
    mpl.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        'figure.figsize': (3.5, 2.625),
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'lines.linewidth': 1.5,
        'lines.markersize': 6,
        'axes.linewidth': 0.8,
        'axes.grid': True,
        'grid.alpha': 0.3,
        'grid.linewidth': 0.5,
        'legend.framealpha': 0.8,
        'legend.edgecolor': '0.8',
    })
```

### 7.2 多步预测折线图

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_multi_horizon_prediction(results_dict, horizons=[15, 30, 60]):
    """
    results_dict: {model_name: {'mae': [...], 'rmse': [...], 'mape': [...]}}
    """
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 2.5))
    metrics = ['mae', 'rmse', 'mape']
    metric_labels = ['MAE', 'RMSE', 'MAPE (%)']

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A', '#9D78B8']
    linestyles = ['-', '--', ':', '-.', '-']
    markers = ['o', 's', '^', 'D', 'v']

    for idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
        ax = axes[idx]
        for i, (model_name, values) in enumerate(results_dict.items()):
            ax.plot(horizons, values[metric],
                   color=colors[i % len(colors)],
                   linestyle=linestyles[i % len(linestyles)],
                   marker=markers[i % len(markers)],
                   label=model_name, linewidth=1.5, markersize=6)
        ax.set_xlabel('Prediction Horizon (min)')
        ax.set_ylabel(label)
        ax.set_xticks(horizons)
        ax.grid(True, alpha=0.3)
        if idx == 2:
            ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

    plt.tight_layout()
    plt.savefig('multi_horizon_prediction.pdf', bbox_inches='tight')
```

### 7.3 消融实验柱状图

```python
def plot_ablation_study(ablation_results, datasets):
    """
    ablation_results: {variant_name: {dataset: mae_value}}
    """
    fig, ax = plt.subplots(figsize=(7.16, 3.5))
    variants = list(ablation_results.keys())
    n_variants = len(variants)
    x = np.arange(len(datasets))
    width = 0.8 / n_variants

    colors = plt.cm.Set2(np.linspace(0, 1, n_variants))
    hatches = ['', '//', '\\\\', 'xx', '++', 'oo']

    for i, variant in enumerate(variants):
        values = [ablation_results[variant][ds] for ds in datasets]
        bars = ax.bar(x + i * width, values, width,
                     label=variant, color=colors[i],
                     hatch=hatches[i % len(hatches)],
                     edgecolor='black', linewidth=0.5)
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                   f'{val:.3f}', ha='center', va='bottom', fontsize=7)

    ax.set_xlabel('Dataset')
    ax.set_ylabel('MAE')
    ax.set_xticks(x + width * (n_variants - 1) / 2)
    ax.set_xticklabels(datasets)
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    ax.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('ablation_study.pdf', bbox_inches='tight')
```

### 7.4 注意力热力图

```python
def plot_attention_heatmap(attention_weights, x_labels=None, y_labels=None):
    fig, ax = plt.subplots(figsize=(4, 3.5))
    im = ax.imshow(attention_weights, cmap='YlOrRd', aspect='auto')
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Attention Weight', fontsize=10)
    if x_labels is not None:
        ax.set_xticks(np.arange(len(x_labels)))
        ax.set_xticklabels(x_labels, fontsize=8, rotation=45)
    if y_labels is not None:
        ax.set_yticks(np.arange(len(y_labels)))
        ax.set_yticklabels(y_labels, fontsize=8)
    ax.set_xlabel('Key Position')
    ax.set_ylabel('Query Position')
    plt.tight_layout()
    plt.savefig('attention_heatmap.pdf', bbox_inches='tight')
```

### 7.5 概率预测置信区间图（通用模板）

合并原 `plot_fan_chart` 与 `plot_probabilistic_prediction`，支持可选的采样轨迹展示：

```python
def plot_probabilistic_prediction(time_steps, samples, ground_truth,
                                   show_trajectories=True, max_trajectories=50):
    """
    通用概率预测可视化，支持置信区间和采样轨迹。
    适用于 DiffSTG、Conformalized ST-GCN 等概率预测模型。

    参数:
        time_steps: 时间步数组
        samples: (num_samples, time_steps) 多次采样结果
        ground_truth: 真实值数组
        show_trajectories: 是否展示单条采样轨迹
        max_trajectories: 最多展示的轨迹数
    """
    fig, ax = plt.subplots(figsize=(7.16, 3))

    # 可选：多条半透明采样轨迹
    if show_trajectories:
        for i in range(min(max_trajectories, samples.shape[0])):
            ax.plot(time_steps, samples[i], color='#E31A1C', alpha=0.1, linewidth=0.5)

    # 计算分位数
    q5 = np.percentile(samples, 5, axis=0)
    q25 = np.percentile(samples, 25, axis=0)
    q50 = np.percentile(samples, 50, axis=0)
    q75 = np.percentile(samples, 75, axis=0)
    q95 = np.percentile(samples, 95, axis=0)

    # 绘制置信区间
    ax.fill_between(time_steps, q5, q95, alpha=0.15, color='#E31A1C', label='90% CI')
    ax.fill_between(time_steps, q25, q75, alpha=0.3, color='#E31A1C', label='50% CI')
    ax.plot(time_steps, q50, color='#E31A1C', linewidth=2, label='Median')

    # 真实值
    ax.plot(time_steps, ground_truth, color='black', linewidth=2, label='Ground Truth')

    ax.set_xlabel('Time')
    ax.set_ylabel('Traffic Flow')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('probabilistic_prediction.pdf', bbox_inches='tight')
```

### 7.6 校准图（Calibration Plot）

```python
def plot_calibration_plot(nominal_coverage, actual_coverage):
    """
    nominal_coverage: [0.1, 0.2, ..., 0.9]
    actual_coverage: 实际覆盖率
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot([0, 1], [0, 1], 'k--', label='Perfect Calibration')
    ax.plot(nominal_coverage, actual_coverage, 'ro-', label='Our Model')
    ax.set_xlabel('Nominal Coverage')
    ax.set_ylabel('Actual Coverage')
    ax.legend(loc='best')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('calibration_plot.pdf', bbox_inches='tight')
```

### 7.7 预测对比时间序列图

```python
def plot_prediction_comparison(time_steps, ground_truth, predictions,
                                confidence_intervals=None):
    fig, ax = plt.subplots(figsize=(7.16, 3))
    ax.plot(time_steps, ground_truth, color='black', linewidth=2, label='Ground Truth')
    ax.plot(time_steps, predictions, color='#E31A1C', linewidth=1.5,
            linestyle='--', label='Prediction')
    if confidence_intervals is not None:
        lower, upper = confidence_intervals
        ax.fill_between(time_steps, lower, upper,
                       color='#E31A1C', alpha=0.2, label='95% CI')
    ax.axvline(x=time_steps[0], color='gray', linestyle=':', alpha=0.5)
    ax.text(time_steps[0], ax.get_ylim()[1], 'Forecast Start',
            ha='right', va='top', fontsize=8)
    ax.set_xlabel('Time')
    ax.set_ylabel('Traffic Flow')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('prediction_comparison.pdf', bbox_inches='tight')
```

### 7.8 时间误差热力图

```python
def plot_temporal_error_heatmap(error_matrix, hours=24, days=7):
    """
    error_matrix: (days, hours) 每天每小时的平均误差
    """
    fig, ax = plt.subplots(figsize=(8, 3))
    im = ax.imshow(error_matrix, cmap='YlOrRd', aspect='auto')
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Day of Week')
    ax.set_xticks(range(hours))
    ax.set_yticks(range(days))
    ax.set_yticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.colorbar(im, ax=ax, label='MAE')
    plt.tight_layout()
    plt.savefig('temporal_error_heatmap.pdf', bbox_inches='tight')
```

### 7.9 跨域迁移矩阵热力图

```python
def plot_transfer_matrix(transfer_results, datasets):
    """
    transfer_results: (n_source, n_target) MAE矩阵
    datasets: 数据集名称列表
    """
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(transfer_results, cmap='RdYlGn_r', aspect='auto')
    ax.set_xticks(range(len(datasets)))
    ax.set_yticks(range(len(datasets)))
    ax.set_xticklabels(datasets, rotation=45, ha='right')
    ax.set_yticklabels(datasets)
    ax.set_xlabel('Target Domain')
    ax.set_ylabel('Source Domain')
    plt.colorbar(im, ax=ax, label='MAE')
    for i in range(len(datasets)):
        ax.text(i, i, 'N/A', ha='center', va='center', color='gray')
    plt.tight_layout()
    plt.savefig('transfer_matrix.pdf', bbox_inches='tight')
```

---

## 八、图例放置模式

| 模式 | 代码 | 优点 | 缺点 |
|------|------|------|------|
| 外部右侧 | `loc='center left', bbox_to_anchor=(1, 0.5)` | 不遮挡数据 | 增加宽度 |
| 底部 | `loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3` | 节省水平空间 | 增加高度 |
| 最佳位置 | `loc='best'` | 自动选择 | 可能不稳定 |
| 子图外部共享 | `fig.legend(lines, labels, loc='lower center', ncol=4)` | 节省空间 | 适用场景有限 |

**图例位置**：优先右上角或下方，避免遮挡关键数据。

---

## 九、架构图绘制工具与格式要求

### 9.1 推荐工具

**高质量矢量绘图：**
- TikZ/LaTeX：最高质量，与 LaTeX 完美集成，适合架构图
- Adobe Illustrator / Inkscape：专业矢量绘图

**Python 学术图表：**
- Matplotlib + SciencePlots：学术图表标准
- Seaborn：统计图表
- Plotly：交互式图表

**快速原型：**
- draw.io (diagrams.net)：免费在线，模板丰富
- PPT/Keynote：最快速，格式转换麻烦

### 9.2 配色与检查工具

- ColorBrewer 2.0：学术图表专用配色方案
- Viz Palette：色盲友好检查
- Color Universal Design (CUD)：色盲友好配色指南

### 9.3 格式要求

- 矢量格式：PDF/EPS，避免位图
- 分辨率：至少 300 DPI（如必须用位图）
- 字体嵌入：确保所有字体已嵌入

---

## 十、论文可视化速查表（统一版）

按模型类型组织，每篇论文仅出现一次。

### 10.1 GNN 类

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| Graph WaveNet | Sequential Pipeline | 标准多步预测 | Self-Adaptive Adjacency Matrix |
| STGCN | Sequential Pipeline | 多步预测折线图 | 图卷积+门控时间卷积 |
| STGormer | 图 Transformer 架构 | 图建模性能对比 | 动态图演化图 |
| TopKNet | Top-K 节点选择 | 关键节点识别 | 节点重要性热力图 |
| FEDDGCN | 频域增强架构 | 频域分解效果 | 频谱分析图 |

### 10.2 Transformer 类

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| STAEformer | Transformer-based | 6 数据集表格对比 | Adaptive Embedding 注入方式 |
| PDFormer | Transformer-based | DTW 热力图 | Propagation Delay 示意图 |
| STID | MLP-based | 6 数据集+效率对比 | Spatial/Temporal ID 嵌入 |
| MegaCRN | Sequential+Memory | 消融实验+案例分析 | MegaBlock 内部结构 |
| PatchSTG | 空间分块示意图 | 效率-精度权衡散点图 | 训练速度对比柱状图 |
| M3-Net | 无图 MLP 架构 | MLP vs GNN 效率对比 | 参数量-性能散点图 |
| Latent Graph Learning | 隐图发现流程 | 隐图 vs 预定义图对比 | 学习图结构可视化 |
| Balance and Brighten | 双螺旋架构 | 物理一致性对比 | 流守恒验证图 |
| FairTP | 公平性框架流程 | 区域精度对比 | 公平性热力图 |
| LightST | 蒸馏流程图 | 效率-精度散点 | 速度提升柱状图 |
| ST-HCMs | 因果模型层次 | 因果识别准确率 | 因果图对比 |
| CASAformer | 因果注意力架构 | 事故预测精度对比 | 事故因果图 |
| WeaGAN++ | 天气融合架构图 | 天气-交通关联热力图 | 多模态融合图 |
| CityGPT | LLM 架构图 | 跨城市迁移热力图 | 多模态注意力图 |
| Decoder-only Pre-train | 预训练架构图 | 预训练 vs 从头训练对比 | 预训练效果曲线 |

### 10.3 Diffusion 类

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| DiffSTG | Encoder-Decoder+Diffusion | 多采样轨迹+置信区间 | 正向/反向扩散过程 |
| Double-Diffusion | ODE 先验流程 | CRPS 对比 | ODE 引导可视化 |
| DiffRefiner | 扩散细化过程 | 轨迹快照序列 | 去噪方向可视化 |
| GaussianFusion | 多传感器融合框架 | 融合精度对比 | 多传感器贡献可视化 |

### 10.4 Mamba/SSM 类

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| GAMMA-Net | GAT+Mamba 交替层 | 多数据集 MAE 对比 | 线性复杂度对比图 |
| STM3 (KDD'26) | 三路 Mamba 扫描 | MoE 消融实验 | 门控权重可视化 |
| Damba-ST | 领域自适应架构 | 零样本迁移矩阵 | 域偏移度量图 |
| SpoT-Mamba | 时空 Mamba 架构 | 多步预测对比 | 选择性扫描可视化 |

### 10.5 LLM / Foundation Model 类

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| UrbanGPT | LLM-based | Zero-shot/Few-shot 对比 | ST-Encoder 与 LLM 集成 |
| UniST | LLM-based | 多城市多任务对比 | Prompt 学习过程 |
| RAST | RAG 架构图 | 检索效果对比 | 检索模式可视化 |
| FlowDistill | LLM→MLP 蒸馏 | 多维度效率对比 | 蒸馏效果曲线 |
| Expand-and-Compress | 扩展-压缩时间线 | 持续学习性能曲线 | 容量变化图 |

### 10.6 安全/鲁棒性/其他

| 论文 | 架构图范式 | 结果图特点 | 创新可视化 |
|------|-----------|-----------|-------------|
| Stone | OOD 学习框架图 | OOD 检测热力图 | 偏移传播可视化 |
| STRAP | 检索增强框架图 | OOD 泛化性能对比 | 检索模式可视化 |
| Physics-Regularized | 物理约束架构图 | 缺失模式可视化 | 插补效果对比图 |
| Backtime | 后门攻击流程图 | 攻击成功率 vs 强度 | 触发器可视化 |
| DTP-Attack | 攻击流程图 | 成功率 vs 扰动 | 边界行走示意图 |
| Conformalized ST-GCN | 共形预测流程图 | 预测区间图 | 校准曲线图 |
| NuwaDynamics | 因果发现框架图 | 因果图演化序列 | 干预效果图 |
| CaPaint | 因果修复流程 | 提升百分比 | 因果区域热力图 |
| AutoSTF | NAS 搜索空间 DAG | 架构进化时间线 | 搜索过程动画 |
| FedGRU | 联邦学习拓扑图 | 隐私-性能权衡曲线 | 客户端分布地图 |
| Semi-Decentralized | 边缘部署拓扑图 | 延迟-精度权衡图 | 通信开销图 |
| DT-CTFP | 数字孪生架构 | 同步精度对比 | 数字孪生同步状态图 |
| MM-Path | 多模态融合框架 | 路径表示质量对比 | 跨模态注意力热力图 |
| PPTNet | 多粒度预测框架 | 粒度间一致性分析 | 多粒度联动图 |
| UrbanEV | 充电需求预测框架 | 需求预测对比 | 充电站分布热力图 |
| OracleTSC / SignalClaw | LLM+RL 信号控制 | 奖励曲线对比 | LLM 决策可视化 |

---

## 十一、概率预测与不确定性可视化

### 11.1 多采样轨迹展示

- 叠加展示 20-100 条采样轨迹
- 使用低透明度（alpha=0.1-0.3）避免遮挡
- 用不同颜色区分真实值和采样轨迹
- 突出展示轨迹的分散程度反映不确定性

### 11.2 置信区间扇形图

详见第七节代码模板 7.5（`plot_probabilistic_prediction`），支持：
- 多层置信区间：50% CI 深色、90% CI 浅色
- 可选的单条采样轨迹展示
- 中位数粗线突出

### 11.3 校准图

详见第七节代码模板 7.6（`plot_calibration_plot`）。

**校准曲线要点：**
- X 轴：名义覆盖水平
- Y 轴：经验覆盖水平
- 对角线虚线：完美校准
- 标注 ECE（Expected Calibration Error）

### 11.4 不确定性可视化规范

**置信区间图（DiffSTG 风格）：**
- 预测曲线：实线
- 95% 置信区间：深色阴影
- 80% 置信区间：浅色阴影
- 实际观测：散点或细线

**分位数预测图：**
- 展示多个分位数（10%, 25%, 50%, 75%, 90%）
- 使用渐变色带
- 中位数用粗线强调
- 使用半透明填充（alpha=0.3-0.5）

**预测区间图（Conformalized ST-GCN 风格）：**
- X 轴：时间步
- Y 轴：交通流量值
- 实线：点预测
- 阴影区域：90%/95% 预测区间
- 散点：真实观测值
- 用颜色标注区间宽度（窄=自信，宽=不确定）

---

## 十二、误差分析可视化

### 12.1 空间误差热力图

在地图上用颜色编码每个传感器的预测误差：
- 使用渐变色图（绿色=低误差，红色=高误差）
- 识别模型表现差的区域（如匝道合流区、复杂交叉口）

### 12.2 时间误差热力图

详见第七节代码模板 7.8（`plot_temporal_error_heatmap`）。

### 12.3 按交通状态分组的误差分析

| 交通状态 | 流量范围 | 典型 MAE | 特点 |
|---------|---------|---------|------|
| 自由流 | <500辆/小时 | 较低 | 模式简单，预测容易 |
| 轻度拥堵 | 500-1500 | 中等 | 模式复杂，需要空间建模 |
| 严重拥堵 | >1500 | 较高 | 高度非线性，最难预测 |

### 12.4 误差分布演化图

- 多个子图，每个子图对应一个时间窗口
- 核密度估计曲线展示误差分布的变化
- 标注模态数量的变化

---

## 十三、创新性可视化方法

### 13.1 3D 时空立方体

- X、Y 为地理坐标，Z 轴为时间
- 用颜色编码交通流量/速度
- 工具：PyVista、Plotly 3D、Three.js

### 13.2 动态可视化

- **时间动画**：在地图上动画展示交通流的时空演变
- 工具：kepler.gl、deck.gl、Folium 时间滑块

### 13.3 交互式可视化

- **Plotly/Dash 交互图表**：支持缩放、悬停查看详情
- **多视图联动**：地图视图和时间序列视图同步
- 工具：Streamlit、Dash、Bokeh

### 13.4 地理空间可视化

- **地图叠加**：在真实地图上用颜色/线条粗细表示预测值
- **流向图**：用箭头表示交通流方向和强度
- 工具：Folium、kepler.gl、Mapbox GL

---

## 十四、应避免的常见错误

| # | 错误 | 后果 | 正确做法 |
|---|------|------|---------|
| 1 | 信息过载 | 一张图太多线，难以阅读 | 每图最多 5-6 条线 |
| 2 | 缺少标注 | 读者无法理解图表 | 标注坐标轴、单位、图例 |
| 3 | 不一致比例尺 | 误导对比 | 所有子图统一 Y 轴范围 |
| 4 | 过度平滑 | 隐藏重要波动 | 保留原始数据特征 |
| 5 | 忽略色盲友好 | 8%男性读者无法区分 | 使用蓝橙/蓝黄组合 |
| 6 | 分辨率不足 | 打印模糊 | 至少 300 DPI |
| 7 | 缺少误差条 | 无法评估不确定性 | 展示置信区间或误差带 |
| 8 | 时间轴不一致 | 难以对比 | 统一时间窗口 |
| 9 | 图例遮挡数据 | 影响阅读 | 图例放在外部或空白区 |
| 10 | 缺少基线对比 | 无法评估性能 | 至少包含 2-3 个基线 |

---

## 十五、新兴可视化模式（2024-2026）

### 15.1 公平性可视化（FairTP, AAAI 2025）

**区域公平性热力图：**
- 地图上用颜色编码不同区域的预测精度
- 浅色=高精度，深色=低精度
- 对比公平性框架前后的精度分布变化

**传感器公平性时间线：**
- X 轴：时间
- Y 轴：各传感器的预测误差
- 用阴影标注哪些传感器被"牺牲"或"受益"

### 15.2 OOD 检测与鲁棒性可视化

**OOD 检测热力图（Stone, STRAP）：**
- X 轴：时间步，Y 轴：空间节点
- 颜色：OOD 检测分数（红色=OOD，蓝色=正常）
- 用虚线标注分布偏移发生的时间点

**变化点检测图（Latent Dynamics-Aware OOD, 2026）：**
- X 轴：时间步，Y 轴：预测误差
- 用竖虚线标注检测到的变化点
- 用不同颜色区分分布内/分布外区域

**OOD 泛化性能对比图：**
- X 轴：不同 OOD 场景（空间偏移、时间偏移、联合偏移）
- Y 轴：性能下降百分比
- 分组柱状图：不同方法在各场景下的表现

### 15.3 因果图可视化（ST-HCMs, NuwaDynamics）

**因果图对比：**
- 左图：预定义邻接矩阵（无向）
- 右图：学习的因果图（有向）
- 用箭头粗细表示因果强度
- 用颜色区分正/负因果关系

**因果发现动画帧：**
- 多个时间步的因果图快照
- 用颜色标注新增/删除的因果关系

**干预效果可视化：**
- 左侧：原始因果图
- 中间：干预操作（do(X=x)）
- 右侧：干预后的预测分布

### 15.4 知识蒸馏可视化（LightST, FlowDistill）

**知识蒸馏流程图：**
- 教师模型（大，复杂）→ 蒸馏 → 学生模型（小，简单）
- 用箭头标注空间知识和时间知识的流动
- 用颜色区分不同类型的蒸馏损失

### 15.5 黑盒攻击可视化（DTP-Attack, Backtime）

**攻击成功率 vs 扰动大小：**
- X 轴：扰动大小（米），Y 轴：攻击成功率（%）
- 多条线：不同攻击方法对比
- 标注"不可感知"阈值

**攻击触发器可视化：**
- 时间序列图展示正常样本和受攻击样本
- 用红色标注触发器注入位置
- 对比正常预测和受攻击预测

**防御效果可视化：**
- X 轴：攻击强度，Y 轴：预测误差
- 多条线：无防御、不同防御方法
- 用虚线标注"可接受"误差阈值

### 15.6 城市基础模型可视化（CityGPT, UrbanMind）

**跨城市迁移热力图：**
- X 轴：目标城市，Y 轴：源城市
- 颜色深浅：迁移性能（MAE 降低百分比）
- 对角线：本地训练性能

**多模态注意力可视化：**
- 用热力图展示不同模态（文本、图像、时空）的注意力权重
- 用箭头展示跨模态信息流动

### 15.7 NAS 搜索过程可视化（AutoSTF）

**搜索空间可视化：**
- 用有向无环图（DAG）展示搜索空间
- 每个节点代表一个操作（卷积、注意力、跳跃连接）
- 用颜色标注被选中的操作

**架构进化时间线：**
- X 轴：搜索迭代次数，Y 轴：验证性能
- 标注发现的最优架构

### 15.8 联邦学习可视化（FedGRU, Heterogeneous-Aware FL）

**客户端分布地图：**
- 在城市地图上标注不同客户端（传感器区域）
- 用颜色区分不同数据分布类型
- 用圆圈大小标注本地数据量

**隐私-性能权衡曲线：**
- X 轴：隐私保护强度（ε值），Y 轴：预测性能（MAE）
- 标注"可接受"的隐私-性能区域

### 15.9 安全预测可视化（CASAformer, PPTNet）

**事故因果图：**
- 用有向图展示事故因果关系
- 节点：事故类型、天气、时间、路况
- 边：因果强度（用粗细表示）

**多粒度事故预测图：**
- 宏观：城市级事故热点地图
- 中观：路段级事故概率时间序列
- 微观：单点事故特征雷达图

### 15.10 数字孪生可视化（DT-CTFP, DTROS）

**数字孪生同步状态图：**
- 左侧：真实世界传感器数据流
- 右侧：数字孪生模型状态
- 中间：同步状态指示器（绿色=同步，红色=失步）

**仿真-现实差距热力图：**
- X 轴：时间，Y 轴：空间位置
- 颜色：仿真与现实的预测误差

### 15.11 多模态路径可视化（MM-Path）

**多模态路径表示图：**
- 底层：路网拓扑图
- 中层：街景图像拼接
- 上层：POI 语义标签云
- 用箭头展示路径的多模态信息聚合

**跨模态注意力热力图：**
- X 轴：路径节点，Y 轴：模态类型（图像、文本、交通）
- 颜色：注意力权重

### 15.12 天气感知可视化（WeaGAN++, WA-STNet）

**天气-交通关联热力图：**
- X 轴：天气类型（晴、雨、雪、雾），Y 轴：交通指标（流量、速度、密度）
- 用数字标注具体相关系数

**多模态天气融合图：**
- 左侧：气象数据时间序列
- 中间：交通数据热力图
- 右侧：融合后的预测结果

### 15.13 缺失数据插补可视化（Physics-Regularized）

**缺失模式可视化：**
- X 轴：时间，Y 轴：传感器编号
- 颜色：数据可用性（白色=缺失，蓝色=可用）
- 用不同图案标注不同缺失类型（随机缺失、块状缺失、渐进缺失）

**插补效果对比图：**
- 原始数据 vs 缺失数据 vs 插补结果
- 用灰色区域标注缺失区间

### 15.14 边缘部署可视化（Semi-Decentralized, FedGCN）

**边缘计算拓扑图：**
- 节点大小：计算能力
- 边粗细：通信带宽
- 用颜色标注设备类型（传感器、边缘服务器、云）

**延迟-精度权衡图：**
- X 轴：推理延迟（ms），Y 轴：预测精度（MAE）
- 用虚线连接集中式和去中心化方案

### 15.15 跨域迁移可视化（Damba-ST/FlashST 风格）

详见第七节代码模板 7.9（`plot_transfer_matrix`）。

### 15.16 持续学习可视化（Expand-and-Compress）

**Expand-and-Compress 时间线图：**
- X 轴：时间步/数据流
- Y 轴：模型容量（参数量或 prompt 数量）
- 扩展阶段：容量增加（上升曲线）
- 压缩阶段：容量减少（下降曲线）

**性能随时间变化的折线图：**
- X 轴：时间/数据流批次，Y 轴：MAE
- 多条线：不同持续学习策略
- 用竖虚线标注分布漂移发生的时间点

### 15.17 LLM+RL 信号控制可视化（OracleTSC, SignalClaw）

**LLM 决策可视化：**
- 左侧：交通状态（车流量、排队长度）
- 中间：LLM 推理过程（Chain-of-Thought 文本）
- 右侧：信号控制动作
- 用颜色标注不同 LLM 角色（critic、teacher、skill generator）

**奖励门控可视化：**
- X 轴：训练迭代，Y 轴：奖励值
- 实线：LLM 策略奖励，虚线：门控阈值

### 15.18 EV 充电需求可视化（UrbanEV）

**充电站分布热力图：**
- 城市地图上标注充电站位置
- 颜色深浅：充电需求强度
- 圆圈大小：充电站容量

---

---

## 十六、Mamba 架构可视化模式（2024-2026 新兴）

### 16.1 选择性扫描机制可视化

**适用场景：** 当论文提出基于 Mamba/SSM 的交通预测模型，需要向读者解释 Selective Scan 如何处理时空数据时使用。

**传达信息：** Mamba 的核心创新在于选择性扫描（Selective Scan）机制——通过输入依赖的门控动态决定保留或遗忘哪些信息，而非 Transformer 的全局注意力。

**实际案例：**
- **GAMMA-Net**：将图拓扑的 BFS 序作为扫描顺序，展示节点如何沿空间结构进行线性扫描
- **FAST (ICLR'25)**：展示频域增强的 Mamba 扫描，将时域信号变换到频域后再进行选择性过滤
- **SpoT-Mamba**：展示时空联合扫描路径，空间维度和时间维度交替扫描

**可视化方案一：线性扫描流程图**

展示数据沿序列维度的单向扫描过程，用颜色编码门控值（高保留=深色，低保留=浅色）。

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_selective_scan_flow(scan_sequence, gate_values, node_labels=None):
    """
    可视化 Mamba 选择性扫描的数据流。

    参数:
        scan_sequence: 扫描序列的特征矩阵 (seq_len, feature_dim)
        gate_values: 每步的门控值 (seq_len,)，范围 [0, 1]
        node_labels: 节点标签列表
    """
    seq_len = len(gate_values)
    fig, axes = plt.subplots(2, 1, figsize=(7.16, 3.5),
                              gridspec_kw={'height_ratios': [1, 0.4]})

    # 上图：特征热力图，颜色编码门控值
    ax1 = axes[0]
    # 用门控值调制特征显示
    masked_features = scan_sequence * gate_values[:, np.newaxis]
    im = ax1.imshow(masked_features.T, cmap='viridis', aspect='auto',
                    extent=[0, seq_len, 0, scan_sequence.shape[1]])
    ax1.set_ylabel('Feature Dimension')
    ax1.set_title('Selective Scan: Feature Retention by Gate Value')
    plt.colorbar(im, ax=ax1, label='Activated Feature Value')

    # 下图：门控值条形图
    ax2 = axes[1]
    colors = plt.cm.RdYlGn(gate_values)  # 绿色=保留，红色=遗忘
    ax2.bar(range(seq_len), gate_values, color=colors, width=0.8)
    ax2.set_xlabel('Scan Position (BFS Order)')
    ax2.set_ylabel('Gate Value')
    ax2.set_ylim(0, 1.1)
    ax2.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)

    if node_labels:
        ax2.set_xticks(range(seq_len))
        ax2.set_xticklabels(node_labels, fontsize=7, rotation=45)

    plt.tight_layout()
    plt.savefig('selective_scan_flow.pdf', bbox_inches='tight')
```

**可视化方案二：门控热力图叠加图拓扑**

在图结构上用颜色编码每个节点的门控值，展示空间扫描中哪些节点被选择性保留。

```python
import networkx as nx

def plot_scan_on_graph(adj_matrix, gate_values, pos=None, node_labels=None):
    """
    在图拓扑上可视化选择性扫描的门控值。

    参数:
        adj_matrix: 邻接矩阵 (N, N)
        gate_values: 每个节点的门控值 (N,)
        pos: 节点位置字典，None 则自动布局
    """
    G = nx.from_numpy_array(adj_matrix)
    if pos is None:
        pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(5, 4))

    # 节点颜色编码门控值
    node_colors = gate_values
    nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors,
                                    cmap='RdYlGn', vmin=0, vmax=1,
                                    node_size=200, ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)

    if node_labels:
        nx.draw_networkx_labels(G, pos, node_labels, font_size=8, ax=ax)

    # 标注扫描顺序
    scan_order = np.argsort(-gate_values)  # 按门控值降序
    for rank, node in enumerate(scan_order[:5]):  # 标注前5个
        ax.annotate(f'Scan #{rank+1}', xy=pos[node],
                   xytext=(10, 10), textcoords='offset points',
                   fontsize=7, color='red',
                   arrowprops=dict(arrowstyle='->', color='red', lw=0.8))

    plt.colorbar(nodes, ax=ax, label='Gate Value (Retain/Discard)')
    ax.set_title('Selective Scan Gate Values on Graph Topology')
    plt.tight_layout()
    plt.savefig('scan_on_graph.pdf', bbox_inches='tight')
```

### 16.2 Mamba vs Transformer 架构对比图

**适用场景：** 当需要对比 Mamba 架构与 Transformer 架构在交通预测中的差异时使用。

**传达信息：** Mamba 的线性复杂度 O(n) vs Transformer 的二次复杂度 O(n^2)，以及在长序列建模中的效率优势。

**实际案例：**
- **GAMMA-Net**：用 GAT+Mamba 交替层对比纯 GAT+Transformer 方案，展示精度-效率权衡
- **STM3 (KDD'26)**：三路 Mamba 扫描（空间、时间、联合）对比单路 Transformer 注意力

**可视化方案：复杂度-序列长度曲线**

```python
def plot_complexity_comparison():
    """
    Mamba vs Transformer 复杂度对比曲线。
    """
    seq_lengths = np.logspace(1, 4, 100)  # 10 to 10000

    # 复杂度模型
    transformer_flops = seq_lengths ** 2 * 1e-4  # O(n^2)
    mamba_flops = seq_lengths * 1e-2              # O(n)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(seq_lengths, transformer_flops, '--', color='#E31A1C',
            linewidth=2, label='Transformer O(n²)')
    ax.plot(seq_lengths, mamba_flops, '-', color='#4C78A8',
            linewidth=2, label='Mamba O(n)')

    # 标注交叉点
    cross_idx = np.argmin(np.abs(transformer_flops - mamba_flops))
    ax.axvline(x=seq_lengths[cross_idx], color='gray', linestyle=':', alpha=0.5)
    ax.annotate(f'Crossover\nN={int(seq_lengths[cross_idx])}',
               xy=(seq_lengths[cross_idx], mamba_flops[cross_idx]),
               xytext=(30, -30), textcoords='offset points',
               fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'))

    # 标注交通预测常用序列长度
    for n, label in [(12, '1h (5min)'), (288, '1day'), (2016, '1week')]:
        ax.axvline(x=n, color='green', linestyle='-.', alpha=0.3)
        ax.text(n, ax.get_ylim()[1]*0.9, label, fontsize=7,
               ha='center', color='green')

    ax.set_xlabel('Sequence Length N')
    ax.set_ylabel('Computational Cost (FLOPs, relative)')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_title('Computational Complexity: Mamba vs Transformer')
    plt.tight_layout()
    plt.savefig('mamba_vs_transformer_complexity.pdf', bbox_inches='tight')
```

**可视化方案：交替架构对比图（GAMMA-Net 风格）**

用并排的子图展示 GAT+Mamba 交替方案 vs GAT+Transformer 交替方案的架构差异，标注每层的参数量和计算量。

### 16.3 Mamba 多路扫描对比图（STM3 风格）

**适用场景：** 当模型使用多路并行 Mamba 扫描（空间扫描、时间扫描、联合扫描）时使用。

**传达信息：** 不同扫描路径捕获不同类型的时空依赖，门控融合机制动态加权各路输出。

```python
def plot_multi_path_scan(spatial_gate, temporal_gate, joint_gate, fusion_weights):
    """
    可视化三路 Mamba 扫描的门控融合。

    参数:
        spatial_gate: 空间扫描门控值 (seq_len,)
        temporal_gate: 时间扫描门控值 (seq_len,)
        joint_gate: 联合扫描门控值 (seq_len,)
        fusion_weights: 融合权重 (seq_len, 3)
    """
    fig, axes = plt.subplots(2, 1, figsize=(7.16, 4))

    # 上图：三路门控值对比
    ax1 = axes[0]
    x = range(len(spatial_gate))
    ax1.plot(x, spatial_gate, '-', color='#4C78A8', label='Spatial Scan', linewidth=1.5)
    ax1.plot(x, temporal_gate, '--', color='#E8864A', label='Temporal Scan', linewidth=1.5)
    ax1.plot(x, joint_gate, ':', color='#9D78B8', label='Joint Scan', linewidth=1.5)
    ax1.set_ylabel('Gate Value')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_title('Multi-Path Selective Scan Gate Values')
    ax1.grid(True, alpha=0.3)

    # 下图：融合权重堆叠面积图
    ax2 = axes[1]
    ax2.stackplot(x,
                  fusion_weights[:, 0], fusion_weights[:, 1], fusion_weights[:, 2],
                  labels=['Spatial', 'Temporal', 'Joint'],
                  colors=['#4C78A8', '#E8864A', '#9D78B8'], alpha=0.7)
    ax2.set_xlabel('Scan Position')
    ax2.set_ylabel('Fusion Weight')
    ax2.set_ylim(0, 1)
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_title('Gated Fusion Weights')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('multi_path_scan.pdf', bbox_inches='tight')
```

---

## 十七、基础模型评估可视化模式（2024-2026）

### 17.1 Zero-shot vs Fine-tuned 对比图

**适用场景：** 当论文提出交通基础模型（Foundation Model），需要展示预训练模型在未见数据集上的零样本泛化能力时使用。

**传达信息：** 基础模型即使未经目标域微调，也能达到接近或超过从头训练的专用模型的性能，说明模型学到了通用的时空知识。

**实际案例：**
- **UrbanGPT (KDD'24)**：在 PEMS03/04/07/08 上对比 Zero-shot、Few-shot（10%数据）、Full-shot 三种设置
- **UniST (KDD'24)**：跨 6 个城市数据集的 Zero-shot 迁移评估
- **CityGPT**：跨城市 Zero-shot 对比，展示不同城市间的迁移难度差异

**可视化方案：分组柱状图 + 性能差距标注**

```python
def plot_zero_shot_comparison(zero_shot, few_shot, full_shot, datasets, metric='MAE'):
    """
    Zero-shot vs Few-shot vs Full-shot 性能对比。

    参数:
        zero_shot: {dataset: value} 零样本性能
        few_shot: {dataset: value} 少样本性能
        full_shot: {dataset: value} 全量数据性能
        datasets: 数据集名称列表
    """
    fig, ax = plt.subplots(figsize=(7.16, 3.5))
    x = np.arange(len(datasets))
    width = 0.25

    colors = ['#4C78A8', '#E8864A', '#59A14F']
    hatches = ['', '//', '\\\\']

    for i, (name, values, color, hatch) in enumerate(zip(
        ['Zero-shot', 'Few-shot (10%)', 'Full-shot'],
        [zero_shot, few_shot, full_shot],
        colors, hatches
    )):
        vals = [values[ds] for ds in datasets]
        bars = ax.bar(x + i * width, vals, width, label=name,
                     color=color, hatch=hatch, edgecolor='black', linewidth=0.5)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                   f'{val:.2f}', ha='center', va='bottom', fontsize=7)

    # 标注 Zero-shot 与 Full-shot 的性能差距
    for j, ds in enumerate(datasets):
        gap = (zero_shot[ds] - full_shot[ds]) / full_shot[ds] * 100
        color = '#E31A1C' if gap > 10 else '#59A14F'
        ax.annotate(f'Gap: {gap:.1f}%',
                   xy=(x[j] + width, max(zero_shot[ds], full_shot[ds])),
                   xytext=(0, 15), textcoords='offset points',
                   fontsize=7, color=color, ha='center')

    ax.set_xlabel('Dataset')
    ax.set_ylabel(metric)
    ax.set_xticks(x + width)
    ax.set_xticklabels(datasets, rotation=15)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_title('Zero-shot vs Fine-tuned Performance')
    plt.tight_layout()
    plt.savefig('zero_shot_comparison.pdf', bbox_inches='tight')
```

### 17.2 跨城市迁移可视化

**适用场景：** 当模型在多个城市间进行迁移学习评估时使用。

**传达信息：** 哪些城市对之间的迁移最有效，哪些城市作为源域/目标域最优，迁移学习相比从头训练的提升幅度。

**实际案例：**
- **CityGPT**：6 城市间的迁移矩阵热力图
- **Damba-ST (ICDE'26)**：领域自适应的跨城市迁移，展示域偏移度量

**可视化方案：迁移矩阵热力图 + 对角线标注本地性能**

详见第七节代码模板 7.9（`plot_transfer_matrix`）。扩展版本增加：
- 对角线标注本地训练性能
- 每个单元格标注迁移提升/下降百分比
- 用箭头标注最优迁移路径

```python
def plot_transfer_matrix_enhanced(transfer_results, local_performance, datasets):
    """
    增强版迁移矩阵：包含本地性能和迁移增益。

    参数:
        transfer_results: (n_source, n_target) MAE 矩阵
        local_performance: {dataset: local_mae} 本地训练性能
        datasets: 数据集名称列表
    """
    n = len(datasets)
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(transfer_results, cmap='RdYlGn_r', aspect='auto')
    plt.colorbar(im, ax=ax, label='MAE (lower is better)')

    for i in range(n):
        for j in range(n):
            if i == j:
                ax.text(j, i, f'{local_performance[datasets[i]]:.2f}\n(Local)',
                       ha='center', va='center', fontsize=7, fontweight='bold')
            else:
                gain = (local_performance[datasets[j]] - transfer_results[i, j]) / \
                       local_performance[datasets[j]] * 100
                color = 'white' if transfer_results[i, j] > np.median(transfer_results) else 'black'
                ax.text(j, i, f'{transfer_results[i, j]:.2f}\n({gain:+.1f}%)',
                       ha='center', va='center', fontsize=7, color=color)

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(datasets, rotation=45, ha='right')
    ax.set_yticklabels(datasets)
    ax.set_xlabel('Target Domain')
    ax.set_ylabel('Source Domain')
    ax.set_title('Cross-City Transfer Learning Matrix')
    plt.tight_layout()
    plt.savefig('transfer_matrix_enhanced.pdf', bbox_inches='tight')
```

### 17.3 Regime-Dependent Failure 可视化（ICML 2026 Workshop）

**适用场景：** 当需要分析基础模型在不同交通状态（regime）下的失败模式时使用。

**传达信息：** 基础模型并非在所有情况下都优于专用模型，某些特定交通状态（如极端拥堵、事故、天气异常）下可能出现性能退化。

**可视化方案：按交通状态分组的性能对比**

```python
def plot_regime_dependent_performance(regime_results, methods, regimes):
    """
    不同交通状态下的模型性能对比。

    参数:
        regime_results: {method: {regime: mae_value}}
        methods: 方法名称列表
        regimes: 交通状态列表，如 ['Free-flow', 'Moderate', 'Heavy', 'Incident']
    """
    fig, ax = plt.subplots(figsize=(7.16, 3.5))
    x = np.arange(len(regimes))
    n_methods = len(methods)
    width = 0.8 / n_methods

    # 标记基础模型
    foundation_models = ['UrbanGPT', 'UniST', 'CityGPT']
    colors = ['#4C78A8' if m in foundation_models else '#797068' for m in methods]
    markers = ['o' if m in foundation_models else 's' for m in methods]

    for i, method in enumerate(methods):
        values = [regime_results[method][r] for r in regimes]
        ax.bar(x + i * width, values, width, label=method,
              color=colors[i], alpha=0.8, edgecolor='black', linewidth=0.5)

    # 标注基础模型表现差的 regime
    for j, regime in enumerate(regimes):
        for fm in foundation_models:
            best_specialized = min(regime_results[m][regime]
                                   for m in methods if m not in foundation_models)
            fm_val = regime_results[fm][regime]
            if fm_val > best_specialized * 1.1:  # 超过专用模型 10% 以上
                ax.annotate('Failure!',
                           xy=(x[j] + methods.index(fm) * width, fm_val),
                           xytext=(0, 10), textcoords='offset points',
                           fontsize=7, color='red', ha='center',
                           fontweight='bold')

    ax.set_xlabel('Traffic Regime')
    ax.set_ylabel('MAE')
    ax.set_xticks(x + width * (n_methods - 1) / 2)
    ax.set_xticklabels(regimes)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_title('Regime-Dependent Performance: Foundation vs Specialized Models')
    plt.tight_layout()
    plt.savefig('regime_dependent_performance.pdf', bbox_inches='tight')
```

**可视化方案：雷达图展示各 regime 下的相对性能**

```python
def plot_regime_radar(results, methods, regimes):
    """
    雷达图展示不同交通状态下的模型性能。
    面积越小越优（MAE 越低越好）。
    """
    n_regimes = len(regimes)
    angles = np.linspace(0, 2 * np.pi, n_regimes, endpoint=False).tolist()
    angles += angles[:1]  # 闭合

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

    for method in methods:
        values = [results[method][r] for r in regimes]
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=1.5, label=method)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(regimes, fontsize=9)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=8)
    ax.set_title('Performance Across Traffic Regimes\n(lower = better)', fontsize=10)
    plt.tight_layout()
    plt.savefig('regime_radar.pdf', bbox_inches='tight')
```

---

## 十八、概率预测可视化模式（2024-2026）

### 18.1 不确定性量化总览图

**适用场景：** 当论文提出概率预测模型（如 Diffusion Model、Bayesian 方法、Conformal Prediction）时使用。

**传达信息：** 模型不仅给出点预测，还能量化预测的不确定性，为决策提供置信度信息。

**实际案例：**
- **DiffSTG (KDD'24)**：扩散模型生成多条采样轨迹，用分位数区间展示不确定性
- **Conformalized ST-GCN**：共形预测给出理论保证的预测区间
- **Double-Diffusion (2025)**：ODE 先验引导的扩散，展示更紧凑的预测区间

**四合一不确定性可视化面板：**

```python
def plot_uncertainty_panel(time_steps, samples, ground_truth,
                           nominal_coverage, actual_coverage,
                           sharpness_by_horizon, crps_by_method):
    """
    四合一不确定性量化面板。
    包含：(a) 预测区间图, (b) 校准图, (c) 区间宽度随预测步变化, (d) CRPS 对比。

    参数:
        time_steps: 时间步数组
        samples: (num_samples, time_steps) 采样结果
        ground_truth: 真实值
        nominal_coverage: 名义覆盖水平列表
        actual_coverage: 实际覆盖水平列表
        sharpness_by_horizon: {horizon: avg_interval_width}
        crps_by_method: {method_name: crps_value}
    """
    fig, axes = plt.subplots(2, 2, figsize=(7.16, 5))

    # (a) 预测区间图
    ax = axes[0, 0]
    q10 = np.percentile(samples, 10, axis=0)
    q50 = np.percentile(samples, 50, axis=0)
    q90 = np.percentile(samples, 90, axis=0)
    ax.fill_between(time_steps, q10, q90, alpha=0.2, color='#E31A1C', label='80% PI')
    ax.plot(time_steps, q50, color='#E31A1C', linewidth=1.5, label='Median')
    ax.plot(time_steps, ground_truth, 'k-', linewidth=1.5, label='Ground Truth')
    ax.set_xlabel('Time')
    ax.set_ylabel('Traffic Flow')
    ax.legend(fontsize=7)
    ax.set_title('(a) Prediction Intervals')
    ax.grid(True, alpha=0.3)

    # (b) 校准图
    ax = axes[0, 1]
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Perfect')
    ax.plot(nominal_coverage, actual_coverage, 'ro-', markersize=4, label='Model')
    ax.fill_between(nominal_coverage, nominal_coverage, actual_coverage,
                    alpha=0.2, color='red')
    ece = np.mean(np.abs(np.array(nominal_coverage) - np.array(actual_coverage)))
    ax.text(0.05, 0.95, f'ECE = {ece:.3f}', transform=ax.transAxes,
           fontsize=9, va='top')
    ax.set_xlabel('Nominal Coverage')
    ax.set_ylabel('Actual Coverage')
    ax.legend(fontsize=7)
    ax.set_title('(b) Calibration')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    # (c) 区间宽度随预测步变化（Sharpness）
    ax = axes[1, 0]
    horizons = list(sharpness_by_horizon.keys())
    widths = list(sharpness_by_horizon.values())
    ax.plot(horizons, widths, 's-', color='#4C78A8', linewidth=1.5)
    ax.set_xlabel('Prediction Horizon (min)')
    ax.set_ylabel('Average Interval Width')
    ax.set_title('(c) Sharpness (narrower = better)')
    ax.grid(True, alpha=0.3)

    # (d) CRPS 对比柱状图
    ax = axes[1, 1]
    methods = list(crps_by_method.keys())
    crps_vals = list(crps_by_method.values())
    colors = ['#E31A1C' if i == 0 else '#4C78A8' for i in range(len(methods))]
    ax.barh(methods, crps_vals, color=colors, edgecolor='black', linewidth=0.5)
    ax.set_xlabel('CRPS (lower = better)')
    ax.set_title('(d) CRPS Comparison')
    ax.grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    plt.savefig('uncertainty_panel.pdf', bbox_inches='tight')
```

### 18.2 采样轨迹多样性可视化

**适用场景：** 展示扩散模型生成的多条采样轨迹的多样性和覆盖性。

**传达信息：** 好的概率预测模型应生成多样但不离谱的样本——真实值应大部分落在样本覆盖范围内，同时样本不应过于分散（过于保守）。

```python
def plot_sample_diversity(time_steps, samples, ground_truth, n_highlight=5):
    """
    展示采样轨迹多样性，高亮少数几条轨迹便于观察。

    参数:
        time_steps: 时间步数组
        samples: (num_samples, time_steps) 全部采样
        ground_truth: 真实值
        n_highlight: 高亮展示的轨迹数
    """
    fig, ax = plt.subplots(figsize=(7.16, 3))

    # 所有轨迹：极低透明度
    for i in range(samples.shape[0]):
        ax.plot(time_steps, samples[i], color='#4C78A8', alpha=0.05, linewidth=0.5)

    # 高亮几条轨迹
    highlight_indices = np.random.choice(samples.shape[0], n_highlight, replace=False)
    highlight_colors = plt.cm.Set1(np.linspace(0, 1, n_highlight))
    for idx, color in zip(highlight_indices, highlight_colors):
        ax.plot(time_steps, samples[idx], color=color, alpha=0.6,
               linewidth=1, label=f'Sample {idx}')

    # 真实值
    ax.plot(time_steps, ground_truth, 'k-', linewidth=2, label='Ground Truth')

    # 标注覆盖率
    in_range = np.sum((samples.min(axis=0) <= ground_truth) &
                      (samples.max(axis=0) >= ground_truth)) / len(ground_truth)
    ax.text(0.02, 0.95, f'Coverage: {in_range*100:.1f}%',
           transform=ax.transAxes, fontsize=9, va='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax.set_xlabel('Time')
    ax.set_ylabel('Traffic Flow')
    ax.legend(loc='upper right', fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.set_title('Sample Diversity from Diffusion Model')
    plt.tight_layout()
    plt.savefig('sample_diversity.pdf', bbox_inches='tight')
```

### 18.3 概率预测区间对比图（多方法）

**适用场景：** 对比不同概率预测方法的预测区间质量。

**传达信息：** 区间宽度反映不确定性程度，覆盖率反映可靠性，两者需平衡。

```python
def plot_interval_comparison(time_steps, results_dict, ground_truth):
    """
    多方法的预测区间对比。

    参数:
        time_steps: 时间步数组
        results_dict: {method_name: {'lower': array, 'upper': array, 'median': array}}
        ground_truth: 真实值
    """
    fig, axes = plt.subplots(len(results_dict), 1, figsize=(7.16, 2.5 * len(results_dict)),
                              sharex=True)
    if len(results_dict) == 1:
        axes = [axes]

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A']

    for idx, (method, data) in enumerate(results_dict.items()):
        ax = axes[idx]
        color = colors[idx % len(colors)]

        # 预测区间
        ax.fill_between(time_steps, data['lower'], data['upper'],
                       alpha=0.3, color=color, label='90% PI')
        ax.plot(time_steps, data['median'], color=color, linewidth=1.5, label='Median')
        ax.plot(time_steps, ground_truth, 'k-', linewidth=1.5, label='Ground Truth')

        # 计算覆盖率和平均宽度
        coverage = np.mean((ground_truth >= data['lower']) & (ground_truth <= data['upper']))
        avg_width = np.mean(data['upper'] - data['lower'])
        ax.text(0.02, 0.95, f'{method}\nCoverage: {coverage*100:.1f}%, Width: {avg_width:.2f}',
               transform=ax.transAxes, fontsize=8, va='top',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        ax.set_ylabel('Flow')
        ax.legend(loc='upper right', fontsize=7)
        ax.grid(True, alpha=0.3)

    axes[-1].set_xlabel('Time')
    plt.tight_layout()
    plt.savefig('interval_comparison.pdf', bbox_inches='tight')
```

### 18.4 校准图高级版本

**适用场景：** 评估概率预测模型的校准质量。

**传达信息：** 理想情况下，名义覆盖率应等于实际覆盖率（对角线）。偏离对角线越远，校准越差。

```python
def plot_calibration_advanced(models_coverage, nominal_levels):
    """
    多模型校准图对比。

    参数:
        models_coverage: {model_name: [actual_coverage_per_level]}
        nominal_levels: [0.1, 0.2, ..., 0.9]
    """
    fig, ax = plt.subplots(figsize=(4.5, 4))

    # 完美校准线
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1.5, label='Perfect Calibration')

    # 理想区域（±5%）
    ax.fill_between(nominal_levels,
                    np.array(nominal_levels) - 0.05,
                    np.array(nominal_levels) + 0.05,
                    alpha=0.1, color='green', label='±5% Tolerance')

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A']
    markers = ['o', 's', '^', 'D']

    for i, (model, coverage) in enumerate(models_coverage.items()):
        ece = np.mean(np.abs(np.array(nominal_levels) - np.array(coverage)))
        ax.plot(nominal_levels, coverage, f'{markers[i]}-',
               color=colors[i % len(colors)], linewidth=1.5, markersize=5,
               label=f'{model} (ECE={ece:.3f})')

    ax.set_xlabel('Nominal Coverage Level')
    ax.set_ylabel('Empirical Coverage')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_title('Calibration Plot: Multiple Models')
    plt.tight_layout()
    plt.savefig('calibration_advanced.pdf', bbox_inches='tight')
```

---

## 十九、效率对比可视化模式（2024-2026）

### 19.1 参数量 vs 性能散点图

**适用场景：** 当需要展示不同模型在参数量和预测精度之间的权衡时使用。

**传达信息：** 理想模型应位于左下角（低参数量 + 低误差）。散点图直观展示哪些模型是"高效"的，哪些是"高参数低回报"的。

**实际案例：**
- **STID (ICLR'23)**：用参数量-MAE 散点图展示轻量 MLP 架构的优势
- **PatchSTG (KDD'25)**：展示参数效率，PatchSTG 用更少参数达到竞争性能
- **M3-Net**：无图 MLP 架构在参数效率上的优势

```python
def plot_params_vs_performance(models_data, highlight_method='Ours'):
    """
    参数量 vs 预测精度散点图。

    参数:
        models_data: {name: {'params': float, 'mae': float, 'flops': float}}
        highlight_method: 高亮标注的方法名
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    for name, data in models_data.items():
        is_highlight = (name == highlight_method)
        color = '#E31A1C' if is_highlight else '#4C78A8'
        size = 120 if is_highlight else 60
        marker = '*' if is_highlight else 'o'
        alpha = 1.0 if is_highlight else 0.7

        ax.scatter(data['params'], data['mae'], s=size, c=color,
                  marker=marker, alpha=alpha, edgecolors='black', linewidth=0.5,
                  zorder=5 if is_highlight else 3)

        # 标注方法名
        offset = (8, 8) if is_highlight else (5, 5)
        ax.annotate(name, (data['params'], data['mae']),
                   xytext=offset, textcoords='offset points',
                   fontsize=7, fontweight='bold' if is_highlight else 'normal')

    # Pareto 前沿线（连接非支配点）
    sorted_models = sorted(models_data.items(), key=lambda x: x[1]['params'])
    pareto_front = []
    min_mae = float('inf')
    for name, data in sorted_models:
        if data['mae'] < min_mae:
            pareto_front.append((data['params'], data['mae']))
            min_mae = data['mae']
    if len(pareto_front) > 1:
        pareto_x, pareto_y = zip(*pareto_front)
        ax.plot(pareto_x, pareto_y, '--', color='gray', alpha=0.5, linewidth=1)
        ax.text(pareto_x[-1], pareto_y[-1], 'Pareto Front', fontsize=7,
               color='gray', rotation=-10)

    ax.set_xlabel('Parameters (M)')
    ax.set_ylabel('MAE')
    ax.set_xscale('log')
    ax.grid(True, alpha=0.3)
    ax.set_title('Parameter Efficiency')
    plt.tight_layout()
    plt.savefig('params_vs_performance.pdf', bbox_inches='tight')
```

### 19.2 FLOPs vs MAE 权衡曲线

**适用场景：** 对比不同模型的计算量（FLOPs）和预测精度。

**传达信息：** FLOPs 直接反映推理时的计算成本，比参数量更准确地反映实际效率。

```python
def plot_flops_vs_mae(models_data, highlight_method='Ours'):
    """
    FLOPs vs MAE 权衡散点图。
    气泡大小可编码额外维度（如推理时间）。
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    for name, data in models_data.items():
        is_highlight = (name == highlight_method)
        color = '#E31A1C' if is_highlight else '#4C78A8'
        # 气泡大小编码推理时间
        size = data.get('inference_ms', 10) * 5
        marker = '*' if is_highlight else 'o'

        ax.scatter(data['flops'], data['mae'], s=size, c=color,
                  marker=marker, alpha=0.8, edgecolors='black', linewidth=0.5)
        ax.annotate(name, (data['flops'], data['mae']),
                   xytext=(5, 5), textcoords='offset points', fontsize=7)

    ax.set_xlabel('FLOPs (G)')
    ax.set_ylabel('MAE')
    ax.set_xscale('log')
    ax.grid(True, alpha=0.3)
    ax.set_title('Computational Efficiency\n(bubble size = inference time)')
    plt.tight_layout()
    plt.savefig('flops_vs_mae.pdf', bbox_inches='tight')
```

### 19.3 训练时间对比柱状图

**适用场景：** 对比不同模型的训练时间开销。

**传达信息：** 训练效率对实际部署和研究迭代至关重要，尤其对于大规模数据集。

```python
def plot_training_time(training_times, highlight_method='Ours'):
    """
    训练时间对比柱状图。

    参数:
        training_times: {method: hours}
    """
    fig, ax = plt.subplots(figsize=(7.16, 3))

    methods = list(training_times.keys())
    times = list(training_times.values())
    colors = ['#E31A1C' if m == highlight_method else '#4C78A8' for m in methods]

    bars = ax.barh(methods, times, color=colors, edgecolor='black', linewidth=0.5)

    # 标注具体数值和相对倍数
    min_time = min(times)
    for bar, t in zip(bars, times):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2.,
               f'{t:.1f}h ({t/min_time:.1f}x)', va='center', fontsize=8)

    ax.set_xlabel('Training Time (hours)')
    ax.set_title('Training Efficiency Comparison')
    ax.grid(True, axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('training_time.pdf', bbox_inches='tight')
```

### 19.4 内存使用对比

**适用场景：** 展示不同模型的 GPU 内存占用，对边缘部署和资源受限场景尤为重要。

```python
def plot_memory_comparison(memory_data, highlight_method='Ours'):
    """
    GPU 内存使用对比柱状图。
    可同时展示训练和推理时的内存占用。

    参数:
        memory_data: {method: {'train_mem_mb': X, 'infer_mem_mb': Y}}
    """
    fig, ax = plt.subplots(figsize=(7.16, 3.5))
    methods = list(memory_data.keys())
    x = np.arange(len(methods))
    width = 0.35

    train_mem = [memory_data[m]['train_mem_mb'] for m in methods]
    infer_mem = [memory_data[m]['infer_mem_mb'] for m in methods]

    colors_train = ['#E31A1C' if m == highlight_method else '#4C78A8' for m in methods]
    colors_infer = ['#FF6B6B' if m == highlight_method else '#7BC8A4' for m in methods]

    bars1 = ax.bar(x - width/2, train_mem, width, label='Training',
                   color=colors_train, edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x + width/2, infer_mem, width, label='Inference',
                   color=colors_infer, edgecolor='black', linewidth=0.5)

    # 标注数值
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{bar.get_height():.0f}', ha='center', va='bottom', fontsize=7)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
               f'{bar.get_height():.0f}', ha='center', va='bottom', fontsize=7)

    ax.set_ylabel('GPU Memory (MB)')
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=20, ha='right')
    ax.legend()
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_title('GPU Memory Usage Comparison')
    plt.tight_layout()
    plt.savefig('memory_comparison.pdf', bbox_inches='tight')
```

### 19.5 推理速度对比

**适用场景：** 展示不同模型的推理延迟，对实时交通预测系统至关重要。

```python
def plot_inference_speed(inference_data, target_fps=10):
    """
    推理速度对比图，标注实时性阈值。

    参数:
        inference_data: {method: {'latency_ms': X, 'throughput_fps': Y}}
        target_fps: 目标帧率（实时性要求）
    """
    fig, ax1 = plt.subplots(figsize=(7.16, 3.5))

    methods = list(inference_data.keys())
    latencies = [inference_data[m]['latency_ms'] for m in methods]
    throughputs = [inference_data[m]['throughput_fps'] for m in methods]

    x = np.arange(len(methods))
    width = 0.35

    # 延迟柱状图
    bars = ax1.bar(x - width/2, latencies, width, label='Latency (ms)',
                   color='#4C78A8', edgecolor='black', linewidth=0.5)
    ax1.set_ylabel('Latency (ms)', color='#4C78A8')
    ax1.tick_params(axis='y', labelcolor='#4C78A8')

    # 吞吐量折线图（右轴）
    ax2 = ax1.twinx()
    ax2.plot(x, throughputs, 's-', color='#E31A1C', linewidth=1.5, label='Throughput (FPS)')
    ax2.set_ylabel('Throughput (FPS)', color='#E31A1C')
    ax2.tick_params(axis='y', labelcolor='#E31A1C')

    # 实时性阈值线
    target_latency = 1000 / target_fps
    ax1.axhline(y=target_latency, color='green', linestyle='--', alpha=0.5)
    ax1.text(len(methods)-1, target_latency, f'Real-time ({target_fps} FPS)',
            fontsize=8, color='green', va='bottom')

    ax1.set_xticks(x)
    ax1.set_xticklabels(methods, rotation=20, ha='right')

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)

    ax1.grid(True, axis='y', alpha=0.3)
    ax1.set_title('Inference Speed Comparison')
    plt.tight_layout()
    plt.savefig('inference_speed.pdf', bbox_inches='tight')
```

### 19.6 综合效率雷达图

**适用场景：** 多维度综合评估模型效率。

**传达信息：** 在参数量、FLOPs、推理时间、内存、精度五个维度全面对比，面积越小越优。

```python
def plot_efficiency_radar(models_data, highlight_method='Ours'):
    """
    多维效率雷达图。

    参数:
        models_data: {name: {'params': M, 'flops': G, 'latency_ms': X,
                             'mem_mb': Y, 'mae': Z}}
    """
    dimensions = ['Params\n(M)', 'FLOPs\n(G)', 'Latency\n(ms)', 'Memory\n(MB)', 'MAE']
    n_dims = len(dimensions)
    angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

    # 归一化到 [0, 1]
    all_values = {d: [] for d in ['params', 'flops', 'latency_ms', 'mem_mb', 'mae']}
    for data in models_data.values():
        for key in all_values:
            all_values[key].append(data[key])

    for key in all_values:
        min_v, max_v = min(all_values[key]), max(all_values[key])
        all_values[key] = (min_v, max_v)

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A', '#9D78B8']

    for idx, (name, data) in enumerate(models_data.items()):
        values = []
        for key in ['params', 'flops', 'latency_ms', 'mem_mb', 'mae']:
            min_v, max_v = all_values[key]
            normalized = (data[key] - min_v) / (max_v - min_v + 1e-8)
            values.append(normalized)
        values += values[:1]

        is_highlight = (name == highlight_method)
        ax.plot(angles, values, 'o-', linewidth=2 if is_highlight else 1,
               color=colors[idx % len(colors)],
               label=name, markersize=6 if is_highlight else 4)
        if is_highlight:
            ax.fill(angles, values, alpha=0.15, color=colors[idx % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=9)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'], fontsize=7)
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1), fontsize=8)
    ax.set_title('Efficiency Radar (lower = better)', fontsize=10, pad=20)
    plt.tight_layout()
    plt.savefig('efficiency_radar.pdf', bbox_inches='tight')
```

---

## 二十、大规模评估可视化模式（2024-2026）

### 20.1 多数据集 x 多方法热力图

**适用场景：** 当论文在多个数据集上评估多个方法，需要一目了然地展示全局结果时使用。

**传达信息：** 快速识别哪些方法在哪些数据集上表现最好，哪些数据集最具挑战性。

**实际案例：**
- 大多数顶会论文（如 STID、STAEformer）在 6+ 数据集上评估 10+ 方法
- 2024-2026 趋势：评估规模扩大到 10+ 数据集、20+ 方法

```python
def plot_method_dataset_heatmap(results_matrix, methods, datasets, metric='MAE',
                                 highlight_best=True):
    """
    多数据集 x 多方法热力图。

    参数:
        results_matrix: (n_methods, n_datasets) 结果矩阵
        methods: 方法名称列表
        datasets: 数据集名称列表
        metric: 指标名称
        highlight_best: 是否高亮最优结果
    """
    fig, ax = plt.subplots(figsize=(max(8, len(datasets)*1.2),
                                     max(4, len(methods)*0.4)))

    # 使用 viridis 色图（色盲友好）
    im = ax.imshow(results_matrix, cmap='viridis_r', aspect='auto')
    plt.colorbar(im, ax=ax, label=f'{metric} (lower is better)', shrink=0.8)

    # 标注数值
    for i in range(len(methods)):
        for j in range(len(datasets)):
            value = results_matrix[i, j]
            # 判断是否为该数据集最优
            is_best = (value == results_matrix[:, j].min())
            text_color = 'white' if value > np.median(results_matrix) else 'black'
            fontweight = 'bold' if is_best and highlight_best else 'normal'
            text = f'{value:.2f}'
            if is_best and highlight_best:
                text = f'*{value:.2f}*'

            ax.text(j, i, text, ha='center', va='center',
                   fontsize=7, color=text_color, fontweight=fontweight)

    ax.set_xticks(range(len(datasets)))
    ax.set_yticks(range(len(methods)))
    ax.set_xticklabels(datasets, rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels(methods, fontsize=8)
    ax.set_xlabel('Dataset')
    ax.set_ylabel('Method')
    ax.set_title(f'Method × Dataset {metric} Comparison')
    plt.tight_layout()
    plt.savefig('method_dataset_heatmap.pdf', bbox_inches='tight')
```

### 20.2 多指标雷达图

**适用场景：** 当需要在多个评估维度上全面对比方法时使用。

**传达信息：** 单一指标可能产生误导，雷达图展示方法在各维度的综合表现。

```python
def plot_multi_metric_radar(results, methods, metrics):
    """
    多指标雷达图。

    参数:
        results: {method: {metric: value}}
        methods: 方法名称列表
        metrics: 指标名称列表，如 ['MAE', 'RMSE', 'MAPE', 'Inference Speed', 'Memory']
    """
    n_metrics = len(metrics)
    angles = np.linspace(0, 2 * np.pi, n_metrics, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 归一化：每个指标独立归一化到 [0, 1]
    all_vals = {m: [results[mth][m] for mth in methods] for m in metrics}
    norm_ranges = {m: (min(vals), max(vals)) for m, vals in all_vals.items()}

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A', '#9D78B8', '#56B4E9']

    for idx, method in enumerate(methods):
        values = []
        for m in metrics:
            min_v, max_v = norm_ranges[m]
            # 对于越小越好的指标，取反（使得面积小=好）
            if m in ['MAE', 'RMSE', 'MAPE', 'Memory']:
                norm = 1 - (results[method][m] - min_v) / (max_v - min_v + 1e-8)
            else:
                norm = (results[method][m] - min_v) / (max_v - min_v + 1e-8)
            values.append(norm)
        values += values[:1]

        ax.plot(angles, values, 'o-', linewidth=1.5, color=colors[idx % len(colors)],
               label=method, markersize=5)
        ax.fill(angles, values, alpha=0.08, color=colors[idx % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylim(0, 1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1), fontsize=8)
    ax.set_title('Multi-Metric Comparison\n(outer = better)', fontsize=11, pad=20)
    plt.tight_layout()
    plt.savefig('multi_metric_radar.pdf', bbox_inches='tight')
```

### 20.3 带误差线的统计显著性柱状图

**适用场景：** 当实验包含多次重复运行，需要展示结果的统计显著性时使用。

**传达信息：** 确保性能差异不是由随机性导致的，通过误差线和显著性标注增强结论可信度。

```python
def plot_significance_bar_chart(results_with_stats, methods, datasets, metric='MAE'):
    """
    带误差线和显著性标注的柱状图。

    参数:
        results_with_stats: {method: {dataset: {'mean': X, 'std': Y, 'p_value': Z}}}
        methods: 方法名称列表
        datasets: 数据集名称列表
    """
    fig, ax = plt.subplots(figsize=(7.16, 4))
    n_methods = len(methods)
    x = np.arange(len(datasets))
    width = 0.8 / n_methods

    colors = plt.cm.Set2(np.linspace(0, 1, n_methods))

    for i, method in enumerate(methods):
        means = [results_with_stats[method][ds]['mean'] for ds in datasets]
        stds = [results_with_stats[method][ds]['std'] for ds in datasets]

        bars = ax.bar(x + i * width, means, width, yerr=stds,
                     label=method, color=colors[i],
                     edgecolor='black', linewidth=0.5,
                     capsize=3, error_kw={'linewidth': 0.8})

    # 标注显著性（与最佳方法的 p 值比较）
    for j, ds in enumerate(datasets):
        # 找到最佳方法
        best_method = min(methods,
                         key=lambda m: results_with_stats[m][ds]['mean'])
        best_val = results_with_stats[best_method][ds]['mean']

        for i, method in enumerate(methods):
            if method == best_method:
                continue
            p_val = results_with_stats[method][ds].get('p_value', 1.0)
            if p_val < 0.01:
                sig_mark = '**'
            elif p_val < 0.05:
                sig_mark = '*'
            else:
                sig_mark = 'n.s.'

            if sig_mark != 'n.s.':
                bar_x = x[j] + i * width
                bar_y = results_with_stats[method][ds]['mean'] + stds[i]
                ax.text(bar_x, bar_y + 0.02, sig_mark,
                       ha='center', va='bottom', fontsize=8, color='red')

    ax.set_xlabel('Dataset')
    ax.set_ylabel(metric)
    ax.set_xticks(x + width * (n_methods - 1) / 2)
    ax.set_xticklabels(datasets, rotation=15)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_title(f'{metric} with Statistical Significance\n*p<0.05, **p<0.01')
    plt.tight_layout()
    plt.savefig('significance_bar_chart.pdf', bbox_inches='tight')
```

---

## 二十一、消融实验可视化模式（2024-2026）

### 21.1 组件贡献瀑布图

**适用场景：** 当需要展示模型各组件对最终性能的逐步贡献时使用。

**传达信息：** 从基线开始，逐步添加组件，展示每个组件带来的性能增益，直观看出哪个组件贡献最大。

**实际案例：**
- **GAMMA-Net**：消融 GAT 层、Mamba 层、门控融合的各自贡献
- **STM3 (KDD'26)**：消融三路扫描和 MoE 融合的贡献

```python
def plot_component_waterfall(baseline, component_gains, full_model, metric='MAE'):
    """
    组件贡献瀑布图。

    参数:
        baseline: 基线模型的指标值
        component_gains: [(组件名, 增益值)]，增益为负表示降低 MAE（改善）
        full_model: 完整模型的指标值
    """
    fig, ax = plt.subplots(figsize=(7.16, 3.5))

    # 构建瀑布图数据
    labels = ['Baseline']
    values = [baseline]
    bottoms = [0]
    colors_list = ['#797068']

    current = baseline
    for comp_name, gain in component_gains:
        labels.append(comp_name)
        values.append(abs(gain))
        bottoms.append(current - abs(gain) if gain < 0 else current)
        colors_list.append('#59A14F' if gain < 0 else '#E31A1C')
        current += gain

    labels.append('Full Model')
    values.append(full_model)
    bottoms.append(0)
    colors_list.append('#4C78A8')

    x = np.arange(len(labels))
    bars = ax.bar(x, values, bottom=bottoms, color=colors_list,
                 edgecolor='black', linewidth=0.5, width=0.6)

    # 标注数值和增益
    for i, (bar, val) in enumerate(zip(bars, values)):
        if i == 0 or i == len(labels) - 1:
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_y() + val,
                   f'{val:.3f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
        else:
            gain = component_gains[i-1][1]
            sign = '+' if gain > 0 else ''
            ax.text(bar.get_x() + bar.get_width()/2., bar.get_y() + val,
                   f'{sign}{gain:.3f}', ha='center', va='bottom', fontsize=8,
                   color='green' if gain < 0 else 'red')

    # 连接线
    for i in range(len(labels) - 2):
        ax.plot([i + 0.3, i + 0.7], [bottoms[i+1], bottoms[i+1]],
               '--', color='gray', linewidth=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=20, ha='right')
    ax.set_ylabel(metric)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_title('Component Contribution Waterfall')
    plt.tight_layout()
    plt.savefig('component_waterfall.pdf', bbox_inches='tight')
```

### 21.2 超参数敏感性折线图

**适用场景：** 当需要展示模型对关键超参数的敏感性时使用。

**传达信息：** 模型是否对超参数选择鲁棒？最优超参数在哪里？是否存在性能悬崖？

**实际案例：**
- **STAEformer**：展示 attention heads 数量和 embedding dimension 的敏感性
- **GAMMA-Net**：展示 Mamba 层数和 hidden dimension 的影响

```python
def plot_hyperparameter_sensitivity(param_values, performance_dict, optimal_value,
                                      param_name='Hidden Dimension', metric='MAE'):
    """
    超参数敏感性折线图。

    参数:
        param_values: 超参数取值列表
        performance_dict: {method: [performance_at_each_value]}
        optimal_value: 最优超参数值
        param_name: 超参数名称
    """
    fig, ax = plt.subplots(figsize=(5, 3.5))

    colors = ['#E31A1C', '#4C78A8', '#59A14F', '#E8864A']
    markers = ['o', 's', '^', 'D']

    for idx, (method, perfs) in enumerate(performance_dict.items()):
        ax.plot(param_values, perfs, f'{markers[idx]}-',
               color=colors[idx % len(colors)], linewidth=1.5, markersize=6,
               label=method)

    # 标注最优点
    ax.axvline(x=optimal_value, color='gray', linestyle=':', alpha=0.5)
    ax.annotate(f'Optimal = {optimal_value}',
               xy=(optimal_value, ax.get_ylim()[1]),
               xytext=(10, -10), textcoords='offset points',
               fontsize=8, color='gray',
               arrowprops=dict(arrowstyle='->', color='gray'))

    ax.set_xlabel(param_name)
    ax.set_ylabel(metric)
    ax.legend(loc='best', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_title(f'Sensitivity to {param_name}')
    plt.tight_layout()
    plt.savefig(f'sensitivity_{param_name.replace(" ", "_").lower()}.pdf',
               bbox_inches='tight')
```

### 21.3 消融实验表格（带颜色编码）

**适用场景：** 以表格形式展示详细的消融实验结果，用颜色编码直观区分性能差异。

```python
def plot_ablation_table_colorcoded(ablation_data, variants, datasets, metric='MAE'):
    """
    带颜色编码的消融实验表格。

    参数:
        ablation_data: (n_variants, n_datasets) 数值矩阵
        variants: 变体名称列表
        datasets: 数据集名称列表
    """
    fig, ax = plt.subplots(figsize=(max(6, len(datasets)*1.5 + 2),
                                     max(3, len(variants)*0.4 + 1)))
    ax.axis('off')

    # 归一化用于颜色映射
    norm = plt.Normalize(vmin=ablation_data.min(), vmax=ablation_data.max())
    cmap = plt.cm.RdYlGn_r  # 红色=差，绿色=好

    table = ax.table(
        cellText=[[f'{v:.3f}' for v in row] for row in ablation_data],
        rowLabels=variants,
        colLabels=datasets,
        loc='center',
        cellLoc='center'
    )

    # 设置颜色
    for i in range(len(variants)):
        for j in range(len(datasets)):
            cell = table[i+1, j]
            color = cmap(norm(ablation_data[i, j]))
            cell.set_facecolor(color)
            cell.set_text_props(fontsize=8)

            # 高亮最优
            if ablation_data[i, j] == ablation_data[:, j].min():
                cell.set_text_props(fontweight='bold')

    # 设置表头样式
    for j in range(len(datasets)):
        table[0, j].set_facecolor('#4C78A8')
        table[0, j].set_text_props(color='white', fontweight='bold', fontsize=9)
    for i in range(len(variants)):
        table[i+1, -1].set_facecolor('#F0F0F0')
        table[i+1, -1].set_text_props(fontweight='bold', fontsize=9)

    table.auto_set_font_size(False)
    table.scale(1, 1.5)

    ax.set_title(f'Ablation Study: {metric}', fontsize=11, pad=20)
    plt.tight_layout()
    plt.savefig('ablation_table_colored.pdf', bbox_inches='tight')
```

### 21.4 多维度消融联合图

**适用场景：** 同时消融多个维度（如层数、维度、组件组合）时使用。

```python
def plot_multi_dim_ablation(results_grid, dim1_values, dim2_values,
                              dim1_name='Num Layers', dim2_name='Hidden Dim',
                              metric='MAE'):
    """
    多维度消融热力图。

    参数:
        results_grid: (len(dim1_values), len(dim2_values)) 结果矩阵
        dim1_values: 第一个消融维度的取值
        dim2_values: 第二个消融维度的取值
    """
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(results_grid, cmap='viridis_r', aspect='auto')
    plt.colorbar(im, ax=ax, label=metric)

    # 标注数值
    for i in range(len(dim1_values)):
        for j in range(len(dim2_values)):
            value = results_grid[i, j]
            is_best = (value == results_grid.min())
            text_color = 'white' if value > np.median(results_grid) else 'black'
            text = f'{value:.3f}'
            if is_best:
                text = f'{value:.3f}*'
            ax.text(j, i, text, ha='center', va='center',
                   fontsize=8, color=text_color,
                   fontweight='bold' if is_best else 'normal')

    ax.set_xticks(range(len(dim2_values)))
    ax.set_yticks(range(len(dim1_values)))
    ax.set_xticklabels(dim2_values)
    ax.set_yticklabels(dim1_values)
    ax.set_xlabel(dim2_name)
    ax.set_ylabel(dim1_name)
    ax.set_title(f'Ablation: {dim1_name} × {dim2_name}')
    plt.tight_layout()
    plt.savefig('multi_dim_ablation.pdf', bbox_inches='tight')
```

---

> 更新时间：2026-06-19
> 基于论文：STAEformer (AAAI'24), PDFormer (AAAI'23), DiffSTG (KDD'24), UrbanGPT (KDD'24), UniST (KDD'24), Graph WaveNet (IJCAI'19), MegaCRN (AAAI'23), STID (ICLR'23), GAMMA-Net (2026), STM3 (KDD'26), SpoT-Mamba (2024), PatchSTG (KDD'25), Expand-and-Compress (ICLR'25), Damba-ST (ICDE'26), FairTP (AAAI'25), RAST (AAAI'26), ST-HCMs (AAAI'25), LightST (AAAI'25), FlowDistill (2025), DTP-Attack (2026), Double-Diffusion (2025), CaPaint (NeurIPS'24), OracleTSC, SignalClaw, DiffRefiner, GaussianFusion, UrbanEV, Heterogeneous-Aware FL, M3-Net, FEDDGCN, Balance and Brighten, TopKNet, FAST (ICLR'25), CityGPT, Conformalized ST-GCN, ICML 2026 Workshop on Foundation Models for Spatiotemporal
