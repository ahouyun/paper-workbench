# Paper Workbench — 论文写作工作台

> 一套 Claude Code 论文写作 Skill，提供 IEEE Transactions 论文写作的参考资料和工具。**专注交通流预测方向**。
>
> 整合了 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (v3.13.0) 和 [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) (v2.1.0) 的核心能力。

---

## ⚠️ 重要声明

**这是一个"写作参考手册"，不是"论文生产线"。** 它能帮你组织和润色已有的研究成果，但不能替代：
- 你自己的研究想法和技术方案
- 你自己的实验代码和数据处理
- 你对领域文献的真实阅读和理解
- 你与导师和合作者的讨论

---

## 🚀 快速开始

### 安装（30秒）

```bash
git clone https://github.com/ahouyun/paper-workbench.git ~/.claude/skills/paper-workbench
```

### 使用示例

```
# 写论文
"帮我写一篇交通流预测的IEEE论文"

# 搜索文献
"搜索最近的交通预测论文"

# 审稿模拟
"审稿一下我的论文"

# 设计实验
"帮我设计消融实验"

# 画图表
"画一张对比图"

# 润色论文
"润色这段话"

# 图表顾问
"我有这份数据，帮我画成论文图"
"这个图表达到投稿要求了吗？"
"帮我把图表润色成出版级"
```

---

## ✨ 核心功能

| 能力 | 说明 | 文件 |
|------|------|------|
| 📝 **论文撰写** | Abstract/Introduction/Method/Experiment/Conclusion写作模板 | `ieee-expression-patterns-core.md` |
| 📊 **图表制作** | 11种图类型 + Table设计规范 + Figure Caption模板 | `traffic-figure-patterns.md` |
| 🧪 **实验设计** | 4种消融类型 + 效率报告 + 鲁棒性评估 | `ieee-experiment-playbook.md` |
| ✍️ **论文润色** | 51条润色规则 + Claim-Evidence-Boundary + QA检查 | `ieee-polishing.md` |
| 💡 **创新灵感** | 39个创新方向 + 1200+篇论文洞察 | `ieee-innovation-inspiration.md` |
| 📈 **真实数据** | METR-LA/PEMS-BAY/PEMS04/PEMS08真实实验数值 | `ieee-real-experimental-data.md` |
| 🎯 **逐句学习** | 好句vs坏句对比 + 12种标题模式 | `ieee-expression-patterns-new.md` |
| 📐 **逻辑严谨** | Claim-Evidence-Boundary + 六段式漏斗 | `ieee-polishing.md` |
| 📄 **LaTeX模板** | IEEE官方模板 + 自定义TITS模板 | `templates/latex/` |
| 🔍 **引用验证** | 4步验证流程 + Phantom ID检测 | `citation-verification.md` |
| 📋 **投稿指南** | Cover Letter + 审稿回复 + 拒稿处理 | `submission/` |
| 🔬 **深度研究** | 13个智能体的研究团队，7种模式 | `ars-references/socratic-mode-protocol.md` |
| 👥 **多视角审稿** | 5人审稿团 + Devil's Advocate | `ars-references/review-criteria-framework.md` |
| 🔄 **完整流水线** | 10阶段编排：研究→写作→审稿→修改→定稿 | `ars-references/pipeline-state-machine.md` |
| 🎨 **风格校准** | 6维度写作风格分析 | `writing/style-calibration-protocol.md` |
| 📜 **Nature政策** | Nature/Science/Cell期刊规范 | `venues/nature-policy.md` |
| 🎯 **图表顾问** | 先思考后绘制 + 主动拦截 + 视觉自检闭环 | `figure-advisor/figure-workflow.md` |
| 📐 **图表规范** | 6大期刊图表规范 + 中文字体配置 | `figure-advisor/journal-specs.md` |
| 🔍 **图表审查** | 18条避坑清单 + 投稿前合规自检 | `figure-advisor/viz-pitfalls.md` |

---

## 📁 目录结构

```
paper-workbench/
├── SKILL.md                          # 入口路由
├── README.md                         # 本文件
├── install.sh                        # 安装脚本
├── references/
│   ├── README.md                     # 统一索引
│   ├── writing/                      # 写作参考
│   │   ├── ieee-expression-patterns-core.md  # 核心表达模式（1300行）
│   │   ├── ieee-expression-patterns-new.md   # 新发现模式（972行）
│   │   ├── chapter-patterns-ieee.md  # IEEE章节模式
│   │   ├── ieee-polishing.md         # 润色规则（51条）
│   │   ├── traffic-figure-patterns.md # 图表模式（3300行）
│   │   ├── ieee-experiment-playbook.md # 实验设计
│   │   ├── ieee-innovation-inspiration.md # 创新灵感
│   │   ├── style-calibration-protocol.md # 风格校准协议（ARS整合）
│   │   └── traffic-*.md              # 交通预测专项
│   ├── research/                     # 研究工具
│   │   ├── academic-search.md        # 学术检索
│   │   └── citation-verification.md  # 引用验证
│   ├── review/                       # 审稿工具
│   │   ├── ieee-reviewer-simulation.md # 审稿模拟
│   │   └── collaboration-depth-rubric.md # 协作深度评分（ARS整合）
│   ├── submission/                   # 投稿工具
│   │   ├── cover-letter-template.md  # Cover Letter
│   │   ├── ieee-submission-guide.md  # 投稿指南
│   │   └── rejection-handling-guide.md # 拒稿处理
│   ├── venues/                       # 期刊政策
│   │   ├── ieee-tits.md              # IEEE TITS规范
│   │   ├── nature-portfolio.md       # Nature期刊家族
│   │   └── nature-policy.md          # Nature政策（ARS整合）
│   ├── workflow/                     # 工作流
│   │   ├── deep-research-workflow.md # 深度研究工作流
│   │   ├── systematic-review-protocol.md # 系统综述协议
│   │   ├── handoff-schemas.md        # 交接模式（ARS整合）
│   │   ├── compliance-checkpoint-protocol.md # 合规检查点（ARS整合）
│   │   ├── raise-framework.md        # RAISE框架（ARS整合）
│   │   ├── prisma-trAIce-protocol.md # PRISMA协议（ARS整合）
│   │   └── cross-model-verification.md # 跨模型验证（ARS整合）
│   ├── ars-references/               # ARS整合参考（40个文件）
│   │   ├── apa7-style-guide.md       # APA 7风格指南
│   │   ├── review-criteria-framework.md # 审稿标准框架
│   │   ├── pipeline-state-machine.md # 流水线状态机
│   │   └── ...                       # 其他37个文件
│   ├── ars-agents/                   # ARS整合智能体（3个文件）
│   │   ├── report-compiler-agent.md  # 报告编译器
│   │   ├── research-architect-agent.md # 研究架构师
│   │   └── synthesis-agent.md        # 综合智能体
│   ├── ars-templates/                # ARS整合模板（7个文件）
│   │   ├── evidence-assessment-template.md # 证据评估模板
│   │   ├── literature-matrix-template.md # 文献矩阵模板
│   │   └── ...                       # 其他5个文件
│   ├── figure-advisor/               # 图表顾问模块（8个文件）
│   │   ├── README.md                 # 模块概述
│   │   ├── figure-workflow.md        # 8步工作流 + 五条硬性原则
│   │   ├── chart-selection.md        # 图表选择决策框架
│   │   ├── viz-pitfalls.md           # 18条避坑清单
│   │   ├── journal-specs.md          # 期刊图表规范
│   │   ├── plot-recipes.md           # 9类图配方 + Python代码
│   │   ├── data-profiling.md         # 数据剖析报告解读
│   │   ├── visual-review.md          # 视觉自检闭环
│   │   └── publication-checklist.md  # 投稿前合规自检清单
│   └── ars-integration-index.md      # ARS整合索引
├── templates/
│   ├── latex/                        # LaTeX模板
│   └── code/                         # Python代码模板
└── scripts/                          # 辅助脚本
```

---

## 📊 数据来源

| 来源 | 论文数 | 时间范围 |
|------|--------|---------|
| IEEE TITS/TKDE/TNNLS/TVT | 110+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 204 | 2024-2026 |
| WWW/CIKM/IJCAI/SIGIR | 60+ | 2024-2026 |
| Transportation Research | 20+ | 2024-2026 |
| Nature/Scientific Reports | 15+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 综述论文参考文献 | 800+ | 去重后 |

---

## 🔧 依赖

- **Claude Code** (最新版本)
- **Python 3.8+** (用于学术检索API)
- **requests** 库 (`pip install requests`)

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [nature-skills](https://github.com/Yuan1z0825/nature-skills) — Nature论文写作Skill
- [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 学术研究Skill套件
- [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) — 科研数据可视化顾问
- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) — 科研配图Skill
- [LibCity](https://github.com/LibCity/Bigscity-LibCity) — 交通预测统一框架
- [BasicTS](https://github.com/GestaltCogTeam/BasicTS) — 时空预测基准

---

> 如果这个Skill对你有帮助，请给个 ⭐ Star！
