# Paper Workbench — 论文写作工作台

> 一套完整的 Claude Code 论文写作 Skill，支持 IEEE Transactions、Nature/Science/Cell 期刊风格，覆盖从文献检索到审稿回复的全流程。**专注交通流预测方向**。

---

## ✨ 功能一览

| 能力 | 说明 |
|------|------|
| 📝 **论文撰写** | 摘要/引言/方法/实验/结论，按章节结构化写作 |
| 🔍 **文献检索** | 调用 Semantic Scholar / DBLP / arXiv / CrossRef API |
| 📊 **图表制作** | 3300行图表规范 + Python模板 + LaTeX表格 |
| 🧪 **实验设计** | 4种消融类型、效率对比、鲁棒性评估 |
| 🔬 **审稿模拟** | 5个独立审稿人角色，6维度评分 |
| ✍️ **论文润色** | 51条润色规则 + 去AI味 + 逻辑严谨性检查 |
| 💡 **创新灵感** | 39个创新方向，1000+篇论文的技术洞察 |
| 📈 **真实数据** | METR-LA/PEMS-BAY/PEMS04/PEMS08 真实实验数值 |
| 🎯 **逐句学习** | 好句vs坏句对比，12种标题模式，7种写作范式 |
| 📐 **逻辑严谨** | Claim-Evidence-Boundary三要素，六段式漏斗结构 |

---

## 🆕 v2.6 新增功能（突破1000+篇论文）

### 论文覆盖（1089篇）

| 来源 | 论文数 | 时间范围 |
|------|--------|---------|
| IEEE TITS | 110+ | 2024-2026 |
| IEEE TKDE/TNNLS/TVT/TIV | 60+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 204 | 2024-2026 |
| WWW/CIKM/IJCAI/SIGIR | 60+ | 2024-2026 |
| Transportation Research | 20+ | 2024-2026 |
| Nature/Scientific Reports | 15+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 其他期刊 | 50+ | 2024-2026 |

### 技术方向统计

| 技术方向 | 论文数 | 占比 |
|---------|--------|------|
| Graph Neural Network | ~120篇 | 30% |
| Transformer/Attention | ~60篇 | 15% |
| LLM/Foundation Model | ~30篇 | 8% |
| Diffusion Model | ~25篇 | 6% |
| Federated Learning | ~25篇 | 6% |
| Trajectory Prediction | ~30篇 | 8% |
| Accident/Safety | ~20篇 | 5% |
| Transfer Learning | ~20篇 | 5% |
| Uncertainty/Probabilistic | ~15篇 | 4% |
| Physics-Informed | ~15篇 | 4% |
| 其他 | ~40篇 | 9% |

### 写作模式覆盖

| 维度 | 覆盖内容 |
|------|---------|
| **标题命名** | 12种模式（缩写组合、问题质疑、概念隐喻等） |
| **Abstract结构** | 7种开头模式、5种Limitation策略、3种Solution引入 |
| **Introduction** | 六段式漏斗、逆向-正向逻辑、三种技术挑战模式 |
| **实验描述** | 4种消融类型、效率报告、不确定性量化 |
| **图表规范** | 21种可视化模式、5大架构图范式、配色方案 |
| **润色规则** | 51条规则、Claim-Evidence-Boundary、术语台账 |
| **审稿模拟** | 5个审稿人角色、6维度评分、对抗性检查清单 |

---

## 🚀 安装方法

### 方法一：一键安装（推荐）

```bash
# 克隆仓库
git clone https://github.com/ahouyun/paper-workbench.git /tmp/paper-workbench

# 运行安装脚本
cd /tmp/paper-workbench && bash install.sh
```

### 方法二：手动安装

```bash
# 1. 克隆或下载本仓库
git clone https://github.com/ahouyun/paper-workbench.git

# 2. 复制到 Claude Code skills 目录
mkdir -p ~/.claude/skills/
cp -r paper-workbench ~/.claude/skills/

# 3. 完成！重启 Claude Code 即可使用
```

### 方法三：符号链接（开发者模式）

```bash
# 克隆到任意位置
git clone https://github.com/ahouyun/paper-workbench.git ~/projects/paper-workbench

# 创建符号链接
ln -s ~/projects/paper-workbench ~/.claude/skills/paper-workbench
```

---

## 📖 使用方法

安装后，在 Claude Code 中直接说：

| 你说的话 | 触发的能力 |
|---------|-----------|
| "帮我写一篇交通流预测的IEEE论文" | 全流程写作 |
| "搜索最近的交通预测论文" | 学术检索 |
| "审稿一下我的论文" | 审稿模拟 |
| "帮我设计消融实验" | 实验设计 |
| "画一张对比图" | 图表制作 |
| "润色这段话" | 论文润色 |
| "有什么创新方向？" | 创新灵感 |
| "逐句分析这篇论文" | 写作模式学习 |

---

## 📁 目录结构

```
paper-workbench/
├── SKILL.md                          # 入口路由文件
├── README.md                         # 本文件
├── install.sh                        # 安装脚本
├── references/
│   ├── README.md                     # 统一索引（快速导航）
│   ├── writing/                      # 写作参考 (30个文件)
│   │   ├── chapter-patterns-ieee.md  # IEEE章节模式（1375行）
│   │   ├── ieee-expression-patterns.md  # 表达模式（2400+行）
│   │   ├── ieee-polishing.md         # 润色规则（1050行，51条）
│   │   ├── traffic-figure-patterns.md   # 图表模式（3300行，21种）
│   │   ├── ieee-experiment-playbook.md  # 实验设计（1096行）
│   │   ├── ieee-innovation-inspiration.md  # 创新灵感（1920行，39方向）
│   │   ├── ieee-real-experimental-data.md  # 真实数据（1498行）
│   │   └── traffic-*.md              # 交通预测专项
│   ├── research/                     # 研究工具
│   │   └── academic-search.md        # 学术检索指南（API调用）
│   ├── review/                       # 审稿工具
│   │   └── ieee-reviewer-simulation.md  # 审稿模拟（5审稿人）
│   ├── figure-table/                 # 图表工具
│   │   ├── chart-templates.md        # Python图表模板
│   │   ├── academic-style.md         # 学术视觉规范
│   │   └── latex-tables.md           # LaTeX表格模板
│   └── workflow/                     # 工作流
├── agents/                           # Agent定义
├── workflows/                        # 工作流脚本
├── prompts/                          # 提示词模板
└── scripts/                          # 辅助脚本
```

---

## 🎯 支持的模式

| 模式 | 适用场景 | 目标期刊 |
|------|---------|---------|
| `ieee_trans` | IEEE Transactions 论文 | TITS, TKDE, TNNLS, TPAMI, TVT, TIV |
| `nature` | Nature/Science/Cell | Nature Portfolio |
| `english_research` | 通用英文研究论文 | 任意 |
| `chinese_thesis` | 中文毕业论文 | 学校模板 |
| `deep_research` | 深度研究/文献综述 | - |
| `systematic_review` | PRISMA 系统综述 | - |

---

## 📊 数据来源

### 论文覆盖（1089篇）

| 来源 | 论文数 | 时间范围 |
|------|--------|---------|
| IEEE TITS | 110+ | 2024-2026 |
| IEEE TKDE/TNNLS/TVT/TIV | 60+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 204 | 2024-2026 |
| WWW/CIKM/IJCAI/SIGIR | 60+ | 2024-2026 |
| Transportation Research | 20+ | 2024-2026 |
| Nature/Scientific Reports | 15+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 其他期刊 | 50+ | 2024-2026 |

### 创新方向（39个）

GNN、Transformer、Mamba/SSM、Diffusion、LLM/Foundation Model、Neural ODE、因果推断、对比学习、知识蒸馏、异构图、保形预测、时空点过程、联邦学习、高效注意力、元学习、OOD泛化、公平性、数字孪生、量子计算等。

### 标准数据集

METR-LA、PEMS-BAY、PEMS03/04/07/08、LargeST、NYC Taxi、XXLTraffic

---

## 🔧 依赖

- **Claude Code** (最新版本)
- **Python 3.8+** (用于学术检索 API)
- **requests** 库 (`pip install requests`)

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [nature-skills](https://github.com/Yuan1z0825/nature-skills) — Nature 论文写作 Skill
- [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 学术研究Skill套件
- [LibCity](https://github.com/LibCity/Bigscity-LibCity) — 交通预测统一框架
- [BasicTS](https://github.com/GestaltCogTeam/BasicTS) — 时空预测基准
- [LargeST](https://github.com/liuxu77/LargeST) — 大规模交通预测基准

---

> 如果这个 Skill 对你有帮助，请给个 ⭐ Star！
