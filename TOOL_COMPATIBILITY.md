# 工具兼容性指南

> 本 skill 设计为**工具无关**，可适配多种 AI 编程工具。

---

## 支持的工具

| 工具 | 适配状态 | 安装方式 |
|------|----------|----------|
| **Claude Code** | ✅ 完全支持 | `~/.claude/skills/paper-workbench` |
| **Codex CLI** | ✅ 完全支持 | `~/.codex/skills/paper-workbench` |
| **Cursor** | ✅ 完全支持 | `.cursor/skills/paper-workbench` |
| **Windsurf** | ✅ 完全支持 | `.windsurf/skills/paper-workbench` |
| **Aider** | ✅ 完全支持 | 配置文件中指定 |
| **Continue** | ✅ 完全支持 | `.continue/skills/paper-workbench` |
| **Cline** | ✅ 完全支持 | 配置文件中指定 |

---

## 安装方式

### 通用安装

```bash
# 克隆仓库
git clone https://github.com/ahouyun/paper-workbench.git

# 根据使用的工具，复制到对应目录
# Claude Code
cp -r paper-workbench ~/.claude/skills/

# Codex CLI
cp -r paper-workbench ~/.codex/skills/

# Cursor
cp -r paper-workbench .cursor/skills/

# Windsurf
cp -r paper-workbench .windsurf/skills/

# 或者使用符号链接（推荐）
ln -s $(pwd)/paper-workbench ~/.claude/skills/paper-workbench
ln -s $(pwd)/paper-workbench ~/.codex/skills/paper-workbench
```

### 使用安装脚本

```bash
# 自动检测工具并安装
./install.sh

# 或指定工具
./install.sh --tool claude
./install.sh --tool codex
./install.sh --tool cursor
```

---

## 工具特性适配

### Claude Code

- **Skill 格式**: `SKILL.md` 作为入口
- **加载方式**: 自动加载 `SKILL.md`
- **Agent 调用**: 通过 `Agent` 工具调用子代理
- **文件操作**: 通过 `Read`, `Write`, `Edit` 工具

### Codex CLI

- **Skill 格式**: `SKILL.md` 作为入口
- **加载方式**: 通过 `/skill` 命令加载
- **Agent 调用**: 通过内置代理系统
- **文件操作**: 通过内置文件操作

### Cursor

- **Skill 格式**: `.cursorrules` 或 `SKILL.md`
- **加载方式**: 自动加载项目中的规则文件
- **Agent 调用**: 通过 Composer 或 Chat
- **文件操作**: 通过内置编辑器

### Windsurf

- **Skill 格式**: `.windsurfrules` 或 `SKILL.md`
- **加载方式**: 自动加载项目中的规则文件
- **Agent 调用**: 通过 Cascade
- **文件操作**: 通过内置编辑器

---

## 通用设计原则

### 1. 文件格式

所有参考文件使用 **Markdown** 格式，不依赖特定工具的语法。

### 2. 路径引用

使用**相对路径**，不使用绝对路径或工具特定路径。

### 3. 命令抽象

工具特定命令通过**抽象层**处理：

```yaml
# 不要写
claude --model claude-sonnet-4-20250514

# 要写
使用当前会话的默认模型
```

### 4. Agent 调用

Agent 调用使用**通用描述**，不绑定特定工具：

```yaml
# 不要写
使用 Claude Code 的 Agent 工具

# 要写
启动子代理执行任务
```

### 5. 文件操作

文件操作使用**通用动词**：

```yaml
# 不要写
使用 Read 工具读取文件

# 要写
读取文件内容
```

---

## 工具特定配置

### Claude Code 配置

创建 `.claude/settings.json`：

```json
{
  "skills": ["paper-workbench"],
  "model": "claude-sonnet-4-20250514",
  "maxTokens": 8192
}
```

### Codex CLI 配置

创建 `.codex/config.yaml`：

```yaml
skills:
  - paper-workbench

model: codex-mini
max_tokens: 8192
```

### Cursor 配置

创建 `.cursorrules`：

```markdown
# Paper Workbench Skill

请参考 SKILL.md 中的说明执行任务。
```

### Windsurf 配置

创建 `.windsurfrules`：

```markdown
# Paper Workbench Skill

请参考 SKILL.md 中的说明执行任务。
```

---

## 兼容性检查

### 检查清单

- [ ] SKILL.md 使用 Markdown 格式
- [ ] 所有路径使用相对路径
- [ ] 命令描述不绑定特定工具
- [ ] Agent 调用使用通用描述
- [ ] 文件操作使用通用动词
- [ ] 配置文件支持多工具
- [ ] 安装脚本支持多工具

### 测试方法

```bash
# 测试 Claude Code
cd ~/.claude/skills/paper-workbench
claude --skill paper-workbench "帮我写一篇交通预测论文的Introduction"

# 测试 Codex CLI
cd ~/.codex/skills/paper-workbench
codex --skill paper-workbench "帮我写一篇交通预测论文的Introduction"

# 测试 Cursor
cd .cursor/skills/paper-workbench
# 在 Cursor 中打开项目，使用 Composer 或 Chat
```

---

## 常见问题

### Q: 如何在多个工具之间共享配置？

A: 使用符号链接或配置文件同步工具。

### Q: 某个工具不支持某个功能怎么办？

A: 参考该工具的文档，使用替代方案。本 skill 的核心功能（写作逻辑、参考文件）在所有工具中都可用。

### Q: 如何添加对新工具的支持？

A: 1. 在本文件中添加工具说明
   2. 创建工具特定的配置文件
   3. 更新安装脚本

---

## 更新日志

- **v7.3.0** (2026-06-23): 添加工具兼容性指南
- 支持 Claude Code, Codex CLI, Cursor, Windsurf, Aider, Continue, Cline
