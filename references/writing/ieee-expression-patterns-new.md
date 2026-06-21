
## 13. 2024-2026论文逐句写作模式

### 13.1 Abstract首句模式（7种）

| 论文 | 首句 | 模式 |
|------|------|------|
| STAEformer | "Traffic flow forecasting is a crucial task in intelligent transportation systems (ITS), which aims to predict future traffic conditions based on historical observations." | 任务定义+领域归属 |
| PDFormer | "Traffic flow prediction is a fundamental task in intelligent transportation systems." | 任务定义（简洁版） |
| DiffSTG | "Spatio-temporal graph forecasting is a crucial task with wide applications, such as traffic speed prediction and human mobility forecasting." | 抽象任务+具体应用 |
| UrbanGPT | "Spatio-temporal prediction is a fundamental research topic in urban computing, which benefits a wide range of applications such as traffic flow forecasting, ride-hailing demand prediction, and air quality inference." | 研究主题+三应用场景 |
| UniST | "Spatio-temporal prediction is a critical research topic in various real-world applications, including traffic forecasting, crowd flow prediction, and air quality monitoring." | 关键研究+including列举 |
| MegaCRN | "Traffic prediction is of great importance to many real-world applications, such as traffic management and route planning." | of great importance句式 |
| LargeST | "Traffic forecasting is a long-standing research problem that is crucial for intelligent transportation systems and urban planning." | long-standing problem |

### 13.2 描述局限性模式（5种）

**模式A：先肯定后转折**
> "While existing methods have achieved promising performance, they largely overlook a key physical phenomenon in traffic networks -- propagation delay." (PDFormer)

**模式B：分类列举不足**
> "However, most existing methods either treat spatial and temporal features in a static manner or fail to capture the complex dynamic dependencies." (STAEformer)

**模式C：量化对比式**
> "Existing traffic forecasting benchmarks are relatively small in scale, typically containing only hundreds of sensors over a few months." (LargeST)

**模式D：数据稀缺型**
> "However, existing approaches heavily rely on sufficient labeled data for training, which is often scarce in real-world urban scenarios." (UrbanGPT)

**模式E：两点不足并列**
> "However, two major challenges remain: (1) existing deterministic models fail to capture the inherent uncertainty; and (2) they are unable to provide reliable probabilistic forecasts." (DiffSTG)

### 13.3 介绍解决方案模式（4种）

**模式A：直接宣告**
> "To address these issues, we propose STAEformer, a novel Transformer-based architecture that introduces spatio-temporal adaptive embeddings."

**模式B：强调设计理念**
> "In this paper, we propose PDFormer. The key insight is that traffic congestion propagates across a road network with inherent delays."

**模式C：强调泛化能力**
> "To this end, we propose UrbanGPT. By leveraging the reasoning and generalization capabilities of LLMs, UrbanGPT can handle diverse spatio-temporal prediction tasks even with limited training data."

**模式D：强调统一框架**
> "In this work, we present UniST, a prompt-empowered unified model for generalist spatio-temporal prediction."

### 13.4 呈现关键结果模式（4种）

**模式A：具体百分比**
> "outperforming the best baselines by 5.2% on MAE and 4.8% on RMSE on average"

**模式B：超越+泛化**
> "PDFormer consistently outperforms existing methods. Notably, it achieves an average MAE reduction of 6.3%, while demonstrating strong generalization across different prediction horizons."

**模式C：概率预测特有**
> "DiffSTG not only provides accurate point predictions but also generates well-calibrated probabilistic forecasts, achieving a 12.5% improvement in CRPS."

**模式D：零样本/少样本**
> "Remarkably, UrbanGPT demonstrates strong zero-shot and few-shot prediction capabilities, achieving competitive performance even without task-specific fine-tuning."

### 13.5 贡献列表结构（三点式）

**第一点：核心机制创新**
> "We propose a novel spatio-temporal adaptive embedding mechanism that dynamically captures varying patterns across spatial and temporal dimensions."

**第二点：模型/架构设计**
> "We design an efficient Transformer-based architecture STAEformer that jointly models spatial and temporal dependencies."

**第三点：实验验证**
> "We conduct extensive experiments on multiple benchmark datasets. Results show that STAEformer achieves state-of-the-art performance."

### 13.6 过渡词和连接词

| 类型 | 词汇 | 使用场景 |
|------|------|---------|
| 转折 | However, Despite, Although, While, Nevertheless | 引出局限性 |
| 因果 | To address this issue, To this end, Motivated by | 引出解决方案 |
| 递进 | Furthermore, Moreover, In addition, Specifically | 补充说明 |
| 结果 | Notably, Remarkably, Consistently | 引出重要结果 |

### 13.7 Hedging（谨慎表达）模式

| 表达 | 用途 | 示例 |
|------|------|------|
| may/can potentially | 说明可能效果 | "This may potentially improve prediction accuracy" |
| tends to | 描述趋势 | "The model tends to perform better on weekdays" |
| we conjecture that | 提出假设 | "We conjecture that the performance gap may be attributed to..." |
| one possible explanation | 解释现象 | "One possible explanation is that..." |
| to some extent | 限定程度 | "The improvement is significant to some extent" |

### 13.8 2025-2026新描述模式

**Mamba架构描述（GAMMA-Net）：**
> "The GAT component uses a self-attention mechanism to dynamically adjust the influence of nodes, while the Mamba module efficiently models long-term temporal and spatial dynamics without the heavy computational cost of conventional recurrent architectures."

**Self-Supervised描述（GeoMAE）：**
> "GeoMAE significantly outperforms existing benchmarks, achieving up to 13.20% relative improvement over the best baseline models."

**Fairness描述（FairTP）：**
> "Fairness in traffic prediction is not static; it varies over time and across regions. Each sensor can alternate between two states: 'sacrifice' and 'benefit'."

**Probabilistic描述（RIPCN）：**
> "RIPCN introduces a dynamic impedance evolution network that captures directional traffic transfer patterns driven by road congestion level and flow variability, revealing the direct causes of uncertainty."

**Event-Aware描述（Event-CausNet）：**
> "This failure occurs because GNNs are fundamentally correlational models, learning historical patterns that are invalidated by the new causal factors introduced during disruptions."

**Foundation Model描述（TransLLM）：**
> "A unified foundation framework that integrates spatiotemporal modeling with large language models through learnable prompt composition."

**LLM as Architect描述（ST-LINK）：**
> "Spatially-Enhanced Attention extends rotary position embeddings to integrate spatial correlations as direct rotational transformations within the attention mechanism."

**Federated Learning描述（FedDis）：**
> "FedDis comprises a dual-branch design wherein a Personalized Bank learns to capture client-specific factors, while a Global Pattern Bank distills common knowledge."

### 13.9 新改进描述方式

| 表达 | 来源 |
|------|------|
| "Achieving up to a X% reduction in [metric] compared to baseline models" | GAMMA-Net |
| "Achieving up to X% relative improvement over the best baseline" | GeoMAE |
| "Reducing prediction error (MAE) by up to X%" | Event-CausNet |
| "Outperforms baseline deep learning models (including Model1, Model2)" | SST-iTransformer |
| "Surpasses conventional deep learning and LLM approaches" | ST-LINK |
| "Delivers competitive performance on both regression and planning" | TransLLM |
| "Achieves strong predictive performance with a lower parameter count" | MCST-Mamba |
| "Significantly improves prediction fairness while minimizing accuracy degradation" | FairTP |

### 13.10 实验描述模式（来自顶论文）

**数据集描述：**
> "We conduct experiments on two widely-used traffic benchmark datasets: METR-LA and PEMS-BAY. METR-LA collects traffic speed data from 207 loop detectors on the highways of Los Angeles County, spanning from March 1st to June 30th, 2012."

**基线选择：**
> "We compare our method with the following baselines, which can be categorized into three groups: (1) RNN-based methods: DCRNN and GWNet; (2) GNN-based methods: STGCN, MTGNN, AGCRN; (3) Transformer-based methods: STAEformer and PDFormer."

**结果呈现：**
> "As shown in Table 1, our method consistently outperforms all baselines across all datasets and prediction horizons. Specifically, on METR-LA, our model achieves an average improvement of 5.0% in MAE over the best baseline."

**消融实验：**
> "To validate the contribution of each component, we design the following variants: w/o Spatial: remove the spatial attention module; w/o Temporal: remove the temporal attention module; w/o Adaptive: replace adaptive embeddings with fixed positional encodings."

**效率分析：**
> "Our model has 2.3M parameters and 1.2G FLOPs, which is significantly more efficient than PDFormer (5.7M params, 3.8G FLOPs) while achieving better prediction accuracy."

### 13.11 Method部分写作模式

**Problem Formulation标准开头：**
> "We model the traffic network as a directed graph G = (V, E, A), where V is the set of N nodes representing traffic sensors, E is the set of edges, and A ∈ R^(N×N) is the adjacency matrix."

**输入输出张量定义：**
> "The input to our model is a tensor X ∈ R^(N×T×C), where N is the number of traffic sensors, T is the number of historical time steps, and C denotes the number of traffic features."

**问题形式化：**
> "The spatiotemporal traffic prediction problem can be formulated as learning a mapping function f_θ: X_{t-T+1:t} → X_{t+1:t+T'}"

**整体架构描述：**
> "As illustrated in Fig. 2, the proposed model consists of three main components: (1) an input embedding layer, (2) a stack of L spatiotemporal attention blocks, and (3) an output projection layer."

**设计选择解释：**
> "We adopt a parallel architecture rather than a sequential one because spatial and temporal dependencies can be captured simultaneously, which reduces the computational cost."

**复杂度分析：**
> "The time complexity of our spatial attention module is O(N²d). For the temporal attention module, the complexity is O(T²d). Therefore, the overall time complexity is O((N²+T²)d)."

### 13.12 Conclusion/Future Work写作模式

**贡献总结+未来方向：**
> "In this paper, we proposed [Method] for traffic flow prediction. Extensive experiments demonstrated [key findings]. Future work includes: (1) extending to multi-modal data, (2) exploring real-time deployment, (3) investigating causal relationships."

**局限性承认：**
> "Our method has two limitations. First, it requires accurate delay estimates. Second, the computational cost scales quadratically with the number of sensors."

**未来工作与局限性呼应：**
> "To address the computational limitation, we plan to explore sparse attention mechanisms. To handle missing delay estimates, we will investigate learned delay prediction."

**实际部署考量：**
> "Future work will focus on deploying the model on edge devices with limited computational resources, exploring model compression and quantization techniques."

### 13.13 2026年新写作风格

**问题递进式（PatchSTG）：**
> "Traffic forecasting is a fundamental component of intelligent transportation systems, yet remains challenging in real-world settings due to irregular sensor distributions and the high computational cost."

**双因素分解式（ADMFormer）：**
> "Traffic series contain heterogeneous temporal patterns: (1) stable periodic regularities, and (2) event-driven fluctuations. Spatial dependencies among nodes are inherently dynamic and sparse."

**范式批判式（U-STS-LLM）：**
> "While deeply connected, forecasting and imputation have historically evolved as separate sub-fields. The dominant paradigm, STGNNs, while effective, are often specialized and exhibit limited generalizability."

**安全导向式（EP-Diffuser）：**
> "For the safe operation of autonomous vehicles, it is equally important to cover the distribution for plausible motion alternatives."

**隐私-效率权衡式（AutoFed）：**
> "Due to significant privacy concerns surrounding traffic data, most existing methods rely on local training, resulting in data silos and limited knowledge sharing."

### 13.14 新评估指标（2024-2026）

| 指标 | 定义 | 何时使用 | 报告格式 |
|------|------|---------|---------|
| **CRPS** | 预测CDF与观测值的积分平方差 | 概率预测 | CRPS (↓) |
| **Pinball Loss** | 分位数回归的非对称损失 | 分位数预测 | Q=0.1/0.25/0.5/0.75/0.9 |
| **ACE** | 预期覆盖率与实际覆盖率的偏差 | 校准评估 | ACE (↓) |
| **Sharpness** | 预测区间的平均宽度 | 区间评估 | Sharpness (↓) |
| **PICP** | 观测值落在预测区间内的比例 | Conformal Prediction | 90% PICP, 95% PICP |
| **PINAW** | 归一化的预测区间宽度 | Conformal Prediction | 90% PINAW, 95% PINAW |
| **Coverage Gap** | 实际覆盖率与理论保证的差距 | Conformal Prediction | Coverage Gap (↓) |
| **Spatial Equity** | 不同路段预测精度的变异系数 | 公平性评估 | SEI (↓) |
| **DTW** | 预测序列与实际序列的形状相似性 | 时间偏移评估 | DTW (↓) |
| **Directional Accuracy** | 预测变化方向与实际方向的一致性 | 趋势评估 | DA (%) |
| **Peak-Hour MAE** | 高峰时段的加权MAE | 实际应用评估 | PHW-MAE (↓) |
| **Degradation Rate** | 精度随预测步长的退化速率 | 长期预测评估 | DR (%) |

### 13.15 新评估指标报告格式

**概率预测表格：**
```
| Model    | MAE  | RMSE | CRPS (↓) | 90% PICP | 90% PINAW |
|----------|------|------|----------|----------|-----------|
| DiffSTG  | 2.93 | 5.61 | 1.82     | 0.912    | 0.234     |
| ProbGWNet| 2.98 | 5.72 | 1.91     | 0.887    | 0.256     |
```

**公平性评估表格：**
```
| Model  | Overall MAE | Worst-10% MAE | Best-10% MAE | SEI (↓) |
|--------|-------------|---------------|--------------|---------|
| STGCN  | 2.85        | 5.12          | 1.34         | 0.42    |
| DCRNN  | 2.78        | 4.89          | 1.28         | 0.39    |
```

**分步长评估表格：**
```
| Model    | 15min | 30min | 45min | 60min | DR(%) |
|----------|-------|-------|-------|-------|-------|
| STAE     | 2.12  | 2.58  | 3.01  | 3.42  | 61.3  |
| PDFormer | 2.08  | 2.49  | 2.87  | 3.21  | 54.3  |
```

### 13.16 2026年IEEE TITS新写作模式

**矛盾权衡式（FAST）：**
> "Existing methods typically face a trade-off between expressiveness and efficiency: Transformer-based models capture global dependencies well but suffer from quadratic complexity, while recent selective state-space models are computationally efficient yet less effective at modeling spatial interactions."

**三重挑战并列式（3S-TBLN）：**
> "In highway traffic speed prediction, three essential elements should be considered: 1) the complex spatial diffusion of traffic over time; 2) the influence of traffic patterns on prediction accuracy; and 3) the crucial role of bidirectional learning mechanisms."

**问题根源追溯式（CAST-CKT）：**
> "Traffic prediction in data-scarce, cross-city settings is challenging due to complex nonlinear dynamics and domain shifts. Existing methods often fail to capture traffic's inherent chaotic nature for effective few-shot learning."

**统一假设质疑式（GC-MoE）：**
> "Spatio-temporal forecasting on sensor graphs is commonly tackled with a single backbone architecture applied uniformly across all nodes, although graph regions can exhibit different dynamics."

**技术趋势驱动式（LEAD）：**
> "Driven by the evolution toward 6G and AI-native edge intelligence, network operations increasingly require predictive and risk-aware adaptation under stringent computation and latency constraints."

**宏微观对比式（MMCAformer）：**
> "Existing studies have primarily relied on aggregated, macroscopic traffic flow data to predict future traffic trends, whereas road traffic dynamics are also influenced by individual, microscopic human driving behaviors."

**社会背景切入式（GEnSHIN）：**
> "With the acceleration of urbanization, intelligent transportation systems have an increasing demand for accurate traffic flow prediction."

**特定场景问题化式（Vessel Traffic）：**
> "Maritime traffic flow data are often highly sparse with intermittent bursts, making robust forecasting challenging."

### 13.17 WWW/CIKM 2025-2026写作模式

**反问式标题（WWW 2025）：**
> "Do We Really Need GCNs in Traffic Forecasting? A Graph-Less Pure-MLP Architecture"

**预训练范式创新（DoP, CIKM 2025）：**
> "We argue that mask reconstruction is a suboptimal pre-training paradigm for traffic forecasting because there exists a great gap between pre-training and downstream tasks caused by their inconsistent training targets."

**可解释性框架（SS-MoE, CIKM 2025）：**
> "However, existing methods are mostly confined to shallow LLM utilization, where the semantic capacity of LLMs is ignored and data is directly fed in."

**频域解耦（FEDDGCN, CIKM 2025）：**
> "Existing approaches are still limited by the insufficient capability of spatial-temporal pattern decoupling and underutilization of frequency domain information."

### 13.18 Transportation Research写作模式

**LLM+交通融合（STLLM-DF）：**
> "Centralized multimodal transport systems face significant challenges due to data isolation, missing values, and heterogeneous spatial-temporal features, which hinder accurate prediction in traffic flow and travel demand."

**范式转换式（From Optimization to Prediction）：**
> "The traffic assignment problem is essential for traffic flow analysis, traditionally solved using mathematical programs under the Equilibrium principle. These methods become computationally prohibitive for large-scale networks."

**博弈论引入（Federated Learning）：**
> "Federated learning-based traffic flow prediction has attracted growing interest in the field. However, designing a fair and efficient incentive mechanism to encourage collaboration among diverse participants remains a key challenge."

---

> 本节交通预测内容整合自：PDFormer (AAAI'23), STAEformer (AAAI'24), DiffSTG (KDD'24), UrbanGPT (KDD'24), UniST (KDD'24), MegaCRN (AAAI/TITS'23/'24), D2STGNN (VLDB/TKDE'22-'24), STID (CIKM/TNNLS'22-'24), FlashST (ICML'24), Expand-and-Compress (ICLR'25), TEAM (PVLDB'25), PatchSTG (KDD'25), LEAF (ACL'25), Damba-ST (ICDE'26), OpenCity (2025), STGformer (2024), FairTP (AAAI'25), RAST (AAAI'26), ST-HCMs (AAAI'25), LightST (AAAI'25), FlowDistill (2025), GAMMA-Net (2026), FAST (ICME'26), MLA-STNet (2026), STM3 (KDD'26), RIPCN (KDD'26), U-STS-LLM (2026), FedLLM (2026), ACTFormer (TNNLS'26), DIST (TNNLS'25), MSTC-GAT (TNNLS'25), DDAMGCN (TNNLS'25), CHGNet (TVT'26), RoadDiff (TVT'25), TrafficLLM (TVT'25), CIWI-CKT, CAST-CKT, PIMCST, MoE-FedTP, FedDis, SimpleST, STemDist, MA-GLTC, ConFormer, Adap-STWT (TITS'26), PGCRN (TITS'25), iTPGT-former (TITS'24), D³STN (TITS'24), MVSTG (TITS'24), W-Diffusion (TITS'26), FastSTI (TITS'24), Sofed (TITS'26), REFOL (TITS'24), CROSS-Net (TITS'26), SAMformer (ICML'24), ScaleSTF, Double-Diffusion, ICST-DNET, Chronos (Amazon), Timer (ICML'24), TimeMixer, Moirai (Salesforce), Moirai-MoE, TimesFM (Google), MOMENT (ICML'24), UrbanFM, BjTT, UQGNN, RDGCN, GraphTrafficGPT, MetaDG (AAAI'26), HyperD (AAAI'26), STDN (AAAI'25), SSL-STMFormer (AAAI'25), ModWaveMLP (AAAI'24), STONE (KDD'24), FedGTP (KDD'24), CityBench (KDD'24), UoMo (KDD'24), ST-ReP (AAAI'25), LLGformer (WWW'25), Trffc (WWW'25), Unveiling Delay Effects (WWW'24), M3-Net (CIKM'25), FEDDGCN (CIKM'25), TopKNet (CIKM'25), Seeing Forest Trees (CIKM'24), ByGCN (CIKM'24), Riding Wave (IJCAI'25), Make Bricks (IJCAI'24), TESTAM (ICLR'24), WardropNet (ICLR'24), Talking Trails (AAAI'26), ST-LEGO (WWW'26), STELA (WWW'26), ST-LINK (CIKM'25), MF3 (WWW'26), WED-Net (WWW'26), VisionST (WWW'26), KnowLCP (AAAI'26), CaTFormer (AAAI'25), NEST (AAAI'24), BehaviorGPT (NeurIPS'24), GeoPro-Net (AAAI'25), Beta Distribution (AAAI'25), RDPI (AAAI'25), PhyMPGN (ICLR'24), PhyMPGN, STEMO (KDD'24), Conservation-informed (KDD'24), Interpretable MoE (KDD'24), Efficient Large-Scale (KDD'24), TelTrans (AAAI'24), Tel2Veh (WWW'24), Adaptive Frequency Pathways (AAAI'26), Responsive Dynamic Graph (AAAI'25), LLeCaT (TITS'25), Cross-City Correlation (TITS'26), Taming Spatial Heterophily (TITS'26), Online Test-Time Adaptation (TITS'25), Spatio-Temporal VL Model (TITS'26), DAGCAN (TITS'25), Task-Oriented Spatial Graph (TITS'25), Conformal GNN (TITS'25), Geometric Deep Learning (TITS'25), V-DCRNN (TITS'25), MT-STNet (TITS'24), Voronoi STGCN (TITS'24), DSTIGFN (TITS'26), Bicycle Traffic Prediction (TITS'26), Noise-Robust Bus (TITS'26), Dirichlet Graph (TITS'25), SEDA (TITS'24), G²-HGNN (TITS'25), High/Low Frequency Attention (TITS'25), Multi-Form ST (TITS'25), Sparse Cross Attention (TITS'25), Knowledge-Based Multiple (TITS'24), TRECK (TITS'24), ST-Augmentation (TITS'25), TCN-DMAttention (TITS'26), CSP-AIT-Net (TITS'26), Management Actions (TITS'25), TAMHA-DDPM (TITS'25), Versatile Behavior (TITS'26), Multi-Granularity Graph Diffusion (TITS'26), Intention-Aware Diffusion (TITS'25), CNDM (TITS'26), Diffutory (TITS'25), AirTraj-Diff (TITS'25), Security-Enhanced HFL (TITS'25), Security-Enhanced VFL (TITS'25), Fed Few-Shot (TITS'25), Clustered Fed (TITS'25), Network-State-Intelligent (TITS'25), Co-Evolving (TITS'25), Bridging Temporal Gaps (TITS'26), Physics-Guided Transfer (TITS'24), Network-Wide Dynamics (TITS'24), Nonlocal Traffic (TITS'24), Physics-Inspired Energy (TITS'24), DT-CTFP (TITS'25), Multi-Scale Spatio-Temporal (TITS'26), DualRisk (TITS'24), STORM (TITS'24), Vessel Traffic (TITS'26), Carbon Emission (TITS'25), Meta-Learning Conflict (TITS'26), STAEformer (AAAI'23), PDFormer (AAAI'23), HyperD (AAAI'26), STDN (AAAI'25), SSL-STMFormer (AAAI'25), Decomposed ST-Mamba (AAAI'25), ModWaveMLP (AAAI'24), Pivotal GNN (AAAI'24), STONE (KDD'24), FedGTP (KDD'24), CityBench (KDD'24), UoMo (KDD'24), UniST (KDD'24), Talking Trails (AAAI'26), ST-LEGO (WWW'26), STELA (WWW'26), ST-LINK (CIKM'25), MF3 (WWW'26), WED-Net (WWW'26), VisionST (WWW'26), KnowLCP (AAAI'26), CaTFormer (AAAI'25), NEST (AAAI'24), BehaviorGPT (NeurIPS'24), GeoPro-Net (AAAI'25), Beta Distribution (AAAI'25), RDPI (AAAI'25), PhyMPGN (ICLR'24), STEMO (KDD'24), Conservation-informed (KDD'24), Interpretable MoE (KDD'24), Efficient Large-Scale (KDD'24), TelTrans (AAAI'24), Tel2Veh (WWW'24), Adaptive Frequency Pathways (AAAI'26), Responsive Dynamic Graph (AAAI'25) 等论文。更新时间：2026-06-20。涵盖1000+篇论文。

### 13.19 实验设计最佳实践（2024-2026论文）

**数据集选择标准：**
- 小规模：METR-LA (207 sensors), PEMS-BAY (325 sensors), PEMS04/08
- 大规模：LargeST (San Diego 716, Bay Area 2352, California 8600)
- 跨城市：多城市数据集组合

**数据划分标准：**
- 7:1:2 或 6:2:2 的 train/validation/test split
- 按时间顺序划分，避免数据泄露

**预测时域标准：**
- 15min (3 steps), 30min (6 steps), 60min (12 steps)
- 报告每个时域的MAE/RMSE/MAPE

**基线选择原则：**
- 覆盖不同技术范式（RNN/TCN/Attention/ODE/GNN）
- 包含SOTA方法（STAEformer, PDFormer等）
- 包含简单baseline（HA, STID）
- 报告所有方法的参数量

**消融实验设计：**
- 逐一移除关键组件
- 使用 "W/o" 命名规范（W/o SA, W/o TSA, W/o Graph）
- 在多个数据集上验证
- 用可视化对比展示结果

**效率报告维度：**
- Parameters（参数量）
- FLOPs（浮点运算量）
- GPU Memory
- Training/Inference Time
- MAE vs FLOPs bubble chart

**公平比较原则：**
- 统一数据处理
- 统一超参数搜索
- 统一评估流程
- 多数据集验证

### 13.20 KDD 2026论文写作模式

**领域知识驱动（RIPCN）：**
> "RIPCN introduces a dynamic impedance evolution network that captures directional traffic transfer patterns driven by road congestion level and flow variability, revealing the direct causes of uncertainty."

**挑战编号列举（STM3）：**
> "The long-term spatio-temporal dependency learning brings two new challenges: 1) The long-term temporal sequence naturally includes multiscale information, which is hard to extract efficiently; 2) The multiscale temporal information from different nodes is highly correlated and hard to model."

**不确定性量化标配（EnergyMamba）：**
> "existing works have two key limitations: (1) they usually formulate this task as a purely time-series prediction problem without explicitly modeling the spatial dependencies among different regions, and (2) they fail to provide reliable predictions with uncertainty estimates."

**因果推断引入（CausalPOI）：**
> "most methods rely on proximity-based graphs and correlation-driven modeling, which overlook the functional dependencies between POIs and fail to capture the causal effects of urban interventions."

**物理信息引导（DSPR）：**
> "Existing data-driven models often achieve strong statistical performance but struggle to respect regime-dependent interaction structures and transport delays inherent in real-world systems."

### 13.21 2025-2026新方法写作范式

**Mamba/SSM范式（TrafficMamba）：**
- 强调效率优势："linear complexity vs quadratic complexity"
- 双向扫描机制："bidirectional scanning captures both forward and backward temporal dependencies"

**Transformer变体范式（PDFormer）：**
- 从交通流理论出发："traffic congestion propagates through road networks with inherent delays"
- 显式建模传播延迟："explicitly modeling the time delay of spatial information propagation"

**LLM/基础模型范式（UrbanGPT, UniST）：**
- 强调泛化能力："zero-shot and few-shot prediction capabilities"
- 跨域迁移："transfer to unseen cities without fine-tuning"

**扩散模型范式（DiffSTG）：**
- 概率预测："probabilistic forecasting rather than point estimation"
- 不确定性量化："provides calibrated uncertainty estimates"

**图神经网络创新（DGCRN）：**
- 动态图学习："dynamic graph structure evolves over time"
- 元学习："meta-learning generates graph parameters"

**多模态融合范式：**
- 互补性："satellite imagery, GPS trajectories, camera data provide complementary information"
- 异质图："heterogeneous graph structure handles multi-modal data"

**联邦学习范式（FedST）：**
- 隐私保护："privacy-preserving collaborative learning"
- 跨域协作："cross-city knowledge transfer without sharing raw data"

**物理信息范式：**
- 物理约束："traffic flow theory as inductive bias"
- 可解释性："physically interpretable predictions"

### 13.22 OpenAlex API搜索结果（2024-2026）

**WWW 2024-2026（9篇）：**
- Unveiling Delay Effects (2024, 37 citations) - 时空延迟微分方程视角
- LLGformer (2025, 17 citations) - 可学习长程图Transformer
- STKOpt (2025, 6 citations) - 自动化时空知识优化
- VisionST (2026) - 跨模态交通预测
- WED-Net (2026) - 天气效应解耦
- ST-LEGO (2026) - LLM作为模块化架构师
- FedDis (2026) - 因果解耦联邦学习
- MIGC-CMamba (2026) - 跨域Mamba

**CIKM 2024-2025（12篇）：**
- Urban Traffic Accident Risk (2024, 26 citations) - 事故风险预测
- Spatio-temporal Graph Normalizing Flow (2024, 9 citations) - 概率预测
- FEDDGCN (2025, 2 citations) - 频率增强解耦动态GCN
- M3-Net (2025, 11 citations) - 无图MLP模型
- SS-MoE (2025) - 语义空间专家混合
- DoP (2025) - Decoder-only预训练增强

**Transportation Research Part C 2024-2026（20篇）：**
- MAST-GNN (2024, 38 citations) - 空域复杂度预测
- Driver Lane Change (2024, 30 citations) - 换道意图预测
- Hybrid Traffic Simulation (2024, 28 citations) - 仿真+ML混合
- Cross-City Transfer (2025, 18 citations) - 跨城市迁移学习
- i-CLTP (2025, 9 citations) - 对比学习+Transformer
- Game-theoretic FL (2026) - 博弈论联邦学习
- Joint Dynamic Pruning (2026) - 动态剪枝

**IEEE TVT 2024-2026（7篇）：**
- Latent Gaussian Processes (2024, 11 citations) - 隐高斯过程图学习
- Federated Meta-Learning (2024, 6 citations) - 联邦元学习
- STGCNFormer (2025, 4 citations) - 时空双流GCN+Transformer
- Cross-City Self-Supervised (2026) - 跨城市自监督图学习

### 13.23 IEEE TITS/TKDE/TNNLS 2024-2026论文（DBLP API验证）

**IEEE TITS 2024（34篇）：**
- Spatiotemporal Multiscale GCN (10.1109/TITS.2024.3354802)
- Confined Attention Bi-GRU (10.1109/TITS.2024.3375890)
- PIGAT: Physics-Informed Graph Attention Transformer (10.1109/TITS.2024.3386128)
- Multi-Task Collision-Aware Graph Transformer (10.1109/TITS.2023.3345296)
- MT-STNet Multi-Task Spatiotemporal (10.1109/TITS.2024.3411638)
- Dynamic Spatiotemporal Straight-Flow (10.1109/TITS.2024.3443887)
- DSFormer-LRTC Dynamic Spatial Transformer (10.1109/TITS.2024.3436523)
- STORM Event-Triggered Abnormal Crowd (10.1109/TITS.2024.3390185)
- FastSTI Conditional Pseudo Numerical Diffusion (10.1109/TITS.2024.3469240)
- Blockchain-Based Federated Learning (10.1109/TITS.2024.3391053)

**IEEE TITS 2025（19篇）：**
- 6G Enabled Real-Time Traffic (10.1109/TITS.2025.3571773)
- Edge Computing Large-Scale GPT (10.1109/TITS.2024.3456890)
- Attention-Driven ST Deep Hybrid (10.1109/TITS.2025.3540852)
- Selective Transfer Learning (10.1109/TITS.2025.3596309)
- Cluster-Granularity Transfer (10.1109/TITS.2025.3552111)
- Satellite Imagery Domain Adaptation (10.1109/TITS.2025.3589218)
- Graph Transformer Dynamic Edge (10.1109/TITS.2024.3513325)
- TRACER Transfer Knowledge (10.1109/TITS.2025.3546284)
- Federated Transfer Learning (10.1109/TITS.2025.3545445)
- Dynamic Routing ST-Transformer (10.1109/TITS.2025.3552404)
- TLAST Time-Lag Aware (10.1109/TITS.2025.3583391)
- Score-Based ST Point Process (10.1109/TITS.2025.3605287)
- Sparse Cross Attention GCN (10.1109/TITS.2025.3533560)
- Online Test-Time Adaptation (10.1109/TITS.2025.3600237)
- High/Low Frequency Attention (10.1109/TITS.2025.3564305)
- DGODE Dynamic Graph ODE (10.1109/TITS.2025.3612204)

**IEEE TITS 2026（10篇）：**
- Bicycle Traffic Prediction (10.1109/TITS.2025.3633930)
- Functional Encryption Privacy (10.1109/TITS.2026.3673039)
- Cross-City Correlation (10.1109/TITS.2025.3647158)
- Congestion Propagation GCN (10.1109/TITS.2025.3628554)
- Bayesian Optimization GAT (10.1109/TITS.2025.3632402)
- Meta-Learning Traffic Conflict (10.1109/TITS.2025.3648403)
- Physics-Informed Deep Learning (10.1109/TITS.2025.3642303)
- Sofed Online Federated (10.1109/TITS.2026.3658759)
- TCN-DMAttention Congestion (10.1109/TITS.2025.3626524)
- Self-Supervised Bilateral Learning (10.1109/TITS.2026.3667856)

**IEEE TKDE 2024-2026（17篇）：**
- STWave++ Multi-Scale Spectral (10.1109/TKDE.2023.3324501)
- Spatio-Temporal Memory Multi-Level (10.1109/TKDE.2023.3322405)
- Uncertainty Quantification (10.1109/TKDE.2023.3312261)
- CLEAR Representation Learning (10.1109/TKDE.2025.3536009)
- Spatio-Temporal Multivariate Probabilistic (10.1109/TKDE.2025.3539680)
- S-MGHSTN Streaming Accident (10.1109/TKDE.2025.3557864)
- Lane-Level Traffic Prediction (10.1109/TKDE.2025.3580465)
- ST-LLM+ Graph Enhanced LLM (10.1109/TKDE.2025.3570705)
- Federated GNN Hypergraph (10.1109/TKDE.2025.3607895)
- MTNet Multi-Task (10.1109/TKDE.2025.3638147)

**IEEE TNNLS 2024-2026（8篇）：**
- Robust Disentangled STGNN (10.1109/TNNLS.2025.3635636)
- Multiscale Dynamic Delay (10.1109/TNNLS.2025.3617860)
- MSTC-GAT Multilayer Attention (10.1109/TNNLS.2025.3630903)
- One Size Fits All Unified (10.1109/TNNLS.2023.3259045)
- TraverseNet (10.1109/TNNLS.2022.3186103)

### 13.24 arXiv 2026最新论文（40篇，API验证）

**2026年6月（最新）：**
- Do Time Series Foundation Model Benchmarks Hide Regime-Dependent Failures? (2026-06-16)
- From GPU to Microcontroller: Online Ridge Regression (2026-06-16)
- CIWI-CKT: Chaos-Informed Wave Interference (2026-06-14)
- MA-GLTC: Memory-Augmented Graph Liquid Time-Constant (2026-06-14)
- PatchSTG: Scalable Spatiotemporal Graph Transformers (2026-06-02)
- GC-MoE: Graph-Conditioned Mixture of Experts (2026-05-28)
- EvoXXLTraffic: Scaling to Sensor-Evolving Networks (2026-05-28)

**2026年5月：**
- ADMFormer: Adaptive-Decomposition Transformer (2026-05-25)
- U-STS-LLM: Unified Spatio-Temporal Steered LLM (2026-05-12)
- TSNN: Non-parametric Interpretable Framework (2026-05-09)
- LTE-ODE: Local Truncation Error-Guided Neural ODEs (2026-05-05)
- Efficient Prompt Learning for Traffic (2026-05-08)

**2026年3-4月：**
- GAMMA-Net: Graph Attention + Multi-Axis Mamba (2026-04-18)
- Unveiling Stochasticity: Multi-modal Probabilistic (2026-04-17)
- Beyond Static Forecasting: World Models (2026-04-09)
- Long-Horizon Conformal ST-Transformers (2026-03-17)
- NeST-S6: Spatial PDE-aware SSM (2026-03-12)
- VisiFold: Temporal Folding Graph (2026-03-12)

**2026年1-2月：**
- UniST-Pred: Robust Unified Framework (2026-02-15)
- PIMCST: Physics-Informed Multi-Phase (2026-02-02)
- GEnSHIN: Graphical Enhanced ST Hierarchical (2026-01-08)

### 13.25 Mamba/SSM论文（21篇，arXiv API验证）

**2026年（7篇）：**
- GAMMA-Net: GAT + Multi-Axis Mamba (2026-04-18, MAE降低16.25%)
- FAST: Attention + SSM协同 (ICME 2026, RMSE降低4.3%)
- NeST-S6: PDE-aware SSM (2026-03-12, MAE降低48-65%)

**2025年（11篇）：**
- HiSTM: Hierarchical ST Mamba (2025-08-07)
- MCST-Mamba: Multivariate Mamba (2025-07-05)
- DKGCM: Fourier Bidirectional Mamba (2025-06-26)
- GAMDTP: Graph Attention Mamba (2025-04-07)

**2024年（3篇，奠基工作）：**
- ST-Mamba: Spatial-Temporal SSM (2024-04-20)
- ST-MambaSync: Mamba+Transformer (2024-04-24)

### 13.26 LLM/Foundation Model论文（37篇，arXiv API验证）

**LLM+道路预测（8篇）：**
- ST-LLM (2024), TPLLM (2024), Strada-LLM (2024)
- FlowDistill (2025), FedLLM (2026), U-STS-LLM (2026)

**LLM+移动流量（4篇）：**
- Mobile Traffic LLM (2025), Chain-of-Thought (2026)

**LLM+交通系统（5篇）：**
- CrossTrafficLLM (2025), TransLLM (2025), TrafficClaw (2026)

**Vision/多模态LLM（3篇）：**
- Vision-LLMs (2025), CrashChat (2025), TB-Bench (2025)

**Diffusion+交通（4篇）：**
- ChatTraffic (2023), LSDM (2025, LLM+Diffusion融合)

**Foundation Model（6篇）：**
- Self-Refined FM (2024), PreMixer (2024), Efficient Prompt (2026)
- ReasonLight (2026), Safe Mobility FM (2026)

**Urban FM（3篇）：**
- Urban General Intelligence (2024), Urban-R1 (2025), CITYREP (2026)

### 13.27 2024-2025实验描述6大模式

**模式1：实验设置描述标准开头**
> "We conduct extensive experiments on X real-world benchmark datasets..."
> "All experiments are repeated 5 times with different random seeds, and we report the mean and standard deviation."

**模式2：数据集描述标准格式**
> "METR-LA collects traffic speed data from 207 sensors on the Los Angeles County highway system over 4 months (March 2012 to June 2012)."
> "PEMS04 contains traffic flow data from 307 detectors in San Bernardino."

**模式3：数据划分标准**
> "We follow the standard data splitting strategy: 70% for training, 10% for validation, and 20% for testing."
> "We adopt a unified evaluation protocol across all datasets with consistent data splits, preprocessing, and metrics."

**模式4：公平对比声明**
> "All methods are re-implemented using the same framework and hyperparameter tuning budget."
> "For fair comparison, we use the same data preprocessing, evaluation protocol, and training strategy for all methods."

**模式5：Ablation Study描述**
> "To verify the effectiveness of each component, we conduct ablation studies by removing one component at a time."
> "Removing X leads to the largest performance drop, demonstrating its importance."

**模式6：效率报告**
> "Table 5 compares the computational cost. Our method achieves the best accuracy-efficiency trade-off with 2.5M parameters and 3.2 GFLOPs."
> "Our model trains 2.3x faster than STAEformer while achieving comparable accuracy."

### 13.28 图表设计模式（15篇论文分析）

**Architecture图设计：**
- 分层展示：Input → Spatial Embedding → Temporal Embedding → Transformer Encoder → Prediction
- 颜色编码：蓝色=空间模块，橙色=时间模块，绿色=输出
- 箭头明确数据流方向

**Prediction Comparison曲线：**
- 实线=Ground Truth，虚线=各模型预测值
- 不同颜色区分15min/30min/60min预测horizon
- 每个子图代表一个sensor

**Attention Heatmap设计：**
- 使用jet或viridis colormap
- 横轴=sensor节点，纵轴=time steps
- 颜色深浅表示attention weight大小

**Ablation柱状图：**
- X轴=组件名称（w/o Module A, w/o Module B, Full Model）
- Y轴=性能指标（MAE/RMSE）
- 使用error bar表示标准差

**效率散点图：**
- 横轴=训练时间或参数量，纵轴=MAE
- 气泡大小代表参数量
- 理想位置为左下角（高效+高精度）

**跨城市迁移热力图：**
- 行=源城市，列=目标城市
- 单元格=迁移后的性能指标
- 颜色深浅表示性能增益

**Figure Caption模板：**
> "Fig. X. The overall architecture of [ModelName]. It consists of [Module1], [Module2], and [Module3]."
> "Fig. X. Prediction comparison on [DatasetName] at [Horizon] horizon."
> "Fig. X. Visualization of [Component] on [Dataset]."
> "Fig. X. Case study of traffic prediction on [Date/Location]."

### 13.41 交通流预测实验设置标准模板

**数据集描述标准格式：**
> "METR-LA collects traffic speed data from 207 sensors on the Los Angeles County highway system over 4 months (March 2012 to June 2012). PEMS-BAY contains 6 months of traffic speed data collected from 325 sensors in the San Francisco Bay Area."

**数据划分标准：**
> "We follow the standard data splitting strategy: 70% for training, 10% for validation, and 20% for testing."
> "We adopt a unified evaluation protocol across all datasets with consistent data splits, preprocessing, and metrics."

**实现细节标准描述：**
> "We use Adam optimizer with an initial learning rate of 0.001, which decays by 0.1 every 20 epochs. The batch size is set to 64."
> "All experiments are repeated 5 times with different random seeds, and we report the mean and standard deviation."

**Baseline对比声明：**
> "For fair comparison, we use the same data preprocessing, evaluation protocol, and training strategy for all methods."
> "We compare with three types of baselines: (1) Graph neural network-based methods, (2) Transformer-based methods, (3) LLM-based methods."

### 13.42 2025-2026 IEEE TITS高引论文（CrossRef验证）

**2026年：**
- Spatio-Temporal Data Enhanced Vision-Language Model (10.1109/tits.2025.3628271)
- Contrastive Learning + TCN-DMAttention (10.1109/tits.2025.3626524)
- Cross-City Correlation Learning (10.1109/tits.2025.3647158)
- Dynamic Spatiotemporal GCN (10.1109/tits.2025.3628554)
- Heterogeneity-Guided Tensor Decomposition (10.1109/tits.2026.3658186)

**2025年高引：**
- Attention-Driven ST Deep Hybrid NN (102 citations, 10.1109/tits.2025.3540852)
- LLM in Adaptive Traffic Signal Control (41 citations, 10.1109/tits.2024.3498735)
- Spatio-Temporal Contrastive Learning (37 citations, 10.1109/tits.2024.3487982)
- Federated Transfer Learning (19 citations, 10.1109/tits.2025.3545445)

### 13.43 AAAI 2025-2026交通预测论文（DBLP验证）

**AAAI 2026：**
- RAST: Retrieval Augmented Spatio-Temporal Framework (10.1609/AAAI.V40I46.41264)
- Inter-Client Dependency Recovery Federated (10.1609/AAAI.V40I34.40130)
- Meta Dynamic Graph (10.1609/AAAI.V40I19.38699)

**AAAI 2025：**
- Decomposed Spatio-Temporal Mamba (10.1609/AAAI.V39I11.33281)
- SSL-STMFormer (10.1609/AAAI.V39I11.33321)
- FairTP: Prolonged Fairness (10.1609/AAAI.V39I25.34838)
- Efficient Spatio-Temporal Distillation (10.1609/AAAI.V39I1.32096)

### 13.44 Transportation Research Part C 2025-2026

- CONTINA: Confidence Interval for Traffic Demand (2504.13961v2)
- MoGERNN: Inductive Traffic Predictor (2501.12281v2)
- Physics-Informed Meta ML for MFD (2508.14137v2)
- Q-Net: Queue Length Estimation (2509.24725v4)
- Adaptive Domain Decomposition PINN (2605.08028v1)
- T-STAR: Context-Aware Transformer (2602.06866v2)

### 13.29 CIKM 2025交通预测论文

- Forecasting at Full Spectrum (2505.01279v2)
- ST-LINK: Spatially-Aware LLM (2509.13753v1)
- CityLight: Universal Traffic Signal Control (2406.02126v4)
- HGAurban: Heterogeneous Graph Autoencoding (2410.10915v2)

### 13.30 2025-2026新评估方法（12篇论文）

**合成Benchmark（ChaosNetBench）：**
- 可控混沌动力学下的评估
- 解决单一领域、单一holdout split的问题

**动态传感器网络（EvoXXLTraffic）：**
- 27年California PeMS数据
- 传感器网络随时间变化的真实场景

**几何结构指标（TGSI）：**
- 超越点误差，评估形态保持
- 将时间序列转换为图像评估几何结构

**概率校准评估（Unveiling Stochasticity）：**
- GMM层将确定性模型转为概率预测器
- 评估calibration和sharpness

**效率-准确率联合评估（STGCN深度研究）：**
- 3-block架构无有利tradeoff
- 超过2倍计算成本仅换<0.5%改进

**干扰鲁棒性（UniST-Pred）：**
- 结构不确定性（道路封闭）
- 观测不确定性（传感器故障）

**跨域泛化（CAST-CKT）：**
- 混沌分析器量化可预测性regime
- chaos-aware attention实现regime自适应

**Conformal Prediction：**
- 带统计保证的预测区间
- 校准性和预测区间宽度

**多时长退化分析：**
- 性能随horizon增加的退化曲线
- 为不同时长选择合适模型

### 13.31 图表设计模式（12篇论文分析）

**必备图类型：**
1. Model Architecture Diagram（100%论文）
2. Performance Comparison Table（100%论文）

**高频图类型：**
3. Heatmap（50%论文）- 性能对比、注意力权重
4. Bubble Chart（25%论文）- 精度/效率/内存三维权衡
5. Attention Visualization（42%论文）- 社区检测、邻接矩阵重排序
6. Embedding Visualization（33%论文）- t-SNE/UMAP降维
7. Case Study（33%论文）- 预测曲线对比

**新兴图类型（2025-2026）：**
8. SVD-Based Visualization - 分析Mamba状态转移矩阵
9. Probabilistic Calibration Histogram - PIT直方图
10. Spatial Residual Analysis - Moran's I空间依赖检验
11. Vector Similarity Topology - 向量相似度拓扑对比

**真实Caption模板：**
> "Figure 1: Model Architecture of proposed [ModelName]."
> "Figure 3: Performance heatmaps of twelve predictive models on the Metr-LA dataset for forecasting horizons of 3, 6, and 12 time steps, showing MAE (left), RMSE (center) and MAPE (right)."
> "Figure 3: Bubble position indicates MAE and training time, while bubble size denotes GPU memory usage."
> "Figure 7: Community detection based on spatial and temporal attention."
> "Figure 4: Embedding visualization of SPAE. A more uniform and complete circular distribution of colors indicates lower similarity among nodes."

**Table设计规范：**
- 最佳结果 **加粗**，次佳结果 <u>下划线</u>
- 无法运行用 dash (–)
- 颜色编码：深色 = 更好性能
- 单位缩写：K=10^3, M=10^6
- 指标顺序：MAE, RMSE, MAPE
- 预测步长：15min, 30min, 60min (3, 6, 12 steps)

### 13.32 arXiv 2025-2026最新论文（40篇，API验证）

**GNN方向（9篇）：**
- CIWI-CKT: Chaos-Informed Wave Interference (2026-06-14)
- MA-GLTC: Memory-Augmented Graph Liquid Time-Constant (2026-06-14)
- PatchSTG: Scalable Spatiotemporal Graph Transformers (2026-06-02)
- GC-MoE: Graph-Conditioned Mixture of Experts (2026-05-28)
- GAMMA-Net: Graph Attention + Multi-Axis Mamba (2026-04-18)
- VisiFold: Temporal Folding Graph (2026-03-12)
- GEnSHIN: Graphical Enhanced ST Hierarchical (2026-01-08)
- Meta Dynamic Graph (2026-01-15)
- RIPCN: Road Impedance Principal Component (2025-12-25)

**Transformer方向（4篇）：**
- FAST: Attention + SSM协同 (ICME 2026)
- MMCAformer: Macro-Micro Cross-Attention (2026-02-17)
- Long-Horizon Conformal ST-Transformers (2026-03-17)
- Geographically-aware Transformer Digital Twin (2026-02-05)

**LLM/Foundation Model方向（5篇）：**
- U-STS-LLM: Unified Spatio-Temporal Steered LLM (2026-05-12)
- FedLLM: Federated LLM (2026-04-17)
- LEAD: LLM-Enhanced Adapter Diffusion (2026-01-29)
- LSDM: LLM-Enhanced Diffusion (2025-07-23)
- Efficient Prompt Learning (2026-05-08)

**Mamba/SSM方向（3篇）：**
- GAMMA-Net: Multi-Axis Mamba (2026-04-18)
- NeST-S6: PDE-aware SSM (2026-03-12)
- DKGCM: Fourier Bidirectional Mamba (2025-06-26)

**其他方向（19篇）：**
- Unveiling Stochasticity: Probabilistic (2026-04-17)
- DRIFT: Risk-Constrained Diffusion (2026-06-15)
- From GPU to Microcontroller: Edge Deploy (2026-06-16)
- STGCN Architectural Depth Study (2026-06-08)
- Do TSFM Benchmarks Hide Failures (2026-06-16)
- Beyond Static Forecasting: World Models (2026-04-09)
- CoMemNet: Continual Learning (2026-05-07)
- PHGNet: Prototype Hypergraph (2026-05-25)
- RCSNet: Road-Conditioned (2026-05-27)
- PIMCST: Physics-Informed Multi-Phase (2026-02-02)
- UniST-Pred: Robust Unified (2026-02-15)
- DYNA-PRUNER: Input-Adaptive Pruning (2026-06-13)
- Safe Urban Traffic: Conformal + RL (2026-02-04)
- Long-Horizon Incident-Aware (2026-03-17)
- DWAFM: Dynamic Weighted Graph (2026-03-01)
- ADMFormer: Adaptive-Decomposition (2026-05-25)
- OmniTraffic: Controllable Generation (2026-06-14)
- Vessel Traffic: Learnable Tweedie (2026-06-05)

### 13.33 KDD/AAAI/NeurIPS 2025-2026（30+篇）

**KDD 2025-2026：**
- MoST: Multi-modality Foundation Model (2026)
- Multimodal Embeddings Traffic Accident (2026)
- Seeing the Unseen: Confounder Representations (2025)
- UoMo: Universal Mobile Traffic (2024)
- CityBench: LLM Urban Tasks (2024)

**AAAI 2025-2026：**
- RAST: Retrieval Augmented ST Framework (2026)
- Inter-Client Dependency Federated (2026)
- Meta Dynamic Graph (2026)
- Decomposed ST-Mamba (2025)
- SSL-STMFormer (2025)
- FairTP: Prolonged Fairness (2025)
- Efficient ST Distillation (2025)

**NeurIPS 2024：**
- DeMo: Motion Decoupling (2024)
- BehaviorGPT: Smart Agent Simulation (2024)

### 13.34 WWW/CIKM/IJCAI 2025-2026（20篇）

**WWW 2025-2026（8篇）：**
- VisionST: Cross-modal Traffic (2026)
- FedDis: Causal Disentanglement Federated (2026)
- ST-LEGO: LLM Modular Architects (2026)
- MIGC-CMamba: Cross-Domain Mamba (2026)
- LLGformer: Learnable Long-range Graph (2025)
- STKOpt: Automated Knowledge Optimization (2025)
- Mitigating Spatial Disparity (2025)
- Exploring Search Volumes Event-Aware (2025)

**CIKM 2025（7篇）：**
- M3-Net: Cost-Effective Graph-Free MLP (2025)
- SS-MoE: Semantic Spatial Experts (2025)
- FEDDGCN: Frequency-Enhanced Decoupling (2025)
- TopKNet: Top-K Pivotal Nodes (2025)
- DoP: Decoder-only Pre-training (2025)
- Extracting Global Temporal Patterns (2025)
- Traffic Safety Evaluation (2025)

**IJCAI 2025（5篇）：**
- Unveiling Noise Priors Diffusion (2025)
- Riding the Wave: Overload Scenarios (2025)
- STAMImputer: Spatio-Temporal MoE (2025)
- Vision Language Models Traffic Profiling (2025)
- Balancing Imbalance: Data-Scarce (2025)

### 13.35 2025-2026最新写作技巧（15篇论文分析）

**Abstract写作标准模板：**
> "[背景句] Traffic forecasting is a critical task in intelligent transportation systems, enabling real-time traffic management and route planning. [问题句] However, existing methods struggle to capture the complex spatiotemporal dependencies inherent in traffic data. [方法句] In this paper, we propose [Model Name], a novel [技术] that [核心创新]. [技术细节] Specifically, [1-2句描述关键技术模块]. [实验句] Extensive experiments on [数据集名称] demonstrate that [Model Name] outperforms state-of-the-art methods by [X]% in MAE and [Y]% in RMSE. [意义句] Our approach provides new insights into [领域贡献]."

**Introduction四段式模板（IEEE TITS标准）：**
> 第1段（领域重要性）："Traffic prediction, which aims to forecast future traffic states based on historical observations, plays a pivotal role in intelligent transportation systems (ITS)."
> 第2段（现有方法及局限）："Existing methods can be broadly categorized into three families: (1) statistical models, (2) traditional machine learning, and (3) deep learning methods. Despite their success, these methods suffer from several limitations."
> 第3段（本文方法）："To address these limitations, we propose [Model Name], a novel adaptive graph learning framework for traffic prediction."
> 第4段（贡献总结）："The main contributions of this paper are summarized as follows: (1) We propose..., (2) We design..., (3) We conduct..."

**Contribution Statement三种风格：**
> IEEE TITS风格："The main contributions of this paper are summarized as follows: 1. We propose... 2. We design... 3. Extensive experiments..."
> AAAI风格："Methodologically, we propose... Theoretically, we provide... Empirically, we demonstrate..."
> NeurIPS风格："We identify a fundamental limitation... We propose [Model] with a novel [技术], which provably mitigates... We establish new state-of-the-art results..."

### 13.36 实验描述标准模式（15篇论文分析）

**数据集描述三要素：**
> "[Dataset] contains [data_type] data collected from [N] sensors/detectors in [location] over [time_period]."

**基线分类描述：**
> "We compare our method with several state-of-the-art baselines: (1) GNN-based methods: DCRNN, STGCN, GWNet; (2) Transformer-based methods: STAEformer, PDFormer; (3) LLM-based methods: UrbanGPT, UniST."

**消融实验描述：**
> "To verify the effectiveness of each component, we design the following variants: w/o [Module1]: Remove the [模块]; w/o [Module2]: Replace with [替代]; Full Model: Complete architecture."

**效率分析描述：**
> "Table Z compares the computational efficiency. Our model achieves the best trade-off between accuracy and computational cost with [X]M parameters and [Y]G FLOPs."

### 13.37 图表设计模式（16篇论文分析）

**必备图类型：**
1. Architecture Diagram（100%论文）- 从左到右或从上到下流水线
2. Performance Comparison（100%论文）- 多子图并排不同预测步长
3. Attention Heatmap（70%论文）- Viridis/Plasma色系
4. Ablation Bar Chart（75%论文）- 柱状图+误差棒
5. Case Study Map（50%论文）- 真实路网热力图

**Table设计规范：**
- 最佳结果**加粗**，次佳<u>下划线</u>
- 三线表格式，顶部横线加粗
- 列按预测步长(15/30/45/60min)分组
- 底部注释说明实验设置

**Figure Caption模板：**
> "Fig. 1. The overall architecture of [ModelName]. It consists of [Module1], [Module2], and [Module3]."
> "Fig. 3. Visualization of [Component] on [Dataset]. Darker colors indicate stronger correlations."
> "Fig. 5. Prediction results comparison. The red line represents our prediction, black line represents ground truth."

### 13.45 2025年写作新趋势

1. **LLM/Foundation Model论文**：必须提到"foundation model"或"large language model"，强调zero-shot/few-shot能力
2. **不确定性量化**：不仅报告MAE/RMSE，还要报告CRPS/PICP/PINAW
3. **可解释性**：增加Visualization子节展示attention权重
4. **效率与可扩展性**：必须报告参数量、训练时间、GPU内存
5. **多模态融合**：引入文本、图像、图谱等多源数据

### 13.38 IEEE TITS 2025-2026写作模式（20篇论文分析）

**问题重新定义型（MLSTP）：**
> "Existing methods often define trajectory prediction as a static task... However, this approach leads to significant long-term prediction errors."

**瓶颈突破型（GAN Pre-Training）：**
> "Existing methods extract traffic data's features by designing sophisticated spatiotemporal graph neural network models, and have reached a bottleneck."

**物理机理驱动型（DSTGCN）：**
> "Most ST-GNNs construct the graph adjacency matrix using predefined rules or trainable parameters, without fully leveraging the congestion relationships within traffic flows to guide graph structure learning."

**多因素挑战编号列举型（ICST-DNET）：**
> "However, making accurate predictions is challenging due to three factors: 1) traffic diffusion, i.e., the spatial and temporal causality..., 2) the poor interpretability..., and 3) the latent pattern of traffic speed fluctuations..."

**LLM增强型（LLeCaT）：**
> "Previous studies have focused on predicting accident hotspots, risks, or traffic states using simple accident features. Yet, because traffic accidents are infrequent and exhibit spatio-temporal biases..."

**隐私保护驱动型（Sofed）：**
> "As concerns over data privacy grow, direct data sharing is increasingly restricted, prompting substantial interest in Federated Graph Learning for traffic prediction."

**研究空白填补型（OD Demand）：**
> "Existing studies mainly focus on modeling and predicting OD demands in the short term, while studies for long-term OD demand forecasting are limited."

**性能退化问题导向型（Online TTA）：**
> "Traditional deep-learning based methods typically rely on historical data to train their models... However, the performance of the trained model usually degrades due to the temporal drift."

### 13.39 KDD/NeurIPS 2024-2025写作模式

**Prompt-based统一模型（UniST）：**
> "UniST leverages large-scale spatiotemporal data for pre-training and employs learnable prompts to adapt to diverse downstream tasks."

**LLM Instruction Tuning（UrbanGPT）：**
> "We introduce a spatio-temporal instruction tuning approach that enables LLMs to reason over spatial and temporal patterns."

**物理引导（STDEN）：**
> "STDEN integrates physics-informed constraints from traffic flow theory into graph neural networks, improving interpretability and generalization."

**传播延迟建模（PDFormer）：**
> "Traffic congestion and flow patterns don't instantly affect all locations — there is a spatial-temporal propagation delay between different road segments."

**自适应嵌入（STAEformer）：**
> "Achieves state-of-the-art performance without requiring a predefined adjacency matrix."

**Meta-Graph（MegaCRN）：**
> "Through meta-learning, the model dynamically generates graph structures at each time step, rather than relying on fixed adjacency matrices."

**扩散概率预测（DiffSTG）：**
> "Generates probabilistic forecasts that capture the uncertainty in future traffic patterns."

### 13.40 新方法架构总结（17篇）

| 类别 | 代表论文 | 核心创新 |
|------|---------|---------|
| Transformer变体 | STAEformer, PDFormer, AutoSTP | 自适应嵌入/传播延迟/NAS |
| State Space Model | ST-Mamba, TrafficMamba, SGMamba | 双向扫描/图信息融入SSM |
| Diffusion Model | DiffSTG, PD-Diff, DSTAGNN改进 | 概率预测/物理信息引导 |
| LLM/Foundation Model | UniST, ST-LLM, TrafficGPT, LLM-Mob | 预训练+提示/语义理解 |
| 因果推断 | CausalSTG | 因果图学习/反事实推理 |
| 小波分析 | STWave | 多分辨率时间频率分析 |

### 13.41 IEEE TITS 2026写作模式（18篇论文）

**问题递进式（DSTIGFN）：**
> "Existing models generally focus on modeling continuous traffic sequences, ignoring the multilevel correlation characteristics of spatio-temporal heterogeneity in traffic networks at different time scales."

**转折递进式（TEg-STGNN）：**
> "Despite achieving competitive overall results, their performance is often compromised in critical scenarios."

**微观-宏观对比式（Adap-STWT）：**
> "These studies tend to focus on interactions between nodes based on macroscopic traffic node attributes, overlooking the profound impact of individual behaviors and decisions of microscopic traffic participants."

**实际需求驱动式（Sofed）：**
> "Most existing methods follow batch learning paradigms, which are unsuitable for dynamic, streaming traffic data. In practical applications, traffic data arrives continuously, calling for online learning techniques."

**编号列举式（Multi-Scale）：**
> "Existing methods in cross-modal correlation modeling overlook two critical issues: 1) Existing cross-modal graph construction methods fail to uncover the latent relationships among cross-modal traffic flows, and 2) the spatio-temporal interaction across different traffic modes is not well modeled."

**范式转换式（MLSTP）：**
> "Existing methods often define trajectory prediction as a static task... However, this approach leads to significant long-term prediction errors and struggles to capture potential patterns."

**因果推断引入式（MSCT）：**
> "Previous studies have established a series of deep learning-based models to predict post-crash traffic conditions. Most of them were developed by learning statistical correlations from data, which may suffer from time-varying confounding bias."

**基础模型范式式（Pretrained Mobility Transformer）：**
> "We utilize these extensive, unlabeled sequences of user trajectories to develop a foundation model for understanding urban space and human mobility."

### 13.42 KDD/AAAI 2026写作模式（13篇论文）

**联邦学习+图学习（FedSTGD）：**
> "Existing methods primarily address static dependencies, overlooking their dynamic nature and resulting in suboptimal performance."

**扩散模型改进（FENCE）：**
> "However, existing diffusion models typically apply a uniform guidance scale across both spatial and temporal dimensions, which is inadequate for nodes with high missing data rates."

**Hidden Global Components（FedHINT）：**
> "We find that the traffic data from different local regions actually contain hidden global components that reflect cross-regional traffic changes."

**突发事件感知（IGSTGNN）：**
> "Most existing work focuses exclusively on capturing spatio-temporal dependencies from historical traffic data, while overlooking the fact that suddenly occurring transportation incidents serve as external disturbances."

**频域解耦（HyperD）：**
> "To tackle these challenges, we propose HyperD (Hybrid Periodic Decoupling), a novel framework that decouples traffic data into periodic and residual components."

### 13.43 新评估指标（15个）

| 指标 | 定义 | 使用场景 |
|------|------|---------|
| CRPS | 预测CDF与观测值的积分平方差 | 概率预测 |
| Pinball Loss | 分位数回归损失 | 分位数预测 |
| NLL | 负对数似然 | 参数化分布 |
| PICP | 预测区间覆盖概率 | Conformal Prediction |
| MPIW | 平均预测区间宽度 | 区间评估 |
| CWC | 覆盖宽度综合准则 | 权衡评估 |
| Coverage Gap | 经验覆盖差距 | 分布偏移 |
| Conditional Coverage | 条件覆盖率 | 公平性评估 |
| DTW | 动态时间规整 | 形状相似性 |
| FID/KID | 生成模型距离 | 扩散模型评估 |
| Spatial Gini | 空间基尼系数 | 公平性评估 |
| Disparate Impact | 差异影响比 | 公平性评估 |
| Robustness Ratio | 鲁棒性比 | 鲁棒性评估 |
| OOD Gap | 分布外性能差距 | 泛化能力 |
| SCP | 空间相关性保持度 | 结构保持 |

### 13.44 IEEE TITS/TKDE 2025-2026写作模式（23篇论文）

**LLM+图注意力（ST-LLM+）：**
> "Through incorporating a proximity-based adjacency matrix derived from the traffic network into the calibrated LLMs, ST-LLM+ captures complex spatio-temporal dependencies within the traffic network."

**每日自适应预测（ASTCL）：**
> "Existing traffic forecasting relies on the assumption that there is a hidden invariant spatial-temporal pattern in the large-scale dataset. However, the traffic patterns are easily influenced by many unpredictable external factors."

**多任务学习（MTNet）：**
> "Traditional research has often focused on predicting traffic flow or speed independently, leading to higher resource consumption due to the need for separate models."

**四元数图神经网络（QSTGNN）：**
> "The quaternion spatio-temporal graph is constructed firstly, such that the information of both short and long-term time steps are preserved in quaternion feature tensor."

**概率预测（Probabilistic）：**
> "To date, most work is focused on point estimation models, which only output a single value w.r.t an attribute of traffic data at a time, falling short of depicting diverse situations and uncertainty in future."

**拥堵传播（DSTGCN）：**
> "Accurate traffic prediction is crucial for the management of intelligent transportation systems. However, most ST-GNNs construct the graph adjacency matrix using predefined rules or trainable parameters, without fully leveraging the congestion relationships."

**文本到交通生成（ChatTraffic）：**
> "The analysis of traffic situations under abnormal conditions is one of the bottleneck issues in Intelligent Transportation Systems. Influenced by the suddenness, randomness, and uncertainty, this issue is challenging to achieve through existing deep learning methods."

**意图感知扩散（Intention-Aware Diffusion）：**
> "Accurate prediction of future trajectories for surrounding agents is crucial for ensuring the safety and reliability of autonomous driving systems."

**Conformal Prediction（Travel Time + Weather）：**
> "Traffic flow forecasting is essential for managing congestion, improving safety, and optimizing various transportation systems. However, it remains a prevailing challenge due to the stochastic nature of urban traffic."

**在线测试时适应（Online TTA）：**
> "Traditional deep-learning based methods typically rely on historical data to train their models. However, the performance of the trained model usually degrades due to the temporal drift between the historical and future data."

### 13.45 KDD/AAAI 2025-2026写作模式（10篇论文）

**空间数据管理视角（Efficient Large-Scale）：**
> "From a spatial data management perspective, we revisit the problem of large-scale traffic forecasting."

**物理守恒律（Conservation-informed）：**
> "Data-centric methods have shown great potential in understanding and predicting spatiotemporal dynamics. However, deep learning models often lack interpretability, fail to obey intrinsic physics, and struggle to cope with the various domains."

**Mamba分解（Decomposed ST-Mamba）：**
> "By virtue of the ability to effectively learn spatial and temporal dependencies from a global view, Transformers have achieved superior performance in long-term traffic prediction."

**公平性框架（FairTP）：**
> "Existing approaches primarily focus on improving overall accuracy, often neglecting a critical issue: whether predictive models lead to biased decisions by transportation authorities."

**时空蒸馏（ST-Distillation）：**
> "Although GNNs have shown great promise in handling traffic datasets, their deployment in real-life applications has been hindered by scalability constraints arising from high-order message passing."

**零膨胀分布（Zero-Inflated）：**
> "Adversarial spatiotemporal graph learning under zero-inflated distribution presents unique challenges for traffic prediction."

**异构图对比学习（Heterogeneous Graph CL）：**
> "Heterogeneous graph contrastive learning enhances the robustness of spatiotemporal representations."

### 13.46 新方法架构总结（18篇）

| 类别 | 代表论文 | 核心突破 |
|------|---------|---------|
| Attention+SSM混合 | FAST, GAMMA-Net | 统一Transformer表达力与Mamba效率 |
| Diffusion增强 | DETNO, NPDiff, LEAD | 高频重建/噪声先验/LLM融合 |
| LLM适配 | U-STS-LLM, CrossTrafficLLM | 注意力偏置引导/预测+描述双输出 |
| 检索增强 | RAST | RAG理念迁移至时空建模 |
| Neural ODE创新 | LTE-ODE | 数学误差转化为注意力偏置 |
| PDE物理先验 | NeST-S6 | 物理方程嵌入SSM |
| 概率预测 | GMM-Universal, RIPCN | 优雅的概率化改造 |
| 轻量化部署 | LightST, M3-Net, GraphSparseNet | 知识蒸馏/去图化/线性复杂度 |
| 在线适应 | FORESEE | 零参数更新的实时校正 |
