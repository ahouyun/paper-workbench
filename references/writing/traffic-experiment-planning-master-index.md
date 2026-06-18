# 交通论文 experiment-planning master index

> 目标：把 `paper-workbench` 中与交通 / 时空预测论文实验包直接相关的四条链统一成一个总入口。
>
> 这个文件不重复展开所有细节，而是负责：
> 1. 先判断当前请求属于哪类实验规划任务
> 2. 告诉 skill 先加载哪条 planning reference
> 3. 把 baseline、figure、experiment、provenance 串成一条最小执行链
> 4. 避免一次性把所有交通实验参考全塞进上下文

---

## 1. 这个 index 管什么

当用户请求以下任务时，优先先看本文件：

- 帮我设计实验包
- 帮我规划主表 / 消融 / 鲁棒性实验
- 帮我规划 Figure 1 / Table I / case study
- 帮我检查 claim 是否有对应实验支撑
- 帮我检查数字能不能写进摘要 / 引言 / 结果
- 帮我准备实验部分或 rebuttal 的证据链

本文件只做 experiment-planning 路由和最小决策，不替代具体参考文件。

---

## 2. experiment-planning 路由总图

| 任务类型 | 优先加载 |
|---|---|
| baseline 选择 / comparator coverage | `references/writing/traffic-baseline-master-index.md` |
| 实验设计 / 主结果表 / 消融 / 鲁棒性 | `references/writing/ieee-experiment-playbook.md` |
| 图表规划 / Figure 1 / Table I / case figure | `references/writing/ieee-visual-playbook.md` |
| 具体数字 / 数据规模 / 时延 / 参数量 / 改善百分比核验 | `references/writing/ieee-data-provenance-checklist.md` |
| trajectory / demand 专项实验与图表 | `references/writing/trajectory-demand-patterns.md` |
| traffic / ITS 专项叙事与结果组织 | `references/writing/traffic-writing-patterns.md` |
| 不确定属于哪类实验规划任务 | 先本文件，再按任务分流 |

### 硬规则

1. 不要在设计实验包时只挑 baseline，而不检查 artifact 与 provenance。
2. 不要在设计 figure/table 时跳过 reviewer question。
3. 不要在写具体数字前跳过 provenance 检查。
4. 若用户同时问 baseline、实验、图表，先锁 claim，再按本 index 顺序分流。

---

## 3. 六份核心文件的职责分工

### 3.1 `traffic-baseline-master-index.md`

负责：

- baseline family 路由
- comparator coverage 检查
- related work / results / rebuttal 中 baseline 叙事入口

用于：

- 选 baseline
- 检查 baseline 是否够强
- 判断需要哪一类 comparator

### 3.2 `ieee-experiment-playbook.md`

负责：

- claim -> experiment question -> protocol -> metric -> artifact -> conclusion sentence
- 主结果、消融、效率、鲁棒性实验打包
- reviewer-friendly 实验节排序

用于：

- 设计完整实验包
- 规划主表与实验节结构
- 检查 claim 是否真的对应实验问题

### 3.3 `ieee-visual-playbook.md`

负责：

- Figure 1 / Table I / qualitative / tradeoff / failure figure 的角色分配
- reviewer-question-driven 图表规划
- chart/table 选型

用于：

- 规划 figure/table
- 规划 caption role
- 判断哪些图是证据，哪些图只是装饰

### 3.4 `ieee-data-provenance-checklist.md`

负责：

- 数字、规模、速度、参数、改善幅度的 provenance 核验
- 区分 `real / synthetic / generated / augmented / mixed / secondary_reported`
- 阻止未核实数字进入摘要、引言、实验、图表、结论

用于：

- 检查任何具体数字能否进入论文
- 检查图表中的数字是否合法
- 检查 borrowed results 是否被误写成当前实验

### 3.5 `trajectory-demand-patterns.md`

负责：

- trajectory prediction 的 multi-modal / interaction / map / failure 分析路线
- demand forecasting 的 region heterogeneity / event sensitivity / exogenous / OD 路线
- 这两类任务的结果排序与高价值图表

用于：

- trajectory / demand 任务的专项实验规划
- 补充通用 IEEE playbook 不够细的任务偏置

### 3.6 `traffic-writing-patterns.md`

负责：

- traffic / ITS 论文的结果组织、失败边界、部署约束表达
- 更偏 T-ITS / TVT 风格的实验叙事

用于：

- 把实验包写成交通审稿人更容易接受的叙事
- 检查结果顺序是否回答了交通任务的关键问题

---

## 4. 最小 experiment-planning 决策树

### Step 1: 先判当前问题要锁什么

问自己：

1. 现在缺的是 **comparator**，还是 **experiment question**？
2. 现在缺的是 **artifact**，还是 **number provenance**？
3. 现在是通用 traffic forecasting，还是 trajectory / demand 专项任务？

### Step 2: 再判 claim 类型

问自己：

- 你主打的是 accuracy 吗？
- mechanism 吗？
- efficiency 吗？
- robustness / OOD / failure boundary 吗？
- uncertainty / multi-modality 吗？
- event-awareness / exogenous signals 吗？
- transfer / foundation / unified capability 吗？

### Step 3: 再判先加载哪条链

- comparator coverage 不清楚 -> 先 `traffic-baseline-master-index.md`
- claim 对应什么实验不清楚 -> 先 `ieee-experiment-playbook.md`
- 不知道该画什么图/表 -> 先 `ieee-visual-playbook.md`
- 准备写具体数字 -> 先 `ieee-data-provenance-checklist.md`
- trajectory / demand 任务边界不清楚 -> 补 `trajectory-demand-patterns.md`
- 交通/ITS 场景下结果怎么讲不清楚 -> 补 `traffic-writing-patterns.md`

---

## 5. 统一执行顺序

默认按下面顺序组织交通论文实验包：

1. identify task family
2. identify core claims
3. load baseline route and lock comparator coverage
4. map each claim to experiment question and protocol
5. assign one artifact to each major question
6. check whether each artifact needs table / figure / case study / failure analysis
7. run provenance check on all concrete numbers
8. only then write experiment section, results, captions, or rebuttal wording

### 最小链条

`claim -> baseline -> experiment -> artifact -> provenance -> conclusion sentence`

如果中间任何一环缺失，说明实验包还没锁定。

---

## 6. 典型用户请求 -> 加载策略

### 6.1 “帮我设计 traffic forecasting 实验包”

加载顺序：

1. `traffic-baseline-master-index.md`
2. `ieee-experiment-playbook.md`
3. 若要规划图表，再补 `ieee-visual-playbook.md`
4. 若开始写数字，再补 `ieee-data-provenance-checklist.md`

### 6.2 “帮我设计 trajectory prediction 实验和图表”

加载顺序：

1. `trajectory-demand-patterns.md`
2. `traffic-baseline-master-index.md`
3. `ieee-experiment-playbook.md`
4. `ieee-visual-playbook.md`
5. 需要写具体数字时补 `ieee-data-provenance-checklist.md`

### 6.3 “帮我设计 demand forecasting 主表和 case study”

加载顺序：

1. `trajectory-demand-patterns.md`
2. `traffic-baseline-master-index.md`
3. `ieee-experiment-playbook.md`
4. `ieee-visual-playbook.md`
5. 若涉及事件日、峰值、区域 bucket 数字，再补 provenance checklist

### 6.4 “帮我检查摘要里的实验数字能不能写”

加载顺序：

1. `ieee-data-provenance-checklist.md`
2. 若需要回查数字来自哪个实验，再补 `ieee-experiment-playbook.md`

### 6.5 “帮我准备 rebuttal，说实验不够强 / 图不够说明问题”

加载顺序：

1. `traffic-baseline-master-index.md`
2. `ieee-experiment-playbook.md`
3. `ieee-visual-playbook.md`
4. 若引用具体数字，再补 provenance checklist

---

## 7. reviewer-friendly 的统一检查框架

无论是哪类交通论文，实验包至少回答以下问题：

1. 你和哪些强 baseline 比了？
2. 你的核心 claim 分别由哪个实验问题支撑？
3. 每个实验问题对应哪个 table / figure / case artifact？
4. 你付出了什么代价：参数、时延、显存、标注、复杂度？
5. 你在哪里失效，或者在哪些场景收益不明显？
6. 这些具体数字是否都有 provenance？

如果有一个问题答不上来，就说明还需要继续加载对应 reference。

---

## 8. 审稿风险快速检查

若出现以下情况，说明 experiment-planning 链没有闭合：

1. 有 baseline 名单，但没有与 claim 对齐的 experiment question
2. 有主结果表，但没有强相关 comparator
3. 有 figure，但答不出 reviewer question
4. 有漂亮案例图，但没有 failure boundary
5. 有具体数字，但来源不清
6. 有 trajectory claim，却没有 multi-modal / interaction / map / failure 证据
7. 有 demand claim，却没有 region / event / exogenous / OD 证据
8. 声称 T-ITS 式实际价值，却没有 cost 或 deployment-boundary artifact

---

## 9. 给 `paper-workbench` 的直接执行提示

当用户提到：

- experiment package
- experiment planning
- benchmark design
- ablation
- robustness
- figure planning
- table planning
- provenance
- can I write this number

先调用本 index 做分流，再决定加载具体 reference。

### 最小执行顺序

1. identify task family
2. identify core claims
3. load one primary planning reference
4. only then load adjacent references needed to close the chain

不要默认一次把 baseline、visual、experiment、provenance 全部加载进上下文。

---

## 10. 最终硬规则

1. baseline 只是实验包的一环，不等于完整实验规划。
2. 每条 claim 都要能落到 experiment question 和 artifact。
3. 每个 figure/table 都必须回答一个 reviewer question。
4. 每个具体数字进入论文前都必须过 provenance。
5. trajectory 与 demand 任务不能直接套 traffic flow 的默认实验模板。
6. 当用户只问实验包时，优先加载本 index + 当前最关键的一条 planning reference，不要把所有交通实验参考一起塞进上下文。
