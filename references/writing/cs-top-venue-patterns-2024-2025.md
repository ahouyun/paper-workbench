# 2024-2025 CS 顶会最佳论文写作模式

> 基于 NeurIPS 2024、ICML 2024、ICLR 2024/2025 最佳论文和高影响力论文的真实 Abstract 分析。
> 补充 Research-Paper-Writing-Skills 中已有的 SAM、Llama 2、FlashAttention 等论文。

---

## 1. 真实 Abstract 分析

### 1.1 VAR — Visual Autoregressive Modeling (NeurIPS 2024 Best Paper)

**论文：** Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction
**作者：** Keyu Tian, Yi Jiang, Zehuan Yuan, Bingyue Peng, Liwei Wang
**摘要原文：**

> We present Visual AutoRegressive modeling (VAR), a new generation paradigm that redefines the autoregressive learning on images as coarse-to-fine "next-scale prediction" or "next-resolution prediction", diverging from the standard raster-scan "next-token prediction". This simple, intuitive methodology allows autoregressive (AR) transformers to learn visual distributions fast and generalize well: VAR, for the first time, makes GPT-like AR models surpass diffusion transformers in image generation. On ImageNet 256×256 benchmark, VAR significantly improve AR baseline by improving Frechet inception distance (FID) from 18.65 to 1.73, inception score (IS) from 80.4 to 350.2, with around 20× faster inference speed. It is also empirically verified that VAR outperforms the Diffusion Transformer (DiT) in multiple dimensions including image quality, inference speed, data efficiency, and scalability. Scaling up VAR models exhibits clear power-law scaling laws similar to those observed in LLMs, with linear correlation coefficients near −0.998 as solid evidence. VAR further showcases zero-shot generalization ability in downstream tasks including image in-painting, out-painting, and editing. These results suggest VAR has initially emulated the two important properties of LLMs: Scaling Laws and zero-shot task generalization.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 贡献+范式定义 | `We present [Name], a new [范式] that redefines [任务] as [新定义]` |
| 第2句 | 突破声明 | `This simple methodology allows [能力]: [Name], for the first time, makes [突破]` |
| 第3句 | 量化结果 | `On [benchmark], [Name] significantly improves [基线] by [具体数字]` |
| 第4句 | 多维度对比 | `It is also empirically verified that [Name] outperforms [基线] in multiple dimensions` |
| 第5句 | Scaling law | `Scaling up [模型] exhibits clear power-law scaling laws` |
| 第6句 | 泛化能力 | `[Name] further showcases zero-shot generalization ability in [任务]` |
| 第7句 | 总结 | `These results suggest [Name] has initially emulated [LLM特性]` |

**关键技巧：**
- "for the first time" 用在真正突破性的结果上，有数据支撑
- 量化结果非常具体：FID 从 18.65 到 1.73，IS 从 80.4 到 350.2
- "linear correlation coefficients near −0.998 as solid evidence" — 用数字说话
- 结尾用 "these results suggest" 而非 "this groundbreaking work"

---

### 1.2 Mamba — Linear-Time Sequence Modeling (ICML 2024)

**论文：** Mamba: Linear-Time Sequence Modeling with Selective State Spaces
**作者：** Albert Gu, Tri Dao
**摘要原文：**

> Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5× higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1-2句 | 背景+挑战 | `Foundation models are almost universally based on [架构]. Many [替代] have been developed to address [问题], but they have not performed as well as [基线]` |
| 第3句 | 诊断 | `We identify that a key weakness of such models is [根本原因]` |
| 第4句 | 改进1 | `First, simply letting [参数] be functions of [输入] addresses [弱点]` |
| 第5句 | 改进2 | `Second, we design [工程创新]` |
| 第6句 | 集成 | `We integrate these [组件] into [架构名]` |
| 第7句 | 性能 | `[Name] enjoys [优势] and [扩展性]` |
| 第8-9句 | 泛化 | `As a general [backbone], [Name] achieves [性能] across [模态]. On [任务], [Name] outperforms [基线] and matches [更强基线]` |

**关键技巧：**
- 开头先建立 Transformer 的统治地位，再引出替代方案的不足
- "We identify that a key weakness" — 诊断式开头，显示洞察力
- 技术改进用 "First... Second..." 结构化
- "matches Transformers twice its size" — 用倍数关系展示效率
- "across several modalities" — 强调泛化性

---

### 1.3 Depth Anything V2 (NeurIPS 2024)

**论文：** Depth Anything V2
**作者：** Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, Hengshuang Zhao
**摘要原文：**

> This work presents Depth Anything V2. Without pursuing fancy techniques, we aim to reveal crucial findings to pave the way towards building a powerful monocular depth estimation model. Notably, compared with V1, this version produces much finer and more robust depth predictions through three key practices: 1) replacing all labeled real images with synthetic images, 2) scaling up the capacity of our teacher model, and 3) teaching student models via the bridge of large-scale pseudo-labeled real images. Compared with the latest models built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate. We offer models of different scales (ranging from 25M to 1.3B params) to support extensive scenarios. Benefiting from their strong generalization capability, we fine-tune them with metric depth labels to obtain our metric depth models. In addition to our models, considering the limited diversity and frequent noise in current test sets, we construct a versatile evaluation benchmark with precise annotations and diverse scenes to facilitate future research.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 简介 | `This work presents [Name] [Version]` |
| 第2句 | 方法论声明 | `Without pursuing fancy techniques, we aim to reveal crucial findings` |
| 第3句 | 三大改进 | `through three key practices: 1) ..., 2) ..., 3) ...` |
| 第4句 | 效率对比 | `Compared with [基线], our models are significantly more efficient (more than Nx faster) and more accurate` |
| 第5句 | 模型系列 | `We offer models of different scales (ranging from X to Y) to support extensive scenarios` |
| 第6句 | 下游应用 | `Benefiting from [能力], we [下游应用]` |
| 第7句 | 额外贡献 | `In addition to [主要贡献], we [次要贡献]` |

**关键技巧：**
- "Without pursuing fancy techniques" — 谦逊但自信的表达
- 三大改进用编号结构 "1) ... 2) ... 3) ..."
- "more than 10× faster" — 用倍数而非百分比
- "ranging from 25M to 1.3B params" — 展示覆盖范围
- 额外贡献单独一句，展示论文的完整性

---

### 1.4 AlphaFold 3 (Nature 2024)

**论文：** Accurate structure prediction of biomolecular interactions with AlphaFold 3
**作者：** Abramson et al., Google DeepMind
**摘要原文：**

> The introduction of AlphaFold 2 has spurred a revolution in modelling the structure of proteins and their interactions, enabling a huge range of applications in protein modelling and design. Here we describe our AlphaFold 3 model with a substantially updated diffusion-based architecture that is capable of predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues. The new AlphaFold model demonstrates substantially improved accuracy over many previous specialized tools: far greater accuracy for protein–ligand interactions compared with state-of-the-art docking tools, much higher accuracy for protein–nucleic acid interactions compared with nucleic-acid-specific predictors and substantially higher antibody–antigen prediction accuracy compared with AlphaFold-Multimer v.2.3. Together, these results show that high-accuracy modelling across biomolecular space is possible within a single unified deep-learning framework.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 前作影响 | `[前作] has spurred a revolution in [领域], enabling [应用]` |
| 第2句 | 本文贡献 | `Here we describe [模型] with [架构更新] that is capable of [能力]` |
| 第3句 | 排比对比 | `demonstrates substantially improved accuracy: far greater... much higher... substantially higher...` |
| 第4句 | 总结 | `these results show that [核心结论] is possible within [框架]` |

**关键技巧：**
- 用前作建立 credibility
- "Here we describe" 引出贡献
- 排比结构强调多维度优势
- "these results show that" 总结

---

### 1.5 GNoME — Scaling deep learning for materials discovery (Nature 2023)

**论文：** Scaling deep learning for materials discovery
**作者：** Merchant et al., Google DeepMind
**摘要原文：**

> Novel functional materials enable fundamental breakthroughs across technological applications from clean energy to information processing. From microchips to batteries and photovoltaics, discovery of inorganic crystals has been bottlenecked by expensive trial-and-error approaches. Concurrently, deep-learning models for language, vision and biology have showcased emergent predictive capabilities with increasing data and computation. Here we show that graph networks trained at scale can reach unprecedented levels of generalization, improving the efficiency of materials discovery by an order of magnitude. Building on 48,000 stable crystals identified in continuing studies, improved efficiency enables the discovery of 2.2 million structures below the current convex hull, many of which escaped previous human chemical intuition. Our work represents an order-of-magnitude expansion in stable materials known to humanity.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 领域重要性 | `[材料] enable fundamental breakthroughs across [应用]` |
| 第2句 | 具体挑战 | `discovery has been bottlenecked by [方法局限]` |
| 第3句 | 跨领域类比 | `Concurrently, [其他领域] have showcased [能力]` |
| 第4句 | 核心声明 | `Here we show that [方法] can reach [水平], improving [效率] by [量级]` |
| 第5句 | 量化结果 | `Building on [已有工作], [方法] enables [发现规模]` |
| 第6句 | 意义 | `Our work represents [量级扩展] in [领域]` |

---

### 1.6 DeepSeek-R1 (Nature 2025)

**论文：** DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning
**作者：** DeepSeek-AI et al.
**摘要原文：**

> General reasoning represents a long-standing and formidable challenge in artificial intelligence (AI). Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought (CoT) prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent on extensive human-annotated demonstrations and the capabilities of models are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labelled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions and STEM fields, surpassing its counterparts trained through conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically used to guide and enhance the reasoning capabilities of smaller models.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 领域挑战 | `[问题] represents a long-standing and formidable challenge in [领域]` |
| 第2句 | 现有进展 | `Recent breakthroughs, exemplified by [技术], have achieved considerable success on [任务]` |
| 第3句 | 局限 | `However, this success is heavily contingent on [依赖] and [能力不足]` |
| 第4句 | 核心声明 | `Here we show that [能力] can be incentivized through [方法], obviating the need for [依赖]` |
| 第5句 | 机制 | `The proposed [框架] facilitates the emergent development of [模式]` |
| 第6句 | 结果 | `Consequently, the trained model achieves superior performance on [任务]` |
| 第7句 | 泛化 | `Moreover, [ emergent patterns] can be systematically used to guide and enhance [能力]` |

**关键技巧：**
- "long-standing and formidable challenge" — 用两个形容词强调挑战的难度
- "obviating the need for" — 比 "removing the need for" 更学术
- "emergent development" — 强调自然涌现而非人工设计
- "Consequently" — 因果关系连接词
- "systematically used to guide and enhance" — 强调可复现性和实用价值

---

## 2. Abstract 写作模式汇总

### 2.1 四步结构（IEEE/Nature/NeurIPS 通用）

高影响力论文的 Abstract 通常遵循四步压缩证明结构：

1. **Importance** — 为什么这个问题重要（1-2 句）
2. **Bottleneck** — 现有方法缺什么（1-2 句）
3. **Contribution** — 本文引入什么（2-3 句）
4. **Evidence** — 结果证明了什么（1-2 句）

### 2.2 开头句模式

**直接引入贡献（最常见）：**
- "We present [Name], a new [范式] that redefines [任务] as [新定义]." — VAR
- "This work presents [Name] [Version]." — Depth Anything V2
- "We introduce the [Name] project: a new task, model, and dataset for [领域]." — SAM

**前作影响力 + 本文延续：**
- "The introduction of [前作] has spurred a revolution in [领域]." — AlphaFold 3

**背景 + 挑战：**
- "Foundation models are almost universally based on [架构]. Many [替代] have been developed, but they have not performed as well as [基线]." — Mamba
- "[材料] enable fundamental breakthroughs. Discovery has been bottlenecked by [局限]." — GNoME

### 2.3 量化结果句模式

**具体数字（最佳）：**
- "VAR significantly improves FID from 18.65 to 1.73, IS from 80.4 to 350.2" — VAR
- "5× higher throughput than Transformers" — Mamba
- "more than 10× faster" — Depth Anything V2

**倍数关系：**
- "matching Transformers twice its size" — Mamba
- "improving the efficiency by an order of magnitude" — GNoME

**范围覆盖：**
- "ranging from 25M to 1.3B params" — Depth Anything V2
- "across several modalities such as language, audio, and genomics" — Mamba

### 2.4 结尾句模式

**总结意义：**
- "These results suggest [Name] has initially emulated [特性]." — VAR
- "Our work represents an order-of-magnitude expansion in [领域]." — GNoME
- "these results show that [结论] is possible within [框架]." — AlphaFold 3

**额外贡献：**
- "In addition to [主要贡献], we [次要贡献]." — Depth Anything V2

---

## 3. Introduction 写作模式

### 3.1 漏斗结构（通用）

**第1段：大背景 + 核心挑战**
```
[技术] has become the de-facto standard for [任务]. However, [核心挑战].
```

**第2段：现有方法及局限**
```
Existing approaches include [方法类别]. However, these methods [具体局限].
```

**第3段：本文方法/发现**
```
We identify that a key weakness is [根本原因]. We propose [方法] that [创新].
```

### 3.2 Introduction 开头模式

**模式 A：技术统治地位 + 替代方案不足**
> "Foundation models are almost universally based on the Transformer architecture. Many subquadratic-time architectures have been developed to address Transformers' computational inefficiency, but they have not performed as well as attention on important modalities such as language." — Mamba

**模式 B：直接切入核心问题**
> "Understanding protein structure is fundamental to biology and medicine." — AlphaFold 3

**模式 C：领域重要性 + 挑战**
> "Novel functional materials enable fundamental breakthroughs across technological applications. Discovery has been bottlenecked by expensive trial-and-error approaches." — GNoME

### 3.3 贡献列表模式

**编号式（最常见）：**
```
Our contributions are threefold:
1) [贡献1]
2) [贡献2]
3) [贡献3]
```

**嵌入式（Nature 风格）：**
```
Here we show that [核心贡献]. [支撑贡献1]. [支撑贡献2].
```

---

## 4. 关键表达模式

### 4.1 引出贡献

- "We present [Name], a new [范式] that redefines [任务]." — VAR
- "We identify that a key weakness is [X], and make several improvements." — Mamba
- "Here we describe [Name] with [架构更新]." — AlphaFold 3
- "Here we show that [方法] can reach [水平]." — GNoME
- "This work presents [Name]. Without pursuing fancy techniques, we aim to reveal crucial findings." — Depth Anything V2

### 4.2 量化对比

- "significantly improves [指标] from X to Y" — VAR
- "Nx higher throughput than [基线]" — Mamba
- "more than Nx faster and more accurate" — Depth Anything V2
- "by an order of magnitude" — GNoME
- "matching [基线] twice its size" — Mamba

### 4.3 泛化声明

- "across several modalities such as language, audio, and genomics" — Mamba
- "zero-shot generalization ability in downstream tasks" — VAR
- "models of different scales to support extensive scenarios" — Depth Anything V2
- "high-accuracy modelling across biomolecular space" — AlphaFold 3

### 4.4 对冲与自信

**自信（有数据支撑）：**
- "for the first time, makes [X] surpass [Y]" — VAR
- "achieves state-of-the-art performance across several modalities" — Mamba

**谦逊（避免过度声明）：**
- "has initially emulated" — VAR（用 "initially" 限定）
- "these results suggest" — VAR（用 "suggest" 而非 "prove"）
- "Without pursuing fancy techniques" — Depth Anything V2

---

## 5. 常见错误与修正

### Abstract 错误

| 错误 | 修正 | 参考论文 |
|------|------|----------|
| "In recent years, ..." | 直接陈述挑战 | Mamba: "Foundation models are almost universally based on..." |
| "Our method significantly outperforms" | 给出具体数字 | VAR: "FID from 18.65 to 1.73" |
| "This is a groundbreaking work" | 删除主观评价 | AlphaFold 3: "these results show that..." |
| "Extensive experiments demonstrate" | 具体化 | Depth Anything V2: "more than 10× faster" |
| "A novel method for..." | 用技术名 | VAR: "We present VAR" |

### Introduction 错误

| 错误 | 修正 | 参考论文 |
|------|------|----------|
| 背景段太长（>5 句） | 精简到 3-4 句 | Mamba: 2 句背景 |
| 文献罗列无分析 | 选择性引用 | Mamba: "linear attention, gated convolution and recurrent models, and SSMs" |
| 贡献列表过于详细 | 3-5 条核心贡献 | Depth Anything V2: 三大改进 |
| 缺少路线图 | 添加简短路线图 | Depth Anything V2: "In addition to our models..." |
