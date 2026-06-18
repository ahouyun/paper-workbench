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
