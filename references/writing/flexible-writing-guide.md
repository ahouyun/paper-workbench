# 灵活写作指南 (Flexible Writing Guide)

> **核心理念：学习原则，不是背诵模板。** 每篇论文都应该有自己的声音。

---

## 一、为什么模板化写作会被拒稿

**编辑的原话：** "当多个用户使用同一套规则时，产出的论文会呈现出高度相似的结构和风格。当编辑在短时间内看到多篇结构、用词、贡献列表格式完全一致的论文时，会触发AIGC检测警觉。"

**模板化写作的特征：**
- 每段开头都是 "However," 或 "In this paper,"
- 每个贡献都是 "We propose a novel..."
- 每个结果都是 "Extensive experiments demonstrate..."
- 每段结构都是 问题→方法→结果

**解决方案：** 学习原则，然后根据你的具体研究灵活运用。

---

## 二、Abstract写作：不是填空，是讲故事

### 原则：Abstract = 一个完整的故事

一个好的Abstract应该回答5个问题，但顺序和措辞可以灵活变化：

1. **为什么重要？** — 你研究的问题为什么值得研究
2. **什么问题？** — 现有方法的不足
3. **怎么做？** — 你的解决方案
4. **效果如何？** — 关键实验结果
5. **意味着什么？** — 更广泛的影响

### 同一个意思，不同的表达

**问题："交通预测很重要"**

| 风格 | 示例 |
|------|------|
| 直接陈述 | "Accurate traffic flow prediction is critical for intelligent transportation systems." |
| 应用导向 | "Efficient traffic management relies on accurate forecasting of future traffic conditions." |
| 问题驱动 | "Traffic congestion costs billions annually, and accurate prediction is key to mitigation." |
| 技术驱动 | "The growing deployment of traffic sensors creates opportunities for data-driven forecasting." |
| 挑战导向 | "Predicting traffic flow remains challenging due to complex spatiotemporal dependencies." |

**不要总是用同一种风格。** 根据你的研究特点选择最合适的开场方式。

### 同一个创新，不同的描述方式

**创新："我们提出了一个新的注意力机制"**

| 风格 | 示例 |
|------|------|
| 强调机制 | "We introduce a delay-aware attention mechanism that explicitly models propagation delays." |
| 强调效果 | "By modeling propagation delays, our approach achieves 8.7% MAE reduction." |
| 强调洞察 | "We observe that traffic congestion propagates with delays, and design an attention mechanism to capture this." |
| 强调对比 | "Unlike standard attention that treats spatial relationships as instantaneous, our mechanism accounts for temporal delays." |
| 强调简洁 | "A simple modification to the attention mechanism—adding a delay term—significantly improves prediction." |

---

## 三、Introduction写作：不是漏斗，是对话

### 原则：Introduction = 与读者的对话

好的Introduction不是机械地执行"漏斗结构"，而是引导读者理解你的研究动机。

### 对话式写作示例

**模板化写法（避免）：**
```
Traffic prediction is important. However, existing methods have limitations. 
In this paper, we propose a novel method. Extensive experiments demonstrate...
```

**对话式写法（推荐）：**
```
Every morning, millions of drivers face the same question: will the highway 
be congested? Accurate traffic prediction could answer this, but current 
methods struggle with a fundamental challenge—traffic congestion doesn't 
happen everywhere at once. It propagates through the network with delays 
that most models ignore.

We set out to fix this. Our key insight is that the delay itself carries 
information about the network's structure. By explicitly modeling these 
delays, we can predict not just where congestion will occur, but when.
```

### 不同的Introduction开场方式

| 方式 | 示例 | 适用场景 |
|------|------|---------|
| **故事开场** | "Every morning, millions of drivers face..." | 应用导向的研究 |
| **数据开场** | "Traffic congestion costs the US economy $87 billion annually." | 强调社会影响 |
| **问题开场** | "Why do traffic prediction models fail during rush hour?" | 解决具体问题 |
| **观察开场** | "We observe that traffic congestion propagates through networks with varying delays." | 基于观察的创新 |
| **挑战开场** | "Predicting traffic flow is like predicting weather—complex, dynamic, and essential." | 复杂系统研究 |
| **技术开场** | "Graph neural networks have revolutionized traffic prediction, but they share a blind spot..." | 技术驱动的研究 |

---

## 四、Method写作：不是说明书，是设计思路

### 原则：Method = 为什么这样设计

好的Method部分不仅描述"是什么"，更要解释"为什么"。

### 模块描述的灵活方式

**模板化写法（避免）：**
```
We propose Module X. Module X consists of Component A and Component B.
Component A does... Component B does...
```

**设计思路写法（推荐）：**
```
Our key observation is that traffic congestion propagates with delays. 
This motivates us to design a delay-aware attention mechanism.

The mechanism works in three steps:
1. First, we estimate the propagation delay between each pair of sensors...
2. Then, we adjust the attention weights to account for these delays...
3. Finally, we aggregate the delay-adjusted features...

The intuition is simple: if congestion takes 10 minutes to propagate 
from sensor A to sensor B, then the attention from B to A should look 
10 minutes into the past, not the present.
```

### 数学公式的灵活呈现

**模板化写法（避免）：**
```
The attention mechanism is defined as:
Attention(Q,K,V) = softmax(QK^T/√d_k)V
```

**设计思路写法（推荐）：**
```
Standard attention treats all spatial relationships as instantaneous:
Attention(Q,K,V) = softmax(QK^T/√d_k)V

But traffic congestion propagates with delays. If sensor i influences 
sensor j with delay τ_ij, we should attend to the state of i at time 
t - τ_ij, not t. This gives us our delay-aware attention:

Attention_delay(Q,K,V) = softmax(QK^T_delay/√d_k)V

where K_delay shifts each key by its corresponding delay τ_ij.
```

---

## 五、实验写作：不是数字堆砌，是发现叙述

### 原则：实验部分 = 讲述你的发现

好的实验部分不是简单地报告数字，而是讲述你通过实验发现了什么。

### 结果描述的灵活方式

**模板化写法（避免）：**
```
As shown in Table 1, our method outperforms all baselines. 
Our method achieves MAE of 2.49 on METR-LA.
```

**发现叙述写法（推荐）：**
```
Three findings emerge from our experiments:

First, the delay-aware attention consistently improves prediction 
across all datasets (Table 1). On METR-LA, it reduces MAE from 
2.69 to 2.49—an 7.4% improvement that grows to 12.1% on the 
60-minute horizon. This confirms our hypothesis that modeling 
propagation delays is particularly important for long-term prediction.

Second, the improvement is most pronounced during rush hours 
(Figure 3). During peak congestion, delays are longer and more 
variable, making our delay-aware mechanism especially valuable.

Third, the learned delay patterns align with known traffic physics 
(Figure 4). The attention weights show higher delays on highways 
than urban roads, consistent with the higher speeds and longer 
propagation distances on highways.
```

### 消融实验的灵活描述

**模板化写法（避免）：**
```
We conduct ablation studies. Removing component X increases MAE by 3.2%.
This demonstrates the effectiveness of component X.
```

**洞察驱动写法（推荐）：**
```
To understand what drives our model's performance, we conduct 
ablation studies (Table 2).

The most impactful component is the delay estimation module: 
removing it increases MAE by 3.2% on METR-LA. This is expected—
without accurate delay estimates, the attention mechanism cannot 
properly align temporally shifted features.

Interestingly, the dynamic graph module contributes less (1.1% 
MAE improvement). We hypothesize that the predefined graph already 
captures most spatial dependencies, leaving limited room for 
improvement through dynamic graph learning.
```

---

## 六、灵活写作的核心原则

### 原则1：不要复制粘贴句子

即使你看到一篇论文写得很好，也不要直接复制。理解它为什么好，然后用你自己的话表达。

### 原则2：每段要有自己的声音

每段的第一句话应该告诉读者这段要讲什么。不要总是用同样的句式开头。

### 原则3：用具体例子代替抽象描述

**抽象：** "Our model captures complex spatiotemporal dependencies."
**具体：** "Our model learns that congestion on Highway 101 propagates southward with a 15-minute delay during morning rush hour."

### 原则4：用对比代替绝对声明

**绝对：** "Our method is the best."
**对比：** "On METR-LA, our method reduces MAE by 8.7% compared to the strongest baseline (STAEformer), with the improvement being most pronounced on the 60-minute horizon."

### 原则5：承认局限性

**回避：** 不提局限性
**诚实：** "Our method has two limitations. First, it requires accurate delay estimates, which may be unavailable in networks with few sensors. Second, the computational cost scales quadratically with the number of sensors, limiting its applicability to very large networks."

### 原则6：用你的研究特点决定写作风格

| 研究特点 | 推荐风格 |
|---------|---------|
| 解决具体问题 | 问题驱动开场 |
| 提出新架构 | 技术驱动开场 |
| 发现新现象 | 观察驱动开场 |
| 应用导向 | 应用场景开场 |
| 理论贡献 | 数学驱动开场 |

---

## 七、自查清单

在提交论文前，检查是否模板化：

- [ ] 是否每段开头都是 "However," 或 "In this paper,"？
- [ ] 是否每个贡献都是 "We propose a novel..."？
- [ ] 是否每个结果都是 "Extensive experiments demonstrate..."？
- [ ] 是否每段结构都是 问题→方法→结果？
- [ ] 是否有具体的例子和数字，而不是泛泛而谈？
- [ ] 是否承认了局限性？
- [ ] 是否有你自己的声音和风格？

---

> 核心理念：学习原则，不是背诵模板。每篇论文都应该有自己的声音。
> 更新时间：2026-06-20
