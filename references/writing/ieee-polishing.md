# IEEE 学术润色指南

借鉴 nature-polishing 的学术润色流程，适配 IEEE Transactions 风格。

## 12 步润色流程

1. **Sentence split** — 长句拆分为 ≤30 词的句子
2. **Section ID** — 确认当前所在 Section，应用对应时态
3. **Hourglass check** — 每段是否从宽到窄（或反之），避免平面叙述
4. **Tense audit** — 检查时态一致性
5. **Sentence edit** — 逐句精修
6. **Vocabulary upgrade** — 替换模糊词汇为精确术语
7. **Template check** — 检查 AI 模板化表达
8. **Citation audit** — 检查引用完整性和格式
9. **House style** — 应用 IEEE 格式规范
10. **Overclaim detection** — 检查过度声明
11. **Proofreading** — 语法、拼写、标点
12. **Plain-text output** — 输出清洁文本

---

## 时态规范

| Section | 时态 | 示例 |
|---------|------|------|
| Abstract | 过去（方法和结果）+ 现在（意义） | "We proposed..." / "The results show..." |
| Introduction | 现在（领域现状）+ 过去（prior work） | "Research focuses on..." / "Smith proposed..." |
| Method | 现在（描述算法）+ 过去（实验设置） | "The algorithm computes..." / "We set..." |
| Results | 过去 + 量化 | "The accuracy reached 95.2%." |
| Conclusion | 现在（总结意义）+ 过去（具体结果） | "This approach provides..." / "We demonstrated..." |

---

## IEEE 写作风格

### 推荐

- 第三人称，正式语态
- 被动语态可接受（"The method was evaluated..."）
- 精确技术术语
- 数学符号一致

### 避免

| 避免 | 替代 |
|------|------|
| "novel" / "innovative" | 让读者判断，或用 "proposed" |
| "state-of-the-art" | 引用具体对比结果 |
| "it is well known that" | 引用具体文献 |
| "we propose a novel method" | "we propose [具体方法名]" |
| "significant improvement" | "X% improvement" |
| "various" / "several" | 具体数量 |
| "etc." | 列举完整或用 "including" |

---

## Hedging 校准

根据证据强度选择措辞：

| 证据强度 | 措辞 |
|----------|------|
| 强证据（实验验证） | "demonstrate", "prove", "confirm" |
| 中等证据（部分验证） | "indicate", "suggest", "support" |
| 弱证据（推测） | "may", "might", "it is possible that" |
| 理论推导 | "derive", "show", "establish" |

---

## Overclaim 检测

### 常见过度声明

- **绝对化**："always", "never", "all", "none" → 加限定条件
- **无根据因果**："A causes B"（仅相关性）→ "A is associated with B"
- **范围膨胀**："in all scenarios" → "in the tested scenarios"
- **未验证的 "first"**："this is the first work to..." → 确认文献确实没有

### 检查清单

- [ ] 每个声明都有证据支持
- [ ] 没有绝对化表达（除非数学证明）
- [ ] 因果声明有因果证据（非仅相关性）
- [ ] "first" 声明经过文献验证
- [ ] 贡献声明中的每个动词都可验证

---

## 数学表达润色

- 所有符号首次出现时定义
- 保持符号一致性（同一概念用同一符号）
- 复杂公式前有文字说明
- 算法伪代码有行号
- 定理/引理环境格式正确

---

## 图表润色

- 分辨率 ≥ 300 DPI
- 字号 ≥ 8pt（缩放后可读）
- 图 caption 在下方
- 表 caption 在上方
- 标注坐标轴单位
- 图例清晰
- 颜色考虑黑白打印（线型区分）

---

## Reusable Moves Observed in TPAMI and TKDE Papers

This section captures recurring polishing moves observed in strong papers from
`TPAMI` and `TKDE`.

### 1. Write the abstract as a compressed proof, not a trailer

Prefer this order:

1. importance of the problem;
2. concrete bottleneck in existing methods;
3. what is introduced;
4. what evidence proves the claim.

Good IEEE Trans abstracts frequently end with:

- a quantitative result,
- a benchmark coverage statement,
- or a service sentence such as `this survey summarizes...`, `this roadmap outlines...`.

Avoid ending with empty praise.

#### Real Abstract Examples as Compressed Proofs

**SAM abstract (4 moves):**
1. Importance: "We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation."
2. What is built: "SAM is designed and trained to be promptable, enabling zero-shot transfer to new image distributions and tasks."
3. Evidence scope: "We built the largest segmentation dataset to date, with over 1 billion masks on 11M licensed and privacy-respecting images."
4. Result: "Zero-shot performance is often competitive with or superior to prior fully supervised results."

**Llama 2 abstract (4 moves):**
1. What we built: "In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters."
2. Optimization target: "Our fine-tuned LLMs, called LLAMA 2-CHAT, are optimized for dialogue use cases."
3. Evidence: "Our models outperform open-source chat models on most benchmarks we tested..."
4. Scope qualification: "...based on our human evaluations for helpfulness and safety, may be a suitable substitute for closed-source models."

**PEFT Survey abstract (3 moves):**
1. Context: "With the continuous growth in number of parameters of transformer-based PLMs..."
2. Solution: "PEFT offers an effective solution by reducing the number of fine-tuning parameters and memory usage while achieving comparable performance to full fine-tuning."
3. Scope: [implied — comprehensive survey covering all major PEFT methods]

### 2. Use challenge-solution pairing in the introduction

When the setup is complex, map the problem explicitly:

- `(C1), (C2)` for challenges;
- `(S1), (S2)` for method responses.

This move is common in stronger recent method papers because it makes the logic easy to review
and easy to defend.

### 3. Make contribution bullets evidence-bound

Each contribution bullet should be traceable to later evidence:

- method contribution -> method section + benchmark table;
- theory contribution -> theorem or derivation section;
- system or dataset contribution -> deployment or statistics section;
- survey contribution -> taxonomy figure or comparison table.

If a contribution cannot be mapped forward, weaken or remove it.

### 4. Replace vague praise with measurable nouns

Prefer:

- `improves MAE by ...`
- `reduces memory usage by ...`
- `requires only ... trainable parameters`
- `covers ... hours of video`
- `deploys ... sensing devices`

Avoid:

- `remarkable`
- `significant` without scale
- `effective` without operating condition
- `novel` without substance

### 5. Open each major section with a local objective

At the beginning of a section or subsection, tell the reader what this block is doing.

Examples of section-local purposes:

- define notation and assumptions,
- isolate the optimization target,
- explain one module,
- justify one design choice,
- answer one experimental question.

This keeps dense two-column IEEE pages navigable.

### 6. Keep captions explanatory, not merely referential

Better captions usually state:

- what the figure or table compares,
- what the axes or groups mean,
- and what the reader should notice first.

Caption templates:

- `Comparison of ... under ... settings.`
- `Taxonomy of ... organized by ...`
- `Tradeoff between ... and ...`
- `Ablation results showing the effect of ...`

### 7. Results narration should answer five reviewer questions

When polishing results prose, force this sequence:

1. What is being compared?
2. Which setting matters here?
3. What is the main numerical pattern?
4. Why is that pattern plausible?
5. What limitation or tradeoff remains?

This avoids result paragraphs that only restate table entries.

#### Real Results Narration Examples

**SAM results narration (Section 7.1):**
> "SAM higher mIoU on 16 of 23 datasets (up to ~47 IoU gap). Oracle (best of 3 masks): SAM outperforms RITM on all datasets. Human study: SAM consistently rated substantially higher than RITM. SAM mean ratings: 7-9 ('object identifiable, errors small and rare'). Ambiguity-unaware SAM (single output) still higher than RITM but lower than full SAM."

**Analysis:**
1. What is compared: SAM vs. RITM
2. Setting: 23 diverse datasets, single point prompt
3. Main pattern: 16/23 datasets, up to ~47 IoU gap
4. Why plausible: Oracle analysis shows ambiguity handling helps
5. Limitation: Ambiguity-unaware variant still has gap

**Llama 2 results narration (Section 3.4.2):**
> "Llama 2-Chat models outperform open-source models by a significant margin on both single turn and multi-turn prompts. Particularly, Llama 2-Chat 7B model outperforms MPT-7B-chat on 60% of the prompts. Llama 2-Chat 34B has an overall win rate of more than 75% against equivalently sized Vicuna-33B and Falcon 40B models. The largest LLAMA 2-CHAT model is competitive with ChatGPT."

**Analysis:**
1. What is compared: Llama 2-Chat vs. open-source and closed-source models
2. Setting: 4,000+ prompts, single and multi-turn
3. Main pattern: 7B beats MPT-7B on 60%; 34B >75% vs. Vicuna/Falcon; 70B competitive with ChatGPT
4. Why plausible: Progressive improvement with model scale
5. Limitation: Explicitly stated (4 limitations listed)

### 8. Put efficiency next to quality when efficiency is part of the claim

If the paper claims the method is efficient, do not separate:

- accuracy in one place,
- memory or parameter count in another place.

Readers and reviewers should see the tradeoff immediately.

### 9. Survey papers need synthesis language, not paper-by-paper narration

When polishing survey text:

- summarize one category before listing examples;
- compare families on the same axes;
- emphasize boundaries, overlaps, and blind spots;
- reserve citations for support, not for replacing analysis.

Avoid the rhythm:

- `Paper A does ... Paper B does ... Paper C does ...`

### 9b. Critical reviews need concept-first language

For critical reviews or meta-scientific papers, the writing should:

- define the focal concept early and explicitly;
- explain how the current field uses it too loosely or inconsistently;
- compare that usage against mature adjacent disciplines;
- end with corrective recommendations, not only criticism.

Do not polish a critical review as if it were a survey of tools.

### 10. Conclusion should close the argument, not only repeat the title

A stronger IEEE Trans conclusion usually:

1. restates the precise problem;
2. summarizes the strongest evidence;
3. clarifies the practical or scientific implication;
4. names a real limitation or next-step boundary.

### 11. Figure role checklist

Before finalizing figures, check:

- Does Figure 1 explain the paper fast?
- Is there one figure for system understanding, not just result display?
- Does each result figure answer a distinct question?
- Are labels readable after column-width scaling?
- Can the figure survive grayscale printing or low-saturation display?

### 12. Table role checklist

Before finalizing tables, check:

- Is the main table the anchor of the experiment section?
- Does the ablation table isolate claims one by one?
- Are metric directions and units explicit?
- Are the strongest baselines included?
- Are missing baselines or settings explained honestly?

### 13. Version evolution papers need clear before/after framing

When polishing papers that present iterative improvements (v1 → v2 → v3):

- State the specific improvement in each version
- Use quantitative gap reduction: "reduces gap from X% → Y%"
- Include cost-efficiency claims: "achieves Z at only $W"
- Use side-by-side visual comparisons

**Real examples:**
- Depth Anything V2: "significantly outperforms V1 in fine-grained details and robustness"
- Open-Sora: "narrows the gap with Sora from 4.52% → 0.69%"
- InternLM3: "trained on only 4 trillion high-quality tokens, saving more than 75% of the training cost"

### 14. Efficiency claims need cost-benefit framing

When polishing efficiency claims, always pair:

- **Cost**: parameters, memory, latency, compute, or dollar amount
- **Benefit**: accuracy, quality, or capability gain
- **Comparison**: vs. baseline or SOTA

**Real examples:**
- HAT: "20.8M params, 102.4G Multi-Adds" (cost) + "state-of-the-art PSNR/SSIM" (benefit)
- DoRA: "no additional inference overhead" (cost) + "outperforms LoRA at rank 32" (benefit)
- Open-Sora: "$200K training cost" (cost) + "narrows gap with Sora to 0.69%" (benefit)
- EfficientViT: "48.9× TensorRT speedup" (cost) + "without sacrificing accuracy" (benefit)

### 15. Multi-modal papers need cross-task evaluation

When polishing papers that span multiple modalities or tasks:

- Evaluate on each modality/task separately
- Use consistent metrics across tasks
- Include cross-task ablations
- Show zero-shot or few-shot transfer

**Real examples:**
- DoRA: "commonsense reasoning, visual instruction tuning, and image/video-text understanding"
- LWM: "language, image, and video understanding and generation"
- MiDaS: "zero-shot cross-dataset transfer" across 6 datasets
- InternVL: classification, segmentation, retrieval, video understanding, multimodal dialogue (5 dimensions)
- CogVLM2: image understanding (9 benchmarks) + video understanding (3 benchmarks)
- MiniCPM-V: image, video, document, text, omni, audio, speech (7 dimensions)

### 16. First-claim papers need careful evidence

When polishing papers that claim "first" or "surpass":

- Verify the claim against all known baselines
- Use specific numbers: "For the first time, GPT-style autoregressive models surpass diffusion models"
- Include the comparison context: "in image generation quality on ImageNet 256×256"
- Add scaling law evidence if available

**Real examples:**
- VAR: "For the first time, GPT-style autoregressive models surpass diffusion models in image generation quality"
- DeepSeek-V3: "no irrecoverable loss spikes or perform any rollbacks" during 2.788M H800 GPU hours
- InternVL2.5-78B: "the first open-source MLLMs to achieve over 70% on the MMMU benchmark"

### 17. System papers need infrastructure details

When polishing system papers (LLM, framework, platform):

- Include hardware details: GPU type, count, memory
- Report training cost: GPU hours, dollar amount, carbon footprint
- List deployment options: frameworks, quantization, platforms
- Include reproducibility details: code, data, checkpoints

**Real examples:**
- DeepSeek-V3: "2.788M H800 GPU hours"; "671B total parameters and 37B activated per token"
- Llama 2: "3.3M GPU hours total"; "539 tCO₂eq"
- MiniCPM-V: "deployable on iOS, Android, and HarmonyOS"; "int4 quantization for 16GB VRAM"
- InternVL: "8 A100 GPUs with 80GB memory"; "training in ~1 day on a single 8-A100 node"

### 18. Efficient papers need deployment metrics

When polishing papers that claim efficiency:

- Report inference speed: tokens/s, FPS, latency
- Include memory footprint: GPU memory, model size
- List deployment targets: mobile, edge, cloud
- Compare against larger models at same capability level

**Real examples:**
- MiniCPM-V: "1.3B params"; "deployable on iOS/Android/HarmonyOS"; "19× fewer token cost"
- EfficientViT: "48.9× TensorRT speedup over SAM-ViT-H without accuracy loss"
- MiniCPM-o: "154.3 tokens/s decoding speed"; "0.6s TTFT"; "19.0 GB GPU memory"
- HAT: "20.8M params, 102.4G Multi-Adds"

### 19. Autonomous driving papers need multi-task evaluation

When polishing autonomous driving papers:

- Evaluate perception, prediction, and planning separately
- Use standard benchmarks: nuScenes, Waymo, Argoverse
- Report metrics at multiple time horizons (1s, 2s, 3s)
- Include end-to-end metrics alongside per-task metrics

**Real examples:**
- UniAD: motion: 0.71m minADE, occ: 63.4% IoU, planning: 0.31% avg.Col
- UniAD planning: L2 distance at 1s/2s/3s + collision rate at 1s/2s/3s
- Key pattern: "planning-oriented philosophy" unifies perception, prediction, and planning

### 20. Real-time detection papers need speed-accuracy Pareto

When polishing real-time detection papers:

- Lead with speed-accuracy Pareto plot (AP vs FPS)
- Report multiple model variants (tiny → extra-large)
- Include latency at different batch sizes
- Compare against both accuracy-focused and speed-focused baselines

**Real examples:**
- YOLOv7: 51.4% AP at 161 fps (YOLOv7) → 56.8% AP at 36 fps (YOLOv7-E6E)
- DINO: 49.4 AP in 12 epochs, 51.3 AP in 24 epochs
- Key pattern: "trainable bag-of-freebies" — training enhancements that don't increase inference cost

### 21. Infrastructure papers need hardware utilization metrics

When polishing infrastructure/system papers:

- Report hardware utilization: TFLOPS/GPU, MFU (Model FLOP Utilization)
- Include weak scaling (MFU vs model size) and strong scaling (MFU vs GPU count)
- Compare against baseline implementations (HuggingFace, Megatron)
- Report memory savings alongside speed improvements

**Real examples:**
- FlashAttention: "225 TFLOPs/sec per A100, equivalent to 72% model FLOPs utilization"
- Megatron-LM: "Up to 47% Model FLOP Utilization (MFU) on H100 clusters"
- Colossal-AI: "up to 2.76 times training speedup on large-scale models"
- Key pattern: Infrastructure papers prove efficiency through hardware utilization, not just algorithmic complexity

### 22. Depth estimation papers need zero-shot cross-dataset evaluation

When polishing depth estimation papers:

- Evaluate on multiple datasets without fine-tuning (zero-shot transfer)
- Report both relative depth metrics (WHDR) and absolute depth metrics (AbsRel, δ1)
- Include version evolution with quantified improvements
- Show improvement-FPS tradeoff

**Real examples:**
- MiDaS: "19% average improvement over DPTL-384 baseline at 512px"
- MiDaS version evolution: v2.0 → v2.1 (~10%) → v3.0 (~21%) → v3.1 (~28%)
- Key pattern: "Mixing Datasets for Zero-shot Cross-dataset Transfer" — train on mixture, evaluate zero-shot

### 23. Image restoration papers need multi-degradation evaluation

When polishing image restoration papers (denoising, deblurring, super-resolution):

- Evaluate across multiple degradation types and levels
- Report both full-reference metrics (PSNR, SSIM) and perceptual metrics (LPIPS, NIQE)
- Include real-world degradation results alongside synthetic benchmarks
- Show visual comparisons at critical degradation levels

**Real examples from 2024-2026 TIP papers:**
- DeepSN-Net: blind image restoration across denoising, deblurring, and deraining
- Degradation-Aware Prompted Transformer: unified medical image restoration across multiple degradation types
- Multiscale Spatial-Frequency Learning: remote sensing restoration with degradation decoupling
- Key pattern: "unified framework" that handles multiple degradation types simultaneously

### 24. Diffusion model papers need generation quality metrics

When polishing papers using diffusion models for image generation/restoration:

- Report FID, IS, precision, recall for generation tasks
- Include inference speed (steps, latency) alongside quality
- Show diversity metrics for generation tasks
- Compare against both GAN-based and diffusion-based baselines

**Real examples from 2024-2026 TIP papers:**
- VDMUFusion: diffusion-based image fusion with versatile framework
- FrDiff: framelet-based conditional diffusion for pansharpening
- Real-Scene Image Dehazing: Laplacian pyramid-based conditional diffusion
- Key pattern: diffusion models increasingly used for low-level vision tasks, not just generation

### 25. Deepfake detection papers need cross-dataset generalization

When polishing deepfake detection papers (TIFS domain):

- Evaluate on multiple forgery methods not seen during training
- Report both binary detection accuracy and forgery type classification
- Include cross-dataset evaluation (train on one, test on another)
- Show robustness to post-processing (compression, resize, noise)

**Real examples from 2024-2026 TIFS papers:**
- IDCNet: image decomposition + cross-view distillation for generalizable detection
- GenFace: large-scale fine-grained benchmark with cross appearance-edge learning
- DomainForensics: bi-directional adaptation for cross-domain detection
- Key pattern: "generalizable detection" is the primary research goal, not just accuracy on seen forgeries

### 26. Multimodal papers need modality ablation

When polishing multimodal papers (TMM domain):

- Evaluate each modality's contribution through ablation
- Report performance with missing or noisy modalities
- Include cross-modal alignment metrics
- Show modality fusion effectiveness

**Real examples from 2024-2026 TMM papers:**
- Adaptive Multimodal Graph Integration Network: multimodal sentiment analysis
- 3UR-LLM: end-to-end multimodal LLM for 3D scene understanding
- Uncertainty-Aware Audio-Visual Segmentation: dynamic fusion for multimodal alignment
- Key pattern: "modality-aware" mechanisms that adaptively weight different modalities

---

## 去AI味润色规则 (Anti-AI Polishing Rules)

### 23. 消除空洞证据声明

**Bad:** "Extensive experiments demonstrate the effectiveness of our method."
**Good:** "We evaluate on COCO, LVIS, and ADE20K. Our method outperforms SAM by 2.1 mIoU on ADE20K."
**Rule:** Every evidence claim must name the dataset and the specific result.

### 24. 消除泛化优越性声明

**Bad:** "Our method achieves state-of-the-art performance across all benchmarks."
**Good:** "Our method outperforms DINO by 2.1 AP on COCO and by 1.8 AP on LVIS."
**Rule:** Cite specific method + specific metric + specific number.

### 25. 消除"In This Paper"填充词

**Bad:** "In this paper, we propose a novel framework for..."
**Good:** "We propose FlashAttention, an IO-aware exact attention algorithm..."
**Rule:** Delete "In this paper." Start with the contribution.

### 26. 消除"Despite Significant Progress"模板开头

**Bad:** "Despite significant progress in deep learning, image segmentation remains challenging."
**Good:** "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length." (FlashAttention)
**Rule:** State the specific technical bottleneck directly.

### 27. 消除"Novel"过度使用

**Bad:** "We propose a novel and innovative approach that leverages a novel architecture..."
**Good:** "We propose DINO, which improves denoising anchor boxes for end-to-end object detection."
**Rule:** "Novel" once per paper max. Use "proposed" or "our" instead.

### 28. 消除"Comprehensive"空洞修饰

**Bad:** "We conduct comprehensive experiments and thorough analysis..."
**Good:** "We built the largest segmentation dataset to date, with over 1 billion masks on 11M images." (SAM)
**Rule:** Replace adjectives with numbers.

### 29. 消除"Promising Results"结尾

**Bad:** "Experimental results show promising performance and demonstrate the potential of our approach."
**Good:** "Our models outperform open-source chat models on most benchmarks we tested, and may be a suitable substitute for closed-source models." (Llama 2)
**Rule:** End with a specific, qualified claim.

### 30. 消除强制动机句

**Bad:** "With the rapid development of artificial intelligence, deep learning has been widely applied in various fields."
**Good:** "Modern autonomous driving systems are typically developed as a stack of standalone modules." (UniAD)
**Rule:** Skip the history lesson. State the current situation directly.

### 31. 消除模糊数据集引用

**Bad:** "Experiments on several benchmarks confirm..."
**Good:** "We evaluate on COCO, LVIS, and ADE20K."
**Rule:** Name the datasets.

### 32. 消除模板贡献声明

**Bad:** "We propose a novel method that significantly improves performance."
**Good:** "We design the first fully differentiable multi-task framework that unifies perception, prediction, and planning modules." (UniAD)
**Rule:** Each contribution bullet must be specific and verifiable.

### 33. 消除结论模板

**Bad:** "In conclusion, this paper proposes... The experimental results fully demonstrate..."
**Good:** End with a specific insight or implication that wasn't already stated.

### 规则 29: Claim-Evidence-Boundary 三要素

每个重要的科学陈述必须包含三要素，缺一不可：

| 要素 | 说明 | 示例 |
|------|------|------|
| **Claim** (主张) | 你说了什么 | "Our model outperforms existing methods." |
| **Evidence** (证据) | 什么支持它 | "On METR-LA, our model reduces MAE by 3.2%." |
| **Boundary** (边界) | 主张在哪里停止 | "This improvement is most pronounced on the 60-min horizon." |

**典型缺陷（必须避免）：**
- ❌ 有主张无证据："Our method achieves the best performance." (没给数字)
- ❌ 有数据无明确观点："MAE is 2.49 on METR-LA." (没说这意味着什么)
- ❌ 暗示无范围条件："Our model is superior." (在哪种设置下？)

**正确写法：**
- ✅ "Our model reduces MAE by 3.2% on PEMS04 (from 17.35 to 16.79), with the improvement being most pronounced on the 60-min horizon (5.1% MAE reduction), suggesting that the temporal attention module is particularly effective for long-range dependencies."

### 规则 30: 术语台账 (Terminology Ledger)

在撰写任何文本之前，先建立术语台账，确保全文一致性：

| 类别 | 正式名称 | 缩写 | 首次出现 | 备注 |
|------|----------|------|---------|------|
| 方法名 | Spatio-Temporal Adaptive Transformer | ST-AT | §1 | 不要混用"Spatiotemporal" |
| 数据集 | PEMS-BAY | - | §4.1 | 不要用"PEMS Bay Area" |
| 指标 | Mean Absolute Error | MAE | §4.2 | 全文统一 |
| 符号 | 邻接矩阵 | A | §3.1 | 不要用"A_d"或"Adj" |

**核心原则：一个东西只用一个名称。一致性优先于词汇多样性。**

### 规则 31: 过度声称控制 (Over-claim Control)

| 避免使用 | 安全替代 |
|---------|---------|
| prove | show, demonstrate |
| conclusively | strongly suggest |
| unprecedented | to our knowledge, rarely reported |
| the best | among the strongest, competitive with |
| superior | outperforms, achieves lower error |
| first | to our knowledge, among the earliest |

**证据强度分级：**
- **强**: show, demonstrate, establish, reveal, identify
- **中等**: suggest, indicate, support the view that, are consistent with
- **推测性**: may reflect, could arise from, appears to, seems likely

### 规则 32: 交付前 QA 检查清单

**内容完整性：**
- [ ] 每个 Claim 都有 Evidence 支持
- [ ] 每个 Evidence 都有 Boundary 限定
- [ ] 所有表格和图表在正文中都有引用
- [ ] 消融实验覆盖所有核心模块
- [ ] 效率对比包含参数量、FLOPs、推理时间

**一致性检查：**
- [ ] 术语台账中的所有名称全文一致
- [ ] 数值精度（小数位数）全文统一
- [ ] 表格格式（对齐、加粗规则）全文统一

**实验完整性：**
- [ ] 至少在4个标准数据集上报告结果
- [ ] 报告15/30/60分钟三个预测时域
- [ ] 包含与至少8个基线方法的对比
- [ ] 包含消融实验（至少3个组件）
- [ ] 包含可视化分析（预测曲线、注意力热图）

### 去AI味润色检查清单

- [ ] 无"Extensive experiments"空洞声明
- [ ] 无"state-of-the-art"泛化优越性
- [ ] 无"In this paper"填充词
- [ ] 无"Despite significant progress"模板开头
- [ ] "Novel"出现不超过1次
- [ ] 无"Comprehensive"空洞修饰
- [ ] 结尾无"promising results"空洞总结
- [ ] 无"With the rapid development of..."强制动机
- [ ] 所有数据集已命名
- [ ] 所有对比引用了具体方法和数字
- [ ] 贡献声明具体且可验证
