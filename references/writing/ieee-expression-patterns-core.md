# IEEE Transactions Expression Patterns

## Goal

Provide reusable sentence logic for IEEE Transactions papers without turning the prose into template sludge.

Based on analysis of 115+ real IEEE Transactions papers from 2024-2026, including TPAMI, TNNLS, TKDE, TIP, TMM, TSE, TVCG, and top-tier venues (CVPR, NeurIPS, ICML, ICLR, ECCV, ACL, SIGGRAPH) frequently extended into IEEE Trans papers.

Use this guide for:

- title drafting,
- abstract drafting,
- introduction funnel construction,
- contribution bullet writing,
- method section language,
- result interpretation,
- limitation writing,
- survey synthesis,
- transition-heavy polishing,
- and anti-AI pattern removal.

---

## 1. Title Patterns

### 1.1 Method Papers

**Core pattern:** `Problem + technical mechanism + task`

The title names what problem is solved, what mechanism solves it, and what task domain benefits.

**Real examples from collected papers:**

| Paper | Title | Pattern |
|-------|-------|---------|
| HAT (TPAMI 2024) | Hybrid Attention Transformer for Image Restoration | Mechanism + Task |
| FlashAttention (NeurIPS 2022) | Fast and Memory-Efficient Exact Attention with IO-Awareness | Property + Mechanism + Technical Key |
| Mamba (ICML 2024) | Linear-Time Sequence Modeling with Selective State Spaces | Complexity Claim + Mechanism |
| DINO (ICLR 2023) | DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection | Base + Improvement + Task |
| DoRA (ICML 2024) | Weight-Decomposed Low-Rank Adaptation | Mechanism (pure technical name) |
| UniAD (CVPR 2023) | Planning-oriented Autonomous Driving | Philosophy + Domain |
| EfficientViT (ICCV 2023) | EfficientViT: Lightweight Multi-Scale Attention for Dense Prediction | Name + Property + Task |
| VAR (NeurIPS 2024) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | Paradigm + Subtitle with Mechanism |
| IP-Adapter (2023) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion | Name + Compatibility + Task |

**Common title structures for method papers:**

- `[Name]: [Mechanism] for [Task]` -- FlashAttention, EfficientViT
- `[Base] with [Improvement] for [Task]` -- DINO
- `[Property] [Mechanism]` -- Mamba, DoRA
- `[Task]-oriented [Philosophy]` -- UniAD
- `[Name]: [Claim] via [Mechanism]` -- VAR

**Avoid:**

- `A Novel Method for...` (let the name speak)
- `An Innovative Approach to...` (empty praise)
- Titles longer than 20 words

### 1.2 Survey Papers

**Declare the paper type in the title.**

**Real examples from collected papers:**

| Paper | Title | Pattern |
|-------|-------|---------|
| PEFT Survey (TPAMI 2024) | Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment | Topic + Type |
| Diffusion Survey (TPAMI 2024) | Diffusion Models: A Comprehensive Survey of Methods and Applications | Topic + Type + Scope |
| SAM Survey (TPAMI 2024) | A Comprehensive Survey on Segment Anything Model for Vision and Beyond | Type + Topic + Scope |
| Reasoning LLM Survey (TKDE 2024) | From System 1 to System 2: A Survey of Reasoning Large Language Models | Metaphor + Type + Topic |
| LLM+KG Roadmap (TKDE 2024) | Unifying Large Language Models and Knowledge Graphs: A Roadmap | Verb + Two Topics + Type |
| Software Testing Survey (TSE 2024) | Software Testing With Large Language Models: Survey, Landscape, and Vision | Topic + Type Triple |

**Common title structures for survey papers:**

- `A [Qualifier] Survey on [Topic]` -- SAM Survey
- `[Topic]: A [Qualifier] Survey of [Scope]` -- Diffusion Survey
- `[Topic]: [Type], [Perspective], and [Perspective]` -- Software Testing Survey
- `Unifying [A] and [B]: A Roadmap` -- LLM+KG
- `From [Source] to [Target]: A Survey of [Topic]` -- Reasoning LLM

**Title qualifiers observed:** Comprehensive, Critical, Systematic, Unified, Holistic

### 1.3 Benchmark and Dataset Papers

**Emphasize the artifact name and scale.**

**Real examples:**

| Paper | Title | Pattern |
|-------|-------|---------|
| SAM (TPAMI 2023) | Segment Anything | Artifact name (minimal) |
| Ego4D (CVPR 2022) | Ego4D: Around the World in 3,600 Hours of Egocentric Video | Name + Scale Descriptor |
| SA-1B | (within SAM paper) | Named dataset with scale marker |
| MONAI (2022) | MONAI: Medical Open Network for AI | Name + Abbreviation Expansion |

**Common title structures for benchmark papers:**

- `[Name]: [Scale or Scope Descriptor]` -- Ego4D
- `[Name]: [What It Does]` -- SAM, MONAI
- `[Name]: A Large-Scale [Qualifier] [Artifact Type] for [Domain]` -- common benchmark pattern

### 1.4 System and Infrastructure Papers

**Emphasize speed, memory, scalability, or hardware utilization.**

**Real examples:**

| Paper | Title | Pattern |
|-------|-------|---------|
| FlashAttention | Fast and Memory-Efficient Exact Attention with IO-Awareness | Property Pair + Mechanism |
| Megatron-LM | Training Multi-Billion Parameter Language Models Using Model Parallelism | Scale + Task + Mechanism |
| Colossal-AI | A Unified Deep Learning System For Large-Scale Parallel Training | Property + System + Task |
| DeepSeek-V3 | (implicit: 671B MoE LLM) | Scale + Architecture |

**Key observation:** System paper titles often contain `Fast`, `Efficient`, `Memory-Efficient`, `Scalable`, `Unified`, `Large-Scale`.

---

## 2. Abstract Patterns

### 2.1 Four-Move Abstract Structure

High-performing IEEE Trans abstracts follow a four-move compressed proof structure:

1. **Importance** -- why the problem matters (1-2 sentences)
2. **Bottleneck** -- what existing approaches lack (1-2 sentences)
3. **Contribution** -- what the paper introduces (2-3 sentences)
4. **Evidence** -- what results prove the claim (1-2 sentences)

### 2.2 Opening Sentences: Problem Importance + Specific Bottleneck

**Real opening examples:**

**SAM (TPAMI 2023):**
> "We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation."

Pattern: Direct artifact introduction. No throat-clearing.

**Llama 2 (Meta 2023):**
> "In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters."

Pattern: `In this work, we [verb] and [verb] [Name], [appositive with scale].`

**PEFT Survey (TPAMI 2024):**
> "With the continuous growth in number of parameters of transformer-based pretrained language models (PLMs), particularly the emergence of large language models (LLMs) with billions of parameters, many natural language processing (NLP) tasks have demonstrated remarkable success."

Pattern: `With the [trend], [domain] tasks have demonstrated [outcome].`

**FlashAttention (NeurIPS 2022):**
> "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length."

Pattern: `[Subject] are [problem adjectives] on [setting], since [root cause].`

**UniAD (CVPR 2023):**
> "Modern autonomous driving systems are typically developed as a stack of standalone modules for perception, prediction, and planning."

Pattern: `Modern [systems] are typically developed as [current paradigm].`

**Mamba (ICML 2024):**
> "Prior subquadratic models fall short of Transformers on information-dense data."

Pattern: `Prior [model family] fall short of [baseline] on [data type].`

**VAR (NeurIPS 2024):**
> "We present VAR, a new generation paradigm that reformulates autoregressive image generation as visual autoregressive modeling."

Pattern: `We present [Name], [appositive with paradigm shift].`

### 2.3 Middle Sentences: Proposed Approach + Key Innovation

**Real middle examples:**

**SAM:**
> "The Segment Anything Model (SAM) is designed and trained to be promptable, enabling zero-shot transfer to new image distributions and tasks."

Pattern: `[Model] is designed and trained to [capability], enabling [transfer benefit].`

**FlashAttention:**
> "We propose an algorithm to overcome this: FlashAttention, an IO-aware exact attention algorithm."

Pattern: `We propose [solution]: [Name], [appositive with technical identity].`

**DoRA:**
> "We propose DoRA, a PEFT method that decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning."

Pattern: `We propose [Name], [appositive] that [mechanism].`

**EfficientViT:**
> "We propose EfficientViT, a new family of vision transformers with lightweight multi-scale attention."

Pattern: `We propose [Name], [appositive with family/paradigm].`

**Depth Anything V2:**
> "We present Depth Anything V2, a solution that significantly outperforms V1 in fine-grained details and robustness."

Pattern: `We present [Name] [Version], [appositive with improvement areas].`

### 2.4 Ending Sentences: Quantitative Results + Significance

**Real ending examples:**

**SAM:**
> "Zero-shot performance is often competitive with or superior to prior fully supervised results."

Pattern: `[Capability] performance is often [comparative] with or [superior] to [baseline class].`

**Llama 2:**
> "Our models outperform open-source chat models on most benchmarks we tested, and based on our human evaluations for helpfulness and safety, may be a suitable substitute for closed-source models."

Pattern: `Our models [verb] [baseline] on [scope], and [qualification], may be [qualified claim].`

**FlashAttention:**
> "We achieve 225 TFLOPs/sec per A100, equivalent to 72% model FLOPs utilization."

Pattern: `We achieve [metric], equivalent to [utilization percentage].`

**Mamba:**
> "Mamba achieves linear-time sequence modeling and outperforms Transformers on language modeling."

Pattern: `[Name] achieves [complexity claim] and [verb] [baseline] on [task].`

**Open-Sora:**
> "Open-Sora 2.0 significantly narrows the gap with OpenAI's Sora, reducing it from 4.52% to 0.69%."

Pattern: `[Name] [verb] the gap with [baseline], reducing it from [X] to [Y].`

**CogVLM2:**
> "CogVLM2 achieves GPT4V-level performance with only 8B parameters."

Pattern: `[Name] achieves [baseline]-level performance with only [resource].`

**MiniCPM-V:**
> "Scores 13 on the Artificial Analysis Intelligence Index benchmark, outperforming Qwen3.5-0.8B's score of 10 with 19x fewer token cost."

Pattern: `Scores [X] on [benchmark], outperforming [baseline]'s score of [Y] with [efficiency gain].`

### 2.5 Abstract Anti-Patterns

**Avoid:**

- Ending with empty praise: `Experimental results show promising performance.`
- Generic scope: `Extensive experiments demonstrate effectiveness.`
- Unquantified claims: `Our method achieves state-of-the-art results.`

**Replace with:** specific datasets, specific metrics, specific numbers.

---

## 3. Introduction Funnel Language

### 3.1 Move 1: Importance (Broad Context)

**Purpose:** Establish why the topic matters. Connect to broader trends.

**Real phrases from collected papers:**

- `Large language models have shown great promise as highly capable AI assistants...` (Llama 2)
- `Large language models pre-trained on web-scale datasets have revolutionized NLP...` (SAM)
- `With the continuous growth in number of parameters of transformer-based PLMs...` (PEFT Survey)
- `... has revolutionized ... through ...` (SAM)
- `Modern autonomous driving systems are typically developed as a stack of standalone modules...` (UniAD)
- `Transformers have become the de-facto standard for sequence modeling...` (Mamba)
- `Image restoration is a long-standing and fundamental problem in low-level vision...` (HAT)
- `Multimodal large language models (MLLMs) have demonstrated remarkable capabilities...` (CogVLM2)

**Pattern templates:**

- `[Technology] has shown great promise as [capability]...`
- `With the [trend], [domain] has demonstrated [outcome]...`
- `Modern [systems] are typically [current paradigm]...`
- `[Technology] has become the de-facto standard for [task]...`

**Avoid:**

- `With the rapid development of artificial intelligence, deep learning has been widely applied in various fields.` (too generic)
- `In recent years, [topic] has attracted increasing attention.` (empty)

### 3.2 Move 2: Current Method Families

**Purpose:** Map the landscape. Show you understand the field.

**Real phrases from collected papers:**

- `Existing approaches can be broadly grouped into ...`
- `Prior work mainly falls into three categories: ...`
- `A key capability of LLMs is their ability to address new tasks via prompt engineering...` (SAM)
- `Auto-regressive transformers are pretrained on an extensive corpus of self-supervised data, followed by alignment with human preferences via techniques such as RLHF...` (Llama 2)
- `CLIP and ALIGN use contrastive learning to achieve zero-shot generalization...` (SAM)
- `Existing methods for image restoration can be broadly categorized into CNN-based and Transformer-based approaches...` (HAT)
- `Prior subquadratic sequence models include S4, S5, and RWKV...` (Mamba)
- `Parameter-efficient fine-tuning methods have been proposed to reduce the computational burden...` (PEFT Survey)

**Pattern templates:**

- `Existing approaches can be broadly grouped into [category 1], [category 2], and [category 3].`
- `Prior work mainly falls into [N] categories: ...`
- `[Method family 1] and [method family 2] represent two mainstream paradigms for [task].`
- `[Technology] achieves [capability] through [mechanism]...`

### 3.3 Move 3: Gap Identification

**Purpose:** Name what current methods cannot do. Be specific.

**Real phrases from collected papers:**

- `Despite their progress, these approaches still struggle with ...`
- `However, they remain limited by ...`
- `High computational requirements have limited the development of [X] to a few players.` (Llama 2)
- `None of these models are suitable substitutes for closed "product" LLMs...` (Llama 2)
- `... lacks an equivalent foundation model.` (SAM)
- `Prior subquadratic models fall short of Transformers on information-dense data.` (Mamba)
- `However, existing Transformer-based methods suffer from high computational complexity...` (HAT)
- `Full fine-tuning of these models is computationally expensive and memory-intensive...` (PEFT Survey)
- `However, the quadratic complexity of self-attention limits their applicability to long sequences...` (FlashAttention)

**Pattern templates:**

- `Despite their progress, these approaches still struggle with [specific limitation].`
- `However, [model family] remains limited by [specific bottleneck].`
- `[Current paradigm] suffers from [specific problem]...`
- `[Gap statement]: [model/task] lacks [what is missing].`

**Strong gap moves observed:**

- Name the baseline explicitly: `None of these models are suitable substitutes for [X].`
- Quantify the gap: `High computational requirements have limited development to a few players.`
- State the technical root cause: `The quadratic complexity of self-attention limits...`

### 3.4 Move 4: Challenge Breakdown

**Purpose:** Decompose the problem into labeled sub-challenges. Use (C1), (C2) labels when the problem is dense.

**Real phrases from collected papers:**

- `This setting raises two major challenges: ...`
- `We identify the following key obstacles: ...`
- `This problem is particularly challenging due to ...`
- `There are three key challenges in [task]: (1) ..., (2) ..., (3) ...`
- `Two main challenges arise: first, ...; second, ...`
- `The challenge lies in [X], which requires [Y].`

**Challenge-solution pairing pattern (observed in stronger papers):**

```
Challenge (C1): [Description]
Response  (S1): [How the method addresses it]

Challenge (C2): [Description]
Response  (S2): [How the method addresses it]
```

This explicit mapping is common in method papers because it makes the logic easy to review and easy to defend.

### 3.5 Move 5: Response / Proposal

**Purpose:** Announce what the paper does. Transition from problem to solution.

**Real phrases from collected papers:**

- `To overcome these challenges, we ...`
- `Our approach addresses these issues by ...`
- `In this work, we develop and release [Name]...` (Llama 2)
- `We introduce the [Name] project: a new task, model, and dataset for [task]...` (SAM)
- `... offers an effective solution by reducing [X] while achieving comparable performance to [Y].` (PEFT Survey)
- `To address this, we propose [Name], which [mechanism]...` (DoRA)
- `In this paper, we propose [Name], a [paradigm] that [mechanism]...` (VAR)
- `We present [Name], [appositive]...` (EfficientViT, Depth Anything V2)

**Pattern templates:**

- `To [address/overcome] these [challenges/issues], we propose [Name]...`
- `In this work, we [verb] [Name], [appositive]...`
- `[Name] offers an effective solution by [mechanism]...`
- `We present [Name], [appositive with key innovation]...`

### 3.6 Move 6: Contributions

**Purpose:** List concrete, verifiable contributions. Each bullet maps to a paper section.

**Real phrases from collected papers:**

- `The main contributions of this paper are as follows:`
- `The main contributions of this paper are summarized as follows:`
- `We are releasing the following models to the general public for research and commercial use:` (Llama 2)
- `Our contributions are three-fold:`

**Contribution section patterns -- see Section 4 for detailed bullet patterns.**

### 3.7 Move 7: Paper Organization

**Purpose:** Guide the reader through the paper structure. Standard in IEEE Trans.

**Standard template:**

```
The rest of this paper is organized as follows.
Section II reviews related work.
Section III presents [system model / problem formulation / preliminaries].
Section IV describes the proposed method.
Section V [provides theoretical analysis / presents experimental results].
Section VI [presents experimental results / discusses limitations].
Section VII concludes this paper.
```

**Variations observed:**

- `The remainder of this paper is organized as follows.`
- `The rest of this paper is organized as follows. Section II introduces...`
- Some papers omit this paragraph when the paper is short (e.g., Letters).

---

## 4. Contribution Bullet Patterns

### 4.1 Strong Verbs Observed in Real Papers

**Tier 1 -- Strongest (concrete, verifiable):**

- `propose` -- `We propose [Name], which [mechanism].`
- `develop` -- `We develop and release [Name].`
- `derive` -- `We derive [theorem/formula] showing that...`
- `design` -- `We design the first [artifact] that [capability].`
- `introduce` -- `We introduce the [task/concept]...`
- `build` -- `We build [Name], the largest [artifact] to date.`
- `present` -- `We present [Name], [appositive].`
- `construct` -- `We construct a [benchmark/dataset] comprising...`

**Tier 2 -- Process-oriented:**

- `conduct` -- `We conduct [experiments/studies] across [scope].`
- `evaluate` -- `We evaluate [method] on [benchmarks].`
- `establish` -- `We establish a new baseline for [task].`
- `deploy` -- `We deploy [system] on [platform/hardware].`
- `demonstrate` -- `We demonstrate that [finding].`

**Tier 3 -- Analytical:**

- `summarize` -- `We summarize existing methods into [N] categories.`
- `systematize` -- `We systematize the literature on [topic].`
- `identify` -- `We identify [N] key challenges in [task].`
- `classify` -- `We classify [methods] into [taxonomy].`
- `reveal` -- `We reveal that [finding].`

### 4.2 Real Contribution Bullet Examples

**SAM (artifact-bound, parallel structure):**
- `Task: We introduce the promptable segmentation task...`
- `Model: We describe SAM, a promptable segmentation model...`
- `Data: We build SA-1B, the largest segmentation dataset to date...`
- `RAI: We conduct a responsible AI analysis...`

Pattern: `Label: Verb + artifact + evidence noun.`

**Llama 2 (numbered list, product-focused):**
1. `LLAMA 2, an updated version of LLAMA 1, trained on a new mix of publicly available data.`
2. `LLAMA 2-CHAT, a fine-tuned version of LLAMA 2 that is optimized for dialogue use cases.`

Pattern: `Product name + modification + key improvement.`

**PEFT Survey (review + taxonomy + experiments):**
- `We present a comprehensive analysis and review of PEFT methods...`
- `We identify the key techniques and approaches... and classify them into additive, partial, reparameterized, hybrid, and unified fine-tuning methods.`
- `We conduct extensive experiments to evaluate the effectiveness of several representative PEFT methods...`

Pattern: `Verb + scope + artifact (review/taxonomy/experiments).`

**DoRA (mechanism + benefit + scope):**
- `We propose DoRA, a PEFT method that decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning.`
- `DoRA consistently outperforms LoRA across three task categories: commonsense reasoning, visual instruction tuning, and image/video-text understanding.`

Pattern: `Method name + decomposition + benefit + scope.`

**VAR (first-claim + scaling law):**
- `For the first time, GPT-style autoregressive models surpass diffusion models in image generation quality.`
- `We discover power-law Scaling Laws in VAR transformers.`

Pattern: `First-claim + scaling law discovery.`

**UniAD (framework + philosophy + metrics):**
- `We design the first fully differentiable multi-task framework that unifies perception, prediction, and planning modules.`
- `UniAD achieves SOTA in prediction and planning -- motion: 0.71m minADE, occ: 63.4% IoU, planning: 0.31% avg.Col.`

Pattern: `Framework name + philosophy + multi-task metrics.`

**DeepSeek-V3 (architecture + scale + efficiency):**
- `DeepSeek-V3, a Mixture-of-Experts (MoE) language model with 671B total parameters and 37B activated per token.`
- `The full training required only 2.788M H800 GPU hours with no irrecoverable loss spikes or perform any rollbacks.`

Pattern: `Architecture + scale + efficiency claim.`

**HAT (mechanism + property + benchmark):**
- `We propose HAT, a hybrid attention mechanism combining channel attention and spatial attention for image restoration.`
- `HAT achieves state-of-the-art PSNR/SSIM across five SR benchmarks.`

Pattern: `Mechanism description + benchmark claim.`

### 4.3 Contribution Bullet Template

Each contribution bullet should follow this structure:

```
We [strong verb] [artifact name], [appositive or relative clause] that [mechanism/capability], [evidence clause].
```

**Evidence clause types:**

- benchmark result: `achieving X% on [benchmark].`
- scale claim: `comprising [N] [units].`
- efficiency claim: `requiring only [resource].`
- capability claim: `enabling [new capability].`

### 4.4 Contribution Anti-Patterns

**Avoid:**

| Anti-Pattern | Problem | Fix |
|---|---|---|
| `We present a novel...` | "novel" is empty praise | Delete "novel" or replace with specific mechanism |
| `We propose an innovative...` | "innovative" is self-congratulation | Let the reader judge |
| `Our method significantly improves...` | "significantly" is unquantified | `improves ... by X% on [benchmark]` |
| `We conduct comprehensive experiments...` | "comprehensive" is vague | `We evaluate on [N] benchmarks: [list]` |
| `Our approach achieves state-of-the-art...` | "state-of-the-art" without evidence | `outperforms [method] by [X] on [benchmark]` |
| `We propose a novel and innovative method...` | Double empty adjectives | Delete both; name the method |

---

## 5. Method Section Language

### 5.1 Module Motivation Phrases

**Purpose:** Explain why a module is needed before describing how it works.

**Real phrases from collected papers:**

- `To capture [property], we introduce [module]...`
- `A key challenge in [task] is [problem]. To address this, we design [module]...`
- `Since [observation], we propose [mechanism] to [goal]...`
- `The [module] is motivated by the need to [capability]...`
- `Standard [approach] fails to [capability] because [reason]. We therefore [solution]...`
- `To bridge the gap between [A] and [B], we [mechanism]...`
- `Inspired by [observation/technique], we [adaptation]...`

**Pattern templates:**

- `To [goal], we [action] [module name].`
- `Since [observation], we [action] to [goal].`
- `[Current approach] fails to [capability] because [reason]. We therefore [solution].`

### 5.2 Mathematical Formulation Phrases

**Purpose:** Introduce notation, define problems, state assumptions.

**Real phrases from collected papers:**

**Notation introduction:**
- `Let [symbol] denote [meaning].`
- `We use [symbol] to represent [meaning].`
- `The input is represented as [symbol] where [description].`
- `Formally, given [input], we aim to find [output] that optimizes [objective].`

**Problem definition:**
- `The objective is to minimize [function] subject to [constraints].`
- `We formulate [task] as [optimization problem].`
- `The problem can be stated as follows:`
- `\textit{Problem:} Given [input], find [output] that optimizes [objective] subject to [constraints].`

**Assumption statements:**
- `We make the following assumptions:`
- `Assumption 1: [statement].`
- `Under the assumption that [condition]...`

**Equation introduction:**
- `The [process] can be expressed as:`
- `The [function] is defined as:`
- `Equation (X) [describes/models/computes]...`

### 5.3 Algorithm Description Phrases

**Purpose:** Describe procedures, pseudo-code, and computational steps.

**Real phrases from collected papers:**

- `The overall procedure is summarized in Algorithm X.`
- `Given [input], the algorithm proceeds as follows:`
- `First, we [step 1]. Then, we [step 2]. Finally, we [step 3].`
- `The [process] iterates until [convergence condition].`
- `The computational complexity of [module] is O([complexity]).`
- `In practice, we [implementation detail] to [efficiency goal].`
- `We implement [mechanism] using [framework/hardware].`

**Pseudocode introduction:**
- `Algorithm X outlines the [process].`
- `The key steps of [process] are:`
- `For each [element] in [set], we [operation].`

### 5.4 Technical Advantage Phrases

**Purpose:** Explain why the proposed design is better than alternatives.

**Real phrases from collected papers:**

- `Compared with [alternative], our [module] has the advantage of [property].`
- `Unlike [baseline], which [limitation], our approach [capability].`
- `This design enables [benefit] while maintaining [property].`
- `The [module] achieves [goal] with only [resource cost].`
- `This formulation allows [capability] without [drawback].`
- `[Module] provides [benefit] at the cost of [tradeoff].`
- `A key advantage of [design] is that [property].`

**Pattern templates:**

- `Unlike [baseline], which [limitation], our [method] [capability].`
- `Compared with [alternative], our design [advantage].`
- `This [design/choice] enables [benefit] while [maintaining/achieving] [property].`

### 5.5 Section Opening with Local Objective

**Purpose:** At the beginning of a section or subsection, tell the reader what this block does.

**Real examples:**

- `This section defines the notation and assumptions used throughout the paper.`
- `We first describe the overall architecture, then detail each component.`
- `In this section, we present the proposed [Name] framework.`
- `We begin by formulating the problem, then describe our solution.`
- `The following subsections detail each module of the proposed method.`

---

## 6. Result Interpretation Patterns

### 6.1 Setting Identification

**Purpose:** Name what is being compared, on what data, under what conditions.

**Real phrases from collected papers:**

- `On dataset X, our method...`
- `Across [N] benchmark subjects, ...`
- `On real-world [domain] datasets, ...`
- `Among [N] [artifacts], ...`
- `In the [setting] setting, ...`
- `Under [condition], ...`
- `We evaluate on [benchmark 1], [benchmark 2], and [benchmark 3].`

**Prefer specific scope over generic claims:**

| Avoid | Prefer |
|---|---|
| `Extensive experiments show...` | `On 23 diverse datasets covering [domains]...` |
| `We evaluate on several benchmarks...` | `We evaluate on COCO, LVIS, and ADE20K.` |
| `Our method performs well...` | `Our method outperforms [baseline] by [X] on [benchmark].` |

### 6.2 Main Outcome Statement

**Purpose:** State the primary result with numbers.

**Real examples from collected papers:**

**SAM:**
> "SAM achieves higher mIoU on 16 of 23 datasets (up to ~47 IoU gap)."

Pattern: `[Method] [metric verb] on [N] of [M] datasets (up to [gap]).`

**Llama 2:**
> "Llama 2-Chat 7B model outperforms MPT-7B-chat on 60% of the prompts."

Pattern: `[Model] [verb] [baseline] on [percentage] of [evaluation unit].`

**PEFT Survey:**
> "ProPELT_adapter uses ~1.50% of trainable parameters but achieves optimal average performance."

Pattern: `[Method] uses [resource percentage] but achieves [performance claim].`

**HAT:**
> "HAT achieves state-of-the-art PSNR/SSIM across all five SR benchmarks."

Pattern: `[Method] achieves [metric] across [N] benchmarks.`

**VAR:**
> "VAR-d30 achieves 1.97 FID on ImageNet 256x256, surpassing diffusion models."

Pattern: `[Model] achieves [metric value] on [benchmark], surpassing [baseline class].`

### 6.3 Reason Explanation

**Purpose:** Explain why the result makes sense. Connect mechanism to outcome.

**Real examples from collected papers:**

**SAM ablation:**
> "Automatic-only data performs only ~0.5 mIoU lower than all stages combined."

Pattern: `[Variant] performs only [delta] lower than [full version].`

**Llama 2 reward model:**
> "Interestingly, GPT-4 performs better than other non-Meta reward models, despite not being trained directly nor targeting specifically this reward modeling task."

Pattern: `Interestingly, [unexpected result] despite [counter-explanation].`

**Llama 2 safety scaling:**
> "As we increase the amount of safety data in model training, the mean safety RM score improves significantly while the helpfulness counterpart remains relatively stable."

Pattern: `As we increase [variable], [primary metric] improves while [secondary metric] remains stable.`

**Common reason phrases:**

- `This gain is consistent with the role of [mechanism].`
- `The improvement likely stems from [reason].`
- `This is because [mechanism] [explains outcome].`
- `We attribute this to [reason].`
- `The result confirms that [hypothesis].`

### 6.4 Boundary Noting

**Purpose:** Acknowledge where the result holds and where it does not.

**Real examples from collected papers:**

**SAM:**
> "Ambiguity-unaware SAM (single output) still higher than RITM but lower than full SAM."

Pattern: `[Degraded variant] still [comparative] but [lower/weaker] than [full version].`

**Llama 2:**
> "Llama 2-Chat 34B has an overall win rate of more than 75% against equivalently sized Vicuna-33B and Falcon 40B models."

Pattern: `[Model] has [win rate] against [specific baselines].` (scope-qualified)

**Boundary phrases:**

- `However, the margin narrows when [condition].`
- `This advantage diminishes under [condition].`
- `The gain is most pronounced in [setting] but less so in [setting].`
- `Note that [caveat].`

### 6.5 Result Paragraph Template

A strong result paragraph follows this five-part sequence:

1. **What is being compared?** -- name methods, datasets, metrics
2. **Which setting matters?** -- specify the condition
3. **What is the main numerical pattern?** -- state the numbers
4. **Why is that pattern plausible?** -- explain the mechanism
5. **What limitation or tradeoff remains?** -- note boundaries

**Example skeleton:**

```
On [dataset], our method improves [metric] by [X] over [baseline].
This gain is consistent with [mechanism].
However, the margin narrows when [condition].
```

---

## 7. Limitation Writing Patterns

### 7.1 Specific Limitation Language

**Purpose:** Name limitations precisely. Avoid fake humility.

**Real phrases from collected papers:**

**SAM limitations (Section 8):**
- `Can miss fine structures, hallucinate small disconnected components.`
- `Boundaries not as crisp as computationally intensive "zoom-in" methods.`
- `Dedicated interactive methods outperform with many points.`
- `Heavy image encoder means not real-time overall.`
- `Text-to-mask is exploratory and not entirely robust.`

**Llama 2 limitations (explicitly listed):**
- `4k prompts do not cover real-world usage.`
- `Diversity of prompts could be a factor.`
- `Only evaluate final generation of multi-turn conversation.`
- `Human evaluation is inherently subjective and noisy.`

**General limitation phrases:**

- `The current study is limited to [scope].`
- `Our evaluation does not yet cover [domain/setting].`
- `This result should therefore be interpreted within [boundary].`
- `[Method] assumes [condition], which may not hold in [setting].`
- `A limitation of [method] is [specific technical constraint].`
- `[Method] is sensitive to [hyperparameter/condition].`

**Pattern templates:**

- `[Method] [limitation verb] [specific failure mode].`
- `A key limitation is [specific constraint].`
- `The current work does not address [specific gap].`
- `We acknowledge that [specific limitation].`

### 7.2 Future Work Phrases

**Real phrases from collected papers:**

- `An important direction for future work is [specific direction].`
- `We plan to [specific action] in future iterations.`
- `Future work will focus on [specific goal].`
- `A natural extension is to [specific direction].`
- `We leave [specific problem] for future investigation.`
- `Addressing [limitation] remains an open challenge.`

### 7.3 Limitation Anti-Patterns

**Avoid:**

| Anti-Pattern | Problem | Fix |
|---|---|---|
| `There are still some limitations.` | Empty, unspecified | Name the specific limitation |
| `Our method has some room for improvement.` | Vague | `Our method does not yet handle [specific case].` |
| `Future work will address these issues.` | Unspecific | `Future work will [specific action] to [specific goal].` |
| `Despite its limitations, our method...` | Defensive | State limitation, then move on |

---

## 8. Survey Synthesis Patterns

### 8.1 Category Comparison Phrases

**Purpose:** Compare method families on the same axes. Avoid paper-by-paper narration.

**Real phrases from collected papers:**

- `These methods share a common assumption that [assumption].`
- `The main distinction lies in whether [criterion].`
- `A recurring limitation across this family is [limitation].`
- `Compared with [category A], this category offers [benefit] at the cost of [tradeoff].`
- `Both [A] and [B] address [task], but differ in [dimension].`
- `The key difference between [A] and [B] is [dimension].`
- `Category [X] methods tend to [property], whereas category [Y] methods [property].`

**Pattern templates:**

- `[Category] methods share [common property] but differ in [dimension].`
- `Compared with [A], [B] offers [benefit] at the cost of [tradeoff].`
- `The main distinction lies in [dimension].`

### 8.2 Taxonomy Description Phrases

**Purpose:** Introduce and justify the classification scheme.

**Real phrases from collected papers:**

- `We classify [methods] into [N] categories based on [criterion].`
- `The taxonomy is organized along [dimensions].`
- `Figure X presents the proposed taxonomy.`
- `We organize the literature along two axes: [axis 1] and [axis 2].`
- `Based on [criterion], we identify [N] main paradigms: ...`
- `The classification is based on [criterion].`

### 8.3 Gap Analysis Phrases

**Purpose:** Identify what the literature has not addressed.

**Real phrases from collected papers:**

- `Despite extensive research on [topic], [gap] remains underexplored.`
- `A notable gap in the literature is [specific gap].`
- `Existing surveys cover [scope] but omit [gap].`
- `The intersection of [A] and [B] has received limited attention.`
- `Most existing work focuses on [setting], leaving [setting] largely unaddressed.`
- `While [A] has been well studied, [B] remains an open problem.`

### 8.4 Survey Contribution Patterns

**Survey papers combine taxonomy creation with empirical evaluation:**

- `We present a comprehensive analysis and review of [methods]...`
- `We identify the key techniques and approaches... and classify them into [taxonomy].`
- `We conduct extensive experiments to evaluate the effectiveness of [methods]...`
- `We summarize existing work into [N] categories and identify [M] open problems.`

**Key observation:** Strong survey contribution bullets combine taxonomy + synthesis + empirical evaluation, not just literature review.

---

## 9. Transition Patterns

### 9.1 Cause / Effect Transitions

| Transition | Usage |
|---|---|
| `because` | Direct cause (mid-sentence) |
| `therefore` | Logical consequence (sentence start) |
| `as a result` | Consequence (sentence start) |
| `thus` | Formal consequence |
| `consequently` | Strong consequence |
| `this leads to` | Mechanism-to-outcome |
| `which results in` | Relative clause consequence |
| `owing to` | Formal cause attribution |

**Real examples:**

- `Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length.` (FlashAttention)
- `Since [observation], we propose [mechanism]...`

### 9.2 Contrast Transitions

| Transition | Usage |
|---|---|
| `however` | General contrast |
| `in contrast` | Direct opposition |
| `by comparison` | Softer contrast |
| `on the other hand` | Balanced contrast |
| `conversely` | Reversed relationship |
| `nevertheless` | Concession + contrast |
| `yet` | Short, punchy contrast |
| `unlike` | Direct comparison (mid-sentence) |

**Real examples:**

- `Unlike [baseline], which [limitation], our approach [capability].`
- `However, they remain limited by [constraint].`
- `Yet [current paradigm] fails to [capability].`

### 9.3 Refinement Transitions

| Transition | Usage |
|---|---|
| `more specifically` | Narrowing scope |
| `in particular` | Highlighting a subset |
| `specifically` | Naming an instance |
| `for example` | Introducing an instance |
| `that is` | Clarification |
| `namely` | Listing specifics |

**Real examples:**

- `In particular, [specific case]...`
- `More specifically, we [detailed action]...`

### 9.4 Consequence / Implication Transitions

| Transition | Usage |
|---|---|
| `this suggests that` | Moderate evidence implication |
| `this indicates that` | Stronger evidence implication |
| `this confirms that` | Validation implication |
| `this implies that` | Logical implication |
| `accordingly` | Action consequence |
| `as a consequence` | Formal consequence |

**Real examples:**

- `This suggests that [hypothesis].`
- `The result confirms that [finding].`

### 9.5 Addition / Extension Transitions

| Transition | Usage |
|---|---|
| `furthermore` | Adding a related point |
| `moreover` | Adding a stronger point |
| `in addition` | Supplementing |
| `additionally` | Neutral addition |
| `beyond that` | Scope extension |
| `building on this` | Constructive extension |

### 9.6 Limitation / Concession Transitions

| Transition | Usage |
|---|---|
| `nevertheless` | Concession + continuation |
| `although` | Clause-level concession |
| `despite` | Prepositional concession |
| `this advantage comes with` | Tradeoff introduction |
| `at the cost of` | Explicit tradeoff |
| `however, at the expense of` | Formal tradeoff |

**Real examples:**

- `This advantage comes with [tradeoff].`
- `Despite [concession], [main claim].`

### 9.7 Transition Usage Rules

1. **Use sparingly.** Not every sentence needs a transition word.
2. **Only when the logical relation is real.** Do not use `however` if there is no contrast.
3. **Vary the transitions.** Do not start three consecutive sentences with `Moreover`.
4. **Prefer mid-sentence integration** over sentence-start placement when possible.

---

## 10. Anti-AI Patterns

### 10.1 Patterns to Avoid

These patterns are hallmarks of AI-generated academic text. IEEE Trans reviewers increasingly recognize them.

**Category 1: Empty Evidence Claims**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `Extensive experiments demonstrate the effectiveness of our method.` | Names no dataset, no metric, no number | `We evaluate on COCO, LVIS, and ADE20K. Our method outperforms SAM by 2.1 mIoU on ADE20K.` |
| `Experimental results show promising performance.` | "Promising" is empty | `Our method achieves 51.4% AP on COCO test-dev at 161 FPS.` |
| `Our method achieves state-of-the-art results.` | No evidence | `HAT achieves state-of-the-art PSNR/SSIM across all five SR benchmarks.` |

**Category 2: Generic Superiority Claims**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `Our method achieves state-of-the-art performance across all benchmarks.` | Unspecific | `Our method outperforms DINO by 2.1 AP on COCO and by 1.8 AP on LVIS.` |
| `Significantly improves performance.` | "Significantly" is unquantified | `Improves MAE by 15% under noise level sigma=25.` |
| `Generalizes well.` | "Well" is meaningless | `Retains performance within 2% of in-distribution across three OOD datasets.` |

**Category 3: Template Openings**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `In this paper, we propose a novel framework for...` | "In this paper" is filler; "novel" is empty | `We propose FlashAttention, an IO-aware exact attention algorithm.` |
| `Despite significant progress in deep learning, [task] remains challenging.` | Generic throat-clearing | `Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length.` |
| `With the rapid development of artificial intelligence...` | History lesson | `Modern autonomous driving systems are typically developed as a stack of standalone modules.` |

**Category 4: Empty Modifiers**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `novel` / `innovative` | Self-congratulation | Delete, or use `proposed` |
| `comprehensive` | Vague scope | Replace with numbers: `11M images, 1.1B masks` |
| `significant` (without number) | Unquantified | `by X%` |
| `promising` | Empty praise | State the specific result |
| `various` / `several` | Vague quantity | Name the exact count or list |
| `remarkable` | Hyperbolic | State the specific metric |

**Category 5: Template Closings**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `Experimental results show promising performance and demonstrate the potential of our approach.` | Double empty | `Our models outperform open-source chat models on most benchmarks we tested, and may be a suitable substitute for closed-source models.` |
| `In conclusion, this paper proposes... The experimental results fully demonstrate...` | Template conclusion | End with a specific insight or implication not already stated. |
| `The proposed method has broad application prospects.` | Vague future | `The method deploys on [platform] at [latency].` |

**Category 6: Forced Motivation**

| AI Pattern | Problem | Real Correction |
|---|---|---|
| `With the rapid development of artificial intelligence, deep learning has been widely applied in various fields.` | Generic history | Skip it. State the current situation directly. |
| `In recent years, [topic] has attracted increasing attention from researchers.` | Empty trend statement | `[Topic] is critical for [specific application].` |
| `It is well known that [common knowledge].` | Padding | Delete or cite a specific source. |

### 10.2 Anti-AI Checklist

Before submitting, verify:

- [ ] No `Extensive experiments` without naming datasets and metrics
- [ ] No `state-of-the-art` without citing specific comparison results
- [ ] No `In this paper` as sentence opener (delete it)
- [ ] No `Despite significant progress` as generic opening
- [ ] `Novel` appears at most once in the entire paper
- [ ] No `Comprehensive` without quantitative scope
- [ ] No `promising results` in the conclusion
- [ ] No `With the rapid development of...` forced motivation
- [ ] All datasets are named explicitly
- [ ] All comparisons cite specific methods and numbers
- [ ] All contribution bullets are specific and verifiable
- [ ] No `various` or `several` without exact counts
- [ ] No `it is well known that` without citation
- [ ] No `remarkable` or `impressive` without metric support

### 10.3 The Core Principle

**Every claim must be grounded in:**

1. A named artifact (dataset, benchmark, method, system)
2. A specific metric (mIoU, AP, FID, PSNR, MAE, latency)
3. A number (percentage, count, absolute value)
4. A scope qualifier (on what, under what condition)

If any of these four is missing, the sentence is not publication-ready.

---

## Appendix A: Verb Strength Reference

### Claim-to-Evidence Verb Calibration

| Evidence Strength | Verbs | When to Use |
|---|---|---|
| Strong (experimental proof) | `demonstrate`, `prove`, `confirm`, `establish` | Multiple benchmarks, consistent results |
| Medium (partial evidence) | `indicate`, `suggest`, `support`, `show` | Limited benchmarks or conditions |
| Weak (preliminary) | `may`, `might`, `it is possible that` | Proof-of-concept, early results |
| Theoretical | `derive`, `show`, `establish`, `prove` | Mathematical derivation |
| Process | `propose`, `design`, `develop`, `introduce`, `present` | Describing what the paper does |

### Overclaim Repair Table

| Overclaim | Repair |
|---|---|
| `significantly improves` | `improves ... by X% under [condition]` |
| `is more robust` | `maintains ... under [condition]` |
| `generalizes well` | `retains performance across [N] [datasets/settings]` |
| `validated in real-world settings` | `evaluated on [N] real-world [specific type]` |
| `outperforms all baselines` | `outperforms [specific methods] on [specific benchmarks]` |
| `achieves SOTA` | `achieves [metric] on [benchmark], surpassing [method] by [X]` |

---

## Appendix B: Sentence Length and Rhythm

### Target Metrics

- **Mean sentence length:** 18-25 words
- **Maximum sentence length:** 35 words (split if longer)
- **Standard deviation:** > 5 words (avoid monotone rhythm)

### Sentence Splitting Rules

Split when:

- A sentence has more than two subordinate clauses
- A sentence contains more than three commas
- The main verb is more than 15 words from its subject
- A single sentence tries to make two distinct claims

### Rhythm Variation

- Alternate long and short sentences
- Follow a complex sentence with a short declarative one
- Use a short sentence for emphasis after a technical passage

---

## Appendix C: Hedging Calibration

| Evidence Level | Phrases | Example |
|---|---|---|
| Proven | `demonstrates`, `confirms`, `proves` | `Theorem 1 proves convergence.` |
| Strong empirical | `shows`, `indicates` | `Table III shows a 2.1% improvement.` |
| Moderate | `suggests`, `is consistent with` | `This suggests that [hypothesis].` |
| Preliminary | `may`, `might`, `it is possible` | `This may indicate [possibility].` |
| Theoretical bound | `under Assumption X` | `Under Assumption 1, the bound holds.` |

---

## Appendix D: Real Paper Index

The patterns in this document are extracted from or validated against the following papers:

| Paper | Venue | Year | Type |
|---|---|---|---|
| Segment Anything (SAM) | TPAMI | 2023/2024 | Method + Benchmark |
| Llama 2 | Meta | 2023 | System |
| PEFT Survey | TPAMI | 2024 | Survey |
| Diffusion Models Survey | TPAMI | 2024 | Survey |
| SAM Survey | TPAMI | 2024 | Survey |
| Reasoning LLM Survey | TKDE | 2024 | Survey |
| LLM+KG Roadmap | TKDE | 2024 | Survey/Roadmap |
| Software Testing Survey | TSE | 2024 | Survey |
| HAT | TPAMI | 2024 | Method |
| MiDaS v3.1 | TPAMI | 2022 | Method |
| Latent Diffusion | CVPR | 2022 | Method |
| 3D Gaussian Splatting | SIGGRAPH/TOG | 2023 | Method |
| Depth Anything V2 | NeurIPS | 2024 | Method |
| InternLM2 | Technical Report | 2024 | System |
| Open-Sora | Technical Report | 2024/2025 | System |
| DoRA | ICML | 2024 | Method |
| EfficientViT | ICCV/CVPR | 2023/2024 | Method |
| LLaVA | NeurIPS | 2023 | Method |
| InternVL | CVPR | 2024 | Method |
| CogVLM2 | Technical Report | 2024 | System |
| MiniCPM-V/o | Technical Report | 2024/2025 | System |
| VAR | NeurIPS | 2024 | Method |
| DeepSeek-V3 | Technical Report | 2024 | System |
| Qwen3 | Technical Report | 2025 | System |
| Mamba | ICML | 2024 | Method |
| SAM 2 | Meta | 2024 | Method |
| UniAD | CVPR | 2023 | Method |
| YOLOv7 | CVPR | 2023 | Method |
| DINO | ICLR | 2023 | Method |
| FlashAttention | NeurIPS | 2022 | Infrastructure |
| ViT | ICLR | 2021 | Method |
| MMDetection | OpenMMLab | 2019 | Infrastructure |
| GLM-130B | ICLR | 2023 | System |
| Colossal-AI | ICPP | 2023 | Infrastructure |
| EVA | CVPR | 2023 | Method |
| IP-Adapter | Technical Report | 2023 | Method |
| MONAI | Technical Report | 2022 | Infrastructure |
| Megatron-LM | Technical Report | 2019 | Infrastructure |
| Ego4D | CVPR | 2022 | Benchmark |

---

## 12. Traffic Flow Prediction Expression Patterns

### 12.1 Title Patterns

**Core pattern:** `Spatial-temporal mechanism + traffic forecasting task`

- "PDFormer: Propagation Delay-Aware Dynamic Long-Range Transformer for Traffic Flow Prediction"
- "STAEformer: Spatio-Temporal Adaptive Embedding Makes Better Traffic Forecasters"
- "DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Diffusion Models"
- "D2STGNN: Decoupled Dynamic Spatial-Temporal Graph Neural Network for Traffic Forecasting"

**Keywords to include:** Spatio-Temporal, Graph, Transformer, Diffusion, Traffic Forecasting/Prediction

### 12.2 Abstract Patterns

**Opening (problem statement):**
- "Traffic flow prediction is a fundamental task in intelligent transportation systems, enabling applications such as traffic management, route planning, and congestion mitigation."
- "Accurate spatio-temporal traffic forecasting is crucial for urban computing and intelligent transportation systems."

**Challenge (what makes it hard):**
- "The key challenge lies in capturing complex spatial dependencies among road networks and temporal dynamics of traffic flows."
- "Existing methods struggle to model the propagation delay of traffic congestion across the road network."
- "Traffic data exhibits complex spatio-temporal correlations, including non-stationarity, periodic patterns, and sudden changes due to accidents or events."

**Method (what we do):**
- "We propose [Model], a [mechanism] that [key innovation] for traffic forecasting."
- "Our model consists of three components: (1) a spatial encoder that captures road network topology, (2) a temporal encoder that models traffic dynamics, and (3) a prediction head that generates multi-step forecasts."

**Results (what we achieve):**
- "Extensive experiments on four benchmark datasets (METR-LA, PEMS-BAY, PEMS04, PEMS08) demonstrate that our method achieves state-of-the-art performance, reducing MAE by X% over the best existing method."
- "Our model achieves MAE of 2.52 on METR-LA and 1.52 on PEMS-BAY for 15-minute prediction, outperforming STAEformer by 1.2% and 2.0% respectively."

### 12.3 Introduction Funnel Patterns

**Step 1 - Broad context:**
- "Traffic congestion costs the global economy billions of dollars annually and significantly impacts quality of life in urban areas."
- "Intelligent transportation systems (ITS) rely on accurate traffic prediction to optimize traffic flow and reduce congestion."

**Step 2 - Specific problem:**
- "Traffic flow prediction aims to forecast future traffic states (speed, flow, occupancy) based on historical observations from a network of sensors."
- "The task requires modeling both spatial dependencies (how traffic at one sensor affects neighboring sensors) and temporal dynamics (how traffic patterns evolve over time)."

**Step 3 - Existing approaches:**
- "Early methods rely on statistical models such as ARIMA and VAR, which assume linear relationships and struggle with complex spatio-temporal patterns."
- "Recent deep learning approaches, including graph neural networks (GNNs) and transformers, have significantly improved prediction accuracy by jointly modeling spatial and temporal dependencies."

**Step 4 - Limitations of existing work:**
- "However, existing GNN-based methods use fixed graph structures that cannot adapt to dynamic traffic conditions."
- "Transformer-based methods often employ complex attention mechanisms that are computationally expensive and may not capture the physical propagation of traffic congestion."
- "Most methods treat spatial and temporal modeling jointly, ignoring their distinct characteristics."

**Step 5 - Our approach:**
- "To address these limitations, we propose [Model], which [key innovation]."
- "Our key insight is that [insight]. Based on this insight, we design [mechanism] to [benefit]."

**Step 6 - Contributions:**
- "Our main contributions are as follows:"
- "1) We propose [contribution 1], which [benefit]."
- "2) We design [contribution 2], which [benefit]."
- "3) Extensive experiments on [datasets] demonstrate [results]."

### 12.4 Method Section Patterns

**Module motivation (problem-driven):**
- "A key limitation of existing methods is that they use fixed adjacency matrices to model spatial dependencies, which cannot capture the dynamic nature of traffic networks."
- "However, traffic congestion propagates with delays that vary across different road segments and time periods. Existing attention mechanisms fail to model this propagation delay explicitly."

**Module design (forward process):**
- "Given the input traffic data X ∈ R^{N×T×F} where N is the number of sensors, T is the time steps, and F is the feature dimension, we first apply a spatial attention module to capture inter-sensor dependencies."
- "The spatial attention computes A = softmax(QK^T/√d), where Q and K are derived from the node embeddings."
- "The output of the spatial attention is then fed into a temporal convolution module with kernel size k to capture local temporal patterns."

**Technical advantages:**
- "Our adaptive graph learning mechanism reduces MAE by 3.6% compared to fixed graph structures, particularly on long-term predictions (60-min horizon)."
- "The propagation delay-aware attention explicitly models the temporal lag in congestion propagation, which is especially beneficial for predicting traffic flow at downstream sensors."

### 12.5 Experiment Section Patterns

**Dataset description:**
- "We evaluate our method on four widely-used benchmark datasets: METR-LA (207 sensors, traffic speed), PEMS-BAY (325 sensors, traffic speed), PEMS04 (307 sensors, traffic flow), and PEMS08 (170 sensors, traffic flow). All datasets use 5-minute sampling intervals."

**Metrics description:**
- "We use three standard metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE). Lower values indicate better performance for all metrics."

**Baseline description:**
- "We compare our method with the following baselines: (1) GNN-based methods: DCRNN, STGCN, Graph WaveNet, MTGNN, AGCRN; (2) Transformer-based methods: GMAN, PDFormer, STAEformer; (3) Simple baselines: STID."

**Result description (strong):**
- "On METR-LA, our method achieves MAE of 2.52, 2.85, and 3.20 for 15-, 30-, and 60-minute horizons, outperforming the previous SOTA STAEformer by 1.2%, 0.7%, and 0.6% respectively."
- "The improvement is more pronounced on PEMS04 (3.2% MAE reduction), where the traffic flow data exhibits higher variance and non-stationarity."

**Ablation description:**
- "Removing the spatial attention module leads to a 3.6% increase in MAE (from 2.52 to 2.61), indicating that spatial dependencies are crucial for accurate prediction."
- "Without the adaptive graph learning mechanism, performance degrades by 8.8% on the 60-min horizon, suggesting that dynamic graph structure is particularly important for long-term forecasting."

**Efficiency description:**
- "Our model achieves comparable accuracy to STAEformer (MAE 2.52 vs 2.49) while being 5.2x faster in inference (4.8ms vs 25.6ms) and using 4.1x fewer parameters (3.0M vs 12.5M)."

### 12.6 Result Interpretation Patterns

**Why improvement is larger on certain datasets:**
- "The improvement is more pronounced on PEMS04 (3.2% MAE reduction) compared to METR-LA (1.2%), likely because traffic flow data exhibits stronger spatial correlations that our graph learning mechanism can exploit."

**Why long-term prediction improves more:**
- "The advantage of our method becomes more pronounced as the prediction horizon increases. While the 15-minute improvement over STAEformer is modest (1.2%), the 60-minute improvement reaches 2.5%. This is because our propagation delay-aware attention mechanism effectively captures the temporal lag in traffic congestion propagation, which becomes increasingly important for longer horizons."

**Why simple baselines are competitive:**
- "STID achieves competitive performance with only 100K parameters, suggesting that the spatio-temporal identity embeddings capture much of the predictive signal. However, our method still outperforms STID by 3.1% on PEMS04, demonstrating the value of explicit graph structure modeling for flow prediction tasks."

### 12.7 Anti-AI Patterns for Traffic Prediction

**Bad:** "Our method achieves good results on all datasets."
**Good:** "On METR-LA, our method achieves MAE of 2.52 for 15-minute prediction, outperforming STAEformer by 1.2%."

