# Nature/Science 真实论文写作模式

> 基于 Nature/Science/Cell 2023-2025 高影响力论文的 Abstract/Introduction/Results 写作分析。
> 所有摘要均为真实论文原文。

---

## 1. 真实 Abstract 分析

### 1.1 AlphaFold 3 (Nature 2024)

**论文：** Accurate structure prediction of biomolecular interactions with AlphaFold 3
**作者：** Abramson et al., Google DeepMind
**摘要原文：**

> The introduction of AlphaFold 2 has spurred a revolution in modelling the structure of proteins and their interactions, enabling a huge range of applications in protein modelling and design. Here we describe our AlphaFold 3 model with a substantially updated diffusion-based architecture that is capable of predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues. The new AlphaFold model demonstrates substantially improved accuracy over many previous specialized tools: far greater accuracy for protein–ligand interactions compared with state-of-the-art docking tools, much higher accuracy for protein–nucleic acid interactions compared with nucleic-acid-specific predictors and substantially higher antibody–antigen prediction accuracy compared with AlphaFold-Multimer v.2.3. Together, these results show that high-accuracy modelling across biomolecular space is possible within a single unified deep-learning framework.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 背景+影响 | `[前作] has spurred a revolution in [领域], enabling [应用]` |
| 第2句 | 本文贡献 | `Here we describe [模型] with [架构更新] that is capable of [能力]` |
| 第3句 | 量化对比 | `demonstrates substantially improved accuracy over [基线]: [3个对比维度]` |
| 第4句 | 总结意义 | `these results show that [核心结论] is possible within [框架]` |

**关键技巧：**
- 开头用前作（AlphaFold 2）建立 credibility，不从零开始
- "Here we describe" 引出贡献，不用 "We propose a novel"
- 对比句用排比结构：`far greater... much higher... substantially higher...`
- 结尾用 "these results show that" 总结，不用 "this groundbreaking work"

---

### 1.2 GNoME — Scaling deep learning for materials discovery (Nature 2023)

**论文：** Scaling deep learning for materials discovery
**作者：** Merchant et al., Google DeepMind
**摘要原文：**

> Novel functional materials enable fundamental breakthroughs across technological applications from clean energy to information processing. From microchips to batteries and photovoltaics, discovery of inorganic crystals has been bottlenecked by expensive trial-and-error approaches. Concurrently, deep-learning models for language, vision and biology have showcased emergent predictive capabilities with increasing data and computation. Here we show that graph networks trained at scale can reach unprecedented levels of generalization, improving the efficiency of materials discovery by an order of magnitude. Building on 48,000 stable crystals identified in continuing studies, improved efficiency enables the discovery of 2.2 million structures below the current convex hull, many of which escaped previous human chemical intuition. Our work represents an order-of-magnitude expansion in stable materials known to humanity.

**写作模式拆解：**

| 句子 | 功能 | 模式 |
|------|------|------|
| 第1句 | 领域重要性 | `[材料类型] enable fundamental breakthroughs across [应用领域]` |
| 第2句 | 具体挑战 | `discovery of [X] has been bottlenecked by [方法局限]` |
| 第3句 | 跨领域类比 | `Concurrently, [其他领域] have showcased [能力]` |
| 第4句 | 核心声明 | `Here we show that [方法] can reach [水平], improving [效率] by [量级]` |
| 第5句 | 量化结果 | `Building on [已有工作], [方法] enables [发现规模]` |
| 第6句 | 意义 | `Our work represents [量级扩展] in [领域]` |

**关键技巧：**
- 第1-2句建立 "重要但困难" 的张力
- 第3句用其他领域的成功做类比，暗示本领域也能做到
- "by an order of magnitude" 是 Nature 喜欢的量化表达
- 结尾用 "represents an order-of-magnitude expansion" 声明意义

---

### 1.3 VAR — Visual Autoregressive Modeling (NeurIPS 2024 Best Paper)

**论文：** Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction
**作者：** Tian et al.
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

## 2. Introduction 写作模式

### 2.1 Nature Introduction 的 "漏斗结构"

Nature Introduction 通常 3-5 段，比 IEEE 短但更精炼：

**第1段：大背景 + 核心挑战（面向广泛读者）**
```
[领域] is central to [重要应用]. A key challenge is [核心挑战].
```

**第2段：现有方法及局限**
```
Current approaches include [方法类别]. However, [具体局限].
```

**第3段：本文方法/发现**
```
Here we [核心发现]. Our approach [关键创新]. This enables [能力].
```

### 2.2 Nature vs IEEE Introduction 对比

| 维度 | Nature | IEEE Transactions |
|------|--------|-------------------|
| 长度 | 3-5 段，每段 3-5 句 | 5-8 段，每段 5-10 句 |
| 背景 | 简洁，面向广泛读者 | 详细，面向领域专家 |
| 文献综述 | 融入背景段，不单独成节 | 常有单独 Related Work 节 |
| 贡献列表 | 简短，1-2 句 | 详细，3-5 条 bullet points |
| 开头 | 直接切入事实或挑战 | 可以更技术化 |
| 语言 | 英式英语 | 美式或英式均可 |

### 2.3 Nature Introduction 开头模式（真实例句）

**模式 A：直接切入核心问题**
> "Understanding protein structure is fundamental to biology and medicine."

**模式 B：领域重要性 + 挑战**
> "Novel functional materials enable fundamental breakthroughs across technological applications from clean energy to information processing."

**模式 C：前作影响力 + 本文延续**
> "The introduction of AlphaFold 2 has spurred a revolution in modelling the structure of proteins and their interactions."

**避免的开头：**
- ❌ "In recent years, ..."（太模板化）
- ❌ "With the development of ..."（空泛）
- ❌ "It is well known that ..."（无需声明）

---

## 3. Results 写作模式

### 3.1 Nature Results 结构

Nature 论文 Results 节通常放在 Methods 之前：

**核心发现先行：**
> "Here we show that graph networks trained at scale can reach unprecedented levels of generalization."

**系统性验证：**
> "The new AlphaFold model demonstrates substantially improved accuracy over many previous specialized tools."

**量化对比：**
> "VAR significantly improves AR baseline by improving FID from 18.65 to 1.73, IS from 80.4 to 350.2."

### 3.2 Nature Results 关键表达

**展示发现：**
- "Here we show that ..."
- "We found that ..."
- "Our analysis reveals that ..."
- "Strikingly, ..."
- "Notably, ..."

**量化结果：**
- "X improved by Y% compared to Z"
- "We observed a Z-fold increase in X"
- "X was Y times faster than Z"
- "by an order of magnitude"

**因果关系：**
- "This improvement is attributed to ..."
- "We attribute this to ..."
- "This suggests that ..."
- "This is consistent with ..."

---

## 4. Discussion 对冲语言

### 4.1 声明强度分级

| 证据强度 | Nature 用词 | 示例 |
|----------|-------------|------|
| 强证据 | demonstrate, show, establish | "Our results demonstrate that ..." |
| 中等证据 | suggest, indicate, support | "These findings suggest that ..." |
| 弱证据 | may, might, it is possible | "It is possible that ..." |
| 推测 | speculate, one explanation | "We speculate that ..." |

### 4.2 Nature 对冲 vs IEEE 对冲

Nature 对语言精度要求更高：
- Nature: "Our results suggest that ..."（即使是强证据也用 suggest）
- IEEE: "Our results demonstrate that ..."（强证据可以用 demonstrate）
- Nature 避免 "prove"（除非数学证明）
- Nature 避免 "novel", "groundbreaking", "first"（除非真正首创）

---

## 5. Figure 设计模式

### 5.1 Nature Figure 角色分工

| Figure | 角色 | 内容 |
|--------|------|------|
| Figure 1 | 核心发现 | 主要结果的可视化，最吸引眼球 |
| Figure 2 | 机制/原理 | 方法的工作原理或关键机制 |
| Figure 3 | 系统性验证 | 多场景/多数据集的验证 |
| Figure 4 | 消融/对比 | 消融实验或与现有方法对比 |
| Figure 5（可选） | 应用/展望 | 实际应用案例或未来方向 |

### 5.2 Nature Caption 模式

```
Figure X. [标题]. [描述性说明]. [关键观察]. [统计信息].
```

**示例：**
```
Figure 1. AlphaFold 3 predicts protein structures with high accuracy.
a, Comparison of predicted (blue) and experimental (grey) structures.
b, RMSD distribution across 100 test proteins.
c, Accuracy improvement over AlphaFold 2 on different tasks.
Error bars represent s.d. across n=3 independent runs.
```

---

## 6. 英式英语规范

Nature 要求英式拼写：

| 美式 | 英式 |
|------|------|
| color | colour |
| analyze | analyse |
| program | programme |
| signaling | signalling |
| modeling | modelling |
| favor | favour |
| recognize | recognise |
| center | centre |

---

## 7. 常见错误与修正

### 标题
| 错误 | 修正 |
|------|------|
| "A Novel Method for X" | 直接用技术名 |
| "An Innovative Approach to X" | 具体描述创新 |
| 标题超过 15 词 | 精简到 12-15 词 |

### Abstract
| 错误 | 修正 |
|------|------|
| "In recent years, ..." | 直接陈述挑战 |
| "Our method significantly outperforms ..." | 给出具体数字 |
| "This is a groundbreaking work" | 删除主观评价 |

### Introduction
| 错误 | 修正 |
|------|------|
| 背景段太长（>5 句） | 精简到 3-4 句 |
| 文献罗列无分析 | 选择性引用，给出分析 |
| 贡献列表过于详细 | 3-5 条核心贡献 |
