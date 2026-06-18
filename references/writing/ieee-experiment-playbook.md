# IEEE Transactions Experiment Playbook

> Based on patterns extracted from 115+ IEEE Transactions papers (2024-2026).

## Goal

Turn paper claims into a reviewer-proof experimental package.
Use this guide when the target venue is an IEEE Transactions journal and the user needs help with:

- experiment planning,
- benchmark design,
- ablation packaging,
- efficiency profiling,
- robustness testing,
- metric reporting,
- or experiment-section writing.

---

## 1. Core Principle

Every major claim must map to one experimental question, one evidence artifact, and one reporting slot.

Use this chain:

```
claim -> experiment question -> protocol -> metric -> table/figure -> conclusion sentence
```

If any link is missing, the experiment is not publication-ready.

### Applying the Chain: Worked Example

| Claim | Experiment Question | Protocol | Metric | Artifact | Conclusion |
|-------|-------------------|----------|--------|----------|------------|
| "Our method is more accurate" | Does it outperform SOTA on benchmark X? | Train on X_train, evaluate on X_test, compare 6 baselines | mAP, F1 | Table 1 | "Ours achieves 78.3 mAP, +3.2 over prior best" |
| "Our method is faster" | What is the latency-memory-quality tradeoff? | Measure at multiple resolutions on A100 | FPS, GB, PSNR | Figure 4 | "2x faster at same quality" |
| "Our design is necessary" | Does removing component Y hurt? | Remove Y, retrain, evaluate on same benchmark | mAP | Table 3 | "Removing attention drops mAP by 4.1" |
| "Our method generalizes" | Does it work on unseen distributions? | Evaluate on 5 OOD datasets without retraining | mAP per dataset | Table 5 | "Maintains >70 mAP across all OOD sets" |

---

## 2. Non-Fabrication Rule

Never invent:

- dataset size,
- benchmark subject count,
- train/val/test split,
- metric value,
- runtime,
- parameter count,
- GPU memory,
- annotation volume,
- deployment count,
- user-study size,
- or external-action evidence such as pull requests, accepted patches, or merged changes.

If the value is unknown:

1. leave it unspecified;
2. mark it as `needs evidence`;
3. or rewrite the sentence so it does not imply a nonexistent measurement.

### Safe Wording for Unknown Data

If exact numbers are not available yet, use wording like:

- `we evaluate on a set of real-world applications`
- `we compare against several strong baselines`
- `the final protocol and dataset statistics are summarized in Table X`

Do not write `we evaluate on 20 real-world applications` unless that number is already grounded in evidence.

---

## 3. Article-Type Experiment Routing

### 3.1 Method / System Papers

Minimum package:

1. Main benchmark comparison against strong baselines
2. Ablation study (component removal + replacement)
3. Efficiency analysis (params, FLOPs, memory, latency)
4. Robustness / OOD / harder-setting test
5. Qualitative case study when the task is visual or interaction-heavy

**Real example -- HAT (Chen et al., CVPR 2023 / TPAMI 2024):**
- Main: PSNR/SSIM on Set5, Set14, BSD100, Urban100, Manga109 for x2, x3, x4
- Ablation: Hybrid attention components, overlapping cross-attention, second-stage training
- Efficiency: 20.8M params, 102.4G Multi-Adds vs. SwinIR 11.9M/53.6G
- Robustness: Visual quality on hardest cases (Urban100 structural patterns)

**Real example -- EfficientViT (ICCV 2023 / CVPR 2024):**
- Main: ImageNet classification, COCO detection, ADE20K segmentation
- Ablation: Attention mechanism design choices
- Efficiency: 48.9x TensorRT speedup over SAM-ViT-H
- Robustness: Accuracy at multiple compression ratios

### 3.2 Survey / Roadmap Papers

Minimum package:

1. Taxonomy figure classifying the field
2. Synthesis table comparing method families across key dimensions
3. Benchmark / dataset coverage table showing what has been evaluated where
4. Open-problem matrix identifying gaps

These papers do not need ablations, but they do need synthesis artifacts.

**Real example -- PEFT Survey (Xu et al., TPAMI 2024):**
- Taxonomy: Additive, partial, reparameterized, hybrid methods
- Synthesis: Tables III-VI comparing across RoBERTa, T5, LLaMA
- Coverage: GLUE, WMT16, MMLU benchmarks
- Open problems: Scaling challenges, task transfer, compositionality

### 3.3 Empirical / Software Engineering Papers

Minimum package:

1. Research-question aligned results sections (RQ1, RQ2, ...)
2. Subject-system or study-corpus summary table
3. Baseline / tool comparison
4. Failure analysis or limitation analysis
5. Threats-to-validity block

**Real example structure:**
- Study Design: Subject selection, data collection, metrics
- RQ1: Effectiveness of approach X (with statistical tests)
- RQ2: Comparison with alternative Y
- RQ3: Practitioner perception (survey / interview)
- Threats to Validity: Internal, external, construct, conclusion

### 3.4 Benchmark / Dataset Papers

Minimum package:

1. Dataset construction methodology (collection, annotation, validation)
2. Task definitions with clear input/output specifications
3. Baseline results from multiple method families
4. Analysis of benchmark difficulty and discriminability
5. Comparison with existing benchmarks (coverage, size, annotation quality)

**Real example -- SA-1B (Kirillov et al., 2023):**
- Construction: 3-stage data engine (manual, semi-auto, auto)
- Task: Interactive segmentation with point/box prompts
- Baselines: SAM variants at 3 scales, prior interactive methods
- Analysis: Mask quality, annotation speed (34s -> 14s per mask), diversity (1.1B masks)

### 3.5 Critical Review Papers

Minimum package:

1. Concept-definition table or framework figure
2. Cross-discipline comparison table
3. Evidence-backed critique categories
4. Recommendation matrix

---

## 4. The Five Reviewer Questions

Good IEEE Trans experiments usually answer these five questions in order:

1. **Does the proposed idea outperform strong alternatives?**
2. **Under what datasets, tasks, or operating conditions?**
3. **Which component or design choice causes the gain?**
4. **What is the cost in parameters, memory, latency, FLOPs, or annotation burden?**
5. **Where does the method weaken, fail, or stop generalizing?**

Design the section order around those questions rather than around implementation chronology.

### Question 1: Does It Outperform?

This is the benchmark comparison table -- the single most important table in the paper.

**Requirements:**
- Include strong and recent baselines (not only easy ones)
- Use standard benchmarks recognized by the community
- Report multiple metrics (not just the one where you win)
- Bold the best result; underline second-best when helpful

**Common pitfalls:**
- Comparing only against weak or outdated baselines
- Cherry-picking the metric where your method excels
- Using different evaluation code for different methods
- Not reporting results from the original paper when reimplementing

### Question 2: Under What Conditions?

Specify the evaluation scope precisely:

- Which datasets (with sizes, domains, difficulty levels)
- Which tasks (classification, detection, segmentation, generation)
- Which settings (supervised, semi-supervised, zero-shot, few-shot)
- Which hardware (GPU model, precision, batch size for efficiency claims)

**Real example -- SAM:**
23 diverse datasets covering egocentric, microscopy, X-ray, underwater, aerial, simulation, driving, painting images -- far from the natural image training distribution.

**Real example -- Llama 2:**
8 academic benchmarks spanning code (HumanEval), commonsense (WinoGrande), world knowledge (TriviaQA), reading comprehension, math (GSM8K), MMLU, BBH, AGI Eval.

### Question 3: Which Component Causes the Gain?

This is the ablation study. See Section 6 for full details.

### Question 4: What Is the Cost?

Report efficiency explicitly. See Section 7 for full details.

### Question 5: Where Does It Weaken?

This is the robustness / failure package. See Section 8 for full details.

### Real Examples of the Five Questions Answered

**SAM (Kirillov et al., TPAMI 2023):**
1. **Outperform?** Yes -- SAM achieves higher mIoU on 16 of 23 datasets (up to ~47 IoU gap) vs. RITM.
2. **Under what conditions?** 23 diverse datasets covering egocentric, microscopy, X-ray, underwater, aerial, simulation, driving, painting images.
3. **Which component?** Ablation on data engine stages (each stage increases mIoU), data volume (1M images comparable to full dataset), encoder scaling (ViT-H > ViT-B, marginal over ViT-L).
4. **Efficiency cost?** Image encoder runs once per image; prompt decoder ~50ms in web browser on CPU.
5. **Where does it weaken?** Can miss fine structures, hallucinate small disconnected components; boundaries not as crisp as computationally intensive "zoom-in" methods.

**Llama 2 (Touvron et al., Meta 2023):**
1. **Outperform?** Yes -- Llama 2 70B is close to GPT-3.5 on MMLU (68.9 vs. 70.0) and GSM8K (56.8 vs. 57.1).
2. **Under what conditions?** 8 academic benchmarks (code, commonsense, world knowledge, reading comprehension, math, MMLU, BBH, AGI Eval).
3. **Which component?** SFT quality matters more than quantity (27,540 annotations sufficient); RLHF iterations show progressive improvement; GAtt improves multi-turn consistency.
4. **Efficiency cost?** 3.3M GPU hours total; 539 tCO2eq; Table 2 breaks down by model size.
5. **Where does it weaken?** Significant gap to GPT-4 on coding benchmarks (29.9 vs. 67.0 HumanEval); limited to English; safety testing not exhaustive.

**DeepSeek-V3 (2024):**
1. **Outperform?** Yes -- best on most benchmarks; MATH-500: 90.2 vs. 78.3 (Claude).
2. **Under what conditions?** English, Code, Math, Chinese, Multilingual; 20+ benchmarks.
3. **Which component?** Auxiliary-loss-free load balancing + Multi-Token Prediction + FP8 training.
4. **Efficiency cost?** 2.788M H800 GPU hours; 671B total / 37B activated.
5. **Where does it weaken?** MMLU: 88.5 vs. 88.6 (LLaMA 405B).

**CogVLM2 (2024):**
1. **Outperform?** Yes -- TextVQA 84.2 vs. GPT-4V 78.0; OCRbench 756 vs. 656.
2. **Under what conditions?** Image understanding (9 benchmarks) + Video understanding (3 benchmarks).
3. **Which component?** Visual experts architecture + pixel-only evaluation.
4. **Efficiency cost?** 8B params; int4 quantization for 16GB VRAM inference.
5. **Where does it weaken?** MMMU: 44.3 vs. GPT-4V 56.8.

**MiniCPM-V (2024/2025):**
1. **Outperform?** Yes -- 1.3B model outperforms Qwen3.5-0.8B with 19x fewer token cost.
2. **Under what conditions?** OpenCompass, RefCOCO, HallusionBench, MUIRBench, OCRBench.
3. **Which component?** Intra-ViT early compression + mixed 4x/16x visual token compression.
4. **Efficiency cost?** 1.3B params; deployable on iOS/Android/HarmonyOS.
5. **Where does it weaken?** Unstable speech output in omni mode.

**InternVL (CVPR 2024 Oral):**
1. **Outperform?** Yes -- InternViT-6B: 88.2% on IN-1K with 5.9B params vs. ViT-22B: 89.5% with 21.7B.
2. **Under what conditions?** Classification, segmentation, retrieval, video understanding, multimodal dialogue.
3. **Which component?** InternViT-6B vision encoder + MPO preference optimization.
4. **Efficiency cost?** Mini-InternVL: 90% performance with 5% model size.
5. **Where does it weaken?** MMMU gap to GPT-4o (62.0% vs. higher).

**Mamba (Gu & Dao, 2023 / ICML 2024):**
1. **Outperform?** Yes -- competitive with Transformers of similar size on language modeling.
2. **Under what conditions?** The Pile dataset; zero-shot evaluation on 11 tasks.
3. **Which component?** Selective state space mechanism + hardware-aware implementation.
4. **Efficiency cost?** Linear-time complexity vs. quadratic for Transformers.
5. **Where does it weaken?** SSMs are sensitive to recurrent dynamics; fp32 recommended.

**DoRA (Liu et al., ICML 2024):**
1. **Outperform?** Yes -- DoRA at rank 16 outperforms LoRA at rank 32 across all model families.
2. **Under what conditions?** Commonsense reasoning (8 benchmarks), visual instruction tuning, image/video-text understanding.
3. **Which component?** Weight decomposition into magnitude + direction; LoRA for directional updates.
4. **Efficiency cost?** No additional inference overhead; can use half the rank of LoRA.
5. **Where does it weaken?** LoRA converges faster than DoRA on diffusion models; DoRA quality superior at lower ranks.

**VAR (Tian et al., NeurIPS 2024 Best Paper):**
1. **Outperform?** Yes -- VAR-d30 achieves 1.97 FID on ImageNet 256x256, surpassing diffusion models.
2. **Under what conditions?** ImageNet 256x256 and 512x512; 50,000 images sampled for FID.
3. **Which component?** Multi-scale VQ-VAE tokenizer + next-scale prediction paradigm.
4. **Efficiency cost?** 2.0B params; training via torchrun across 8 GPUs.
5. **Where does it weaken?** Diversity trade-off with higher classifier-free guidance.

**Open-Sora (2024/2025):**
1. **Outperform?** Yes -- narrows gap with Sora from 4.52% to 0.69% on VBench.
2. **Under what conditions?** VBench automated evaluation + human preference comparison.
3. **Which component?** DiT architecture + 3D-VAE + rectified flow + score condition.
4. **Efficiency cost?** $200K training cost for 11B model; 276s for 768x768 on 8xH100.
5. **Where does it weaken?** Still 0.69% gap to Sora; limited to 129 frames.

---

## 5. Claim-to-Evidence Matrix

Build a small matrix before drafting the experiment section.

| Claim Type | Required Evidence | Typical Artifact | Real Pattern |
|------------|-------------------|------------------|--------------|
| Better performance | Benchmark table + multiple metrics + fairness note | Table | SAM: 23-dataset mIoU table; Llama 2: 8-benchmark table |
| Better efficiency | Paired quality-efficiency table or tradeoff figure | Table + Figure | EfficientViT: speedup vs. accuracy curve; PEFT: trainable params % |
| Better robustness | Stress test, OOD test, noise test, or corruption test | Table | SAM: 23 OOD datasets; Llama 2: TruthfulQA + ToxiGen |
| Better interpretability | Qualitative figure, user study, or mechanism analysis | Figure + Table | SAM: mask quality visualization; DoRA: weight decomposition visualization |
| Better generality | Multi-dataset or cross-setting evaluation | Table | PEFT: RoBERTa + T5 + LLaMA across 3 tasks; InternVL: 5 task types |
| Better methodology | Study design table + research question results | Table + RQ sections | Empirical SE papers: RQ-aligned structure |
| Lower annotation cost | Annotation time comparison + quality comparison | Table | SAM: 34s -> 14s per mask; Llama 2: 27,540 annotations sufficient |
| Better training | Training curve + convergence comparison | Figure | Llama 2: RLHF iteration progress; DoRA: convergence comparison |

### Mapping Multiple Claims

Most papers make 2-4 claims. Each claim needs its own row in the matrix.

**Example -- Method paper with 3 claims:**

| # | Claim | Evidence Needed | Artifact |
|---|-------|----------------|----------|
| 1 | Higher accuracy than SOTA | Benchmark table with 6+ baselines | Table 1 |
| 2 | Each component contributes | Ablation table (remove each module) | Table 3 |
| 3 | Works on diverse inputs | OOD evaluation on 5 datasets | Table 5 |

---

## 6. Benchmark Design

### 6.1 Baseline Selection Rules

1. Include strong and recent baselines, not only easy ones.
2. Explain why each baseline belongs in the comparison.
3. Keep data split, preprocessing, and evaluation settings fair.
4. If a baseline is omitted, say why.

**Baseline selection checklist:**
- [ ] At least one classic/foundational method (shows progress over time)
- [ ] At least one recent SOTA method (shows competitiveness)
- [ ] At least one method from a different approach family (shows breadth)
- [ ] At least one efficient/lightweight method (if efficiency matters)
- [ ] Methods evaluated under identical conditions (same data, same metrics, same hardware)

**Real baseline selection patterns:**

| Paper Type | Baseline Strategy | Example |
|------------|-------------------|---------|
| Vision method | Classic + SOTA + different family | SAM: RITM, SimpleClick, FocalClick + SAM variants |
| LLM | Scale-matched + commercial + open-source | Llama 2: Llama 1, GPT-3.5, MPT, Falcon |
| Efficiency method | Full-accuracy + lightweight + efficient | EfficientViT: SAM-ViT-H, MobileSAM, FastSAM |
| PEFT | Full fine-tuning + each PEFT family | DoRA: LoRA, LoRA+, rsLoRA, AdaLoRA |

### 6.2 Dataset Selection Rules

1. Use at least one realistic dataset or deployment setting when the claim is practical.
2. When possible, combine one standard benchmark with one harder or more realistic setting.
3. If only synthetic data are available, state the realism limits directly.

**Dataset selection checklist:**
- [ ] At least one widely-used benchmark (enables comparison with prior work)
- [ ] At least one challenging/diverse benchmark (shows robustness)
- [ ] Dataset statistics reported (size, class distribution, difficulty)
- [ ] Train/val/test split specified (or cross-validation protocol)
- [ ] Data preprocessing described (augmentation, normalization, tokenization)

**Real dataset selection patterns:**

| Paper Type | Standard Bench | Hard/Diverse Bench | Real-World Bench |
|------------|---------------|-------------------|-----------------|
| Segmentation | COCO | Cityscapes, ADE20K | Medical, satellite, industrial |
| Classification | ImageNet | ImageNet-V2, ObjectNet | Domain-specific test sets |
| NLU | GLUE, SuperGLUE | Adversarial NLI, HellaSwag | Domain-specific corpora |
| LLM | MMLU, HumanEval | GSM8K, BBH, AGI Eval | Real user queries |
| Generation | ImageNet FID | MS-COCO FID | User studies |

### 6.3 Evaluation Protocol Standards

**Metrics:**
- Use standard metrics recognized by the community
- Report multiple metrics (not just the one where you win)
- Specify metric implementation (library, version, parameters)
- For custom metrics, provide formal definition and justification

**Evaluation settings:**
- Specify hardware (GPU model, CPU, memory)
- Specify software (framework, version, precision)
- Specify batch size, number of runs, averaging method
- Specify whether results are on test set or validation set

**Fairness:**
- Use same evaluation code for all methods
- Use same data preprocessing for all methods
- Report results from original paper when available
- Note any differences in evaluation conditions

### 6.4 Real Benchmark Setups from Collected Papers

**SAM benchmark setup:**
- Datasets: 23 diverse segmentation datasets
- Metrics: mIoU (primary), boundary IoU, human study preference
- Protocol: Single point prompt, center of ground truth mask
- Hardware: NVIDIA A100 for training; web browser on CPU for inference
- Fairness: Same prompt for all methods; same evaluation code

**Llama 2 benchmark setup:**
- Benchmarks: 8 academic benchmarks (MMLU, HumanEval, GSM8K, etc.)
- Metrics: Accuracy, pass@1, exact match
- Protocol: Standard few-shot prompting (0-shot or 5-shot as specified)
- Hardware: A100-80GB for inference
- Fairness: Same prompting template; same evaluation scripts

**HAT benchmark setup:**
- Datasets: Set5, Set14, BSD100, Urban100, Manga109
- Metrics: PSNR, SSIM (on Y channel in YCbCr space)
- Protocol: Bicubic downsampling; evaluate on L channel
- Hardware: Not specified in paper
- Fairness: Same degradation model for all methods

---

## 7. Ablation Package

### 7.1 Ablation Types

**Type 1: Component Removal**
Remove one core module at a time to measure its contribution.

| Configuration | Module A | Module B | Module C | Metric |
|--------------|----------|----------|----------|--------|
| Full model | Yes | Yes | Yes | 78.3 |
| w/o A | No | Yes | Yes | 74.1 |
| w/o B | Yes | No | Yes | 76.2 |
| w/o C | Yes | Yes | No | 77.8 |

**Type 2: Component Replacement**
Replace one core module with a simpler alternative.

| Configuration | Attention Type | Metric |
|--------------|---------------|--------|
| Ours | Hybrid attention | 78.3 |
| Variant A | Self-attention only | 75.6 |
| Variant B | Cross-attention only | 76.1 |
| Variant C | Linear attention | 73.4 |

**Type 3: Hyperparameter Sensitivity**
Test one key hyperparameter or design decision.

| Value | Metric |
|-------|--------|
| r=4 | 76.1 |
| r=8 | 77.4 |
| r=16 | 78.3 |
| r=32 | 78.5 |

**Type 4: Design Choice Comparison**
Compare alternative design decisions.

| Design Choice | Metric A | Metric B |
|--------------|----------|----------|
| Option 1 (ours) | 78.3 | 45ms |
| Option 2 | 77.1 | 38ms |
| Option 3 | 76.8 | 52ms |

### 7.2 Good Ablation Habits

1. Match each ablation to one claim.
2. Keep row names interpretable (not "Variant 3" but "w/o cross-attention").
3. Avoid ten tiny ablations that answer the same question.
4. If two modules interact strongly, include one interaction ablation.
5. Report the same metrics as the main benchmark.

### 7.3 Real Ablation Examples

**SAM ablation package:**
1. **Data engine stages:** Manual -> Semi-automatic -> Automatic -> All stages. Result: each stage increases mIoU; automatic-only only ~0.5 lower than all combined.
2. **Data volume:** 0.1M -> 1M -> 11M images. Result: 0.1M has large decline; 1M comparable to full dataset.
3. **Image encoder scaling:** ViT-B -> ViT-L -> ViT-H. Result: ViT-H improves substantially over ViT-B; marginal gains over ViT-L.

Key observation: SAM's ablation answers three distinct questions: (1) annotation strategy value, (2) data scale threshold, (3) model scale diminishing returns.

**Llama 2 ablation package:**
1. **SFT data quality vs. quantity:** Millions of third-party examples vs. 27,540 high-quality annotations. Result: quality wins.
2. **RLHF algorithm:** Rejection Sampling vs. PPO vs. combined. Result: combined performs best.
3. **Safety data scaling:** 0% -> 1% -> 10% -> 25% -> 50% -> 100% safety data. Result: safety improves, helpfulness stable, false refusal ~0.05%.
4. **GAtt (Ghost Attention):** With vs. without GAtt for multi-turn consistency. Result: GAtt maintains instruction following over 20+ turns.

Key observation: Llama 2's ablation focuses on *training decisions* (data quality, algorithm choice, data mix ratio) rather than architecture components.

**DoRA ablation package:**
1. **Weight decomposition:** Full DoRA vs. LoRA vs. magnitude-only vs. direction-only.
2. **Rank scaling:** Rank 4, 8, 16, 32 for both DoRA and LoRA.
3. **Model family:** LLaMA-7B/13B/33B, LLaMA-Chat, GPT-NeoX.
4. **Task type:** Commonsense reasoning, visual instruction tuning, video understanding.

Key observation: DoRA's ablation demonstrates *consistent improvement across ranks, models, and tasks*.

**PEFT Survey ablation package:**
1. **Method category comparison:** Additive vs. partial vs. reparameterized vs. hybrid. Tables III-VI.
2. **Model scale:** RoBERTa-base vs. RoBERTa-large; T5-base vs. T5-large; LLaMA-7B vs. LLaMA-13B.
3. **Learning rate sensitivity:** Full fine-tuning performance varies dramatically (25.71% to 41.79% with different LR for LLaMA).

Key observation: Survey ablation compares *method families* across *model scales* and *training conditions*.

---

## 8. Efficiency Package

If the paper claims efficiency, report it explicitly.

### 8.1 Efficiency Metrics

| Metric | What It Measures | When to Report |
|--------|-----------------|----------------|
| Parameters (total) | Model size | Always for neural network methods |
| Parameters (trainable) | Training cost | For PEFT / transfer learning |
| FLOPs | Computational cost | When claiming efficiency |
| GPU memory | Hardware requirement | When deployment matters |
| Latency (ms) | Inference speed | When real-time matters |
| Throughput (samples/s) | Batch processing speed | When scalability matters |
| Training time | Development cost | When training efficiency matters |
| Annotation cost | Human effort | When reducing labeling burden |
| Carbon footprint | Environmental impact | For large-scale training |

### 8.2 Efficiency Reporting Patterns

**Pattern 1: Quality-Efficiency Tradeoff Curve**

Plot accuracy (y-axis) vs. cost (x-axis) for multiple methods. The Pareto frontier shows which methods are best at each cost level.

Used by: EfficientViT, MobileSAM, MiniCPM-V

**Pattern 2: Paired Quality-Efficiency Table**

| Method | Params | FLOPs | Memory | Latency | Accuracy |
|--------|--------|-------|--------|---------|----------|
| Baseline A | 100M | 50G | 8GB | 50ms | 75.0 |
| Baseline B | 50M | 25G | 4GB | 30ms | 72.1 |
| Ours | 45M | 20G | 3GB | 25ms | 76.3 |

Used by: HAT, DoRA, PEFT methods

**Pattern 3: Scaling Law Table**

| Model Size | Params | Training Cost | Metric |
|------------|--------|---------------|--------|
| Small | 7B | 184K GPU-h | 62.0 |
| Medium | 13B | 369K GPU-h | 66.5 |
| Large | 34B | 1.04M GPU-h | 69.3 |
| XLarge | 70B | 1.72M GPU-h | 71.2 |

Used by: Llama 2, DeepSeek-V3

### 8.3 Real Efficiency Reporting Examples

**SAM efficiency reporting:**
- **Inference latency:** ~50ms per prompt in web browser on CPU (prompt encoder + mask decoder).
- **Image encoder cost:** Runs once per image; cost amortized across prompts.
- **Dataset scale:** 1.1B masks, 11M images -- largest segmentation dataset (400x more masks than Open Images).
- **Annotation efficiency:** 34 -> 14 seconds per mask (6.5x faster than COCO).

Key observation: SAM separates *per-prompt cost* (fast, ~50ms) from *per-image cost* (heavy encoder, amortized). This is a common pattern for encoder-decoder architectures.

**Llama 2 efficiency reporting:**
- **Training compute:** 3.3M GPU hours total (Table 2 breaks down by model: 7B->184K, 13B->369K, 34B->1.04M, 70B->1.72M GPU hours).
- **Carbon footprint:** 539 tCO2eq total.
- **SFT data efficiency:** Only 27,540 annotations needed for high-quality SFT.
- **RLHF iteration cost:** Each PPO iteration on 70B takes ~330 seconds.
- **Context distillation:** Enables safety improvements without additional human annotation.

Key observation: System papers report *total training cost* (compute + carbon + data) and *per-iteration cost* for iterative training.

**EfficientViT efficiency reporting:**
- **Speedup:** 48.9x TensorRT speedup over SAM-ViT-H without accuracy loss.
- **Hardware:** Runs on NVIDIA Jetson (edge deployment).
- **Quality:** 1.72 FID on ImageNet 512x512.

Key observation: Efficiency methods report *relative speedup* (vs. baseline) and *absolute hardware requirements* (edge device compatibility).

**PEFT efficiency reporting:**
- **Trainable parameters:** ProPELT_adapter uses ~1.50% of trainable parameters.
- **GPU memory:** QLoRA reduces memory to 1/3 for LLaMA-7B, <1/4 for LLaMA-13B (Table VII).
- **Performance-efficiency tradeoff:** Prompt-tuning achieves smallest parameter count but worst performance (~10% below full fine-tuning).

Key observation: PEFT papers report *percentage of trainable parameters* and *absolute GPU memory* across model scales.

**MiniCPM-V efficiency reporting:**
- **Token cost:** 19x fewer tokens than Qwen3.5-0.8B for same performance.
- **Deployment:** Runs on iOS, Android, HarmonyOS.
- **Model size:** 1.3B parameters.

Key observation: Edge deployment papers report *device compatibility* and *relative cost reduction*.

### 8.4 Do Not Bury Efficiency in Prose

Bad: "Our method is efficient and can run in real-time."

Good: "Our method achieves 45 FPS on an NVIDIA A100 with batch size 1, compared to 22 FPS for the baseline (Table 4)."

---

## 9. Robustness and Failure Package

At least one of the following should appear when the claim is broad:

- OOD setting,
- noise or corruption setting,
- rare-case slice,
- scale-up or scale-down stress test,
- failure case gallery,
- error taxonomy.

IEEE Trans reviewers often trust papers more when failure boundaries are explicit.

### 9.1 OOD Testing

Evaluate on data distributions different from training.

**Real example -- SAM OOD testing:**
23 diverse datasets covering domains far from natural images: egocentric, microscopy, X-ray, underwater, aerial, simulation, driving, painting images. This demonstrates broad generalization without domain-specific fine-tuning.

**Real example -- Llama 2 OOD testing:**
Zero-shot and few-shot evaluation on 8 benchmarks spanning different knowledge domains: code, math, commonsense, world knowledge, reading comprehension. No benchmark-specific fine-tuning.

### 9.2 Noise / Corruption Testing

Evaluate under degraded input conditions.

**Common corruption types:**
- Gaussian noise (varying sigma)
- Motion blur, defocus blur
- JPEG compression artifacts
- Occlusion (random patches)
- Resolution reduction
- Lighting variation
- Weather effects (rain, fog, snow)

**Real pattern:** Report accuracy at multiple corruption severity levels (e.g., ImageNet-C severity 1-5).

### 9.3 Failure Case Gallery

Show specific examples where the method fails.

**Real example -- SAM failure cases (Section 8, Discussion):**
- "Can miss fine structures, hallucinate small disconnected components"
- "Boundaries not as crisp as computationally intensive 'zoom-in' methods"
- "Dedicated interactive methods outperform with many points"
- "Heavy image encoder -> not real-time overall"
- "Text-to-mask is exploratory and not entirely robust"
- "Domain-specific tools (e.g., ilastik) may outperform in their domains"

Key observation: SAM lists 6 specific failure modes with honest assessment. This builds reviewer trust.

**Real example -- Llama 2 failure analysis:**
Explicitly stated limitations of its own evaluation methodology:
- "4k prompts do not cover real-world usage"
- "Diversity of prompts could be a factor"
- "Only evaluate final generation of multi-turn conversation"
- "Human evaluation is inherently subjective and noisy"

Key observation: Llama 2 explicitly lists limitations of its own evaluation methodology. This is a strong trust-building move.

### 9.4 Error Taxonomy

Categorize failure modes systematically.

| Error Type | Description | Frequency | Example |
|-----------|-------------|-----------|---------|
| False positive | Incorrect detection | 12% | Background texture misclassified |
| Missed detection | Object not found | 8% | Small or occluded objects |
| Localization error | Wrong position/size | 15% | Imprecise bounding box |
| Classification error | Wrong category | 5% | Similar-looking classes |

### 9.5 Fairness and Bias Analysis

Evaluate performance across demographic or contextual groups.

**Real example -- SAM fairness analysis:**
Perceived gender, age, and skin tone evaluation (Tables 1-2) to check for performance disparities across groups.

---

## 10. Synthetic or Generated Data Guardrails

Use this section when data are synthetic, generated, augmented, or partly AI-produced.

1. State which data are real and which are generated.
2. State why generated data are necessary.
3. Show that the generated data do not trivially leak the target pattern.
4. Report whether the method is evaluated on real, synthetic, or mixed distributions.
5. If the paper claims practical value, include at least one real-world validation slice when possible.

Never hide data provenance behind generic wording such as `collected from multiple sources`.

### Required Labels for Data Provenance

When experiments involve any non-fully-real dataset, label each split or artifact as one of:

- `real`
- `synthetic`
- `generated`
- `augmented`
- `mixed`

The experiment section should make this visible in text, table notes, or setup description.

---

## 11. Statistics and Reporting

### 11.1 Metric Precision Standards

| Metric Type | Precision | Example |
|------------|-----------|---------|
| Accuracy / mAP / F1 (%) | 1 decimal | 78.3% |
| PSNR (dB) | 2 decimals | 28.45 dB |
| SSIM | 4 decimals | 0.9234 |
| FID | 2 decimals | 3.21 |
| Latency (ms) | 1 decimal or integer | 45.2 ms |
| Parameters | Millions or Billions | 45.2M or 2.0B |
| FLOPs | Giga or Tera | 50.2G or 1.5T |
| Memory (GB) | 1 decimal | 8.3 GB |

Keep metric precision consistent within a column. Mark metric direction if ambiguity is possible (e.g., "higher is better" for accuracy, "lower is better" for FID).

### 11.2 Variance Reporting

Report variance, confidence interval, or repeated-run spread when instability is relevant.

**When to report variance:**
- Results vary significantly across runs (>0.5% for accuracy metrics)
- Method involves randomness (dropout, sampling, augmentation)
- Comparing methods with small differences (<1% improvement)
- Community standard expects it (e.g., reinforcement learning)

**How to report:**
- Mean +/- std over N runs (e.g., "78.3 +/- 0.4 over 5 runs")
- 95% confidence interval (e.g., "78.3 [77.9, 78.7]")
- Min-max range (e.g., "78.3 [77.8, 78.9]")

### 11.3 Statistical Significance

When claiming improvement over baselines:
- Use appropriate statistical tests (paired t-test, Wilcoxon signed-rank)
- Report p-values (p < 0.05 is standard threshold)
- Report effect size when relevant (Cohen's d)

**Real pattern:** Many IEEE Trans papers do not report statistical tests for benchmark comparisons. However, when differences are small (<1%), statistical tests strengthen the claim.

### 11.4 Metric Order Consistency

Use the same metric order across tables and text.

**Bad:** Table 1 reports (Accuracy, F1, Precision, Recall); Table 2 reports (F1, Accuracy, Recall, Precision).

**Good:** All tables report (Accuracy, F1, Precision, Recall) in the same order.

### 11.5 Auditable Evidence Preference

Prefer evidence that a reviewer could in principle verify:

- named public datasets,
- named real-world deployments,
- explicit subject counts,
- explicit pull request or release counts,
- explicit hardware or storage settings,
- explicit baseline names.

Avoid generic phrases such as:

- `extensive experiments`
- `large-scale evaluation`
- `practical effectiveness`

unless they are immediately grounded by real scope descriptors.

---

## 12. Experiment Section Writing Template

### 12.1 Standard Ordering for Method Papers

1. **Experimental Setup**
   - Datasets (sizes, splits, preprocessing)
   - Baselines (names, versions, why selected)
   - Implementation details (framework, hardware, hyperparameters)
   - Evaluation metrics (definitions, computation)

2. **Main Results**
   - Primary benchmark table (all baselines, all metrics)
   - Secondary benchmark tables (additional datasets/tasks)
   - Analysis of results (where we win, where we lose)

3. **Ablation Studies**
   - Component removal ablation
   - Component replacement ablation (if applicable)
   - Hyperparameter sensitivity
   - Design choice comparison

4. **Efficiency Analysis**
   - Parameter count and FLOPs
   - Memory usage
   - Inference latency / throughput
   - Quality-efficiency tradeoff (if applicable)

5. **Robustness / Generalization / Failure Analysis**
   - OOD evaluation
   - Noise/corruption testing
   - Failure case gallery
   - Error taxonomy

6. **Discussion**
   - Interpretation of results
   - Limitations
   - Future work

### 12.2 Standard Ordering for Empirical Papers

1. **Study Design**
   - Research questions
   - Subject system / study corpus
   - Data collection methodology
   - Analysis methodology

2. **RQ1: [First Research Question]**
   - Motivation
   - Methodology
   - Results
   - Interpretation

3. **RQ2: [Second Research Question]**
   - (same structure)

4. **RQ3: [Third Research Question]**
   - (same structure)

5. **Threats to Validity**
   - Internal validity
   - External validity
   - Construct validity
   - Conclusion validity

6. **Discussion**
   - Implications
   - Limitations
   - Future work

### 12.3 Real Experiment Section Structures

**SAM (Kirillov et al., TPAMI 2023):**
1. Section 7: "Zero-Shot Transfer Experiments"
   - 7.1 Zero-Shot Single Point Valid Mask Evaluation (23 datasets, mIoU + human study)
   - 7.2 Zero-Shot Edge Detection (BSDS500, ODS/OIS/AP/R50)
   - 7.3 Zero-Shot Object Proposals (LVIS v1, AR@1000)
   - 7.4 Zero-Shot Instance Segmentation (COCO AP, LVIS AP)
   - 7.5 Zero-Shot Text-to-Mask (proof-of-concept)
   - 7.6 Ablations (data engine stages, data volume, encoder scaling)

Key observation: Each sub-section answers a distinct *capability question*, not just "does it work on benchmark X." Ablation comes last.

**Llama 2 (Touvron et al., Meta 2023):**
1. Section 2.3: Pretrained Model Evaluation (8 benchmarks, 4 sizes)
2. Section 3.4.1: Model-Based Evaluation (win-rate vs. ChatGPT)
3. Section 3.4.2: Human Evaluation (4,000+ prompts, 3 raters each)
4. Section 4.4: Safety Evaluation (TruthfulQA, ToxiGen)

Key observation: System papers include *both* automated benchmarks *and* human evaluations. Safety is a separate major section.

**PEFT Survey (Xu et al., TPAMI 2024):**
1. Experimental Setup (models, datasets, baselines)
2. Main Results (Tables III-VI: RoBERTa, T5, LLaMA across GLUE, WMT16, MMLU)
3. Efficiency Analysis (Table VII: GPU memory comparison)

Key observation: Survey experiments compare *method families* across *model scales* and *tasks*.

**HAT (Chen et al., CVPR 2023 / TPAMI 2024):**
1. Experimental Setup (datasets, baselines, implementation)
2. Main Results (PSNR/SSIM on 5 benchmarks, 3 scales)
3. Ablation Study (attention mechanism, cross-attention, training stages)
4. Visual Comparison (qualitative examples)

Key observation: Image restoration papers include *visual comparison* as a major section.

**DoRA (Liu et al., ICML 2024):**
1. Experimental Setup (models, datasets, baselines)
2. Main Results (commonsense reasoning, visual instruction tuning, video understanding)
3. Analysis (rank scaling, convergence, weight decomposition visualization)

Key observation: PEFT papers evaluate across *multiple model families* and *multiple task types*.

---

## 13. Output Artifacts Checklist

Before calling the experiment package complete, check for:

- [ ] One benchmark anchor table (main comparison with baselines)
- [ ] One ablation anchor table (component contribution analysis)
- [ ] One efficiency or cost artifact when relevant (params, FLOPs, latency, memory)
- [ ] One robustness or limitation artifact (OOD, failure cases, error analysis)
- [ ] One paragraph that interprets, not just restates, each main artifact
- [ ] Claim-to-evidence matrix completed (every claim mapped to evidence)
- [ ] Five reviewer questions answered (outperform? conditions? component? cost? failure?)
- [ ] Dataset and baseline selection justified (why these, why not others)
- [ ] Metric precision consistent within each table
- [ ] Fairness conditions specified (same data, same metrics, same hardware for all methods)

---

## 14. Quick Reference: Common Patterns by Paper Type

### Vision Method Paper
```
1. Setup: Datasets (COCO, ADE20K, etc.), baselines (SOTA methods), metrics (mAP, mIoU)
2. Main: Benchmark table on 2-3 datasets
3. Ablation: Component removal + hyperparameter sensitivity
4. Efficiency: Params, FLOPs, latency comparison
5. Robustness: OOD datasets or corruption testing
6. Qualitative: Visual examples (success + failure cases)
```

### LLM / NLP Paper
```
1. Setup: Benchmarks (MMLU, HumanEval, etc.), baselines (scale-matched), metrics (accuracy, pass@k)
2. Main: Multi-benchmark table (8-15 benchmarks)
3. Ablation: Training decisions (data quality, algorithm, data mix)
4. Efficiency: Training compute, GPU hours, carbon footprint
5. Safety: TruthfulQA, ToxiGen, red teaming
6. Human eval: Preference study with multiple raters
```

### PEFT / Transfer Learning Paper
```
1. Setup: Models (encoder, encoder-decoder, decoder), tasks (NLU, NLG, etc.), baselines (full FT, other PEFT)
2. Main: Cross-model cross-task comparison table
3. Ablation: Rank scaling, method variants
4. Efficiency: Trainable params %, GPU memory
5. Robustness: Cross-scale (base vs. large), cross-domain
```

### Efficiency / Edge Paper
```
1. Setup: Hardware (GPU, edge device), baselines (accuracy-matched, speed-matched), metrics (FPS, memory)
2. Main: Quality-efficiency tradeoff curve or paired table
3. Ablation: Each efficiency technique's contribution
4. Deployment: Real hardware measurements (Jetson, mobile, browser)
5. Robustness: Accuracy at multiple compression/pruning levels
```

---

## 8. Traffic Flow Prediction Experiment Package

### 8.1 Standard Experiment Structure

```
1. Setup: Datasets (METR-LA, PEMS-BAY, PEMS04, PEMS08), metrics (MAE, RMSE, MAPE), prediction horizons (15/30/60 min)
2. Main: Comparison table on all datasets with all horizons
3. Ablation: Component removal (spatial module, temporal module, graph learning, etc.)
4. Efficiency: Parameter count, FLOPs, inference time, GPU memory
5. Analysis: Long-term prediction analysis, case study, visualization
```

### 8.2 Standard Datasets

| Dataset | Sensors | Type | Region | Sampling | Standard Use |
|---------|---------|------|--------|----------|-------------|
| METR-LA | 207 | Speed | LA highways | 5min | Primary speed benchmark |
| PEMS-BAY | 325 | Speed | SF Bay Area | 5min | Secondary speed benchmark |
| PEMS04 | 307 | Flow | San Bernardino | 5min | Primary flow benchmark |
| PEMS08 | 170 | Flow | San Bernardino | 5min | Secondary flow benchmark |

### 8.3 Standard Metrics

| Metric | Formula | Direction | Precision | Notes |
|--------|---------|-----------|-----------|-------|
| MAE | (1/n)Σ|y-ŷ| | ↓ | 2 decimals | Primary metric |
| RMSE | √((1/n)Σ(y-ŷ)²) | ↓ | 2 decimals | Penalizes large errors |
| MAPE | (100/n)Σ|y-ŷ|/\|y\| | ↓ | 2 decimals (%) | Percentage-based |

### 8.4 Standard Prediction Horizons

- **15 min (3 steps)**: Short-term, most commonly reported
- **30 min (6 steps)**: Medium-term
- **60 min (12 steps)**: Long-term, tests model's ability to capture long-range dependencies

### 8.5 Standard Baselines

**GNN-based (must include at least 2):**
- DCRNN (ICLR 2018) - RNN + Graph Convolution
- STGCN (IJCAI 2018) - Convolutional + Graph Convolution
- Graph WaveNet (IJCAI 2019) - Adaptive Graph Learning
- MTGNN (KDD 2020) - Mix-hop + Adaptive Graph
- AGCRN (NeurIPS 2020) - Adaptive Graph + RNN

**Transformer-based (must include at least 1):**
- GMAN (AAAI 2020) - Spatial-Temporal Attention
- PDFormer (AAAI 2023) - Propagation Delay-Aware
- STAEformer (AAAI 2024) - Spatio-Temporal Adaptive Embedding

**Simple baselines (must include):**
- STID (ICLR 2023) - MLP + Identity Embeddings (sanity check)

### 8.6 Main Experiment Table Template

```latex
\begin{table*}[ht]
\centering
\caption{Comparison of Traffic Speed Prediction on METR-LA Dataset}
\label{tab:metr-la}
\small
\begin{tabular}{l|c|ccc|ccc|ccc}
\hline
\multirow{2}{*}{Method} & \multirow{2}{*}{Year} & \multicolumn{3}{c|}{15 min} & \multicolumn{3}{c|}{30 min} & \multicolumn{3}{c}{60 min} \\
 & & MAE↓ & RMSE↓ & MAPE↓ & MAE↓ & RMSE↓ & MAPE↓ & MAE↓ & RMSE↓ & MAPE↓ \\
\hline
DCRNN & 2018 & 2.77 & 5.38 & 7.30\% & 3.15 & 6.45 & 8.80\% & 3.60 & 7.60 & 10.50\% \\
STGCN & 2018 & 2.71 & 5.24 & 7.10\% & 3.47 & 7.24 & 9.57\% & 4.59 & 9.40 & 13.36\% \\
GWNet & 2019 & 2.69 & 5.15 & 6.90\% & 3.07 & 6.22 & 8.37\% & 3.53 & 7.37 & 10.01\% \\
\hline
Ours & -- & \textbf{2.52} & \textbf{4.85} & \textbf{6.45\%} & \textbf{2.85} & \textbf{5.60} & \textbf{7.85\%} & \textbf{3.20} & \textbf{6.35} & \textbf{9.15\%} \\
\hline
\end{tabular}
\end{table*}
```

### 8.7 Ablation Study Template

| Variant | MAE (15min) | MAE (30min) | MAE (60min) | RMSE (60min) |
|---------|-------------|-------------|-------------|--------------|
| Full Model | 2.52 | 2.85 | 3.20 | 6.35 |
| w/o Spatial Attention | 2.61 | 2.95 | 3.32 | 6.52 |
| w/o Temporal Attention | 2.65 | 3.02 | 3.40 | 6.65 |
| w/o Adaptive Graph | 2.58 | 2.93 | 3.35 | 6.55 |
| Fixed Graph (Distance) | 2.71 | 3.10 | 3.52 | 6.89 |
| Random Graph | 2.75 | 3.15 | 3.58 | 7.01 |

### 8.8 Efficiency Comparison Template

| Method | Params (M) | FLOPs (G) | Inference (ms) | GPU Memory (MB) | MAE (15min) |
|--------|-----------|-----------|----------------|-----------------|-------------|
| STGCN | 0.5 | 1.2 | 2.3 | 256 | 2.71 |
| GWNet | 0.8 | 3.5 | 8.7 | 512 | 2.69 |
| STID | 0.3 | 0.8 | 3.1 | 128 | 2.60 |
| STAEformer | 12.5 | 45.2 | 25.6 | 2048 | 2.49 |
| Ours | X.X | X.X | X.X | XXX | X.XX |

### 8.9 Real Number Ranges (for calibration)

**METR-LA Speed Prediction (mph):**
- 15min MAE: 2.49 - 3.99 (SOTA - ARIMA)
- 30min MAE: 2.78 - 4.50
- 60min MAE: 3.09 - 5.50

**PEMS-BAY Speed Prediction (mph):**
- 15min MAE: 1.30 - 1.74 (SOTA - DCRNN)
- 60min MAE: 1.84 - 2.49

**PEMS04 Flow Prediction:**
- 15min MAE: 17.35 - 21.87 (SOTA - ASTGCN)
- 60min MAE: 20.01 - 26.60

**PEMS08 Flow Prediction:**
- 15min MAE: 15.74 - 18.76 (STGCN - DCRNN)
- 60min MAE: 19.50 - 25.29

### 8.10 Common Ablation Patterns for Traffic Prediction

**Spatial module ablation:**
- Remove graph convolution → use identity graph (each node only sees itself)
- Remove attention → use average pooling
- Compare: fixed graph vs adaptive graph vs learned graph

**Temporal module ablation:**
- Remove temporal convolution → only spatial modeling
- Remove RNN → only feedforward
- Compare: different kernel sizes, different sequence lengths

**Graph learning ablation:**
- Fixed distance-based graph
- Fixed KNN graph
- Adaptive graph (Graph WaveNet style)
- Learned graph (our method)

**Prediction horizon analysis:**
- Report MAE/RMSE/MAPE at 15, 30, 45, 60 min
- Show how performance degrades with horizon
- Highlight where your method has the largest improvement

### 8.11 Visualization Patterns

**Spatial visualization:**
- Plot prediction errors on the road network map
- Color-code sensors by MAE magnitude
- Show where your method improves most vs baseline

**Temporal visualization:**
- Plot predicted vs ground truth time series for selected sensors
- Show 24-hour patterns with predicted and actual values
- Highlight peak hours and off-peak hours

**Case study:**
- Select specific time periods with interesting patterns (rush hour, accident, weather event)
- Compare predictions from different methods
- Show how your method captures the pattern better
