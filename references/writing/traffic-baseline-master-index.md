# 交通 baseline master index

> 目标：把 `paper-workbench` 中与交通 / 时空预测 baseline 选择直接相关的 roster 收敛成一个总入口。
>
> 这个文件不重复展开所有细节，而是负责：
> 1. 快速判断当前任务属于哪条 baseline 路线
> 2. 告诉 skill 优先加载哪个 roster
> 3. 提供最小 baseline 选择框架
> 4. 降低一次性加载多个 roster 带来的上下文噪声

---

## 1. 这个 index 管什么

当用户请求以下任务时，优先先看本文件：

- 帮我挑 baseline
- 帮我写 related work
- 帮我检查 baseline 是否够强
- 帮我设计主结果表
- 帮我分析为什么赢了这些方法
- 帮我准备审稿人关于 baseline 的质疑

本文件只做 baseline 路由和最小决策，不替代具体 roster。

---

## 2. baseline 路由总图

| 任务类型 | 优先加载 |
|---|---|
| traffic flow / speed / ST forecasting | `references/writing/traffic-baseline-roster.md` |
| trajectory prediction / motion forecasting | `references/writing/trajectory-demand-baseline-roster.md` |
| demand forecasting / ride-hailing / taxi / bike / metro / OD demand | `references/writing/trajectory-demand-baseline-roster.md` |
| 跨场刊 baseline 叙事或 venue-aware framing | `references/writing/traffic-cross-venue-patterns.md` |
| 不确定属于哪类交通时空任务 | 先本文件，再按任务分流 |

### 硬规则

1. 不要默认把所有交通任务都路由到 traffic forecasting baseline。
2. 不要在需要具体 baseline 选择时只加载跨场刊写作参考，而不加载 roster。
3. 若用户既问 baseline，又问 venue 风格，先加载对应 roster，再补 `traffic-cross-venue-patterns.md`。

---

## 3. 三份核心文件的职责分工

### 3.1 `traffic-baseline-roster.md`

负责：

- traffic flow / speed / generic spatiotemporal forecasting 的 baseline 家族
- DCRNN / STGCN / Graph WaveNet / GMAN / STID / PDFormer / STAEformer / MegaCRN / DiffSTG / UniST 这条主生态
- 用于：
  - flow forecasting baseline selection
  - ST forecasting related work
  - benchmark table comparator coverage
  - rebuttal: “baseline not strong enough”

### 3.2 `trajectory-demand-baseline-roster.md`

负责：

- trajectory prediction baseline 家族
- mobility / travel demand forecasting baseline 家族
- 用于：
  - motion forecasting comparator selection
  - demand forecasting comparator selection
  - map-aware / multi-modal / exogenous-aware / OD-aware 对手覆盖

### 3.3 `traffic-cross-venue-patterns.md`

负责：

- baseline 不是怎么选“名字”，而是怎么写成 reviewer-friendly 叙事
- T-ITS / TVT / TKDE / KDD / NeurIPS / ICML / ICLR 的场刊偏置
- 用于：
  - 把 baseline 列表变成结果分析和 contribution framing
  - 防止“论文名流水账”式 related work

---

## 4. 最小 baseline 选择决策树

### Step 1: 先判任务对象

问自己：

1. 预测的是 **sensor/region 数值**，还是 **agent future trajectory**？
2. 如果是数值预测，是 **flow/speed**，还是 **demand/OD**？
3. 如果是 trajectory，是 **pedestrian** 还是 **autonomous driving / vehicle motion**？

### Step 2: 再判核心 claim

问自己：

- 你主打的是 accuracy 吗？
- mechanism 吗？
- efficiency 吗？
- uncertainty / multi-modality 吗？
- transfer / foundation framing 吗？
- event-awareness / exogenous signals 吗？
- map-awareness / lane-awareness 吗？

### Step 3: 再判 baseline family

#### A. traffic forecasting
至少覆盖：

- 经典图基线
- 强工程基线
- attention / transformer 基线
- 反复杂度基线

如果 claim generative / foundation，再补：

- DiffSTG / UniST 这类路线

#### B. trajectory prediction
至少覆盖：

- early interaction baseline
- graph/relation baseline
- map-aware baseline
- attention/transformer baseline

如果 claim multi-modal / generative，再补：

- Social-GAN / diffusion motion baseline

#### C. demand forecasting
至少覆盖：

- statistical anchor
- classic deep demand baseline
- graph or transformer demand baseline

如果 claim exogenous / event / OD / foundation，再补对应路线 baseline。

---

## 5. 典型用户请求 -> 加载策略

### 5.1 “帮我挑 traffic forecasting baseline”

加载顺序：

1. `traffic-baseline-roster.md`
2. 若还要按 venue 写结果分析，再补 `traffic-cross-venue-patterns.md`

### 5.2 “帮我挑 trajectory prediction baseline”

加载顺序：

1. `trajectory-demand-baseline-roster.md`
2. 若是 T-ITS / TVT 风格投稿，再补 `traffic-cross-venue-patterns.md`

### 5.3 “帮我挑 demand forecasting baseline”

加载顺序：

1. `trajectory-demand-baseline-roster.md`
2. 若强调城市交通运营或 venue 风格，再补 `traffic-cross-venue-patterns.md`

### 5.4 “帮我写交通方向的 related work”

加载顺序：

1. 先按任务加载对应 roster
2. 再加载 `traffic-cross-venue-patterns.md`

原因：

- roster 负责“该写谁”
- cross-venue file 负责“该怎么写”

### 5.5 “审稿人说 baseline 不够强”

加载顺序：

1. 对应 roster
2. 必要时补 `traffic-cross-venue-patterns.md`

检查重点：

- 是否缺历史锚点
- 是否缺当前路线强对手
- 是否缺与你 claim 最接近的 comparator

---

## 6. 写 related work 时的统一规则

无论哪类交通任务，related work 都不要按年份流水账写。

优先按 baseline family 写：

- classic / early anchor
- graph / relation family
- attention / transformer family
- mechanism-specific family
- generative / probabilistic family
- foundation / transfer family

### 对应关系

- traffic forecasting：看 `traffic-baseline-roster.md`
- trajectory / demand：看 `trajectory-demand-baseline-roster.md`
- venue 风格压缩：看 `traffic-cross-venue-patterns.md`

---

## 7. 结果分析时的统一规则

不要写：

- “Our method outperforms all baselines.”

优先写：

- 赢了哪一类 baseline
- 这说明了什么
- 增益出现在哪些条件下
- 哪个 comparator 最能支撑核心 claim

### 推荐句法

- relative to classic baselines...
- compared with strong graph-based comparators...
- against the most relevant transformer baseline...
- the gain is concentrated under...
- this suggests that...

详细展开时：

- comparator 名单来自对应 roster
- 叙事方式来自 `traffic-cross-venue-patterns.md`

---

## 8. 审稿风险快速检查

若出现以下情况，说明应进一步加载具体 roster：

1. 只和 old baseline 比，没有新强 baseline
2. 只和新模型比，没有历史锚点
3. claim generative superiority，但没有 generative comparator
4. claim map-aware superiority，但没有 map-centric comparator
5. claim event-aware superiority，但没有 exogenous-aware comparator
6. claim foundation capability，但没有 transfer-oriented comparator

---

## 9. 给 `paper-workbench` 的直接执行提示

当用户提到：

- baseline
- comparator
- strong baselines
- related work
- rebuttal about baseline strength

先调用本 index 做分流，再决定加载具体 roster。

### 最小执行顺序

1. identify task family
2. identify core claim
3. load one roster
4. only then load cross-venue writing reference if needed

不要默认一次把三个文件全加载进上下文。

---

## 10. 最终硬规则

1. baseline 选择先分任务，再分 claim，再分家族。
2. roster 负责选人，cross-venue file 负责写法。
3. traffic、trajectory、demand 三类任务默认不用同一套 comparator。
4. 当用户只问 baseline 时，优先加载本 index + 一个具体 roster，不要把所有交通参考一起塞进上下文。
