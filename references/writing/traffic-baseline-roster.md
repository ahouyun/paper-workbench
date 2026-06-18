# 交通 / 时空预测 baseline roster

> 目标：给 `paper-workbench` 提供一个稳定的 baseline roster，用于论文写作、实验设计、related work、结果分析、审稿应对。
>
> 这不是“谁最新谁最强”的排行榜，而是回答四个问题：
> 1. 这篇工作在生态里扮演什么角色？
> 2. 什么时候应该把它列为 baseline？
> 3. 它适合支持什么 claim？
> 4. 不应该如何误用它？

---

## 1. 使用原则

### 1.1 baseline roster 的作用

该 roster 主要服务四类任务：

- **related work framing**：按方法家族组织文献，而不是堆名字
- **experiment design**：挑出能回答 reviewer question 的 baseline set
- **results writing**：解释“赢了谁、为什么、在什么条件下赢”
- **rebuttal / review**：防止 baseline 选择过弱、过旧、过偏

### 1.2 不要把 baseline roster 当成固定名单

硬规则：

1. baseline 不是越多越好，而是要覆盖关键方法家族。
2. baseline 不是只选老论文，也不是只选最新论文。
3. baseline 的价值在于回答比较问题，不在于凑引用数。
4. 如果你的方法 claim 某个机制，baseline 里必须有该机制的强代表。

### 1.3 推荐的 baseline 组装逻辑

对 traffic / ST forecasting 论文，最稳的 baseline 包通常覆盖：

1. **经典时空图基线**：DCRNN, STGCN
2. **自适应图/强工程基线**：Graph WaveNet
3. **注意力/Transformer 路线**：GMAN, PDFormer, STAEformer
4. **反复杂度或极简强基线**：STID
5. **机制增强路线**：MegaCRN
6. **概率预测或统一模型路线**：DiffSTG, UniST

如果你的论文属于其中某一条路线，该路线的强代表不能缺席。

---

## 2. baseline family map

| Family | 代表 | 主要角色 |
|---|---|---|
| diffusion / recurrent graph | DCRNN | 社区早期协议锚点，经典时空依赖基线 |
| convolutional graph | STGCN | 早期卷积式时空图基线 |
| adaptive graph + TCN | Graph WaveNet | 长期强工程 baseline，几乎总该考虑 |
| attention pre-transformer bridge | GMAN | attention 家族经典代表 |
| simplification / identity baseline | STID | 反复杂度叙事锚点 |
| traffic-mechanism transformer | PDFormer | 交通现象绑定型 Transformer baseline |
| high-performance transformer | STAEformer | 近年性能导向强 baseline |
| memory / pattern-enhanced graph recurrent | MegaCRN | 记忆增强机制型 baseline |
| probabilistic generative forecasting | DiffSTG | 概率预测 / 分布建模路线代表 |
| universal / prompt / foundation framing | UniST | 统一建模 / 跨任务叙事代表 |

---

## 3. 单模型 roster

### 3.1 DCRNN

**角色定位**

- 经典 diffusion + recurrent graph baseline
- 很多 traffic forecasting 协议和数据处理写法的历史锚点
- 适合作为“早期但仍有代表性”的强参照

**什么时候应纳入**

- 你做 traffic forecasting，尤其是 METR-LA / PEMS-BAY / PEMS 系列
- 你要说明自己比经典图时空模型强
- 你在讨论 chronological split、Gaussian kernel graph、12-in-12-out 等传统协议

**它代表的 claim 对照物**

- 你的方法是否超越经典扩散图时序建模
- 新模型相比 recurrent graph 方法的优势是否真实存在

**不要如何误用**

- 不要把 DCRNN 当成唯一图模型 baseline
- 不要只赢 DCRNN 就宣称 SOTA
- 不要忽略它背后代表的协议传统

**最适合出现的位置**

- related work 中作为 early graph-based anchor
- main table 中作为 classic baseline
- protocol section 中作为 split / graph construction 来源锚点

### 3.2 STGCN

**角色定位**

- 经典 convolution + graph baseline
- 与 DCRNN 一起构成早期 traffic STGNN 的双锚点

**什么时候应纳入**

- 你的方法声称比 recurrent / convolution baselines 更好
- 需要覆盖非 RNN 的经典图建模路线

**它代表的 claim 对照物**

- 你的增益是否来自更强时序建模而非仅更大容量
- 是否真的超越了卷积式时空图建模

**不要如何误用**

- 不要把它当成“弱 baseline 占位符”
- 不要省略 horizon-wise 结果，只报 overall average

**最适合出现的位置**

- baseline family overview
- main benchmark table

### 3.3 Graph WaveNet / GWNet

**角色定位**

- 自适应图学习 + dilated temporal convolution 的长期强基线
- 在大量 traffic forecasting 论文中是“如果没比它，审稿人会问”的 baseline

**什么时候应纳入**

- 几乎所有 traffic flow / speed forecasting method paper
- 你声称自己在结构学习、长依赖、强工程性能上更优

**它代表的 claim 对照物**

- 自适应图是否真的必要
- 你的方法能否超越长期被默认认为“难打”的工程强基线

**不要如何误用**

- 不要只引用原论文结果而不交代复现设置
- 不要在 adaptive graph 相关论文里缺失它

**最适合出现的位置**

- 主结果表
- 结构学习相关 related work
- rebuttal 中作为“strong baseline included”证据

### 3.4 GMAN

**角色定位**

- attention 路线经典代表
- 是从 GNN/RNN 时代到 Transformer 时代之间的重要 attention anchor

**什么时候应纳入**

- 你使用 attention / transformer / dynamic relation 建模
- 你要说明 attention 型方法的相对位置

**它代表的 claim 对照物**

- 新 attention 设计是否优于早期全局 attention 路线
- gain 是否来自 traffic-specific mechanism，而不是仅 attention 本身

**不要如何误用**

- 不要把 GMAN 当成纯粹老旧 baseline 直接略过
- 如果你 claim attention-based modeling，很难不提它

**最适合出现的位置**

- attention family related work
- benchmark table 的 transformer 前代代表

### 3.5 STID

**角色定位**

- 极简强基线
- 反复杂度叙事代表
- 用 very simple identity-style design 质疑“越复杂越好”的默认前提

**什么时候应纳入**

- 你提出复杂模型
- 你声称多个复杂模块必要
- 你需要防止 reviewer 说“是不是简单 MLP 也能做到”

**它代表的 claim 对照物**

- 复杂建模是否真的必要
- 增益是否来自结构性 insight，而不是多堆模块

**不要如何误用**

- 不要因为它“简单”就不放
- 如果你的方法复杂很多，却没和 STID 比，容易被质疑性价比

**最适合出现的位置**

- main table
- efficiency / simplicity discussion
- introduction 中作为方法论反例锚点

### 3.6 PDFormer

**角色定位**

- 交通机制绑定型 Transformer baseline
- 代表“传播延迟、动态长距离依赖、交通现象解释”这一条叙事线

**什么时候应纳入**

- 你做 traffic-specific transformer
- 你声称显式建模传播、动态关系、交通机制
- 你投 T-ITS 风格写法时，想让 reviewer 看到交通 grounding

**它代表的 claim 对照物**

- 你的机制是否比 propagation delay-aware 设计更合理
- 增益是否出现在长 horizon 或动态场景

**不要如何误用**

- 不要只把它当作又一个 Transformer baseline
- 它最重要的不是架构名，而是“交通现象 -> 模块 -> ablation”闭环

**最适合出现的位置**

- related work 的 traffic-specific transformer family
- mechanism-aligned ablation discussion
- T-ITS / TVT 风格论文主表

### 3.7 STAEformer

**角色定位**

- 近年高性能 Transformer 强基线
- 经常扮演“如果你的论文主打 accuracy，就要打赢它”的角色

**什么时候应纳入**

- 你的论文主打 benchmark superiority
- 你在 METR-LA / PEMS 上追求最强指标
- 你声称 adaptive embedding / transformer superiority

**它代表的 claim 对照物**

- 你的性能优势是否能在强 Transformer baseline 上成立
- 你是否仅仅赢了老方法，而没赢近年的高性能方法

**不要如何误用**

- 不要只放 STAEformer 而缺失更老的 anchor baseline，否则谱系不完整
- 不要只比较平均分，不比较 horizon

**最适合出现的位置**

- benchmark main table 的 strongest performance anchor
- abstract / results discussion 中的 direct comparator

### 3.8 MegaCRN

**角色定位**

- memory / pattern enhanced spatiotemporal baseline
- 强调 pattern memory、meta-graph 或 enhanced recurrent mechanisms

**什么时候应纳入**

- 你的方法涉及 pattern memory、prototype、meta knowledge、history bank
- 你声称自己在 complex temporal patterns 上更强

**它代表的 claim 对照物**

- 你的记忆增强机制是否真的有额外价值
- 对历史模式依赖的建模是否比已有 memory route 更有效

**不要如何误用**

- 不要在做 memory-enhanced 方法时忽视它
- 不要只说“比 graph baseline 强”，而不比 memory baseline

**最适合出现的位置**

- mechanism family comparison
- ablation / case study discussion about recurring patterns

### 3.9 DiffSTG

**角色定位**

- probabilistic forecasting / generative route baseline
- 用于把叙事从 point estimate 升级到 distribution-aware forecasting

**什么时候应纳入**

- 你的方法不是只做点预测
- 你声称 uncertainty、distribution modeling、multi-modal future
- 你需要说明自己不只是优化 MAE

**它代表的 claim 对照物**

- 你的概率预测是否真能改善 calibration / uncertainty quality
- 生成式路线是否在复杂未来分布上更合理

**不要如何误用**

- 不要把它和纯 deterministic baselines 用一套单维指标粗暴比较
- 如果比较 DiffSTG，最好补充 CRPS / NLL / interval quality 等概率指标

**最适合出现的位置**

- probabilistic forecasting related work
- uncertainty experiment section
- figure planning for predictive intervals

### 3.10 UniST

**角色定位**

- universal / prompt-empowered / multi-task ST prediction baseline
- 代表“统一建模、跨任务迁移、foundation-style framing”

**什么时候应纳入**

- 你做 universal ST model
- 你强调 zero-shot / few-shot / cross-city / transfer
- 你把时空预测写成基础模型叙事

**它代表的 claim 对照物**

- 你的统一性是不是实证成立
- 你的 transfer claim 是否有足够 scope

**不要如何误用**

- 不要只拿 UniST 做单一数据集的点精度对比
- 不要声称 universal superiority 却没有 transfer 或 task coverage evidence

**最适合出现的位置**

- introduction 中的 paradigm-upgrade family
- multi-task / transfer table
- rebuttal 中回应“scope too narrow”

---

## 4. 按论文类型选 baseline

### 4.1 如果你写的是 classic traffic forecasting method paper

最小可接受 baseline 包：

- DCRNN
- STGCN
- Graph WaveNet
- GMAN
- STID
- PDFormer
- STAEformer

推荐增强：

- MegaCRN
n- 如果你有概率预测或统一建模 claim，再加 DiffSTG / UniST

### 4.2 如果你写的是 traffic-specific Transformer paper

至少覆盖：

- GMAN
- PDFormer
- STAEformer
- Graph WaveNet
- STID

原因：

- GMAN 代表早期 attention
- PDFormer 代表交通机制型 Transformer
- STAEformer 代表性能型 Transformer
- GWNet 是强工程基线
- STID 防止复杂度叙事失控

### 4.3 如果你写的是 simplification / efficient model paper

至少覆盖：

- STID
- Graph WaveNet
- STAEformer
- PDFormer

并且必须补：

- params / latency / memory 表

### 4.4 如果你写的是 probabilistic / generative forecasting paper

至少覆盖：

- DiffSTG
- Graph WaveNet
- PDFormer 或 STAEformer
- STID

并且补充：

- 概率指标
- predictive interval 图
- deterministic vs probabilistic 叙事差异

### 4.5 如果你写的是 universal / foundation ST prediction paper

至少覆盖：

- UniST
- STID
- Graph WaveNet
- STAEformer
- 一个 traffic-specific mechanism model（如 PDFormer）

并且补充：

- multi-task / transfer / zero-shot or few-shot evidence

---

## 5. 结果分析时如何写 baseline

### 5.1 正确写法

不要写：

- “Our method outperforms all baselines.”

优先写：

- “Compared with classic graph-based baselines such as DCRNN and STGCN, our model reduces ...”
- “Against the long-standing strong engineering baseline Graph WaveNet, the gain mainly appears at 60-minute horizons ...”
- “Relative to STID, the improvement suggests that the benefit does not come solely from model capacity ...”
- “Compared with PDFormer, the gain is concentrated under settings where propagation-aware modeling matters most ...”

### 5.2 reviewer-friendly 的 baseline 解释框架

按家族解释，而不是按论文名流水账：

1. classic graph baselines
2. adaptive graph baselines
3. attention / transformer baselines
4. simplification baselines
5. probabilistic / universal baselines

这样更像审稿对话，而不是文献堆砌。

---

## 6. 常见误区

1. 只和老 baseline 比，不和近年强 baseline 比
2. 只和近年 Transformer 比，不保留 DCRNN / STGCN / GWNet 这些生态锚点
3. 缺失 STID，导致复杂度收益站不住
4. 用 DiffSTG 却不报告概率指标
5. 用 UniST 却不报告 transfer / multi-task 证据
6. 用 PDFormer / MegaCRN，却不讨论交通现象或模式机制
7. 用 STAEformer 只作点缀，不把它当真正强对手分析

---

## 7. 给 `paper-workbench` 的直接使用提示

当用户说：

- “帮我挑 baseline”
  - 先判断论文属于哪条路线，再从本 roster 选家族覆盖最完整的一组

- “帮我写 related work”
  - 不按年份流水账写，按 baseline family 写

- “帮我分析结果”
  - 不写“all baselines”，而写“赢了哪一类 baseline，说明了什么”

- “审稿人说 baseline 不够强”
  - 用本 roster 检查是否缺失了：GWNet / STID / PDFormer / STAEformer / DiffSTG / UniST 中与你 claim 直接相关的强代表

---

## 8. 最终硬规则

1. baseline selection 必须覆盖 claim 对应的方法家族。
2. 任何“优于 SOTA”的表述，都要能指出至少一个强且相关的 comparator。
3. 如果你的论文主打交通机制，不能缺 PDFormer 这一类 comparator。
4. 如果你的论文主打高性能，不能缺 STAEformer / Graph WaveNet。
5. 如果你的论文主打简单有效，不能缺 STID。
6. 如果你的论文主打概率预测，不能缺 DiffSTG。
7. 如果你的论文主打统一模型或迁移，不能缺 UniST。
