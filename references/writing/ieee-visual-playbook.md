# IEEE Transactions Visual Playbook

> Based on systematic analysis of 115+ IEEE Transactions papers (2024--2026).
> Covers: TPAMI, TMI, TNNLS, TITS, TVCG, TASE, TMM, TSP, TWC, IoT-J, and related venues.

## Goal

Help the paper use figures and tables as proof artifacts, not decoration.
Use this guide for:

- figure planning,
- chart selection,
- caption writing,
- panel layout,
- and figure-generation requests inside the paper workflow.

---

## 1. Core Principle

**Each figure or table answers one reviewer question.**

If an artifact does not clarify a claim, remove it or merge it into a stronger artifact.

Every visual must pass this test before inclusion:

| Gate question | Pass | Fail |
|---|---|---|
| What reviewer question does this answer? | Specific question identified | "It looks nice" |
| Is the answer already in the text? | Visual adds clarity the text alone cannot | Redundant with a paragraph |
| Could a reviewer cite this figure in a rebuttal? | Yes, as evidence for or against a claim | No, purely decorative |

---

## 2. Figure Roles

### 2.1 Figure 1: Pipeline / Teaser

Figure 1 should do real work. It sets the conceptual frame for the entire paper.
Choose one role:

1. **Pipeline figure** -- shows data flow and processing stages.
2. **Teaser figure** -- demonstrates the problem and the proposed solution in one glance.
3. **Taxonomy or roadmap** -- organizes the design space.
4. **System model** -- shows architecture or deployment context.

**Real examples:**

| Paper | Figure 1 content | Role |
|---|---|---|
| SAM (Kirillov et al., TPAMI 2023) | Three interconnected components: promptable segmentation task, SAM model, data engine | Conceptual teaser |
| FlashAttention-2 (Dao, 2023) | Speed vs. sequence length benchmark on A100 | Tradeoff teaser |
| YOLOv7 (Wang et al., CVPR 2023) | Speed-accuracy Pareto plot across all YOLO variants | Tradeoff teaser |
| UniAD (Hu et al., CVPR 2023) | Full pipeline: Track, Map, Motion, Occ, Planning | Pipeline |
| Mamba (Gu & Dao, 2023) | Selective State Space architecture diagram | System model |
| Llama 2 (Touvron et al., 2023) | Training pipeline: pretraining, SFT, RLHF stages | Pipeline |
| Depth Anything V2 (Yang et al., NeurIPS 2024) | Side-by-side depth map comparisons | Qualitative teaser |
| DINOv2 (Oquab et al., 2024) | Feature visualization and downstream task grid | Capability teaser |

**Rule:** Avoid starting the paper with a decorative figure that adds no reasoning value.

### 2.2 Taxonomy / Roadmap Figures

Used in survey papers and broad-scope method papers to organize the design space.

**Real examples:**

| Paper | Taxonomy structure |
|---|---|
| PEFT Survey (Xu et al., TPAMI 2024) | 5 categories: Addition-based, Specification-based, Reparameterization-based, Selection-based, Hybrid |
| Prompt Engineering Survey (2024) | 6 categories organized by interaction pattern |
| LLM Agent Survey (2024) | Three-layer architecture: Planning, Memory, Action |
| Video Understanding Survey (2024) | Temporal modeling taxonomy: frame-level, clip-level, video-level |

**Pattern:** Top-level split by core design choice (not by chronology or author).

### 2.3 System Model Figures

Show architecture, data flow, or deployment context.

**Real examples:**

| Paper | System model content |
|---|---|
| SAM (Kirillov et al.) | Image encoder, prompt encoder, mask decoder architecture |
| Mamba (Gu & Dao) | Selective SSM block with input-dependent parameters |
| DoRA (Liu et al., ICML 2024) | Weight decomposition: magnitude + direction |
| 3D Gaussian Splatting (Kerbl et al.) | Point-based rendering pipeline |
| UniAD (Hu et al.) | End-to-end autonomous driving pipeline with task heads |

**Rule:** System model figures should show only modules that appear in the method section. Do not invent components absent from the manuscript.

### 2.4 Qualitative Comparison Panels

Show visual examples comparing the proposed method against baselines.

**Real examples:**

| Paper | Panel content |
|---|---|
| SAM | Zero-shot edge prediction across BSDS500 images |
| Depth Anything V2 | Side-by-side depth maps across diverse scenes |
| HAT (Chen et al., TPAMI 2024) | Super-resolution results on real-world images |
| DoRA | Generated images for emoji and Lego styles |
| DINO | Detection results on COCO images |

**Key rules:**
- Same crop logic and zoom scale across all compared methods.
- Proposed method in a stable position (usually last column or bottom row).
- Representative cases, not cherry-picked extremes.

### 2.5 Tradeoff Plots

Show the relationship between two competing metrics (e.g., accuracy vs. speed, quality vs. cost).

**Real examples:**

| Paper | Tradeoff axes |
|---|---|
| YOLOv7 | FPS (x-axis) vs. AP (y-axis) for all YOLO variants |
| FlashAttention | Sequence length (x-axis) vs. speed (y-axis) |
| MiDaS | Improvement (x-axis) vs. FPS (y-axis) |
| Llama 2 | Model size (x-axis) vs. benchmark score (y-axis) |
| VAR (Tian et al., NeurIPS 2024) | FID (x-axis) vs. throughput (y-axis) |

**Rule:** If the proposed method occupies the Pareto frontier, highlight the frontier explicitly.

### 2.6 Error / Failure Galleries

Show where the method fails or reaches its boundary.

**Real examples:**

| Paper | Failure type |
|---|---|
| SAM | Ambiguous object boundaries, thin structures |
| Depth Anything V2 | Reflective surfaces, transparent objects |
| Llama 2 | Multi-turn conversation memory failures |

**Rule:** Failure galleries build credibility. They show the authors understand the method's limits.

---

## 3. Chart Type by Claim

| Claim | Better visual choice | Real example |
|---|---|---|
| Quality comparison | Main benchmark table | SAM Table 3: zero-shot edge detection on BSDS500 |
| Quality vs. efficiency | Scatter plot + summary table | YOLOv7: FPS-AP Pareto plot + 6-variant table |
| Module contribution | Ablation table or bar chart | SAM Figure 13: data engine stages, data volume, encoder scaling |
| Hyperparameter sensitivity | Line plot | Llama 2 Figure 6: reward model scaling trends |
| Category breakdown | Grouped bar chart or heatmap | DeepSeek-V3: benchmark scores across English, Code, Math, Chinese |
| Dataset coverage | Summary table | SAM Table 1: geographic and income representation of SA-1B |
| Taxonomy or landscape | Layered diagram or matrix | PEFT Survey Figure 2: taxonomy tree |
| Scaling behavior | Line plot with log scale | VAR Figure 2: scaling law plots |
| Human evaluation | Bar chart with confidence intervals | Llama 2 Figure 12: win-rate across 4,000 prompts |

When a table communicates the claim more clearly than a chart, prefer the table.

### Chart Selection Decision Tree

```
Is the claim about exact numbers?
  Yes -> Use a table (benchmark, ablation, dataset stats)
  No  -> Is the claim about a trend or relationship?
    Yes -> Use a line plot or scatter plot
    No  -> Is the claim about relative proportions?
      Yes -> Use a grouped bar chart or heatmap
      No  -> Is the claim about a process or architecture?
        Yes -> Use a diagram or pipeline figure
        No  -> Reconsider whether the figure is needed
```

---

## 4. Table Roles

### 4.1 Main Comparison Table (Table I Pattern)

The most important table in the paper. Compares the proposed method against all relevant baselines on primary metrics.

**Real pattern from SAM (Table 3):**

```
Task: Zero-shot edge detection
Dataset: BSDS500
Metrics: ODS, OIS, AP
Baselines: HED, EDETR, OFNet, NKN, SAM variants
Key: SAM outperforms task-specific methods without any fine-tuning
```

**Real pattern from Llama 2 (Table 3):**

```
Task: Academic benchmarks
Metrics: MMLU, HumanEval, GSM8K, etc.
Baselines: Llama 1, GPT-3.5, Falcon, MPT, etc.
Key: Llama 2-70B competitive with GPT-3.5
```

**Structure rules:**
- Bold best results per column.
- Group baselines logically (traditional, learning-based, foundation-model).
- Include model size or complexity if relevant.
- One row for the proposed method, placed last.

### 4.2 Ablation Table (Table II Pattern)

Shows the contribution of individual components by removing or swapping them.

**Real pattern from SAM:**

```
Rows: Data engine stages (RIT -> SA -> Auto), data volume, encoder scaling
Columns: mIoU on evaluation suite
Key: Each stage contributes measurable improvement
```

**Real pattern from DoRA:**

```
Rows: LoRA, LoRA+ (with magnitude), DoRA (full decomposition)
Columns: Multiple downstream tasks
Key: Direction component is the primary contributor
```

**Structure rules:**
- Each row removes exactly one component or changes one setting.
- Show delta (improvement or degradation) in parentheses or footnote.
- Include a "full model" row as the reference point.

### 4.3 Efficiency Table

Compares computational cost across methods.

**Real pattern from FlashAttention:**

```
Metrics: Memory (GB), FLOPs, wall-clock time
Settings: Sequence lengths 512, 1024, 2048, 4096
Key: Constant memory vs. quadratic for standard attention
```

**Real pattern from Llama 2 (Table 2):**

```
Metrics: GPU hours, power consumption, CO2 emissions
Models: Llama 2 7B, 13B, 70B
Key: Transparency about training cost
```

**Include:**
- FLOPs, parameters, memory footprint, inference time.
- Hardware specification (GPU type, batch size).
- Measurement protocol (warm-up runs, averaging).

### 4.4 Dataset Statistics Table

Summarizes the datasets used for training and evaluation.

**Real pattern from SAM (Table 1):**

```
Columns: Dataset, Images, Masks, Avg masks/image, Geographic coverage
Datasets: SA-1B vs. COCO vs. Open Images
Key: SA-1B is 400x larger with better geographic diversity
```

**Include:**
- Number of samples, classes, modalities.
- Train/validation/test split sizes.
- Data source and collection method.
- Any preprocessing or filtering applied.

### 4.5 Notation Table

Defines symbols used throughout the paper.

**When to include:**
- Papers with more than 15 distinct symbols.
- Papers spanning multiple technical domains.
- Papers where the same symbol could mean different things in different contexts.

**Structure:**
- Group by category (variables, functions, operators, sets).
- Include dimensionality or type where helpful.
- Reference the section where each symbol first appears.

---

## 5. Data Provenance in Figures and Tables

### 5.1 Provenance Labels

Every data point in a figure or table must have a traceable origin. Use these labels:

| Label | Meaning | Example |
|---|---|---|
| `real` | Measured from actual experiments or deployed systems | F1 score on held-out test set |
| `synthetic` | Generated by a controlled simulation or synthetic data pipeline | Results on synthetic benchmarks |
| `generated` | Produced by the proposed model itself | GELF-generated images in a qualitative panel |
| `augmented` | Real data modified by augmentation techniques | Results on augmented test sets |
| `reported` | Taken from another paper's published results | Baseline numbers from prior work |
| `reproduced` | Re-run by the authors using published code | Reproduced baseline numbers |

### 5.2 Source Attribution Requirements

For each figure or table, document:

1. **Dataset name** -- "Evaluated on COCO val2017"
2. **Evaluation scope** -- "204 benchmark subjects" or "5,000 images"
3. **Measurement method** -- "Direct measurement" vs. "Aggregated from logs" vs. "Reported in [X]"
4. **Hardware context** -- "Measured on single A100-80GB GPU"
5. **Run specification** -- "Average over 3 runs" or "Single run"

### 5.3 Scope Documentation in Captions

Add a scope clause when the data source is not obvious:

- "Results on 20 real-world applications."
- "Average performance over real-world Bitcoin datasets."
- "Evaluation on 204 benchmark subjects."
- "Qualitative examples from the COCO validation set."

### 5.4 Provenance Checklist

Before finalizing any figure or table:

- [ ] Can I trace every number to a specific experiment or source?
- [ ] Is the data label (real/synthetic/generated/reported/reproduced) explicit?
- [ ] Is the dataset name stated in the caption, footnote, or nearby text?
- [ ] Is the evaluation scope (sample count) stated?
- [ ] Is the measurement method (direct/aggregated/reported) stated?
- [ ] If numbers come from another paper, is the citation present?

---

## 6. Panel Layout Rules

### 6.1 One Visual Message Per Panel

Each panel in a multi-panel figure should convey exactly one idea.

**Bad:** A panel showing both architecture and performance curves.
**Good:** Separate panels for architecture diagram and performance curves.

### 6.2 Consistent Ordering Across Panels

If panels compare methods, use the same method ordering in every panel.

**Example from SAM qualitative comparisons:**
- Panel order: Ground Truth, SAM (Ours), ViTDet, FastSAM
- This order is preserved across all qualitative comparison figures.

### 6.3 Stable Position for Proposed Method

Place the proposed method in a consistent position across all comparison panels:

- **Last column** in horizontal layouts (most common in IEEE Trans papers).
- **Bottom row** in vertical layouts.
- **Rightmost** in paired comparisons.

### 6.4 Same Crop Logic and Zoom Scale

When showing cropped regions for detailed comparison:

- All methods must show the same crop region.
- Zoom scale must be identical.
- Crop border style (solid, dashed) must be consistent.

### 6.5 Story Ordering

If the figure tells a story across panels, order from simplest to hardest:

1. Input or problem setup.
2. Simple baseline result.
3. Progressive improvement.
4. Proposed method result.
5. Failure case or boundary.

### 6.6 Grid Layout Guidelines

| Panel count | Recommended layout | IEEE Trans column width |
|---|---|---|
| 2 | 1x2 or 2x1 | Fits single column |
| 3 | 1x3 | Fits single column |
| 4 | 2x2 | Fits single column |
| 6 | 2x3 or 3x2 | Fits full page |
| 8 | 2x4 or 4x2 | Fits full page |
| 9+ | Consider splitting into multiple figures | May exceed page limits |

### 6.7 Subfigure Labeling

Use consistent labeling: (a), (b), (c), ... in lowercase roman, no period.

Position: top-left corner of each panel, outside the image area.

Font size: same as or slightly larger than panel text.

---

## 7. IEEE Trans Visual Style

### 7.1 Safe Defaults

1. **White background** -- never use colored or dark backgrounds for charts.
2. **Restrained color palette** -- use 4--6 distinguishable colors maximum.
3. **Readable labels** -- minimum 8pt after two-column scaling (typically 6pt final print).
4. **Thin but visible lines** -- 1--1.5pt for data lines, 0.5pt for grid lines.
5. **Grayscale-safe distinctions** -- use different line styles (solid, dashed, dotted) in addition to color.
6. **Direct labeling** over legends when space permits.
7. **Serif font** for text within figures (Times New Roman or similar, matching the paper body).
8. **Consistent font family** across all figures in the paper.

### 7.2 Color Palette Recommendations

**Recommended palettes for IEEE Trans papers:**

**Palette A (6 colors, grayscale-safe):**
```
#1f77b4 (blue)
#ff7f0e (orange)
#2ca02c (green)
#d62728 (red)
#9467bd (purple)
#8c564b (brown)
```

**Palette B (4 colors, high contrast):**
```
#000000 (black)
#e66101 (orange)
#5d3a9a (purple)
#0077bb (blue)
```

**For heatmaps:**
- Use sequential colormaps (white to blue, or white to red).
- Avoid rainbow colormaps (jet, hsv).
- Ensure the colormap is perceptually uniform.

### 7.3 Things to Avoid

1. **Dark UI-style visuals** in a paper figure unless the source content requires it (e.g., showing a dark-mode interface).
2. **Neon palettes** -- they look unprofessional and fail in grayscale.
3. **Dense legends** that could be replaced with direct labels.
4. **Tiny text** that becomes unreadable in two-column print.
5. **3D bar charts** -- they distort perception; use 2D bars instead.
6. **Pie charts** -- use bar charts for better comparison.
7. **Gradient fills** -- they add visual noise without information.
8. **Drop shadows** on chart elements.
9. **Excessive grid lines** -- use light gray grids or none.
10. **Unlabeled axes** -- every axis needs a label and unit.

### 7.4 Typography in Figures

| Element | Font | Size (before scaling) | Weight |
|---|---|---|---|
| Axis labels | Times New Roman | 10--12pt | Regular |
| Tick labels | Times New Roman | 8--10pt | Regular |
| Legend text | Times New Roman | 9--10pt | Regular |
| Panel labels (a), (b) | Times New Roman | 12--14pt | Bold |
| Annotation text | Times New Roman | 9--10pt | Regular or Italic |
| Title (if used) | Times New Roman | 12pt | Bold |

### 7.5 Real Style Examples from Collected Papers

**SAM (TPAMI 2023):**
- Clean white backgrounds.
- Minimal use of color (blue for SAM results, gray for baselines).
- Direct labels on scatter plots instead of legends.
- Consistent panel labeling (a), (b), (c).

**FlashAttention (NeurIPS 2022):**
- Simple bar charts with direct value labels.
- Logarithmic x-axis for sequence length.
- Two-color scheme (blue for FlashAttention, orange for baseline).

**Llama 2 (Meta 2023):**
- Line plots with clear markers at data points.
- Confidence intervals shown as shaded regions.
- Consistent color coding across all figures.

**VAR (NeurIPS 2024):**
- Bold use of red to highlight the proposed method.
- Gray for all baselines.
- Clear axis labels with units.

---

## 8. Caption Patterns

### 8.1 Three-Part Caption Structure

Good captions do three things:

1. **Setting identification** -- what is being shown.
2. **Comparison identification** -- what is being compared.
3. **Notice guidance** -- what the reader should observe.

### 8.2 Caption Templates

**For benchmark figures:**
```
[Task] on [Dataset]. [Proposed method] achieves [key result] compared to [baselines].
```

**Example:** "Zero-shot edge detection results on BSDS500. SAM achieves ODS 0.768, outperforming task-specific methods trained on BSDS500."

**For ablation figures:**
```
Ablation results showing the contribution of [component]. [Key finding].
```

**Example:** "Ablation results showing the contribution of each data engine stage. The automatic stage (SA) provides the largest improvement (+3.2 mIoU)."

**For qualitative comparisons:**
```
Qualitative comparison of [methods] on [task/dataset]. [What to notice].
```

**Example:** "Qualitative comparison of depth estimation methods on indoor scenes. Our method produces sharper boundaries at object edges."

**For tradeoff plots:**
```
[Metric A] vs. [Metric B] for [methods]. [Proposed method] achieves [Pareto position].
```

**Example:** "Accuracy vs. inference speed for real-time detectors. YOLOv7 achieves the Pareto frontier across all speed regimes."

**For system diagrams:**
```
Architecture of [system name]. [Key design choices].
```

**Example:** "Overview of SAM architecture. The heavyweight image encoder runs once; prompts are processed by the lightweight decoder in real-time."

**For taxonomy figures:**
```
Taxonomy of [domain] grouped by [criterion].
```

**Example:** "Taxonomy of parameter-efficient fine-tuning methods grouped by adaptation strategy."

### 8.3 Scope Clauses

Add a scope clause when the data source is not obvious:

- "Results on 20 real-world applications."
- "Average performance over real-world Bitcoin datasets."
- "Evaluation on 204 benchmark subjects."
- "Qualitative examples from the COCO validation set."

### 8.4 Status Cues for Illustrative Figures

Add a status cue when the figure is not a measured result:

- "Illustrative schematic of ..."
- "Conceptual taxonomy of ..."
- "Qualitative examples from ..."

This helps reviewers distinguish measured evidence from explanatory visualization.

### 8.5 Real Caption Examples

**SAM figure captions:**
- Figure 1: "Three interconnected components: promptable segmentation task, SAM model, data engine for SA-1B."
- Figure 2: "Example SA-1B images with overlaid masks (11M images, 1.1B masks, ~100 masks/image average)."
- Figure 3: "Three valid masks from single ambiguous point prompt."
- Figure 4: "SAM overview: heavyweight image encoder, efficient prompt querying, masks at amortized real-time."
- Figure 9: "Point-to-mask evaluation (mIoU, human ratings, varying points, sampling methods)."
- Figure 13: "Ablation results: data engine stages, data volume, image encoder scaling."

**Pattern:** Setting + what is compared + key metric or observation.

**Llama 2 figure captions:**
- Figure 4: "Training of LLAMA 2-CHAT: pretraining, SFT, RLHF with iterative reward modeling."
- Figure 6: "Scaling trends for the reward model. More data and larger size improve accuracy."
- Figure 11: "Evolution of Llama 2-Chat: win-rate % compared to ChatGPT across RLHF iterations."
- Figure 12: "Human evaluation results for LLAMA 2-CHAT compared to open- and closed-source models across ~4,000 helpfulness prompts."

**Pattern:** What is measured + comparison scope + key finding.

**PEFT Survey figure captions:**
- Figure 1: "The evolutionary development of PEFT methods in recent years."
- Figure 2: "Taxonomy of Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models."
- Figure 3: "The detailed architecture of (a) Sequential Adapter, (b) Prefix-tuning, and (c) LoRA."
- Figure 4: "The 5-shot accuracy fluctuates on the MMLU dev set with the increase in evaluation steps when fine-tuning LLaMA-7B-Alpaca."

**Pattern:** What is shown + scope + key observation.

**SAM table captions:**
- Table 1: "Geographic and income representation of SA-1B compared to COCO and Open Images."
- Table 3: "Zero-shot edge detection results on BSDS500."
- Table 5: "Zero-shot instance segmentation on COCO and LVIS."

**Pattern:** Task + dataset + metric scope.

**Llama 2 table captions:**
- Table 1: "LLAMA 2 family of models."
- Table 2: "CO2 emissions during pretraining."
- Table 3: "Overall performance on grouped academic benchmarks compared to open-source base models."
- Table 6: "Statistics of human preference data for reward modeling."

**Pattern:** What is compared + scope + comparison baseline.

---

## 9. Visual Sequences by Paper Type

### 9.1 Method Papers

Recommended visual sequence:

1. **Figure 1:** Teaser or pipeline -- sets the frame.
2. **Setup/system figure** -- shows the proposed architecture.
3. **Main comparison table (Table I)** -- quantitative evidence.
4. **Qualitative comparison figure** -- visual evidence.
5. **Ablation table (Table II)** -- component contribution.
6. **Tradeoff figure** -- efficiency or Pareto analysis.
7. **Failure or limitation figure** -- honest boundary assessment.

**Real sequence: SAM (Kirillov et al., TPAMI 2023)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Figure 1: Three interconnected components | Conceptual teaser |
| 2 | Figure 2: SA-1B images with overlaid masks | Data overview |
| 3 | Figure 3: Three valid masks from single point | Task setup |
| 4 | Figure 4: SAM architecture overview | System model |
| 5 | Figures 5--7: Dataset statistics | Data analysis |
| 6 | Figure 8: 23 evaluation datasets | Evaluation dashboard |
| 7 | Figure 9: Point-to-mask evaluation | Quantitative comparison |
| 8 | Figure 10: Zero-shot edge prediction | Qualitative panel |
| 9 | Figure 11: Mask quality ratings | Tradeoff plot |
| 10 | Figure 12: Zero-shot text-to-mask | Qualitative panel |
| 11 | Figure 13: Ablation results | Ablation figure |

Key observation: SAM has 13 figures. Data analysis figures (5--7) come before experiments, establishing data credibility first.

**Real sequence: FlashAttention (Dao et al., NeurIPS 2022)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Speed-sequence length benchmark | Tradeoff plot |
| 2 | Memory comparison chart | Efficiency tradeoff |
| 3 | H100 speedup benchmark | Benchmark comparison |

Key observation: Infrastructure papers use speed and memory charts as primary visuals; no architecture diagrams needed.

**Real sequence: YOLOv7 (Wang et al., CVPR 2023)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Speed-accuracy Pareto plot | Tradeoff teaser |
| 2 | Detection demo image | Qualitative panel |
| 3 | Pose estimation demo | Qualitative panel |
| 4 | Instance segmentation demo | Qualitative panel |
| 5 | Detection performance table (6 variants) | Benchmark comparison |

Key observation: Real-time detection papers lead with speed-accuracy Pareto plot.

### 9.2 Survey Papers

Recommended visual sequence:

1. **Figure 1:** Taxonomy or roadmap -- organizes the field.
2. **Framework comparison table** -- positions related work.
3. **Category comparison matrix** -- detailed method comparison.
4. **Benchmark/dataset summary table** -- evaluation landscape.
5. **Future directions map** -- open problems.

**Real sequence: PEFT Survey (Xu et al., TPAMI 2024)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Figure 1: Evolutionary development timeline | Taxonomy timeline |
| 2 | Figure 2: Taxonomy tree (5 categories) | Taxonomy tree |
| 3 | Figure 3: Architecture comparison (3 methods) | System model |
| 4 | Figure 4: 5-shot accuracy fluctuation | Training curve |
| 5 | Tables I--II: Method comparison | Method comparison |
| 6 | Tables III--VI: Benchmark results | Benchmark comparison |
| 7 | Table VII: GPU memory usage | Efficiency comparison |

Key observation: Survey visual sequence is taxonomy, then architecture, then performance, then efficiency.

**Real sequence: LLM Agent Survey (2024)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Figure 1: Three-layer agent architecture | Taxonomy |
| 2 | Figure 2: Agent evolution timeline | History |
| 3 | Table I: Method comparison matrix | Comparison |
| 4 | Table II: Benchmark summary | Coverage |
| 5 | Figure 3: Future directions map | Roadmap |

### 9.3 Empirical Papers

Recommended visual sequence:

1. **Study workflow figure** -- shows the research methodology.
2. **Corpus or subject summary table** -- describes the data.
3. **RQ-aligned result tables** -- answers each research question.
4. **Error taxonomy or failure analysis figure** -- categorizes failures.
5. **Recommendation or implication summary matrix** -- actionable findings.

**Real sequence: UniAD (Hu et al., CVPR 2023 Best Paper)**

| Order | Figure/Table | Role |
|---|---|---|
| 1 | Pipeline architecture figure | System model |
| 2 | Stage 1 perception results table | Benchmark comparison |
| 3 | Stage 2 end-to-end results table | Benchmark comparison |
| 4 | nuScenes planning benchmark table | Benchmark comparison |
| 5 | Demo video | Qualitative panel |

Key observation: Autonomous driving papers use pipeline architecture as Figure 1; separate perception and planning evaluation tables.

---

## 10. Figure and Table Integrity Checklists

### 10.1 Figure Integrity Checklist

Before finalizing a figure, check all of the following:

**Readability:**
- [ ] Font readable after two-column scaling (minimum 6pt in final print)?
- [ ] Axis labels present and legible?
- [ ] Legend text readable without magnification?
- [ ] Panel labels (a), (b), (c) clearly visible?

**Grayscale survival:**
- [ ] All data series distinguishable in grayscale?
- [ ] Different line styles (solid, dashed, dotted) used in addition to color?
- [ ] Heatmap uses a sequential colormap that works in grayscale?
- [ ] Critical annotations visible without color?

**Content integrity:**
- [ ] Abbreviations defined on first use in the figure or caption?
- [ ] Legend smaller than the message itself?
- [ ] Caption explains what to notice?
- [ ] Figure does not introduce any fact, module, or number absent from the manuscript?
- [ ] If illustrative rather than measured, is that status made explicit?

**Technical quality:**
- [ ] Resolution at least 300 DPI for raster elements?
- [ ] Vector elements (lines, text) render cleanly at all zoom levels?
- [ ] No compression artifacts in raster images?
- [ ] File format appropriate (PDF/EPS for vector, PNG for raster)?

**Consistency:**
- [ ] Method names match those used in the text and tables?
- [ ] Color scheme consistent with other figures in the paper?
- [ ] Axis ranges appropriate (not truncated to exaggerate differences)?
- [ ] Units specified on all axes?

### 10.2 Table Integrity Checklist

Before finalizing a table, check all of the following:

**Content:**
- [ ] One main message only?
- [ ] All metric directions explicit (up-arrow for higher-is-better, down-arrow for lower-is-better)?
- [ ] Best results in bold?
- [ ] Strongest baselines included?
- [ ] Proposed method row clearly identified?

**Formatting:**
- [ ] Decimals aligned and consistent (same number of decimal places per column)?
- [ ] Column headers concise and unambiguous?
- [ ] Row labels match method names used in figures and text?
- [ ] Units specified in column headers or footnotes?

**Provenance:**
- [ ] Data source stated (dataset name, evaluation protocol)?
- [ ] Evaluation scope stated (sample count, subjects)?
- [ ] Measurement method stated (direct measurement, aggregated, reported)?
- [ ] Statistical significance indicated where appropriate?

**Caption:**
- [ ] Caption identifies the task?
- [ ] Caption identifies the dataset?
- [ ] Caption identifies the comparison scope?
- [ ] Caption is short and precise (one to two sentences)?

### 10.3 Cross-Figure Consistency Check

When the paper has multiple figures and tables:

- [ ] Method names identical across all figures, tables, and text?
- [ ] Color coding identical for the same method across all figures?
- [ ] Metric names and units consistent across all tables?
- [ ] Ordering of baselines consistent (or logically grouped)?
- [ ] No conflicting numbers between figures, tables, and text?
- [ ] Figure numbering sequential and referenced in text?
- [ ] Table numbering sequential and referenced in text?

---

## Appendix: Quick Reference

### Figure Role Selection

| If the paper needs to show... | Use this figure type |
|---|---|
| How the method works | Pipeline or system model |
| That it works better than alternatives | Qualitative comparison panel |
| How much better it works | Main benchmark table |
| Which components matter | Ablation table or bar chart |
| The design space | Taxonomy or roadmap |
| Speed vs. accuracy tradeoff | Scatter plot or Pareto plot |
| Where it fails | Error or failure gallery |
| How it scales | Scaling plot (line plot with log axis) |

### Table Role Selection

| If the paper needs to show... | Use this table type |
|---|---|
| Performance on benchmarks | Main comparison table (Table I) |
| Component contributions | Ablation table (Table II) |
| Computational cost | Efficiency table |
| Data characteristics | Dataset statistics table |
| Symbol definitions | Notation table |
| Method feature comparison | Comparison matrix |

### Caption Checklist

Before writing a caption, answer:

1. What is the setting (task, dataset, condition)?
2. What is being compared (methods, configurations)?
3. What should the reader notice (key result, trend, pattern)?
4. Is the data measured or illustrative?
5. What is the evaluation scope (sample count)?

## 13. Figure Contract (图表合同)

在写任何绘图代码之前，先建立图表合同，明确以下要素：

| 要素 | 说明 | 示例 |
|------|------|------|
| **核心结论** | 一句话，带动词 | "Our temporal attention reduces long-horizon error" |
| **图表原型** | 布局类型 | Quantitative grid / Schematic-led composite |
| **目标期刊** | 决定格式规范 | IEEE TITS (双栏, 183mm宽) |
| **最终尺寸** | 单栏/双栏 | 双栏 ~183mm |
| **面板映射** | 每个panel的内容 | (a) 趋势图 (b) 注意力热图 (c) 案例对比 |
| **证据层次** | hero/validation/controls | (a) 是hero evidence, (b)(c) 是validation |
| **统计需求** | 需要什么统计展示 | 误差条、置信区间、p值 |
| **审稿人风险** | 可能被质疑的点 | "60min结果可能被质疑统计显著性" |

**模板：**
```
Figure Contract:
- Core claim: [一句话结论]
- Prototype: [quantitative grid / schematic-led / mixed]
- Size: [single ~89mm / double ~183mm]
- Panels: (a) [内容] (b) [内容] (c) [内容]
- Hero evidence: panel (a)
- Stats needed: [error bars / CI / p-values]
- Risk: [审稿人可能质疑的点]
```
