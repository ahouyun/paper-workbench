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
| 💡 **创新灵感** | 39个创新方向，1200+篇论文的技术洞察 |
| 📈 **真实数据** | METR-LA/PEMS-BAY/PEMS04/PEMS08 真实实验数值 |
| 🎯 **逐句学习** | 好句vs坏句对比，12种标题模式，7种写作范式 |
| 📐 **逻辑严谨** | Claim-Evidence-Boundary三要素，六段式漏斗结构 |
| 📄 **LaTeX模板** | IEEE官方模板 + 自定义TITS模板 |
| 📋 **投稿指南** | Cover Letter + 审稿回复 + 拒稿处理 |

---

## 🆕 v3.5 新增功能（突破1200+篇论文）

### 论文覆盖（1200+篇）

| 来源 | 论文数 | 时间范围 |
|------|--------|---------|
| IEEE TITS | 110+ | 2024-2026 |
| IEEE TKDE/TNNLS/TVT/TIV | 60+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 204 | 2024-2026 |
| WWW/CIKM/IJCAI/SIGIR | 60+ | 2024-2026 |
| Transportation Research | 20+ | 2024-2026 |
| Nature/Scientific Reports | 15+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 综述论文参考文献 | 800+ | 去重后 |
| 顶级研究组论文 | 55 | 2024-2026 |

### 核心综述论文（2,500+篇参考文献）

| 综述 | 参考文献数 | 被引次数 |
|------|-----------|---------|
| GNN for Traffic Forecasting Survey | 437 | 1216 |
| GenAI for Urban Digital Twins | 358 | 120 |
| LLM Reshaping Transportation | 298 | 33 |
| Traffic Prediction: ST Data to ITS | 266 | 367 |
| GNN for ITS Survey | 241 | 273 |
| Foundation Models for GeoAI | 224 | 98 |

### 核心Benchmark平台

| 平台 | 方法数 | 核心贡献 |
|------|--------|---------|
| LibCity | 60+ | 最全面开源库 |
| OpenSTL | 20+ | 跨领域时空预测 |
| BasicTS | 15+ | 公平评估框架 |
| LargeST | 10+ | 大规模评估(8600传感器) |

### 顶级研究组

| 研究组 | 机构 | 代表论文 |
|--------|------|---------|
| Yu Zheng | Microsoft Research | UrbanGPT, UniST |
| Yuxuan Liang | Sydney/HKUST | STAEformer, PDFormer |
| Yong Li | Tsinghua | UniST, 跨城市迁移 |
| Chao Huang | HKUST | One-for-All |
| Jingyuan Wang | Tsinghua | Revisiting系列 |

---

## 🚀 安装方法

### 方法一：一键安装（推荐）

```bash
git clone https://github.com/ahouyun/paper-workbench.git /tmp/paper-workbench
cd /tmp/paper-workbench && bash install.sh
```

### 方法二：手动安装

```bash
git clone https://github.com/ahouyun/paper-workbench.git
mkdir -p ~/.claude/skills/
cp -r paper-workbench ~/.claude/skills/
```

### 方法三：符号链接（开发者模式）

```bash
git clone https://github.com/ahouyun/paper-workbench.git ~/projects/paper-workbench
ln -s ~/projects/paper-workbench ~/.claude/skills/paper-workbench
```

---

## 📖 使用方法

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
│   ├── README.md                     # 统一索引
│   ├── writing/                      # 写作参考 (32个文件)
│   │   ├── chapter-patterns-ieee.md  # IEEE章节模式
│   │   ├── ieee-expression-patterns.md  # 表达模式
│   │   ├── ieee-polishing.md         # 润色规则（51条）
│   │   ├── traffic-figure-patterns.md   # 图表模式
│   │   ├── ieee-innovation-inspiration.md  # 创新灵感
│   │   ├── flexible-writing-guide.md # 灵活写作指南
│   │   └── traffic-*.md              # 交通预测专项
│   ├── research/                     # 研究工具
│   │   ├── academic-search.md        # 学术检索指南
│   │   └── citation-verification.md  # 引用验证
│   ├── review/                       # 审稿工具
│   │   └── ieee-reviewer-simulation.md  # 审稿模拟
│   ├── submission/                   # 投稿工具
│   │   ├── cover-letter-template.md  # Cover Letter
│   │   ├── ieee-submission-guide.md  # 投稿指南
│   │   ├── rejection-handling-guide.md  # 拒稿处理
│   │   └── statistical-analysis-guide.md  # 统计分析
│   └── figure-table/                 # 图表工具
├── templates/
│   ├── latex/                        # LaTeX模板
│   │   ├── ieee-official-template.tex  # IEEE官方模板
│   │   └── ieee-tits-template.tex    # TITS自定义模板
│   └── code/                         # 代码模板
│       └── ieee_charts.py            # Python图表代码
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

### 论文覆盖（1200+篇）

| 来源 | 论文数 | 时间范围 |
|------|--------|---------|
| IEEE TITS | 110+ | 2024-2026 |
| IEEE TKDE/TNNLS/TVT/TIV | 60+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 204 | 2024-2026 |
| WWW/CIKM/IJCAI/SIGIR | 60+ | 2024-2026 |
| Transportation Research | 20+ | 2024-2026 |
| Nature/Scientific Reports | 15+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 综述论文参考文献 | 800+ | 去重后 |
| 顶级研究组论文 | 55 | 2024-2026 |

### 技术方向（39个）

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
