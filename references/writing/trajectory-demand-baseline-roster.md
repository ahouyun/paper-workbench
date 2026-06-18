# Trajectory / demand baseline roster

> 目标：给 `paper-workbench` 提供 trajectory prediction 与 mobility / travel demand forecasting 方向的 baseline roster。
>
> 写法与 `traffic-baseline-roster.md` 保持一致：不做“论文堆名单”，而是明确每类 baseline 的生态角色、适用场景、claim 对照意义和常见误用。

---

## 1. 使用原则

### 1.1 为什么 trajectory / demand 需要单独 roster

trajectory prediction 与 demand forecasting 的 baseline 选择逻辑，和 traffic flow forecasting 不一样。

- **trajectory prediction** 更强调：
  - 多模态未来
  - agent interaction
  - map grounding
  - safety-relevant failure
  - scene-centric evaluation

- **demand forecasting** 更强调：
  - region heterogeneity
  - peak/event sensitivity
  - exogenous signals
  - OD or region coupling
  - operationally meaningful breakdown

因此不能直接拿 DCRNN / GWNet / STAEformer 那套 baseline 包原样套用。

### 1.2 roster 的四个用途

该 roster 主要服务：

- **related work framing**：按任务家族组织，而不是堆论文名
- **experiment design**：挑出覆盖关键审稿问题的 baseline set
- **results writing**：解释赢了谁，以及为什么这很重要
- **review / rebuttal**：检查 baseline 是否缺失关键强对手

### 1.3 baseline 选择硬规则

1. baseline 必须覆盖你的核心 claim 所在家族。
2. baseline 需要覆盖“强旧基线 + 新强基线 + 与你最接近的机制对手”。
3. trajectory 论文若 claim 多模态或安全性，不能只放 deterministic baseline。
4. demand 论文若 claim event/exogenous/OD 建模，必须放对应机制 baseline。

---

## 2. trajectory baseline family map

| Family | 代表 | 主要角色 |
|---|---|---|
| recurrent trajectory baseline | Social-LSTM | 早期交互式 trajectory 经典锚点 |
| social pooling baseline | Social-GAN | 多模态 + social pooling 经典代表 |
| graph / relation modeling | Trajectron++ | 交互图建模与多实体关系代表 |
| scene / map-centric forecasting | VectorNet, LaneGCN | 地图与场景结构建模代表 |
| multimodal dense predictor | MultiPath | 车载/自动驾驶多模态预测工程锚点 |
| transformer / attention motion forecasting | AgentFormer | multi-agent attention 家族代表 |
| diffusion / generative forecasting | MID, MotionDiffuser | 生成式多模态 trajectory 代表 |
| foundation / pretraining motion model | MotionLM / motion foundation-style methods | 预训练 / unified motion 建模代表 |

---

## 3. trajectory 单模型 roster

### 3.1 Social-LSTM

**角色定位**

- trajectory prediction 早期经典 baseline
- 用 social pooling 展示交互信息比单体轨迹外推更强

**什么时候应纳入**

- 你写 pedestrian / crowd trajectory prediction
- 你要展示自己不是只赢一个 trivial single-agent extrapolation baseline
- 需要保留领域的历史锚点

**它代表的 claim 对照物**

- interaction awareness 是否确实优于独立轨迹预测
- 你的增益是否超越早期 social interaction 机制

**不要如何误用**

- 不要把它当成唯一 interaction baseline
- 不要只和它比就声称 interaction modeling 有显著突破

**最适合出现的位置**

- related work 中的 early social interaction anchor
- pedestrian trajectory 主表中的 classic baseline

### 3.2 Social-GAN

**角色定位**

- 多模态 trajectory prediction 的经典代表
- 让“未来不是单一轨迹”这件事正式进入 baseline 逻辑

**什么时候应纳入**

- 你 claim multi-modality
- 你报告 best-of-K, minADE, minFDE, miss rate
- 你写的是 pedestrian / urban trajectory prediction

**它代表的 claim 对照物**

- 你的多模态建模是否真的强于早期 GAN-based future generation
- gain 是否来自 better uncertainty handling，而不是只靠 sampling 数量

**不要如何误用**

- 不要和 deterministic 方法放一起却只报一套平均误差
- 不要忽略 K 值与评估协议差异

**最适合出现的位置**

- multimodal baseline family
- trajectory 主表中的 generative predecessor

### 3.3 Trajectron++

**角色定位**

- 图关系 / heterogeneous interaction modeling 代表
- 多实体、多类型 agent interaction 建模强对手

**什么时候应纳入**

- 你声称 interaction reasoning 更强
- 你处理 heterogeneous agents、scene-aware interaction
- 你需要覆盖 graph-based motion forecasting 家族

**它代表的 claim 对照物**

- 你的方法是否超越显式 relational modeling
- 交互 gain 是否真的来自新的 scene reasoning，而不是简单图传播

**不要如何误用**

- 不要在多实体交互论文中缺失它
- 不要只报 overall ADE/FDE，不分析 high-interaction subsets

**最适合出现的位置**

- interaction-heavy trajectory paper 的主表
- related work 中的 graph/relation family anchor

### 3.4 VectorNet

**角色定位**

- vectorized scene representation 代表
- 把 map / lane / scene context 结构化进 motion forecasting 的重要锚点

**什么时候应纳入**

- 你声称 map-aware 或 scene-centric reasoning
- 你用 vectorized map representation 或 lane graph

**它代表的 claim 对照物**

- 你的地图建模是否比早期 vectorized context representation 更有效
- scene understanding 是否真的带来 hard-turn / merge / lane-following gain

**不要如何误用**

- 不要把它当普通 old baseline 忽略
- map-aware paper 缺它很容易被问

**最适合出现的位置**

- map-aware trajectory related work
- Argoverse / autonomous driving motion forecasting 主表

### 3.5 LaneGCN

**角色定位**

- lane graph reasoning 强基线
- 自动驾驶 trajectory / motion forecasting 中极常见 comparator

**什么时候应纳入**

- 你的方法处理 lane topology、route consistency、scene structure
- 你声称 improved map compliance 或 lane-aware motion prediction

**它代表的 claim 对照物**

- 你的 map/lane mechanism 是否优于显式 lane graph reasoning
- off-lane / miss reductions 是否可信

**不要如何误用**

- 不要在 autonomous driving trajectory paper 中缺席它
- 不要只报 minADE/minFDE，不讨论 map compliance 或 hard maneuvers

**最适合出现的位置**

- lane-aware baseline group
- trajectory failure analysis related to map structure

### 3.6 MultiPath

**角色定位**

- 多模态 trajectory engineering baseline
- 在工业 / vehicle trajectory forecasting 叙事里很常见

**什么时候应纳入**

- 你做多模态 vehicle trajectory prediction
- 你 claim deployment-oriented multi-future prediction

**它代表的 claim 对照物**

- 你的多模态输出是否在 practical forecasting setup 下更好
- gain 是否体现在 miss rate、diversity、coverage

**不要如何误用**

- 不要只用 average displacement 指标评估它
- 不要忽略 mode count / anchor design / K setting

**最适合出现的位置**

- industrial / AV trajectory paper 主表
- multimodal forecasting discussion

### 3.7 AgentFormer

**角色定位**

- transformer / attention-based multi-agent forecasting 代表
- 体现“把 agent 当 token 做 joint reasoning”这一条路线

**什么时候应纳入**

- 你的方法是 transformer-based trajectory predictor
- 你声称更强 multi-agent reasoning 或 long-range dependency capture

**它代表的 claim 对照物**

- 新 attention design 是否优于已有 multi-agent transformer
- gain 是否真来自 interaction attention，而不是 model scale

**不要如何误用**

- 不要在 transformer motion forecasting 论文里缺失它
- 不要只说 outperform attention baselines，而不点名强代表

**最适合出现的位置**

- transformer family related work
- interaction modeling comparison

### 3.8 MID / MotionDiffuser 类 diffusion baseline

**角色定位**

- diffusion / generative motion forecasting 代表
- 用于多模态未来、uncertainty、distribution modeling 的强对手

**什么时候应纳入**

- 你 claim generative or diffusion forecasting
- 你强调 future distribution、diversity、calibration、rare maneuvers

**它代表的 claim 对照物**

- 你的生成式建模是否比已有 diffusion route 更有效
- gain 是否体现在 uncertainty quality，而不是只在 minADE 上微弱改善

**不要如何误用**

- 不要把 diffusion baseline 和 deterministic baseline 混在一起只报一组数
- 不要忽略 sampling budget 与 evaluation protocol

**最适合出现的位置**

- generative trajectory related work
- calibration / diversity experiment package

### 3.9 Motion foundation / pretraining-style baselines

**角色定位**

- unified / foundation / pretrained motion forecasting 代表
- 体现 trajectory 领域从 task-specific model 向 pretraining / generalist model 的升级

**什么时候应纳入**

- 你 claim transfer, pretraining, zero-shot, unified motion modeling
- 你把 paper 写成 foundation-style trajectory 叙事

**它代表的 claim 对照物**

- 你的统一性和泛化性是否真有 evidence
- gain 是否出现在 cross-dataset / cross-scenario settings

**不要如何误用**

- 不要只在单 benchmark 上和它比较，然后声称 generalization superiority
- 不要忽略 pretraining data scope 差异

**最适合出现的位置**

- foundation / transfer table
- rebuttal 中回应“scope is narrow”

---

## 4. demand baseline family map

| Family | 代表 | 主要角色 |
|---|---|---|
| statistical temporal baseline | ARIMA / historical average | 最基础 operational anchor |
| recurrent ST baseline | DMVST-Net / ST-ResNet style family | 早期需求预测深度学习锚点 |
| graph demand forecasting | Graph WaveNet / AGCRN-like reuse in demand tasks | 图依赖建模代表 |
| region-aware attention / transformer | ST-GDN / transformer-style demand models | 区域异质性与注意力建模代表 |
| exogenous-aware forecasting | DeepUrbanEvent / event-aware demand models | 外部信号/事件驱动建模代表 |
| OD / mobility matrix forecasting | GEML / ODCRN family | OD demand coupling代表 |
| diffusion / generative demand modeling | diffusion-style urban demand methods | 需求分布与生成式预测代表 |
| universal urban foundation model | UrbanGPT / urban foundation-style methods | 统一城市时空建模代表 |

---

## 5. demand 单模型 roster

### 5.1 ARIMA / Historical Average

**角色定位**

- 需求预测最基础 operational anchor
- 虽然不强，但能证明任务确实需要时空模型而不是简单周期外推

**什么时候应纳入**

- 你要展示 task non-triviality
- 你写应用导向或系统导向论文

**它代表的 claim 对照物**

- 你的方法是否超越简单历史规律和短期惯性
- gain 是否不是“复杂模型打简单统计”的假胜利

**不要如何误用**

- 不要把它当唯一 baseline
- 不要只赢它就宣称 practical superiority

**最适合出现的位置**

- 主表中的 classical anchor
- introduction / motivation 中的 trivial-baseline contrast

### 5.2 ST-ResNet / DMVST-Net 家族

**角色定位**

- 早期 demand forecasting 深度学习锚点
- 表示 urban demand forecasting 不只是普通时间序列，而是需要 spatial + temporal fusion

**什么时候应纳入**

- 你做 region-level bike / taxi / ride-hailing demand forecasting
- 你要交代 demand forecasting 从 CNN/RNN fusion 演化而来

**它代表的 claim 对照物**

- 你的新模型是否超越经典 urban demand deep models
- 空间区域相关性是否比早期 grid/city representation 更好地被利用

**不要如何误用**

- 不要在 demand paper 中完全跳过这一代经典工作
- 不要只报 average metric，不分析 dense vs sparse regions

**最适合出现的位置**

- demand related work 中的 early deep baseline group
- main table 中的 classic deep comparator

### 5.3 Graph WaveNet / AGCRN-like demand comparators

**角色定位**

- 图建模在 demand forecasting 中的迁移强基线
- 适合 region graph / zone dependency / long temporal patterns 任务

**什么时候应纳入**

- 你的 demand forecasting 模型使用 graph 或 adaptive graph
- 你 claim better region coupling modeling

**它代表的 claim 对照物**

- 图结构建模是否真的有收益
- 你的 demand graph design 是否超越已有强工程图基线

**不要如何误用**

- 不要直接套 traffic flow 结果叙事
- 要说明 demand graph 的节点和边定义

**最适合出现的位置**

- graph-based demand paper 主表
- region coupling related work

### 5.4 region-aware attention / transformer demand models

**角色定位**

- 需求预测中的 heterogeneous-region attention 代表
- 用于说明不同城区、不同活跃度区域需要差异化建模

**什么时候应纳入**

- 你用 transformer / attention / region token 做 demand forecasting
- 你强调 long-range urban dependency 或 heterogeneous urban dynamics

**它代表的 claim 对照物**

- attention 是否真的比 graph / CNN / RNN family 更有价值
- gain 是否主要出现在高异质性区域或复杂时段

**不要如何误用**

- 不要只比较总平均误差
- 如果 claim heterogeneous gains，必须有 by-region breakdown

**最适合出现的位置**

- transformer demand family
- region-wise analysis section

### 5.5 exogenous-aware / event-aware demand baselines

**角色定位**

- 体现 weather, holiday, POI, event, mobility context 等外部信号建模的重要性
- 在 demand forecasting 中非常关键，因为 reviewer 常问“外部因素到底贡献了多少”

**什么时候应纳入**

- 你显式使用 weather / holiday / event / POI / social signals
- 你 claim improved event-day forecasting or disruption robustness

**它代表的 claim 对照物**

- 外部信号融合是否真的有帮助
- gain 是否集中在特殊时段而不是普通工作日

**不要如何误用**

- 不要 claim exogenous benefits 却不与这类 baseline 比
- 不要只做 overall metric，不拆 event subset

**最适合出现的位置**

- event-aware demand forecasting related work
- ablation by signal source
- event-day case analysis

### 5.6 GEML / ODCRN 类 OD demand baselines

**角色定位**

- OD matrix / origin-destination mobility forecasting 代表
- 强调不是单区域 demand，而是区域对之间的耦合流动

**什么时候应纳入**

- 你的任务是 OD demand forecasting
- 你 claim pairwise mobility interaction or cross-zone flow modeling

**它代表的 claim 对照物**

- 你的方法是否超越已有 OD coupling models
- 贡献是否真的来自 pairwise structure，而不是 aggregate demand smoothing

**不要如何误用**

- 不要把 OD task 和 region aggregate task baseline 混为一谈
- 不要只画总体热力图，不报 OD-level metrics 或 subsets

**最适合出现的位置**

- OD benchmark table
- method motivation for pairwise structure

### 5.7 diffusion / generative demand baselines

**角色定位**

- 需求分布建模、异常时段生成式预测、uncertainty-aware demand forecasting 代表

**什么时候应纳入**

- 你做 uncertainty-aware demand forecasting
- 你 claim multi-future demand or distributional robustness

**它代表的 claim 对照物**

- 生成式 demand modeling 是否改善 peak uncertainty / rare events
- 你的 gain 是否体现在 distribution quality，而不是 only average RMSE

**不要如何误用**

- 不要只用 point metrics 比 generative baseline
- 要补充 interval / calibration / coverage 风格证据

**最适合出现的位置**

- uncertainty-aware demand experiment section
- event/disruption forecasting discussion

### 5.8 UrbanGPT / urban foundation-style baselines

**角色定位**

- unified urban spatiotemporal modeling 代表
- 把需求预测放入更宽的 urban foundation model 叙事

**什么时候应纳入**

- 你 claim universal urban model、cross-task transfer、prompt-based prediction
- 你写的是 city foundation model 叙事

**它代表的 claim 对照物**

- 你的统一性是不是实证成立
- transfer / cross-task capability 是否真实，而不是概念包装

**不要如何误用**

- 不要只用单城市单任务指标比较它
- 不要忽略它的 task scope 与 pretraining scope

**最适合出现的位置**

- unified urban modeling related work
- multi-task / transfer experiment tables

---

## 6. 按论文类型选 baseline

### 6.1 trajectory prediction method paper

最小可接受 baseline 包：

- Social-LSTM
- Social-GAN
- Trajectron++
- VectorNet 或 LaneGCN
- AgentFormer

如果你 claim generative / diffusion：

- 再加 MID / MotionDiffuser 类 baseline

如果你 claim foundation / transfer：

- 再加 motion foundation-style baseline

### 6.2 map-aware autonomous driving trajectory paper

至少覆盖：

- VectorNet
- LaneGCN
- MultiPath
- AgentFormer
- 一个 diffusion/generative motion baseline（若你 claim multi-modal superiority）

### 6.3 demand forecasting method paper

最小可接受 baseline 包：

- ARIMA / HA
- ST-ResNet 或 DMVST-Net family
- 一个 graph demand baseline
- 一个 region-aware attention/transformer baseline

如果你 claim event/exogenous superiority：

- 再加 exogenous-aware demand baseline

如果你是 OD forecasting：

- 再加 GEML / ODCRN family

如果你是 uncertainty/generative forecasting：

- 再加 diffusion/generative demand baseline

### 6.4 unified / foundation urban model paper

至少覆盖：

- 一个 classic demand deep baseline
- 一个 graph demand baseline
- 一个 transformer/attention demand baseline
- UrbanGPT / urban foundation-style baseline

如果带 trajectory task：

- trajectory side 再补 AgentFormer + map-aware baseline + generative baseline

---

## 7. 结果分析时如何写这些 baseline

### 7.1 trajectory 结果分析

不要写：

- “Our method outperforms prior methods on ADE and FDE.”

优先写：

- “Compared with early social-interaction baselines such as Social-LSTM and Social-GAN, the gain suggests that explicit multi-agent reasoning remains necessary under dense interactions ...”
- “Relative to LaneGCN, the improvement is concentrated in map-constrained maneuvers, indicating that our representation better preserves lane-level structure ...”
- “Against diffusion-based motion forecasting baselines, the gain appears mainly in miss-rate and hard-turn scenarios rather than average displacement alone ...”

### 7.2 demand 结果分析

不要写：

- “Our method achieves the best overall MAE.”

优先写：

- “Compared with classic urban demand baselines such as ST-ResNet/DMVST-Net, the improvement mainly appears in sparse and event-sensitive regions ...”
- “Relative to graph demand baselines, the gain is most visible during peak transitions, suggesting better cross-region dependency modeling ...”
- “Compared with exogenous-aware baselines, the advantage is concentrated on abnormal days, which supports our claim that event signals are used more selectively ...”

---

## 8. 常见误区

### 8.1 trajectory

1. 只放 deterministic baseline，却 claim multi-modal superiority
2. map-aware paper 缺失 VectorNet / LaneGCN 一类强 comparator
3. 只报平均误差，不做 hard interaction 或 miss-rate 分析
4. generative baseline 比较时不控制 K 或 sampling budget
5. foundation-style claim 没有 transfer comparator

### 8.2 demand

1. 只放 ARIMA/HA 和自己模型，baseline 过弱
2. graph/transformer demand paper 不和 region-aware baseline 比
3. event-aware claim 没有 exogenous-aware comparator
4. OD task 缺 OD-specific baseline
5. 只报 city-level overall metric，不做 region/event breakdown

---

## 9. 给 `paper-workbench` 的直接使用提示

当用户说：

- “帮我挑 trajectory baseline”
  - 先判断是 pedestrian / AV / map-aware / multi-agent / generative 哪一路

- “帮我挑 demand baseline”
  - 先判断是 region-level / OD / event-aware / exogenous-aware / unified 哪一路

- “帮我写 related work”
  - trajectory 按 social / graph / map / transformer / generative / foundation 家族写
  - demand 按 statistical / classic deep / graph / transformer / exogenous / OD / generative / foundation 家族写

- “审稿人说 baseline 不够强”
  - trajectory 检查是否缺：Social-GAN / Trajectron++ / VectorNet / LaneGCN / AgentFormer / diffusion baseline
  - demand 检查是否缺：classic deep baseline / graph baseline / exogenous-aware baseline / OD baseline / foundation baseline

---

## 10. 最终硬规则

1. trajectory baseline 必须和未来不确定性、交互、地图约束中的至少一个核心问题对齐。
2. demand baseline 必须和区域异质性、事件扰动、外部信号、OD coupling 中的至少一个核心问题对齐。
3. 若 claim multi-modal / generative superiority，不能缺 generative comparator。
4. 若 claim map-aware / lane-aware superiority，不能缺 map-centric comparator。
5. 若 claim event-aware / exogenous-aware superiority，不能缺对应 baseline。
6. 若 claim unified / foundation capability，不能缺 transfer-oriented comparator。
