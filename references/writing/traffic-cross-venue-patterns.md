# 交通 / 时空预测跨场刊写作模式

> 目标：把 IEEE T-ITS、IEEE TVT、IEEE TKDE、KDD、NeurIPS、ICML、ICLR 中交通流预测、时空预测、轨迹预测、需求预测等“有代码、可复现、论文生态丰富”的代表性工作，压缩成可供 `paper-workbench` 路由调用的 venue-aware 写作参考。
>
> 本文件不追求列全论文，而是提炼这些场刊中反复出现、最值得迁移到 skill 的结构模式、claim-evidence-artifact 打包方式、图表套路与 reject-risk。

---

## 1. 适用范围

当用户在这些方向写作时优先参考本文件：

- traffic forecasting
- spatiotemporal forecasting
- trajectory prediction
- mobility / travel demand forecasting
- urban foundation model / universal ST prediction
- traffic benchmark or dataset paper

典型论文家族包括但不限于：

- **经典强基线 / 生态锚点**：DCRNN, STGCN, Graph WaveNet, GMAN
- **反复杂度叙事**：STID
- **交通机制增强**：PDFormer, MegaCRN, D2STGNN
- **概率预测 / 生成式**：DiffSTG
- **统一模型 / 基础模型叙事**：UniST, UrbanGPT
- **近年高性能 Transformer**：STAEformer

硬规则：

1. 不把“有 GitHub 代码”误写成“强实证”。代码是可审计信号，不是证据本身。
2. 不把会议论文结构直接照搬到 T-ITS。要先看 venue 的审稿问题。
3. 不把交通任务包装成抽象时序任务。需要明确网络、传感器、场景、预测 horizon、运营意义。

---

## 2. 场刊气质差异

### 2.1 IEEE T-ITS

偏好：

- 交通问题定义清楚
- 真实部署约束或可审计仿真约束
- horizon / 场景 / 鲁棒性 / 代价一起交代
- 为什么方法符合交通现象，而不是只说精度更高

常见 reviewer 追问：

- 你的机制与传播延迟、非平稳性、稀疏传感器、异常事件有什么对应关系？
- 增益出现在哪些 horizon / 哪些网络条件下？
- 部署代价、鲁棒性和失败边界是什么？

### 2.2 IEEE TVT

偏好：

- vehicular / wireless / edge / V2X / online inference 约束更突出
- 系统时延、通信成本、边缘部署、吞吐或能耗更容易成为一等证据
- 如果论文带控制、通信或车联网背景，工程可实施性比纯 benchmark 排名更重要

写作偏置：

- 贡献句里更适合出现 system / online / vehicular / edge / latency-aware 等词
- 结果节里应给 efficiency / runtime / resource overhead 一个明确位置

### 2.3 IEEE TKDE

偏好：

- 数据建模问题定义清楚
- 结构学习、表示学习、时空依赖建模、泛化性与方法抽象更强
- 相比 T-ITS，交通运营叙事可以稍弱，但任务定义、算法逻辑和实验覆盖必须更规整

写作偏置：

- 需要把 method novelty 讲清楚，尤其是“相比已有 STGNN / Transformer / adaptive graph”到底新在哪
- 更适合把贡献绑定到建模机制、理论直觉、统一框架或学习范式

### 2.4 KDD

偏好：

- data mining 问题抽象 + 强实验包
- 多数据集、多 setting、强 baseline、清楚的 problem formulation
- 方法可以新，但更重要的是问题 framing 准、实验回答完整

写作偏置：

- Introduction 要很快进入“task gap -> why existing families fail -> our response”
- Main table、ablation、OOD/robustness、efficiency 往往缺一不可

### 2.5 NeurIPS / ICML / ICLR

偏好：

- 方法动机尽量抽象而干净
- 机制解释、学习范式、概率建模、理论或统一性更重要
- 如果是交通应用，不能显得只是“在一个应用上跑了几个表”

写作偏置：

- 可以先写建模问题，再落到交通场景
- 但一旦声称交通价值，实验就必须补足 horizon、网络差异、missingness、事件或 domain shift

---

## 3. 跨场刊共通的高价值 paper set 特征

这些论文之所以常被反复引用，不只是因为精度高，而是因为它们至少占住了下面一类位置：

### 3.1 定义了一个长期基线

代表：DCRNN, STGCN, Graph WaveNet, GMAN

可迁移模式：

- 问题定义极清楚
- 数据协议逐渐成为社区默认
- 后续论文容易拿它们做 anchor baseline

写作启发：

- 若你的论文不是新 SOTA，也要争取成为某个 reviewer question 的 anchor artifact
- 比如：更公平协议、更多 horizon 分解、更完整 missing-rate 测试、更强 failure analysis

### 3.2 用反直觉观点打开新叙事

代表：STID

可迁移模式：

- 不只是“我的模型更强”，而是“这个领域可能在错误方向上变复杂”
- 用极简模型挑战复杂模型的默认前提

写作启发：

- 如果你的亮点是 simplification / rethinking / debunking，结构不该伪装成常规复杂方法论文
- 要把“被挑战的默认假设”写成 introduction 的核心张力

### 3.3 把交通现象和模型机制强绑定

代表：PDFormer, MegaCRN, D2STGNN

可迁移模式：

- 不是抽象说 dynamic dependency，而是说 propagation delay、memory pattern、diffusion assumption、dynamic graph 等具体现象
- 每个现象都能映射到一个模块和一个消融

写作启发：

- 贡献不要写“设计三个模块”，要写“针对 X 现象设计 Y 机制，并用 Z 证据验证”

### 3.4 把任务从点预测升级为更高层问题

代表：DiffSTG, UniST, UrbanGPT

可迁移模式：

- 从 deterministic point forecasting 升到 probabilistic forecasting、universal forecasting、instruction-based prediction
- 叙事上不只比 MAE，而是重定义任务边界

写作启发：

- 如果你的论文是范式升级，Figure 1 和 abstract 都应体现“任务重述”，不能只像一个普通 backbone paper

### 3.5 用强工程结果收尾

代表：STAEformer 及近年高性能时空 Transformer 系列

可迁移模式：

- 在标准数据集、标准 horizon、标准 metric 下给出稳定领先
- 通常配套较完整的 benchmark table 和 ablation

写作启发：

- 如果你的核心卖点就是性能，必须把 evaluation package 做到足够完整，否则会被当成 incremental

---

## 4. claim -> evidence -> artifact 的跨 venue 稳定模式

### 4.1 最稳的 claim 类型

1. **mechanism claim**
   - 例：显式传播延迟建模更适合长时域交通预测
2. **scope claim**
   - 例：增益主要出现在长 horizon、稀疏网络或缺失传感器场景
3. **efficiency claim**
   - 例：在接近精度下显著降低参数量 / 推理延迟
4. **robustness claim**
   - 例：在 missingness、noise、domain shift 下退化更慢
5. **reframing claim**
   - 例：复杂图模型并非必要，关键在于建模样本可区分性

### 4.2 最常见的 evidence artifact

| Claim 类型 | 最低证据工件 |
|---|---|
| main effectiveness | 主结果表，按 dataset × horizon 展示 |
| mechanism | 与引言问题一一对应的消融表 / 机制图 |
| robustness | missing-rate / noisy-input / sparse-sensor 结果表或曲线 |
| efficiency | params / FLOPs / latency / memory 表或散点图 |
| failure boundary | case study + error-by-condition 分析 |
| universal / foundation framing | 多任务或 zero-shot / few-shot 迁移表 |

### 4.3 不稳定 claim 的高风险写法

避免：

- “significantly outperforms state-of-the-art methods” 但不写 scope
- “effective in real-world traffic systems” 但没有运营约束或真实协议
- “generalizes well” 但没有 OOD / transfer / cross-dataset evidence
- “interpretable” 但没有可审计 artifact

---

## 5. 引言结构的跨 venue 路由

### 5.1 T-ITS / TVT 风格

推荐六段：

1. 运营重要性或交通现象
2. 具体技术困难
3. 现有方法家族
4. 交通语境下为何失效
5. 方法响应
6. 贡献 + evidence anchors

适合：

- traffic forecasting
- trajectory prediction with deployment relevance
- demand forecasting with network / mobility context

### 5.2 TKDE / KDD 风格

推荐五段：

1. task definition
2. existing modeling families
3. common bottleneck or blind spot
4. method idea and design intuition
5. contributions and experimental scope

适合：

- method paper
- data mining framing
- representation / graph learning emphasis

### 5.3 NeurIPS / ICML / ICLR 风格

推荐四到五段：

1. abstract modeling challenge
2. limitation in existing paradigms
3. proposed framework or learning principle
4. why it should work
5. scoped evidence summary

注意：

- 交通场景不能在实验前完全消失
- 如果全文后面要投 T-ITS 风格版本，最好在 intro 中保留 operational hook

---

## 6. 结果节排序的最佳实践

跨场刊最稳的排序不是“按你实现顺序写”，而是按 reviewer question 排：

1. 是否优于强 baseline
2. 在哪些数据集 / horizon / 条件下优于
3. 为什么优于
4. 代价是什么
5. 在哪里失效

### 推荐结果包

#### 包 A：benchmark core
- Main table: dataset × horizon × metric
- 每个数据集保留场景信息，不只报 overall average

#### 包 B：mechanism verification
- 与引言 challenge 对齐的 ablation
- 模块删减 + 替代设计 + 必要时可视化

#### 包 C：operational realism
- latency / params / memory
- missing rate / sparse sensors / noise / event case

#### 包 D：failure boundary
- 失败场景 case study
- 按条件分桶的 error analysis

---

## 7. 图表套路

### 7.1 Figure 1 按论文定位选，不按习惯选

- **新模型论文**：pipeline / framework figure
- **交通机制论文**：traffic phenomenon -> mechanism teaser
- **经验研究**：study design overview
- **统一模型/基础模型**：task-to-model unification figure

### 7.2 主表的高价值形式

优先：

- by dataset + by horizon
- 多指标并列，但不要只堆指标
- 标出 second-best 仅在表很拥挤时有意义

避免：

- 把所有 horizon 压成一个平均值
- 抹掉 PEMS / METR-LA / PEMS-BAY 等场景差异
- 只在自己有优势的子任务上报结果

### 7.3 高频有效图

1. horizon-wise line plot
2. missing-rate robustness plot
3. efficiency vs performance scatter
4. attention / learned adjacency heatmap
5. qualitative event case study

### 7.4 高风险装饰图

- 没有正文 claim 对应的热力图
- 只好看、不回答问题的城市地图
- 引入正文没定义模块的复杂框图

---

## 8. 代码可复现论文常见的实验协议锚点

这些内容一旦写出来就容易被 reviewer 检查，必须谨慎：

- 数据集名称与时间粒度
- 传感器数量 / 节点数量
- train/val/test split 是否 chronological
- 输入输出窗口长度
- 评估 horizon（15/30/60 min 等）
- normalization 方法
- baseline 来源：原文引用 or 自跑
- 是否使用统一框架（如 LibCity / BasicTS）

如果这些信息拿不准：

- 不写具体数字
- 或标 `needs evidence`
- 或退回到 protocol placeholder，而不是猜

---

## 9. 不同论文类型的 skill 路由建议

### 9.1 method_or_system

优先加载：

- `traffic-writing-patterns.md`
- `traffic-logic-rigor.md`
- `ieee-experiment-playbook.md`
- `traffic-figure-patterns.md`

检查重点：

- challenge -> module -> ablation 是否闭环

### 9.2 empirical_or_software_engineering

优先加载：

- `ieee-writing-spine.md`
- `paper-review.md`
- `ieee-real-experimental-data.md`

检查重点：

- 是否应该改成 RQ-driven structure，而不是硬写 method paper

### 9.3 benchmark_or_dataset

优先加载：

- `ieee-writing-spine.md`
- `ieee-experiment-playbook.md`
- `ieee-data-provenance-checklist.md`

检查重点：

- 数据构建协议
- coverage / annotation / baseline study

### 9.4 foundation / universal ST prediction framing

优先加载：

- `traffic-writing-patterns.md`
- `traffic-anti-ai-writing.md`
- `paper-review.md`

检查重点：

- 不要把“统一 / 通用 / GPT-style”写成空泛概念
- 必须说明 transfer scope、task coverage、failure boundary

---

## 10. 常见 reject risks

1. 把交通任务写成 venue-neutral 的时序预测
2. 贡献句只有模块名，没有现象、证据和范围
3. main table 不按 horizon 拆开
4. 没有 missingness / sparsity / domain shift / event robustness
5. 只报精度，不报效率或部署代价
6. 抽象声称“real-world utility”但没有可审计协议
7. 消融实验与引言提出的问题脱节
8. 结果分析只说“ours is best”，不解释增益出现在哪里
9. foundation / universal 叙事没有 transfer 证据
10. 代码仓库存在但正文协议不清，导致可复现性叙事站不住

---

## 11. 给 `paper-workbench` 的直接执行提示

当用户说：

- “帮我按 T-ITS 风格改这个 intro”
  - 先检查是否有 traffic phenomenon、operational stakes、具体 gap、contribution-evidence anchor

- “帮我设计实验”
  - 默认补齐：main benchmark + horizon breakdown + ablation + robustness + efficiency + failure boundary

- “帮我规划图表”
  - 默认追问 reviewer question，而不是直接列图名

- “帮我润色成顶会/顶刊风格”
  - 先判定是 T-ITS / TVT / TKDE / KDD / NeurIPS-ICML-ICLR 哪一路，不要统一套模板

- “帮我写 contribution”
  - 每条贡献必须含：强动词 + artifact + scoped evidence + section anchor

---

## 12. 最终硬规则

1. 先锁定 venue 和 article type，再写 prose。
2. 先锁定 benchmark/figure/table 角色，再写 results narrative。
3. 交通论文默认要回答：
   - 为什么这是交通问题，而不只是一般时间序列问题？
   - 增益出现在哪些场景？
   - 代价是什么？
   - 在哪里失效？
4. 若答不出上面四个问题，说明论文故事还没锁定，先不要进入终稿式润色。
