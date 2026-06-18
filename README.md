# Paper Workbench — 论文写作工作台

> 一套完整的 Claude Code 论文写作 Skill，支持 IEEE Transactions、Nature/Science/Cell 期刊风格，覆盖从文献检索到审稿回复的全流程。

---

## ✨ 功能一览

| 能力 | 说明 |
|------|------|
| 📝 **论文撰写** | 摘要/引言/方法/实验/结论，按章节结构化写作 |
| 🔍 **文献检索** | 调用 Semantic Scholar / DBLP / arXiv / CrossRef API |
| 📊 **图表制作** | Python 图表模板 + LaTeX 表格 + IEEE 视觉规范 |
| 🧪 **实验设计** | 消融实验、效率对比、鲁棒性评估 |
| 🔬 **审稿模拟** | 5 个独立审稿人角色，6 维度评分 |
| ✍️ **论文润色** | 32 条润色规则 + 去 AI 味 + Claim-Evidence-Boundary |
| 💡 **创新灵感** | 60+ 篇真实论文的创新方向和技术洞察 |
| 📈 **真实数据** | METR-LA/PEMS-BAY/PEMS04/PEMS08 真实实验数值 |

---

## 🚀 安装方法

### 方法一：一键安装（推荐）

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/paper-workbench.git /tmp/paper-workbench

# 运行安装脚本
cd /tmp/paper-workbench && bash install.sh
```

### 方法二：手动安装

```bash
# 1. 克隆或下载本仓库
git clone https://github.com/YOUR_USERNAME/paper-workbench.git

# 2. 复制到 Claude Code skills 目录
mkdir -p ~/.claude/skills/
cp -r paper-workbench ~/.claude/skills/

# 3. 完成！重启 Claude Code 即可使用
```

### 方法三：符号链接（开发者模式）

```bash
# 克隆到任意位置
git clone https://github.com/YOUR_USERNAME/paper-workbench.git ~/projects/paper-workbench

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

---

## 📁 目录结构

```
paper-workbench/
├── SKILL.md                          # 入口路由文件
├── README.md                         # 本文件
├── install.sh                        # 安装脚本
├── references/
│   ├── writing/                      # 写作参考 (35个文件)
│   │   ├── chapter-patterns-ieee.md  # IEEE 章节模式
│   │   ├── ieee-expression-patterns.md  # 表达模式
│   │   ├── ieee-polishing.md         # 润色规则 (32条)
│   │   ├── ieee-visual-playbook.md   # 图表规范
│   │   ├── ieee-experiment-playbook.md  # 实验设计
│   │   ├── ieee-innovation-inspiration.md  # 创新灵感
│   │   ├── ieee-real-experimental-data.md  # 真实数据
│   │   └── traffic-*.md              # 交通预测专项 (9个文件)
│   ├── research/                     # 研究工具
│   │   └── academic-search.md        # 学术检索指南
│   ├── review/                       # 审稿工具
│   │   └── ieee-reviewer-simulation.md  # 审稿模拟
│   ├── figure-table/                 # 图表工具
│   │   ├── chart-templates.md        # Python 图表模板
│   │   ├── academic-style.md         # 学术视觉规范
│   │   └── latex-tables.md           # LaTeX 表格模板
│   └── workflow/                     # 工作流
├── agents/                           # Agent 定义
├── workflows/                        # 工作流脚本
├── prompts/                          # 提示词模板
└── scripts/                          # 辅助脚本
```

---

## 🎯 支持的模式

| 模式 | 适用场景 | 目标期刊 |
|------|---------|---------|
| `ieee_trans` | IEEE Transactions 论文 | TITS, TKDE, TNNLS, TPAMI |
| `nature` | Nature/Science/Cell | Nature Portfolio |
| `english_research` | 通用英文研究论文 | 任意 |
| `chinese_thesis` | 中文毕业论文 | 学校模板 |
| `deep_research` | 深度研究/文献综述 | - |
| `systematic_review` | PRISMA 系统综述 | - |

---

## 🔧 依赖

- **Claude Code** (最新版本)
- **Python 3.8+** (用于学术检索 API)
- **requests** 库 (`pip install requests`)

---

## 📊 数据来源

- 150+ 篇 2024-2026 年 IEEE Transactions 真实论文
- METR-LA, PEMS-BAY, PEMS04, PEMS08 真实实验数据
- STAEformer, PDFormer, DiffSTG, UrbanGPT 等最新基线
- nature-skills 仓库的写作方法论

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [nature-skills](https://github.com/Yuan1z0825/nature-skills) — Nature 论文写作 Skill
- [LibCity](https://github.com/LibCity/Bigscity-LibCity) — 交通预测统一框架
- [BasicTS](https://github.com/GestaltCogTeam/BasicTS) — 时空预测基准

---

> 如果这个 Skill 对你有帮助，请给个 ⭐ Star！
