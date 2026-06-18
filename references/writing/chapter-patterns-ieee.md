# IEEE Transactions 章节模式（增强版）

> 基于 115+ 篇 2024-2026 年 IEEE Transactions 真实论文分析，覆盖 TPAMI、TNNLS、TKDE、TIP、TIFS、TMM、TSE、TCSVT 等期刊。

---

## 一、标准章节顺序

```
Title → Abstract → Index Terms →
I. Introduction → II. Related Work → III. System Model / Problem Formulation →
IV. Proposed Method → V. Theoretical Analysis →
VI. Experimental Results → VII. Discussion →
VIII. Conclusion → References
```

### 章节顺序变体

| 论文类型 | 章节顺序调整 |
|----------|-------------|
| 方法/系统论文 | 标准顺序 |
| 综述/路线图论文 | Introduction → Preliminaries → Taxonomy → 分类综述 → 对比分析 → 应用 → 开放问题 → Conclusion |
| 基准/数据集论文 | Introduction → Related Datasets → 数据集构建 → 任务定义与评估协议 → 统计与标注质量 → 基线与结果 → Discussion → Conclusion |
| 经验/软件工程论文 | Introduction → Background → Research Questions → Approach → Study Design → Results by RQ → Discussion → Threats to Validity → Conclusion |
| 基础设施/系统论文 | Introduction → Background → System Design → Implementation → Theoretical Analysis → Experiments → Related Work → Conclusion |

---

## 二、Title（标题）

### 标题模式

| 论文类型 | 标题模式 | 示例 |
|----------|----------|------|
| 方法论文 | 问题 + 技术机制 + 任务 | "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" |
| 综述论文 | 声明论文类型 | "A Survey on Deep Neural Network Pruning: Taxonomy, Methods, and Applications" (TPAMI 2024) |
| 系统论文 | 强调速度/内存/可扩展性 | "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism" |
| 自动驾驶论文 | 强调哲学/流程 | "UniAD: Planning-oriented Autonomous Driving" (CVPR 2023 Best Paper) |
| 实时检测论文 | 强调速度/训练策略 | "YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors" |
| 深度估计论文 | 强调鲁棒性/零样本 | "Depth Anything V2" (版本演进模式) |
| 数据集论文 | 数据集名称 + 规模 | "GenFace: A Large-Scale, High-Quality, and Diverse Face Forgery Benchmark" (TIFS 2024) |

### 标题规范

- 清晰、简洁、信息丰富
- 避免缩写（除非极其常见）
- 通常 10-15 个词
- 方法论文标题应包含技术关键词
- 综述论文标题必须声明论文类型（Survey, Review, Assessment, Roadmap, Frontiers）

---

## 三、Abstract（摘要，150-250 words）

### 摘要四步结构

所有高质量 IEEE Trans 摘要都遵循四步结构：

1. **问题重要性** — 为什么这个问题重要
2. **现有方法不足** — 为什么现有方法不够好
3. **本文贡献** — 我们做了什么
4. **证据支持** — 实验结果如何

### 按论文类型的摘要模式

#### 模式 A：方法论文摘要

结构：问题 → 局限性 → 方法 → 结果 → 意义

**真实示例 — SAM (Kirillov et al., TPAMI 2023):**
> "We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. The Segment Anything Model (SAM) is designed and trained to be promptable, enabling zero-shot transfer to new image distributions and tasks. We built the largest segmentation dataset to date, with over 1 billion masks on 11M licensed and privacy-respecting images. Zero-shot performance is often competitive with or superior to prior fully supervised results."

**模式分析：**
- Move 1 (任务): "a new task, model, and dataset for image segmentation"
- Move 2 (构建内容): "SAM is designed and trained to be promptable"
- Move 3 (证据范围): "over 1 billion masks on 11M images"
- Move 4 (结果): "competitive with or superior to prior fully supervised results"
- 无空洞赞美；以量化证据结尾

**真实示例 — FlashAttention (Dao et al., NeurIPS 2022):**
> "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. We propose an algorithm to overcome this: FlashAttention, an IO-aware exact attention algorithm."

**模式分析：**
- Move 1 (问题): "slow and memory-hungry on long sequences"
- Move 2 (根因): "quadratic in sequence length"
- Move 3 (解决方案): "IO-aware exact attention algorithm"
- 直接、具体、无冗余

#### 模式 B：综述论文摘要

结构：问题 → 差距 → 范围 → 贡献 → 结构

**真实示例 — PEFT Survey (Xu et al., TPAMI 2024):**
> "With the continuous growth in number of parameters of transformer-based pretrained language models (PLMs), particularly the emergence of large language models (LLMs) with billions of parameters, many natural language processing (NLP) tasks have demonstrated remarkable success. Parameter Efficient Fine-Tuning (PEFT) offers an effective solution by reducing the number of fine-tuning parameters and memory usage while achieving comparable performance to full fine-tuning."

**模式分析：**
- Move 1 (背景): "continuous growth in number of parameters"
- Move 2 (解决方案): "PEFT offers an effective solution"
- Move 3 (优势): "reducing parameters and memory usage while achieving comparable performance"
- 综述摘要关注 *领域需求* 而非 *论文做了什么*

#### 模式 C：系统/产品论文摘要

结构：构建内容 → 优化目标 → 证据 → 贡献

**真实示例 — Llama 2 (Touvron et al., Meta 2023):**
> "In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called LLAMA 2-CHAT, are optimized for dialogue use cases. Our models outperform open-source chat models on most benchmarks we tested, and based on our human evaluations for helpfulness and safety, may be a suitable substitute for closed-source models."

**模式分析：**
- Move 1 (构建内容): "develop and release Llama 2... ranging from 7B to 70B"
- Move 2 (优化目标): "optimized for dialogue use cases"
- Move 3 (证据): "outperform open-source chat models on most benchmarks"
- Move 4 (范围限定): "may be a suitable substitute for closed-source models"
- 适当使用模糊限定词（"may be"）

### 摘要质量检查清单

- [ ] 读者能否一次识别任务、挑战、贡献和结果？
- [ ] 所有主要论点是否有实验支持？
- [ ] 技术名称是否自包含且可读？
- [ ] 是否有任何句子混合了过多信息？
- [ ] 无 "Despite significant progress" 开头
- [ ] 无 "In this paper" 填充词
- [ ] 无 "Extensive experiments" 而不命名数据集
- [ ] "Novel" 最多出现一次
- [ ] 结尾有具体的、有限定的声明（非 "promising results"）
- [ ] "However" 最多出现一次
- [ ] 所有数据集都已命名
- [ ] 所有比较都引用了具体方法和数字

---

## 四、Index Terms（关键词，4-10 个）

- 斜体，按字母序
- 使用 IEEE Thesaurus 标准术语
- 首字母小写（除非专有名词）
- 综述论文应包含 "Survey" 或 "Review" 相关术语

---

## 五、I. Introduction（引言）

### 引言八步漏斗结构

高质量 IEEE Trans 引言反复遵循此漏斗：

1. **广泛背景和重要性**（1-2 段）
2. **现有方法家族或系统范式**（1-2 段）
3. **为什么这些家族不够好**（1-2 段）
4. **明确的任务或问题陈述**（1 段）
5. **挑战分解**，常用标签如 `(C1)`, `(C2)`（1 段）
6. **方法响应**，常映射为 `(S1)`, `(S2)`（1 段）
7. **贡献声明**（必备）
8. **论文组织**（必备）

如果问题技术密度高，优先使用显式的 `挑战 → 响应` 配对。

### 真实漏斗示例

#### 示例 1：SAM 引言（8 步漏斗）

**Step 1 — 广泛背景：**
> "Large language models pre-trained on web-scale datasets have revolutionized NLP with strong zero-shot and few-shot generalization."

**Step 2 — 基础模型概念：**
> "A key capability of these LLMs is the ability to address new tasks described in language via prompt engineering."

**Step 3 — 视觉类比：**
> "In computer vision, CLIP and ALIGN use contrastive learning to align text and image encoders for zero-shot generalization."

**Step 4 — 差距：**
> "Segmentation lacks an equivalent foundation model."

**Step 5 — 任务定义：**
> "We introduce the promptable segmentation task."

**Step 6 — 三个组件：**
> "Task (§2), Model (§3), Data Engine (§4)"

**Step 7 — 数据集：**
> "SA-1B: 1B+ masks from 11M images, 400× more masks than any existing dataset."

**Step 8 — 贡献声明：**
- "Task: We introduce the promptable segmentation task..."
- "Model: We describe SAM, a promptable segmentation model..."
- "Data: We build SA-1B, the largest segmentation dataset..."
- "RAI: We conduct a responsible AI analysis..."

**关键观察：** 每个贡献映射到一个具体工件（任务定义、模型架构、数据集、分析）和一个论文章节。

#### 示例 2：Llama 2 引言（4 步漏斗）

**Step 1 — 背景：**
> "Large Language Models (LLMs) have shown great promise as highly capable AI assistants that excel in complex reasoning tasks requiring expert knowledge across a wide range of fields."

**Step 2 — 差距：**
> "High computational requirements have limited the development of LLMs to a few players. There have been public releases of pretrained LLMs... but none of these models are suitable substitutes for closed 'product' LLMs."

**Step 3 — 贡献：**
> "In this work, we develop and release Llama 2, a family of pretrained and fine-tuned LLMs, LLAMA 2 and LLAMA 2-CHAT, at scales up to 70B parameters."

**Step 4 — 发布模型：**
1. "LLAMA 2, an updated version of LLAMA 1..."
2. "LLAMA 2-CHAT, a fine-tuned version of LLAMA 2..."

**关键观察：** 系统论文将 *发布的产品* 列为贡献，而非仅技术创新。

#### 示例 3：PEFT Survey 引言（4 步漏斗）

**Step 1 — 背景：**
> "With the continuous growth in number of parameters of transformer-based PLMs, particularly the emergence of LLMs with billions of parameters, many NLP tasks have demonstrated remarkable success."

**Step 2 — 差距：**
> "Full fine-tuning of PLMs is computationally expensive and memory-intensive."

**Step 3 — 解决方案：**
> "PEFT offers an effective solution by reducing the number of fine-tuning parameters and memory usage while achieving comparable performance."

**Step 4 — 贡献：**
- "We present a comprehensive analysis and review of PEFT methods..."
- "We identify the key techniques and classify them into five categories..."
- "We conduct extensive experiments to evaluate effectiveness..."

**关键观察：** 综述贡献结合 *综述* + *分类法* + *实验*。

### 引言四种开头模式

#### 模式 1：任务优先（适合小众任务）

1. 用一句话定义任务（什么输出从什么输入）
2. 简要解释任务目标或范围
3. 用 2-3 个代表性场景介绍应用价值

句式骨架：
```
[xxx task] targets at recovering/reconstructing/estimating [xxx output] from [xxx input].
[xxx task] has a variety of applications such as [xxx], [xxx], and [xxx].
```

#### 模式 2：应用优先（适合熟悉任务）

1. 跳过正式任务定义
2. 以应用重要性开篇
3. 可选地附加目标需求（如准确率/效率/鲁棒性）

#### 模式 3：从一般到具体（适合新设置）

1. 从一般任务开始，解释为什么重要
2. 缩小到本文的具体设置
3. 澄清确切的输入/输出和设置边界

#### 模式 4：直接暴露挑战（适合有明确失败案例的任务）

1. 以任务/应用重要性开始
2. 立即总结代表性先前方法如何工作
3. 立即暴露未解决的失败案例 + 技术原因

### 贡献声明要求

- 3-5 条，每条具体可验证
- 使用强动词：propose, develop, derive, demonstrate, prove, design, introduce, build, release, identify, classify, conduct, evaluate, establish, summarize, systematize
- 避免：novel, innovative, state-of-the-art（让读者判断）
- 每条贡献映射到论文的一个 Section
- 每条贡献绑定到一个具体工件（模型、数据集、分类法、定理、基准、系统）

### 真实贡献声明示例

**SAM（工件绑定，并行结构）：**
- "Task: We introduce the promptable segmentation task..."
- "Model: We describe SAM, a promptable segmentation model..."
- "Data: We build SA-1B, the largest segmentation dataset to date..."
- "RAI: We conduct a responsible AI analysis..."

**模式：** 标签: 动词 + 工件 + 证据名词。

**Llama 2（编号列表，产品聚焦）：**
1. "LLAMA 2, an updated version of LLAMA 1, trained on a new mix of publicly available data."
2. "LLAMA 2-CHAT, a fine-tuned version of LLAMA 2 that is optimized for dialogue use cases."

**模式：** 产品名称 + 修改 + 关键改进。

**PEFT Survey（综述 + 分类法 + 实验）：**
- "We present a comprehensive analysis and review of PEFT methods..."
- "We identify the key techniques and approaches... and classify them into additive, partial, reparameterized, hybrid, and unified fine-tuning methods."
- "We conduct extensive experiments to evaluate the effectiveness of several representative PEFT methods..."

**模式：** 动词 + 范围 + 工件（综述/分类法/实验）。

**DoRA (Liu et al., ICML 2024)：**
- "We propose DoRA, a PEFT method that decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning."
- "DoRA consistently outperforms LoRA across three task categories: commonsense reasoning, visual instruction tuning, and image/video-text understanding."

**模式：** 方法名称 + 分解 + 优势 + 范围。

**VAR (Tian et al., NeurIPS 2024 Best Paper)：**
- "For the first time, GPT-style autoregressive models surpass diffusion models in image generation quality."
- "We discover power-law Scaling Laws in VAR transformers."

**模式：** 首次声明 + 缩放定律发现。

**DeepSeek-V3 (2024)：**
- "DeepSeek-V3, a Mixture-of-Experts (MoE) language model with 671B total parameters and 37B activated per token."
- "The full training required only 2.788M H800 GPU hours with no irrecoverable loss spikes or perform any rollbacks."

**模式：** 架构 + 规模 + 效率声明。

### 论文组织段落（必备）

```
The rest of this paper is organized as follows.
Section II reviews related work.
Section III presents the system model and problem formulation.
Section IV describes the proposed method.
Section V provides theoretical analysis.
Section VI presents experimental results.
Section VII concludes this paper.
```

---

## 六、II. Related Work（相关工作）

### 组织原则

- 按技术主题分组（非时间序）
- 每组：范式总结 → 关键局限 → 你的区别
- 覆盖所有最强竞争对手
- 引用密度高（每个技术点 2-5 篇引用）

### 综述论文的 Related Work 差异

综述论文的 "相关工作" 通常融合到引言中，或作为独立的 "Preliminaries / Background" 章节，而非单独的 Related Work 章节。

### 综合语言模式

更好的综合语言：
- "These methods share a common assumption that..."
- "The main distinction lies in whether..."
- "A recurring limitation across this family is..."
- "Compared with..., this category offers... at the cost of..."

避免逐篇论文叙述而不综合。

---

## 七、III. System Model / Problem Formulation（系统模型/问题定义）

### 必备元素

- 系统架构描述
- 数学符号表（notation table）
- 假设条件（assumptions）
- 形式化问题定义

### 符号规范

| 符号类型 | 格式 |
|----------|------|
| 向量 | 小写粗体 $\mathbf{x}$ |
| 矩阵 | 大写粗体 $\mathbf{X}$ |
| 标量 | 小写斜体 $x$ |
| 集合 | 大写花体 $\mathcal{X}$ |
| 转置 | $\mathbf{x}^T$ |
| 期望 | $\mathbb{E}[\cdot]$ |

### 问题定义模板

```
\textit{Problem:} Given [input], find [output] that optimizes [objective]
subject to [constraints].
```

### 硬规则

- 只要论文有正式符号、假设、约束或优化目标，就将 `Problem Formulation` 与 `Method` 分开。
- 不要强行将所有 IEEE Trans 论文塞入 `System Model -> Proposed Method -> Theory`。
- 如果核心贡献是方法论的、经验的或概念性的，让 `study design` 或 `conceptual framework` 成为骨架。

---

## 八、IV. Proposed Method（方法）

### 每个模块三要素

1. **Motivation（动机）**：为什么需要这个模块
   - 问题驱动：因为问题 X 存在，我们设计模块 Y
   - 典型开头："A remaining problem/challenge is...", "However, we...", "Previous methods have difficulty in..."

2. **Design（设计）**：模块的数学描述和算法
   - 定义关键结构（表示、网络、数据结构）
   - 按严格执行顺序描述前向过程
   - 以输出解释或用途结束

3. **Technical Advantage（技术优势）**：为什么比替代方案好
   - 将优势与可测量行为绑定
   - 示例："Our module reduces memory from O(n²) to O(n) while maintaining 98% of the attention quality."

### 方法写作步骤

1. 画出 pipeline 图草图
2. 用草图组织 Method 子节结构
3. 为每个子节规划三部分：动机、模块设计、技术优势
4. 先写模块设计以建立具体骨架
5. 之后添加动机和技术优势

### 真实方法结构示例

#### SAM 方法结构（模块化）

- Section 3: "Segment Anything Model (SAM)"
  - 3.1 Image Encoder（MAE 预训练 ViT-H，1024×1024 输入，16× 下采样嵌入）
  - 3.2 Prompt Encoder（稀疏：点/框/文本；密集：掩码）
  - 3.3 Lightweight Mask Decoder（Transformer 解码器，2 层，~50ms）
  - 3.4 Resolving Ambiguity（3 个掩码，置信度分数）
  - 3.5 Losses and Training（focal + dice loss，交互模拟，11 轮）
  - 3.6 Engineering Efficiency（图像编码器只运行一次，提示解码器很快）

**关键观察：** 每个子节回答一个具体的技术问题，而非泛泛描述。

#### Llama 2 方法结构（系统论文模式）

- Section 2: Pretraining
  - 2.1 Pretraining Data（2T tokens，公开可用来源）
  - 2.2 Training Details（AdamW，cosine LR，GQA）
  - 2.2.1 Training Hardware & Carbon Footprint（3.3M GPU hours，539 tCO₂eq）
  - 2.3 Pretrained Model Evaluation
- Section 3: Fine-Tuning
  - 3.1 Supervised Fine-Tuning（27,540 annotations，"Quality Is All You Need"）
  - 3.2 RLHF（人类偏好数据、奖励建模、迭代微调）
  - 3.3 System Message for Multi-Turn Consistency（GAtt）
  - 3.4 RLHF Results

**关键观察：** 系统论文包含基础设施细节（硬件、碳足迹、数据管线），方法论文则省略。

### 算法伪代码格式

```latex
\begin{algorithm}[t]
\caption{Algorithm Name}
\label{alg:example}
\begin{algorithmic}[1]
\REQUIRE Input parameters
\ENSURE Output
\STATE Initialize ...
\WHILE{condition}
    \STATE Step 1 ...
    \STATE Step 2 ...
\ENDWHILE
\RETURN result
\end{algorithmic}
\end{algorithm}
```

### 复杂度分析

- 时间复杂度：$O(\cdot)$
- 空间复杂度：$O(\cdot)$
- 与 baseline 的复杂度对比表

### 方法写作质量检查

- [ ] 模块名称是否具体且技术性（非 "Feature Extraction Module"）
- [ ] 动机是否问题驱动且有具体后果
- [ ] 前向过程是否用具体操作和张量形状描述
- [ ] 优势是否与可测量行为绑定
- [ ] 章节开头是否陈述内容而非元声明
- [ ] 实现细节是否包含具体超参数

---

## 九、V. Theoretical Analysis（理论分析，可选）

### 定理/引理格式

```latex
\begin{theorem}
\label{thm:convergence}
Under Assumption 1, the proposed algorithm converges to...
\end{theorem}

\begin{proof}
The proof is provided in Appendix A.
\end{proof}
```

### 常见分析类型

- 收敛性证明
- 收敛速度分析
- 近似比/最优性界
- 计算复杂度
- 通信复杂度（分布式场景）

---

## 十、VI. Experimental Results（实验结果）

### 实验设计三问

1. **是否优于强 baseline**：公平对比、标准指标、SOTA included
2. **哪个模块导致增益**：消融实验（remove/replace/disable）
3. **在更难设置下泛化多远**：压力测试、OOD、失败模式

### 实验章节推荐顺序

强实验部分通常按此顺序回答审稿人问题：

1. 方法是否击败强基线？
2. 在哪些数据集、任务或操作条件下？
3. 哪个模块或设计选择导致增益？
4. 效率成本是多少？
5. 方法在何处变弱或失败？

此顺序比按时间顺序呈现结果更有效。

### 真实实验结构示例

#### SAM 实验结构（7 个子节）

1. 7.1: Zero-shot single point evaluation（23 datasets, mIoU + human study）
2. 7.2: Zero-shot edge detection（BSDS500, ODS/OIS/AP/R50）
3. 7.3: Zero-shot object proposals（LVIS v1, AR@1000）
4. 7.4: Zero-shot instance segmentation（COCO AP, LVIS AP）
5. 7.5: Zero-shot text-to-mask（proof-of-concept）
6. 7.6: Ablations（data engine stages, data volume, encoder scaling）

**关键观察：** 每个子节回答一个不同的零样本能力问题。消融放在最后，不是最前。

**消融设计：**
1. 数据引擎阶段：Manual → Semi-automatic → Automatic → All stages
2. 数据量：0.1M → 1M → 11M images
3. 编码器缩放：ViT-B → ViT-L → ViT-H

#### Llama 2 实验结构

1. Section 2.3: Pretrained Model Evaluation（8 benchmarks, 4 sizes）
2. Section 3.4.1: Model-Based Evaluation（win-rate vs. ChatGPT）
3. Section 3.4.2: Human Evaluation（4,000+ prompts, 3 raters each）
4. Section 4.4: Safety Evaluation（TruthfulQA, ToxiGen）

**关键观察：** 系统论文同时包含自动基准和人类评估。安全是独立的主要章节。

#### PEFT Survey 实验结构

- Experimental Setup（models, datasets, baselines）
- Main Results（Tables III-VI: RoBERTa, T5, LLaMA across GLUE, WMT16, MMLU）
- Efficiency Analysis（Table VII: GPU memory comparison）

**关键模式：**
- 跨模型评估：encoder (RoBERTa), encoder-decoder (T5), decoder-only (LLaMA)
- 跨任务评估：NLU (GLUE), MT (WMT16), benchmark (MMLU)
- 效率报告为可训练参数百分比和绝对 GPU 内存

#### HAT 实验结构（Chen et al., CVPR 2023 / TPAMI 2024）

- Experimental Setup（datasets, metrics, baselines）
- Main Results（PSNR/SSIM on 5 benchmarks × 3 scales）
- Visual Comparisons（qualitative results）
- Ablation Studies（attention mechanism, training strategy）

**关键模式：**
- 标准 SR 基准协议：Set5, Set14, BSD100, Urban100, Manga109
- 指标：PSNR, SSIM, Multi-Adds, Parameters
- 视觉比较在 ×4 缩放进行定性评估
- 每个组件消融：hybrid attention, overlapping cross-attention, second-stage training

#### UniAD 实验结构（Hu et al., CVPR 2023 Best Paper）

- Stage 1: Perception Training（tracking AMOTA, mapping IoU-lane）
- Stage 2: End-to-End Training（5 tasks jointly）
- Planning on nuScenes（L2 distance + collision rate at 1s/2s/3s）
- Planning on NAVSIM（NC, DAC, TTC, Comf., EP, PDMS）

**关键模式：**
- 两阶段训练：感知预训练 → 端到端联合训练
- 多任务评估：Track, Map, Motion, Occupancy, Planning
- 规划指标在多个时间范围：1s, 2s, 3s
- "Planning-oriented philosophy" 统一所有任务

#### YOLOv7 实验结构（Wang et al., CVPR 2023）

- Detection on MS COCO（6 model variants, AP + FPS）
- Instance Segmentation（AP_box + AP_mask）
- Anchor-Free Detection（AP_val）

**关键模式：**
- 速度-精度 Pareto 前沿：51.4% AP at 161 fps → 56.8% AP at 36 fps
- 多模型变体：YOLOv7, YOLOv7-X, W6, E6, D6, E6E
- "Trainable bag-of-freebies"：训练增强不增加推理成本

#### FlashAttention 实验结构（Dao et al., NeurIPS 2022）

- Throughput benchmark（A100: 225 TFLOPs/sec, 72% MFU）
- Memory benchmark（10X savings at 2K, 20X at 4K）
- Training speedup（3-5x vs HuggingFace baseline）
- Multi-hardware support（NVIDIA CUDA + AMD ROCm）

**关键模式：**
- 硬件利用率："225 TFLOPs/sec per A100, equivalent to 72% model FLOPs utilization"
- 内存节省随序列长度缩放："10X at 2K, 20X at 4K"
- 版本演进：FlashAttention → FlashAttention-2 (2x faster) → FlashAttention-3 (Hopper optimized)

### 消融实验包

- 一个核心消融表（所有主要贡献）
- 多个聚焦 mini-ablation
- 匹配的定性可视化

### 表格规范

- Caption 在表格上方
- 无竖线，booktabs 风格
- 最小化横线
- 标注指标方向（↑ higher better, ↓ lower better）
- 一致的小数精度
- 一个表格 = 一个信息

### 实验写作质量检查

- [ ] 每个证据声明是否命名了数据集和具体结果？
- [ ] 所有比较是否引用了具体方法和数字？
- [ ] 消融是否报告了每个组件的具体 delta？
- [ ] 结果叙述是否回答：比较了什么？模式是什么？为什么合理？
- [ ] 局限性是否诚实承认？
- [ ] 精度是否适合指标方差？
- [ ] 强基线是否包含？
- [ ] 协议是否在所有方法间一致？

---

## 十一、VII. Discussion（讨论，可选）

- 结果的深层含义
- 与 prior work 的关系
- 实际部署考虑
- 局限性分析

### 局限性写作模式

有用的局限性语言：
- "The current study is limited to..."
- "Our evaluation does not yet cover..."
- "This result should therefore be interpreted within..."
- "An important direction for future work is..."

避免虚假谦虚："There are still some limitations" — 精确命名局限性。

---

## 十二、VIII. Conclusion（结论）

- 重述问题和核心方法
- 总结最强实验证据
- 实际影响或新洞察
- 局限性（任务边界，非实现缺陷）
- 具体未来方向

---

## 十三、References（参考文献）

### 格式

- 方括号编号 [1], [2], ...（按首次出现顺序）
- 8pt 字体，单栏
- 使用 `IEEEtran.bst`

### 期刊格式

```
[1] A. Author, B. Author, and C. Author, ``Title,'' \emph{IEEE Trans. Abbrev.}, vol.~X, no.~X, pp.~X--X, Month Year.
```

### 会议格式

```
[2] A. Author and B. Author, ``Title,'' in \emph{Proc. Conf. Name}, City, Country, Year, pp.~X--X.
```

### 引用数要求

| 论文类型 | 引用数 |
|----------|--------|
| Regular Paper | 30-60+ |
| Letter | 15-25 |
| Survey | 80-200+ |
| 经验研究论文 | 40-80 |

### 引用密度策略

| 章节 | 引用密度 | 说明 |
|------|----------|------|
| Introduction | 每段 3-8 篇 | 覆盖所有相关方法家族 |
| Related Work | 每技术点 2-5 篇 | 覆盖最强竞争对手 |
| Method | 每模块 1-3 篇 | 引用启发来源和对比方法 |
| Experiments | 每 baseline 1 篇 | 确保公平对比 |

### 自引策略

- 自引比例建议：10-20%
- 自引应放在相关工作和方法启发处
- 避免过度自引（审稿人会注意到）

---

## 十四、Figure Families（图表家族）

跨真实 IEEE Trans 论文，强论文反复使用这些图表角色：

### 1. Teaser/Pipeline 图

**用途：** 一眼解释方法或任务的早期视觉。

**SAM 示例：**
- Figure 1: Three interconnected components (task + model + data engine)

**Llama 2 示例：**
- Figure 4: Training pipeline (pretraining → SFT → RLHF)

**UniAD 示例：**
- Pipeline 架构图：Track → Map → Motion → Occupancy → Planning

**规则：** Figure 1 应做真正的解释性工作，而非装饰性工作。

### 2. Taxonomy/Roadmap 图

**用途：** 综述和路线图论文必备。

**PEFT Survey 示例：**
- Figure 1: Evolutionary development timeline
- Figure 2: Taxonomy tree
- Figure 3: Architecture comparison (Sequential Adapter, Prefix-tuning, LoRA)

### 3. System Model 图

**用途：** 在深入方程之前展示实体、信号、模块或信息流。

**SAM 示例：**
- Figure 4: SAM architecture overview

### 4. Tradeoff Plot

**用途：** 质量 vs 内存、延迟、参数或鲁棒性。

**MiDaS 示例：**
- Improvement vs FPS scatter plot

**YOLOv7 示例：**
- 速度-精度散点图 (AP vs FPS)

### 5. Qualitative Panel

**用途：** 视觉密集型论文的并排视觉比较。

**SAM 示例：**
- Figure 2: Example SA-1B images with overlaid masks
- Figure 10: Zero-shot edge prediction
- Figure 12: Zero-shot text-to-mask results

### 6. Scaling Plot

**用途：** 性能 vs 模型大小、数据量或计算量。

**Llama 2 示例：**
- Figure 6: Reward model scaling trends
- Figure 15: Safety data scaling trends

**VAR 示例：**
- Scaling law 分析：loss/quality vs model size/compute

### 7. Training Pipeline 图

**用途：** 多阶段训练过程可视化。

**Llama 2 示例：**
- Figure 4: Training pipeline (pretraining → SFT → RLHF)

**UniAD 示例：**
- 两阶段训练：感知预训练 → 端到端联合训练

### 8. Evaluation Dashboard

**用途：** 多个指标跨多个条件。

**Llama 2 示例：**
- Figure 12: Human evaluation results

**DeepSeek-V3 示例：**
- 20+ benchmarks across 5 categories

### 9. Training Curve

**用途：** 训练过程中的性能变化。

**Llama 2 示例：**
- Figure 5: Training loss curves
- Figure 11: Win-rate evolution across RLHF iterations

### 10. Before/After Comparison

**用途：** 展示改进的视觉效果。

**Llama 2 示例：**
- Figure 9: Multi-turn memory issues + GAtt fix

### 11. Data Analysis 图

**用途：** 数据集统计和分析。

**SAM 示例：**
- Figure 5: Mask center distributions
- Figure 6: Dataset mask properties comparison
- Figure 7: Geographic distribution

### 12. Failure Gallery

**用途：** 展示失败模式以建立可信度。

**规则：** 在 Discussion 或实验末尾包含失败案例分析。

---

## 十五、Table Families（表格家族）

强论文倾向于使用此表格序列：

### 1. Main Benchmark Comparison Table（Table I 模式）

**用途：** 回答 "方法是否击败强基线？"

**SAM 示例：**
- Table 3: Zero-shot edge detection (ODS/OIS/AP/R50)
- Table 4: Zero-shot object proposals (AR@1000)
- Table 5: Zero-shot instance segmentation (AP)

**Llama 2 示例：**
- Table 3: Benchmark comparison (8 benchmarks, 4 model sizes)
- Table 4: Comparison to closed-source models

**HAT 示例：**
- Model comparison: Params, Multi-Adds, PSNR/SSIM across 5 datasets

**设计规则：**
- 标注指标方向（↑/↓）
- 高亮最佳结果（bold）
- 效率指标与质量指标并列

### 2. Ablation Table（Table II 模式）

**用途：** 回答 "哪个模块导致增益？"

**SAM 示例：**
- 数据引擎阶段消融：Manual → Semi-automatic → Automatic → All stages
- 数据量消融：0.1M → 1M → 11M images
- 编码器缩放消融：ViT-B → ViT-L → ViT-H

**设计规则：**
- 使用 remove/replace/disable 变体
- 报告与完整模型的 delta
- 包含组件交互消融（当模块耦合时）

### 3. Efficiency Table

**用途：** 回答 "效率成本是多少？"

**PEFT Survey 示例：**
- Table VII: GPU memory usage comparison

**FlashAttention 示例：**
- 无正式表格；结果以图形呈现
- 速度-序列长度曲线
- 内存对比图

**设计规则：**
- 包含参数量、FLOPs、推理时间、内存使用
- 与 baseline 的复杂度对比

### 4. Dataset Statistics Table

**用途：** 数据集和部署统计。

**SAM 示例：**
- Table 1: Geographic and income representation
- Table 2: Fairness in segmenting people

**Llama 2 示例：**
- Table 1: Model family overview (params, context, GQA, tokens, LR)
- Table 2: CO₂ emissions
- Table 6: Human preference data statistics
- Table 9a/b: Demographic representation
- Table 10: Language distribution

### 5. Model Overview Table

**用途：** 模型家族概览。

**Llama 2 示例：**
- Table 1: Model family overview (params, context, GQA, tokens, LR)

**SAM 2 示例：**
- Model | Size (M) | FPS | SA-V test (J&F) | MOSE val (J&F) | LVOS v2 (J&F)

### 6. Safety/Fairness Table

**用途：** 安全和公平性评估。

**Llama 2 示例：**
- Table 11: Safety benchmarks

**SAM 示例：**
- Table 2: Fairness in segmenting people

### 表格设计规则

- Caption 在表格上方
- 无竖线，booktabs 风格（`\toprule`, `\midrule`, `\bottomrule`）
- 最小化横线
- 标注指标方向（↑ higher better, ↓ lower better）
- 一致的小数精度
- 一个表格 = 一个信息
- 如果行代表不同属性/消融，在行名或属性列中显式编码
- Caption 聚焦于设置/协议/符号，非长讨论

### LaTeX 检查清单

1. 在 preamble 添加包：`\usepackage{booktabs}`, `\usepackage{colortbl,xcolor}`
2. 用 `\toprule/\midrule/\bottomrule` 替代 `\hline` 重样式
3. 将 `\caption{...}` 放在 `\label{...}` 之前，caption 在上方
4. 使用克制的高亮；永远不要着色太多单元格

---

## 十六、Writing Quality Markers（写作质量标记）

### 具体数字 vs 模糊声明

| 差 | 好 |
|----|-----|
| "Extensive experiments demonstrate..." | "We evaluate on COCO, LVIS, and ADE20K." |
| "Our method achieves state-of-the-art performance." | "Our method outperforms DINO by 2.1 AP on COCO and by 1.8 AP on LVIS." |
| "Ablation studies confirm the importance of each component." | "Removing the attention module reduces AP by 3.2 (51.3 → 48.1)." |
| "Our method is more efficient." | "Our module reduces memory from O(n²) to O(n) while maintaining 98% of the attention quality." |
| "Promising results" | "Our models outperform open-source chat models on most benchmarks we tested." |
| "Comprehensive experiments" | "We built the largest segmentation dataset to date, with over 1 billion masks on 11M images." |

### 证据绑定贡献

**规则：** 每个贡献声明必须映射到具体工件和可验证证据。

**差：** "We propose a novel method that significantly improves performance."
**好：** "We design the first fully differentiable multi-task framework that unifies perception, prediction, and planning modules." (UniAD)

### 可测量名词 vs 模糊赞美

| 差 | 好 |
|----|-----|
| "novel and innovative approach" | "IO-aware exact attention algorithm" |
| "significant improvement" | "2.1 AP improvement on COCO" |
| "better performance" | "51.4% AP at 161 fps" |
| "more robust" | "maintains performance across 6 datasets without fine-tuning" |
| "generalizes well" | "retains 98% performance on unseen distributions" |

### 过度声明修复模式

替换：
- "significantly improves" → "improves... by X% under..."
- "is more robust" → "maintains... under..."
- "generalizes well" → "retains performance across..."
- "validated in real-world settings" → "evaluated on... real-world..." / "deployed on..." / "tested using..."

仅当所述证据实际存在时才使用。

---

## 十七、Article Type Routing（论文类型路由）

在起草前，明确决定论文类型：

### 类型 1：Survey/Roadmap（综述/路线图）

**适用：** 对领域进行全面回顾和分类。

**真实论文：**
- "Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment" (TPAMI 2024)
- "From System 1 to System 2: A Survey of Reasoning Large Language Models" (TKDE 2024)
- "Unifying Large Language Models and Knowledge Graphs: A Roadmap" (TKDE 2024)
- "Diffusion Models: A Comprehensive Survey of Methods and Applications" (TPAMI 2024)
- "A Survey on Deep Neural Network Pruning: Taxonomy, Methods, and Applications" (TPAMI 2024)

**推荐骨架：**
1. `Introduction`
2. `Preliminaries / Background`
3. `Taxonomy or roadmap`
4. `Category-by-category review`
5. `Cross-category comparison`
6. `Applications / downstream tasks / deployment view`
7. `Open problems and future directions`
8. `Conclusion`

**要求：**
- 标题应使用 `Survey`, `Review`, `Assessment`, `Roadmap`, `Frontiers` 等词声明论文类型
- 引言必须解释为什么现在还需要额外的综述
- 核心中间章节应按概念或分类法组织，而非按出版年份

**关键图表：**
- Taxonomy tree（必备）
- Evolutionary timeline
- Method comparison table
- Cross-category analysis figure

### 类型 2：Method/System（方法/系统）

**适用：** 提出新方法、算法或系统。

**真实论文：**
- **Segment Anything (SAM)** — Kirillov et al., TPAMI 2023/2024
- **HAT** — Chen et al., CVPR 2023 / TPAMI 2024
- **DoRA** — Liu et al., ICML 2024
- **DINO** — Zhang et al., ICLR 2023
- **YOLOv7** — Wang et al., CVPR 2023
- **Mamba** — Gu & Dao, ICML 2024

**推荐骨架：**
1. `Introduction`
2. `Related Work`
3. `System Model / Problem Formulation`
4. `Proposed Method`
5. `Theoretical Analysis` or `Complexity Analysis`（when relevant）
6. `Experimental Results`
7. `Discussion`（when limitations or deployment issues matter）
8. `Conclusion`

**硬规则：**
- 只要论文有正式符号、假设、约束或优化目标，就将 `Problem Formulation` 与 `Method` 分开

### 类型 3：Benchmark/Dataset（基准/数据集）

**适用：** 构建新数据集或基准。

**真实论文：**
- "GenFace: A Large-Scale, High-Quality, and Diverse Face Forgery Benchmark" (TIFS 2024)
- "Ego4D: Around the World in 3,600 Hours of Egocentric Video"

**推荐骨架：**
1. `Introduction`
2. `Related Datasets / Benchmarks`
3. `Dataset or benchmark construction`
4. `Task definitions and evaluation protocols`
5. `Statistics, splits, and annotation quality`
6. `Baselines and benchmark results`
7. `Discussion of scope and limitations`
8. `Conclusion`

### 类型 4：Empirical Study（经验研究）

**适用：** TSE 风格的实证研究。

**真实论文：**
- "Software Testing With Large Language Models: Survey, Landscape, and Vision" (TSE 2024)
- "Mutation-Guided Unit Test Generation With a Large Language Model" (TSE 2024)
- "On the Need to Rethink Trust in AI Assistants for Software Development: A Critical Review"

**推荐骨架：**
1. `Introduction`
2. `Background / Related Work`
3. `Research Questions` or `Study Goals`
4. `Approach / System / Prompting or pipeline design`
5. `Experimental Setup` or `Study Design`
6. `Results by research question`
7. `Discussion`
8. `Threats to Validity`（when the discipline expects it）
9. `Conclusion`

### 类型 5：Infrastructure/System（基础设施/系统）

**适用：** 训练框架、推理优化、分布式系统。

**真实论文：**
- **FlashAttention** — Dao et al., NeurIPS 2022
- **Megatron-LM** — Shoeybi et al., 2019
- **Colossal-AI** — Li et al., ICPP 2023

**推荐骨架：**
1. `Introduction`（计算瓶颈分析）
2. `Background / Preliminaries`（硬件层次结构、并行策略）
3. `System Design`（算法 + 硬件感知设计）
4. `Implementation Details`（CUDA kernel、通信原语）
5. `Theoretical Analysis`（复杂度、通信量）
6. `Experiments`（吞吐量、显存、扩展性）
7. `Related Work`
8. `Conclusion`

**关键模式：**
- 标题常含 "Fast", "Efficient", "Memory-Efficient", "Scalable"
- 摘要强调硬件利用率
- 实验报告：吞吐量 (samples/s, TFLOPS/GPU)、显存峰值、扩展性曲线
- 图表：速度-序列长度曲线、显存对比柱状图、多GPU扩展性图
- 系统论文需要详细的硬件配置（GPU型号、CUDA版本、batch size）

### 类型 6：Autonomous Driving（自动驾驶）

**适用：** 感知-预测-规划一体化。

**真实论文：**
- **UniAD** — Hu et al., CVPR 2023 (Best Paper)

**推荐骨架：**
1. `Introduction`（端到端 vs 模块化）
2. `Related Work`（感知、预测、规划分别综述）
3. `Method`（感知 → 地图 → 运动 → 占用 → 规划）
4. `Experimental Setup`（nuScenes, metrics）
5. `Results`（分任务评估 + 端到端评估）
6. `Ablation Studies`（模块贡献）
7. `Conclusion`

**关键模式：**
- 标题含 "Planning-oriented", "End-to-End", "Unified"
- 方法部分按 pipeline 顺序
- 评估指标分层：感知、预测、规划
- 两阶段训练：感知预训练 + 端到端联合训练

### 类型 7：Medical Imaging（医学影像）

**适用：** 临床导向、跨数据集泛化。

**真实论文：**
- **MONAI** — 2022

**关键模式：**
- 强调临床相关性和泛化能力
- 跨数据集评估
- 标注质量和一致性分析

### 类型 8：Real-Time Detection（实时检测）

**适用：** 速度-精度 Pareto 前沿。

**真实论文：**
- **YOLOv7** — Wang et al., CVPR 2023
- **DINO** — Zhang et al., ICLR 2023

**推荐骨架：**
1. `Introduction`（实时检测需求）
2. `Related Work`（单阶段 vs 双阶段检测器）
3. `Method`（架构设计 + 训练策略）
4. `Experiments`（速度-精度 Pareto 前沿）
5. `Extensions`（分割、姿态估计等）
6. `Conclusion`

**关键模式：**
- 核心图表：速度-精度散点图 (AP vs FPS)
- 实验报告：多模型变体 (tiny → extra-large)、多分辨率测试
- 表格列：Model, Test Size, AP, AP50, AP75, FPS, Latency

### 类型 9：Depth Estimation（深度估计）

**适用：** 相对深度 → 度量深度、零样本跨数据集。

**真实论文：**
- **MiDaS v3.1** — Ranftl et al., TPAMI 2022
- **Depth Anything V2** — Yang et al., NeurIPS 2024

**关键模式：**
- 核心能力：零样本跨数据集泛化
- 评估指标：AbsRel, δ1, WHDR（数据集不同指标不同）
- 版本演进：v2.0 → v2.1 → v3.0 → v3.1，每次迭代量化改进

### 类型 10：Multimodal/Vision-Language（多模态/视觉-语言）

**适用：** 视觉-语言理解和生成。

**真实论文：**
- **InternVL** — CVPR 2024 (Oral)
- **CogVLM2** — 2024
- **MiniCPM-V** — 2024/2025
- **LLaVA** — Liu et al., NeurIPS 2023 (Oral)

**关键模式：**
- 多能力维度评估（图像理解、视频理解、文档解析、文本能力等）
- 缩放行为：参数量从 1B 到 241B
- 版本化消融：1.0→1.5→2.0→2.5→3.0→3.5
- 效率声明："90% of the performance with just 5% of the model size"

### 类型 11：Critical Review（批判性评论）

**适用：** 对领域概念的批判性分析。

**推荐骨架：**
1. `Introduction`
2. `Conceptual foundations`
3. `How the target field currently uses the concept`
4. `Gap analysis against mature adjacent disciplines`
5. `Recommendations or revised framework`
6. `Conclusion`

**关键模式：**
- "In the current literature, the term... is often used to denote..."
- "However, this usage does not align with..."
- "Related disciplines typically distinguish between... and..."
- "This mismatch leads to..."
- "We therefore recommend..."

---

## 十八、Anti-AI Patterns（去AI味模式）

### 摘要去AI味

| 编号 | 差 | 好 | 规则 |
|------|-----|-----|------|
| A1 | "Despite significant progress in deep learning..." | "Transformers are slow and memory-hungry on long sequences..." (FlashAttention) | 陈述具体技术瓶颈 |
| A2 | "In this paper, we propose a novel framework..." | "We propose FlashAttention, an IO-aware exact attention algorithm..." | 删除 "In this paper" |
| A3 | "Extensive experiments on multiple benchmarks demonstrate..." | "Zero-shot performance is often competitive with or superior to prior fully supervised results." (SAM) | 命名数据集和具体结果 |
| A4 | "We propose a novel and innovative approach that leverages a novel architecture..." | "We propose DINO, which improves denoising anchor boxes..." | "Novel" 最多一次 |
| A5 | "We conduct comprehensive experiments and thorough analysis..." | "We built the largest segmentation dataset to date, with over 1 billion masks on 11M images." (SAM) | 用数字替代形容词 |
| A6 | "Experimental results show promising performance..." | "Our models outperform open-source chat models on most benchmarks we tested." (Llama 2) | 以具体限定声明结尾 |
| A7 | "However... However... However..." | 使用 "However" 最多一次 | 重组其他句子 |
| A8 | "With the rapid development of artificial intelligence..." | "Modern autonomous driving systems are typically developed as a stack of standalone modules." (UniAD) | 跳过历史课 |
| A9 | "Experiments on several benchmarks confirm..." | "We evaluate on COCO, LVIS, and ADE20K." | 命名数据集 |
| A10 | "Our method achieves state-of-the-art performance." | "E2E-YOLO is the first real-time end-to-end object detector with 56.8 AP." (YOLOv7) | 具体方法名 + 具体指标 + 具体数字 |

### 引言去AI味

| 编号 | 差 | 好 | 规则 |
|------|-----|-----|------|
| I1 | "With the rapid development of artificial intelligence..." | "Transformers are slow and memory-hungry on long sequences..." (FlashAttention) | 直接陈述技术问题 |
| I2 | "Despite significant progress in deep learning..." | "Prior subquadratic models fall short of Transformers on information-dense data." (Mamba) | 陈述具体瓶颈 |
| I3 | "In recent years, attention mechanisms have attracted increasing attention." | "Attention mechanisms enable models to focus on relevant parts of the input." | 删除 "In recent years" |
| I4 | "We propose a novel and innovative approach..." | "We propose DINO, which improves denoising anchor boxes..." | "Novel" 最多一次 |
| I5 | "We conduct comprehensive experiments..." | "We built the largest segmentation dataset to date..." (SAM) | 用数字替代形容词 |
| I6 | "We propose a novel method that significantly improves performance." | "We design the first fully differentiable multi-task framework..." (UniAD) | 具体且可验证 |
| I7 | "However... However... However..." | 使用 "However" 最多一次 | 重组句子 |
| I8 | "As an important research direction, image segmentation has attracted much attention." | "Image segmentation enables autonomous driving, medical diagnosis, and robotics." | 陈述具体应用 |
| I9 | "Existing methods have some limitations." | "Existing methods require O(n²) memory for sequence length n, limiting application to long sequences." | 具体技术限制 |
| I10 | "We propose a method to solve this problem." | "We observe that self-attention matrices are often sparse. We exploit this sparsity to reduce computation." | 陈述洞察 |

### 方法去AI味

| 编号 | 差 | 好 | 规则 |
|------|-----|-----|------|
| M1 | "Feature Extraction Module", "Processing Module" | "Deformable Attention Backbone", "Cross-Modal Fusion Layer" | 使用具体技术名称 |
| M2 | "This module is important for the overall system." | "Existing attention mechanisms require O(n²) memory, limiting application to high-resolution images." | 问题驱动，有具体后果 |
| M3 | "The module processes the input and produces the output." | "Given input feature map F ∈ R^(H×W×C), we first apply 1×1 convolution to reduce channels to C/4..." | 具体操作和张量形状 |
| M4 | "Our module is more efficient and effective." | "Our module reduces memory from O(n²) to O(n) while maintaining 98% of the attention quality." | 与可测量行为绑定 |
| M5 | "In this section, we present our proposed method." | "We decompose the pipeline into three modules: tracking, mapping, and planning." | 陈述内容而非元声明 |
| M6 | "We use a standard transformer architecture." | "We use a 12-layer transformer with hidden dimension 768, 12 attention heads, and GELU activation." | 包含具体超参数 |

### 实验去AI味

| 编号 | 差 | 好 | 规则 |
|------|-----|-----|------|
| E1 | "Extensive experiments demonstrate..." | "We evaluate on COCO, LVIS, and ADE20K. Our method outperforms SAM by 2.1 mIoU on ADE20K." | 命名数据集和具体结果 |
| E2 | "Our method achieves state-of-the-art performance." | "Our method outperforms DINO by 2.1 AP on COCO and by 1.8 AP on LVIS." | 引用具体方法 + 具体数字 |
| E3 | "Ablation studies confirm the importance of each component." | "Removing the attention module reduces AP by 3.2 (51.3 → 48.1)." | 报告具体 delta |
| E4 | "Table 1 shows the results. Our method performs best." | "Table 1 shows that our method outperforms the strongest baseline (DINO) by 2.1 AP on COCO val." | 回答：比较了什么？模式？原因？ |
| E5 | 只报告成功，无失败案例 | "Our method struggles with small objects (< 16px), where the AP drops by 5.2." | 诚实承认局限性 |
| E6 | "Our method achieves 97.3456% accuracy." | "Our method achieves 97.3% accuracy." | 精度适合指标方差 |
| E7 | 只与弱或过时基线比较 | 包含最强公开方法 | 审稿人会注意到缺失的强基线 |
| E8 | 不同方法使用不同数据分割/预处理/评估设置 | "All methods use the same train/val split, input resolution (512×512), and evaluation protocol." | 公平比较需要一致协议 |

---

## 十九、Verified Paper Sources（已验证论文来源）

本文件中的模式提取自以下真实论文：

### TPAMI 2022-2024

- **Segment Anything (SAM)** — Kirillov et al., TPAMI 2023/2024. 可提示分割。
- **MiDaS v3.1** — Ranftl et al., TPAMI 2022. 单目深度估计。
- **HAT** — Chen et al., CVPR 2023 / TPAMI 2024. 图像超分辨率。
- **PEFT Survey** — Xu et al., TPAMI 2024. 参数高效微调综述。
- **Diffusion Models Survey** — Yang et al., TPAMI 2024.
- **SAM Comprehensive Survey** — TPAMI 2024.
- **A Survey on Deep Neural Network Pruning** — TPAMI 2024.

### TKDE 2024

- **From System 1 to System 2: A Survey of Reasoning LLMs** — TKDE 2024.
- **Unifying LLMs and Knowledge Graphs: A Roadmap** — TKDE 2024.

### TSE 2024

- **Software Testing With LLMs: Survey, Landscape, and Vision** — TSE 2024.
- **Mutation-Guided Unit Test Generation With a LLM** — TSE 2024.

### TIFS 2024

- **GenFace** — TIFS 2024. 人脸伪造基准。

### CVPR/ICLR/NeurIPS/ICML 2022-2024

- **Llama 2** — Touvron et al., Meta 2023. 7B-70B LLMs with RLHF.
- **FlashAttention** — Dao et al., NeurIPS 2022. IO-aware 注意力。
- **DINO** — Zhang et al., ICLR 2023. 端到端目标检测。
- **YOLOv7** — Wang et al., CVPR 2023. 实时目标检测。
- **UniAD** — Hu et al., CVPR 2023 (Best Paper). 端到端自动驾驶。
- **DoRA** — Liu et al., ICML 2024 (Oral). PEFT。
- **VAR** — Tian et al., NeurIPS 2024 (Best Paper). 视觉自回归建模。
- **Depth Anything V2** — Yang et al., NeurIPS 2024. 深度估计。
- **Mamba** — Gu & Dao, ICML 2024. 选择性状态空间。
- **SAM 2** — Ravi et al., Meta 2024. 视频分割。
- **LLaVA** — Liu et al., NeurIPS 2023 (Oral). 多模态指令调优。
- **InternVL** — CVPR 2024 (Oral). 视觉-语言模型。
- **3D Gaussian Splatting** — Kerbl et al., SIGGRAPH 2023.
- **EfficientViT** — ICCV 2023 / CVPR 2024. 高效视觉 Transformer。
- **Vision Transformer (ViT)** — Dosovitskiy et al., ICLR 2021.

### 系统/基础设施论文

- **Megatron-LM** — Shoeybi et al., 2019. 模型并行。
- **Colossal-AI** — Li et al., ICPP 2023. 分布式训练。
- **MONAI** — 2022. 医学影像框架。

### 大规模模型技术报告

- **InternLM2** — Cai et al., 2024.
- **Open-Sora** — 2024/2025. 视频生成。
- **CogVLM2** — 2024. 多模态理解。
- **MiniCPM-V/MiniCPM-o** — OpenBMB, 2024/2025.
- **DeepSeek-V3** — DeepSeek, 2024. 671B MoE LLM.
- **Qwen3** — Alibaba, 2025. Dense + MoE LLMs.
- **GLM-130B** — Zeng et al., ICLR 2023.
- **EVA** — Wang et al., CVPR 2023.
- **IP-Adapter** — Ye et al., 2023.
- **TAPAS** — Google, ACL 2020.

---

## 十四、写作顺序与规划策略

### 14.1 写作顺序 ≠ 阅读顺序

推荐的撰写顺序（先写结果，最后写摘要）：

1. **Results** — 先确定核心发现，围绕证据组织
2. **Introduction & Conclusion** — 基于结果确定贡献和故事线
3. **Title** — 基于贡献确定标题
4. **Discussion** — 解释发现的意义
5. **Methods** — 详细描述技术细节
6. **Abstract** — 最后写，浓缩全文

**核心原则：围绕证据和论证功能组织，而不是按时间顺序。**

### 14.2 漏斗结构 (Hourglass Structure)

强研究论文遵循 `宽 → 窄 → 宽` 的模式：
- **引言**：从领域全景收窄到研究空白，再陈述本研究
- **讨论/结论**：从具体发现扩展到更广泛的影响和局限

### 14.3 引言写作的逆向-正向逻辑

**逆向推理（先回答）：**
1. 我们解决什么技术问题？为什么没有成熟方案？
2. 我们的贡献是什么（新任务/新指标/新技术问题/新技术）？
3. 贡献的好处、为什么能解决挑战、带来什么新洞察？
4. 如何用先前方法引导读者到我们解决的挑战？

**正向故事（按此顺序写）：**
1. 介绍论文任务
2. 用先前方法引出技术挑战
3. 提出贡献来解决挑战
4. 解释技术优势并明确表达新洞察

### 14.4 技术挑战写作的三种模式

**Version 1（已有任务）：**
通用挑战 → 传统方法 → 最新方法 → 我们解决的剩余挑战

**Version 2（有传统方法支撑的洞察）：**
主流方法局限 → 古典方法中类似洞察 → 古典方法不足 → 现代方法仍未解决 → 我们的方法

**Version 3（新任务）：**
直接定义挑战并分解为具体挑战点
