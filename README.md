# Paper Workbench — 论文写作工作台

> 一套 Claude Code 论文写作 Skill，提供 IEEE Transactions 论文写作的参考资料和工具。**专注交通流预测方向**。

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
│   │   └── traffic-*.md              # 交通预测专项
│   ├── research/                     # 研究工具
│   │   ├── academic-search.md        # 学术检索
│   │   └── citation-verification.md  # 引用验证
│   ├── review/                       # 审稿工具
│   │   └── ieee-reviewer-simulation.md # 审稿模拟
│   ├── submission/                   # 投稿工具
│   │   ├── cover-letter-template.md  # Cover Letter
│   │   ├── ieee-submission-guide.md  # 投稿指南
│   │   └── rejection-handling-guide.md # 拒稿处理
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
- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) — 科研配图Skill
- [LibCity](https://github.com/LibCity/Bigscity-LibCity) — 交通预测统一框架
- [BasicTS](https://github.com/GestaltCogTeam/BasicTS) — 时空预测基准

---

> 如果这个Skill对你有帮助，请给个 ⭐ Star！
