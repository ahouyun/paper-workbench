# Trajectory / demand forecasting 写作与实验参考

> 目标：补足 `paper-workbench` 在 trajectory prediction 与 mobility / travel demand forecasting 方向的专项参考。
>
> 这两类任务和 traffic flow forecasting 共享时空建模骨架，但在论文叙事、结果分析、图表角色、审稿问题上并不相同。不能直接套 traffic flow 的默认模板。

---

## 1. 为什么需要单独参考

### 1.1 trajectory prediction 与 traffic flow forecasting 的差别

trajectory prediction 常见对象是：

- pedestrian trajectory
- vehicle trajectory
- agent motion forecasting
- multi-agent interaction forecasting
- map-aware trajectory prediction

核心问题通常不是“预测某个传感器未来数值”，而是：

- 多模态未来
- 交互影响
- 地图约束
- 意图不确定性
- 安全相关失败模式

因此不能直接照搬：

- dataset × horizon 的表格逻辑
- 只报 MAE/RMSE 的结果叙事
- 只做 speed/flow 类型的 case figure

### 1.2 demand forecasting 与 traffic flow forecasting 的差别

demand forecasting 常见对象是：

- ride-hailing demand
- taxi / metro / bike demand
- OD demand
- region-level mobility demand
- event-aware urban demand forecasting

核心问题往往是：

- 区域异质性
- 周期性与突发事件共存
- exogenous signals 是否真的有用
- spatial partition / zone graph 如何定义
- 需求高峰和低流量区域的误差不均衡

因此不能只用 flow forecasting 的“路网 + 传感器”叙事替代。

---

## 2. article type routing

### 2.1 trajectory prediction 常见 article type

1. **method_or_system**
   - 新的交互建模、地图建模、多模态生成、意图推断方法
2. **benchmark_or_dataset**
   - 新轨迹数据集、场景集、预测 benchmark
3. **empirical_or_software_engineering**
   - 比较不同 motion forecasting pipeline、评估协议或 safety metric 的研究

### 2.2 demand forecasting 常见 article type

1. **method_or_system**
   - region/graph/transformer/diffusion 等需求预测模型
2. **empirical_or_software_engineering**
   - 对不同区域划分、外部信号、事件鲁棒性、评估协议的经验研究
3. **benchmark_or_dataset**
   - 城市需求数据集、OD benchmark、multi-modal mobility benchmark

硬规则：

- 如果论文主要贡献是新的 benchmark / evaluation setup，不要硬伪装成纯模型论文。
- 如果论文主要是在分析错误模式或协议差异，应优先考虑经验研究结构。

---

## 3. trajectory prediction 的写作主线

### 3.1 引言最稳的张力来源

trajectory prediction 的引言更适合围绕这些张力：

1. **future is multi-modal**
2. **agent interaction matters**
3. **map / scene context constrains motion**
4. **rare maneuvers and safety-critical failures matter**
5. **best-of-K metrics can hide practical failure**

### 3.2 trajectory 引言推荐结构

1. task importance and deployment context
2. why future uncertainty makes point prediction insufficient
3. existing families: recurrent / graph / attention / generative / scene-centric
4. concrete bottleneck in interaction, map grounding, or uncertainty handling
5. proposed response
6. contribution list with evidence anchors

### 3.3 trajectory contribution 的好写法

优先写成：

- interaction mechanism + safety-relevant evidence
- map-aware representation + off-lane / miss reduction
- multi-modal decoder + calibration / coverage evidence
- scene-centric reasoning + hard-scenario gains

避免：

- “novel trajectory framework”
- “significantly improves prediction performance” without metric scope

---

## 4. demand forecasting 的写作主线

### 4.1 引言最稳的张力来源

demand forecasting 更适合围绕：

1. **heterogeneous spatial demand patterns**
2. **periodicity + event disruption coexist**
3. **low-demand regions are easy to ignore but operationally important**
4. **external signals may help but are noisy / unstable**
5. **aggregate gains may hide region-level failures**

### 4.2 demand forecasting 引言推荐结构

1. operational need: dispatching, fleet planning, public transport balancing
2. spatial-temporal heterogeneity in urban demand
3. existing model families and what they miss
4. concrete bottleneck: event sensitivity, sparse regions, OD coupling, exogenous fusion
5. method or study response
6. contributions + evaluation scope

### 4.3 demand contribution 的好写法

优先写成：

- region-aware / OD-aware modeling + difficult-region evidence
- event-aware or exogenous fusion design + disruption-case evidence
- multi-scale urban dependency modeling + cross-zone gain pattern
- forecasting system + dispatch-relevant or planning-relevant value

避免：

- 把 demand forecasting 写成 generic time-series regression
- 只报 city-level average，不报区域分布差异

---

## 5. claim -> evidence -> artifact 迁移规则

### 5.1 trajectory prediction

| Claim | 推荐证据 | 推荐 artifact |
|---|---|---|
| better average accuracy | ADE / FDE / minADE / minFDE | 主结果表 |
| better multi-modality | miss rate / coverage / calibration / diversity | 主表 + 多轨迹可视化 |
| better interaction reasoning | hard interaction subsets / collision-related analysis | subset table + case figure |
| better map compliance | off-road / lane violation / map consistency | robustness table + scene figure |
| safer failure profile | worst-case / tail-risk / hard scenario metrics | failure analysis figure |

### 5.2 demand forecasting

| Claim | 推荐证据 | 推荐 artifact |
|---|---|---|
| better demand accuracy | MAE / RMSE / MAPE / SMAPE / WAPE | 主结果表 |
| better peak handling | peak-hour subset / event-day subset | subset table + line figure |
| better sparse-region performance | by-zone bucket analysis | bucket plot / region heatmap |
| exogenous signals help | ablation by signal source | ablation table |
| operational value | dispatch / allocation proxy or scenario-specific gain | case study figure / discussion table |

硬规则：

- trajectory 论文不能只报平均 ADE/FDE 而不讨论多模态失败。
- demand 论文不能只报 city-level average 而不讨论 region heterogeneity。

---

## 6. 结果节排序

### 6.1 trajectory prediction

推荐顺序：

1. main benchmark metrics
2. multi-modal quality / miss-rate / calibration
3. interaction or map-aware mechanism verification
4. hard-scenario / safety-relevant failure analysis
5. efficiency if deployment is claimed

### 6.2 demand forecasting

推荐顺序：

1. main demand forecasting table
2. by-region / by-time / by-event breakdown
3. exogenous or graph mechanism ablation
4. peak / sparse / event-case analysis
5. efficiency or deployment cost if claimed

不要按“模型模块实现顺序”写结果。

---

## 7. 图表套路

### 7.1 trajectory prediction 高频有效图

1. **scene + predicted trajectories overlay**
   - 展示 GT 与 multiple futures
2. **hard interaction case figure**
   - 交汇、变道、避障、拥挤场景
3. **miss-rate / calibration curve**
4. **error by horizon / by maneuver type plot**
5. **map compliance figure**
   - off-road or lane adherence cases

### 7.2 trajectory prediction 高风险图

- 只挑最漂亮 case，不展示失败模式
- 多模态图里没有说明哪条是 GT、哪条是 prediction
- scene figure 好看但不回答具体 reviewer question

### 7.3 demand forecasting 高频有效图

1. **region heatmap**
   - 预测误差或 demand intensity spatial map
2. **peak-hour line chart**
   - 高峰 / 非高峰对比
3. **event-day case figure**
   - 节假日、天气、演唱会、突发事件前后
4. **bucket plot by region activity**
   - 高频区、中频区、低频区误差对比
5. **OD matrix visualization**
   - 若任务是 OD demand forecasting

### 7.4 demand forecasting 高风险图

- 只有城市整体曲线，没有区域差异
- heatmap 漂亮但没有误差解释
- 不交代 zone partition / grid protocol

---

## 8. 实验设计注意点

### 8.1 trajectory prediction

必须先确认：

- single-agent 还是 multi-agent
- map available 还是 map-free
- deterministic 还是 multi-modal probabilistic
- evaluation split 是否 standard
- top-K / best-of-K 设置是否公平

高价值补充实验：

- by maneuver type
- by scene density
- by horizon length
- by rare-event subset
- calibration / diversity / miss-rate

### 8.2 demand forecasting

必须先确认：

- region-based, grid-based, graph-based, 还是 OD-based
- 是否引入 exogenous signals
- zone partition 如何定义
- split 是否按时间顺序
- 是否包含 event days / holidays / abnormal periods

高价值补充实验：

- peak vs off-peak
- dense vs sparse regions
- event vs normal day
- ablation by exogenous channel
- cross-city or cross-period transfer

---

## 9. 常见 reject risks

### 9.1 trajectory prediction

1. 只报平均误差，不讨论 multi-modal failure
2. 没有 hard-scenario 或 interaction-specific 分析
3. 地图/场景机制 claim 没有 map-consistency evidence
4. best-of-K 设定不公平
5. 案例图只展示成功例子
6. 安全相关价值被声称但没有 failure boundary

### 9.2 demand forecasting

1. 只报 overall average，不报区域异质性
2. 高峰期 / event day 表现没有单独分析
3. exogenous feature claim 没有消融支持
4. zone / grid / OD protocol 写不清
5. operational value 被声称但没有可审计 evidence
6. 低需求区域失败被平均指标掩盖

---

## 10. route 给 `paper-workbench` 的直接提示

当用户提到：

- trajectory prediction / motion forecasting / trajectory forecasting
  - 默认先检查：multi-modal future、interaction、map grounding、safety-relevant failure

- demand forecasting / ride-hailing demand / taxi demand / OD demand
  - 默认先检查：region heterogeneity、peak/event sensitivity、exogenous signals、operational value

- 帮我设计图表
  - trajectory 优先给 scene overlay / miss-rate / hard-case figure
  - demand 优先给 region heatmap / peak-hour line / event-day case

- 帮我写结果分析
  - trajectory 不要只说 ADE/FDE 更低，要说明在哪类未来更稳
  - demand 不要只说 overall MAE 更低，要说明哪些区域、哪些时段收益更明显

---

## 11. 最终硬规则

1. trajectory 论文默认把“未来不确定性”当成一等问题。
2. demand 论文默认把“区域异质性 + 事件扰动”当成一等问题。
3. 不要把 traffic flow 的主表模板原样套到 trajectory 或 demand。
4. 所有声称的 operational value 都需要可审计 artifact。
5. 如果论文核心卖点涉及安全、调度或部署，失败边界必须可见。
