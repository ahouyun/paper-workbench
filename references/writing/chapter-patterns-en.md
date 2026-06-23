# 英文论文章节模式

## 通用结构

1. Abstract
2. Introduction
3. Related Work
4. Method
5. Experiments
6. Conclusion

## 每章核心要求

### Abstract
- Answer: problem → contribution → why it works → results
- No detailed steps, technical terms only

### Introduction
- Task → challenge → solution → why it works → contributions
- Never present naive solution first then describe improvement

### Related Work
- Group by technical topic, not by year
- Summarize paradigm then limitation for each topic
- End each topic clarifying your distinction

### Method
- For each module: design → motivation → technical advantages
- Pipeline figure maps to subsections
- Write module design first, then add motivation

### Experiments
- Three questions: better than baselines? which modules cause gain? how far generalizes?
- Ablation studies tied to every key claim
- Tables: caption above, no vertical lines, booktabs style

### Conclusion
- Restate problem and core idea
- Summarize strongest experimental evidence
- Add limitation paragraph (task boundaries, not implementation flaws)
- Concrete future direction

## Section Length Guide

| Section | CVPR/ECCV | NeurIPS/ICML | IEEE Trans |
|---------|-----------|--------------|------------|
| Abstract | ~150 words | ~200 words | 150-200 words |
| Introduction | ~1 page | 1-1.5 pages | 1.5-2 pages |
| Related Work | 0.5-1 page | 0.5-1 page | 1.5-2 pages |
| Method | 1.5-2 pages | 2-3 pages | 3-5 pages |
| Experiments | 2-3 pages | 3-4 pages | 4-8 pages |
| Conclusion | 0.5 page | 0.5-1 page | 1-1.5 pages |

## Real Paper Structure Examples

### SAM (Kirillov et al., TPAMI 2023)
- Abstract: 4 sentences, ~100 words
- Introduction: 8-step funnel
- Method: 3 modules (Image Encoder, Prompt Encoder, Mask Decoder)
- Experiments: 6 capability evaluations + ablations
- Conclusion: 4 sentences

### FlashAttention (Dao et al., NeurIPS 2022)
- Abstract: 4 sentences, ~80 words
- Introduction: Problem → Solutions → Gap → Contribution
- Method: 1 core algorithm with tiling + recomputation
- Experiments: Throughput, memory, training speed
- Conclusion: 5 sentences

### DINO (Zhang et al., ICLR 2023)
- Abstract: 3 sentences, ~60 words
- Introduction: Context → Improvements → Gap → Contribution
- Method: 2 key innovations (mixed query selection, look-forward twice)
- Experiments: Training schedule ablation, backbone scaling
- Conclusion: 3 sentences
