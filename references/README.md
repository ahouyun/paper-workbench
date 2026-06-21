# Paper Workbench 参考文件索引

> 统一的论文写作参考体系，覆盖交通流预测领域。

---

## 核心文件（按功能分类）

### 写作模式与表达

| 文件 | 行数 | 内容 |
|------|------|------|
| `ieee-expression-patterns.md` | 2600+ | IEEE论文表达模式，13种写作模式、好句vs坏句对比、实验描述模式 |
| `chapter-patterns-ieee.md` | 1375 | IEEE章节模式，写作顺序、漏斗结构、技术挑战写作 |
| `flexible-writing-guide.md` | 300+ | 灵活写作指南，避免模板化 |

### 创新灵感

| 文件 | 行数 | 内容 |
|------|------|------|
| `ieee-innovation-inspiration.md` | 1920+ | 39个创新方向，涵盖GNN/Transformer/Mamba/Diffusion/LLM/Neural ODE/因果推断等 |

### 实验数据

| 文件 | 行数 | 内容 |
|------|------|------|
| `ieee-real-experimental-data.md` | 1498 | 真实实验数据，METR-LA/PEMS-BAY/PEMS04/PEMS08数值 |
| `ieee-experiment-playbook.md` | 1096 | 实验设计指南，4种消融类型、效率报告 |

### 图表制作

| 文件 | 行数 | 内容 |
|------|------|------|
| `traffic-figure-patterns.md` | 3300 | 交通预测图表模式，21种可视化模式 |
| `ieee-visual-playbook.md` | 862 | IEEE视觉规范（已合并到traffic-figure-patterns.md） |

### 润色与逻辑

| 文件 | 行数 | 内容 |
|------|------|------|
| `ieee-polishing.md` | 1050 | 51条润色规则，含逻辑严谨性检查 |
| `traffic-anti-ai-writing.md` | 871 | 去AI味写作指南 |
| `traffic-logic-rigor.md` | 1419 | 逻辑严谨性指南（已合并到ieee-polishing.md） |

### 基线方法

| 文件 | 行数 | 内容 |
|------|------|------|
| `traffic-baseline-roster.md` | 502 | 交通预测基线方法库 |
| `traffic-baseline-master-index.md` | 282 | 基线方法索引 |

### 其他参考

| 文件 | 行数 | 内容 |
|------|------|------|
| `nature-writing-style.md` | 253 | Nature写作风格 |
| `nature-figure-standards.md` | 372 | Nature图表标准 |
| `nature-polishing-rules.md` | 396 | Nature润色规则 |
| `citation-management.md` | 134 | 引用管理 |
| `writer-guidelines.md` | 234 | 作者指南 |

---

## 快速导航

### 按任务查找

| 任务 | 推荐文件 |
|------|---------|
| 写摘要 | `ieee-expression-patterns.md` + `chapter-patterns-ieee.md` |
| 写引言 | `chapter-patterns-ieee.md` + `traffic-logic-rigor.md` |
| 写实验 | `ieee-experiment-playbook.md` + `ieee-real-experimental-data.md` |
| 画图表 | `traffic-figure-patterns.md` |
| 润色论文 | `ieee-polishing.md` + `traffic-anti-ai-writing.md` |
| 找创新方向 | `ieee-innovation-inspiration.md` |
| 找基线方法 | `traffic-baseline-roster.md` |

### 按数据集查找

| 数据集 | 推荐文件 |
|--------|---------|
| METR-LA | `ieee-real-experimental-data.md` |
| PEMS-BAY | `ieee-real-experimental-data.md` |
| PEMS04/08 | `ieee-real-experimental-data.md` |
| LargeST | `ieee-innovation-inspiration.md` |

---

## 文件维护

- **已合并文件**: `traffic-writing-patterns.md`, `traffic-logic-rigor.md`, `ieee-visual-playbook.md` 的内容已合并到对应主文件
- **最后更新**: 2026-06-20
- **总行数**: ~21,700行
- **涵盖论文**: 400+篇（2024-2026）
