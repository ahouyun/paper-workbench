# Paper Workbench — 论文写作工作台 v7.5.0

> 一套**工具无关**的论文写作 Skill，提供 IEEE Transactions 论文写作的参考资料和工具。**专注交通/智能交通/自动驾驶方向**。
>
> 支持 Claude Code, Codex CLI, Cursor, Windsurf, Aider, Continue, Cline 等多种 AI 编程工具。
>
> 整合了 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (v3.13.0) 和 [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) (v2.1.0) 的核心能力。
>
> **基于 900+ 篇 IEEE TITS/TNNLS/TVT/TIV/KDD/AAAI/NeurIPS/ICML/CVPR/ACL/SIGGRAPH 2024-2026 论文的真实写作模式分析。**

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

**Claude Code:**
```bash
git clone https://github.com/ahouyun/paper-workbench.git ~/.claude/skills/paper-workbench
```

**Codex CLI:**
```bash
git clone https://github.com/ahouyun/paper-workbench.git ~/.codex/skills/paper-workbench
```

**Cursor / Windsurf / 其他:**
```bash
git clone https://github.com/ahouyun/paper-workbench.git .cursor/skills/paper-workbench
# 或使用符号链接
ln -s $(pwd)/paper-workbench ~/.claude/skills/paper-workbench
ln -s $(pwd)/paper-workbench ~/.codex/skills/paper-workbench
```

> 详见 [TOOL_COMPATIBILITY.md](TOOL_COMPATIBILITY.md) 了解各工具的详细安装和配置方式。

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
| 📐 **图表规范** | NeurIPS/ICML/ICLR/CVPR/KDD/VLDB等顶会+IEEE/ACM期刊规范 | `figure-advisor/journal-specs.md` |
| 🎯 **图表顾问** | 先思考后绘制 + 主动拦截 + 视觉自检闭环 | `figure-advisor/figure-workflow.md` |
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
│   │   └── conference-specs.md       # 顶会规范
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
│   ├── _archived/                    # 归档目录
│   │   └── nature/                   # Nature相关文件（已归档）
│   └── ars-integration-index.md      # ARS整合索引
├── templates/
│   ├── latex/                        # LaTeX模板
│   └── code/                         # Python代码模板
└── scripts/                          # 辅助脚本
```

---

## 📊 数据来源

### 核心论文覆盖（190+ 篇，按方法类别）

| 方法类别 | 论文数 | 代表论文 |
|---------|--------|---------|
| 时空图神经网络 | 10 | Graph WaveNet, STGCN, DCRNN, PDFormer |
| Transformer | 10 | STAEformer, PDFormer, AGSTFormer, UrbanGPT |
| 新方法（扩散/LLM/Mamba） | 10 | ICST-DNET, ST-LLM, ST-Mamba, GAMMA-Net |
| 轨迹预测 | 10 | BEVTraj, StyleFormer, Social-Pose, Intention-Aware Diffusion |
| 交通控制 | 10 | VF-MAPPO, MATLIT, CoordLight, MetaSignal |
| 多模态融合 | 10 | GraphBEV++, MambaFusion, DiffFusion, ModalPatch |
| 需求预测 | 10 | TSAGE, MMDNet, DT-CTFP, AUMS |
| 联邦学习/边缘计算 | 10 | FedGau, PSFL, FedCPC, UAV-VEC-KD |
| 场景理解 | 10 | AD-SAM, DiffSemanticFusion, MMDrive, BEVTraj |
| 公共交通 | 10 | DQN Transit, MADRL DRT, Bus-Pooling, PPO Bus Speed |
| 交通安全 | 10 | GrDBN-GPR, KAN-RL, KLEP, Bayesian Games |
| 智慧城市/恶劣天气 | 10 | FedLLM, CAST-CKT, 4D Radar, CADENet |
| 点云/LiDAR | 10 | PASS, Fade3D, RobMOT, TransBridge |
| 视频预测/场景生成 | 10 | GAIA-2, DiVE, DiST-4D, Genesis, LiDARCrafter |
| 自监督学习 | 10 | STIseq2seq, CCL, SID, CE-MERL |
| 持续学习/领域适应 | 10 | TRACER, CGSTT, CIDTL, pFedLVM |
| 新图架构 | 10 | Hypergraph, Graph Transformer, MDHGAT, KG-GNN |
| 交通预测（TITS） | 10 | ASTMGCNet, TDGCRN, DSTA-GNN, ICST-DNET |
| 自动驾驶（TITS） | 10 | BEVTraj, RESAR-BEV, CarPLAN, SDD Planner |

### 补充数据来源（900+ 篇论文引用）

| 来源 | 论文引用数 | 时间范围 |
|------|-----------|---------|
| IEEE TITS/TNNLS/TVT/TIV/TPAMI/TIP/TMM | 135+ | 2024-2026 |
| KDD/AAAI/NeurIPS/ICLR/ICML | 234+ | 2024-2026 |
| CVPR/ECCV/ICCV | 58+ | 2024-2026 |
| ACL/EMNLP/NAACL | 43+ | 2024-2026 |
| SIGGRAPH/TOG | 5+ | 2024-2026 |
| arXiv预印本 | 150+ | 2025-2026 |
| 综述论文参考文献 | 800+ | 去重后 |
| **总计** | **900+** | — |

---

## 📝 写作模式库（基于 190+ 篇真实论文）

### Section 指南（6个文件，每个含真实论文示例）

| 文件 | 行数 | 核心内容 |
|------|------|---------|
| `references/sections/abstract.md` | 222行 | 3种模板 + 场馆要求 + 压缩策略 |
| `references/sections/introduction.md` | 598行 | 12种模板变体 + 快速入门 + 贡献要点 |
| `references/sections/method.md` | 392行 | 三元素框架 + 10篇真实方法解析 |
| `references/sections/experiments.md` | 1049行 | 190+论文覆盖 + 19种方法类别 |
| `references/sections/related-work.md` | 200行 | 4种组织结构 + 综合写法 |
| `references/sections/conclusion.md` | 225行 | 限制讨论策略 + Future Work模式 |

### 核心写作参考（基于 115+ 篇 IEEE Trans 论文）

| 文件 | 行数 | 核心内容 |
|------|------|---------|
| `references/writing/ieee-expression-patterns.md` | 3391行 | 标题/摘要/引言/方法/结果/结论表达模式 |
| `references/writing/ieee-expression-patterns-core.md` | 1300行 | 核心表达模式精简版 |
| `references/writing/ieee-expression-patterns-new.md` | 1476行 | 2024-2026新发现模式 |
| `references/writing/traffic-figure-patterns.md` | 3422行 | 21种可视化模式 + 图表设计 |
| `references/writing/ieee-innovation-inspiration.md` | 39个方向 | 创新灵感库 |

### 写作质量保障

| 文件 | 核心内容 |
|------|---------|
| `references/review/paper-review.md` | 7维度审稿检查 + 严重性权重 |
| `references/review/humanizer-patterns.md` | 51种AI写作模式 + 集群检测 |
| `references/writing/aigc-governance.md` | AIGC治理策略 + 误报意识 |
| `references/writing/paragraph-clarity.md` | 段落清晰度检查 + 跨节一致性 |

---

## 🔧 依赖

- **AI 编程工具**：Claude Code / Codex CLI / Cursor / Windsurf / Aider / Continue / Cline（任选其一）
- **Python 3.8+** (用于学术检索API)
- **requests** 库 (`pip install requests`)

> 详见 [TOOL_COMPATIBILITY.md](TOOL_COMPATIBILITY.md) 了解各工具的兼容性说明。

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [nature-skills](https://github.com/Yuan1z0825/nature-skills) — Nature论文写作Skill（已整合部分能力）
- [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 学术研究Skill套件
- [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) — 科研数据可视化顾问
- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) — 科研配图Skill
- [LibCity](https://github.com/LibCity/Bigscity-LibCity) — 交通预测统一框架
- [BasicTS](https://github.com/GestaltCogTeam/BasicTS) — 时空预测基准

---

> 如果这个Skill对你有帮助，请给个 ⭐ Star！
