#!/bin/bash
# Paper Workbench 安装脚本
# 用法: bash install.sh

set -e

echo "=========================================="
echo "  Paper Workbench 安装程序"
echo "  论文写作工作台 for Claude Code"
echo "=========================================="
echo ""

# 检测 Claude Code skills 目录
if [ -d "$HOME/.claude/skills" ]; then
    SKILLS_DIR="$HOME/.claude/skills"
elif [ -d "$HOME/.config/claude/skills" ]; then
    SKILLS_DIR="$HOME/.config/claude/skills"
else
    SKILLS_DIR="$HOME/.claude/skills"
    mkdir -p "$SKILLS_DIR"
    echo "✓ 创建 skills 目录: $SKILLS_DIR"
fi

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$SKILLS_DIR/paper-workbench"

# 检查是否已安装
if [ -d "$TARGET_DIR" ]; then
    echo "⚠ 已检测到已安装版本: $TARGET_DIR"
    read -p "是否覆盖安装? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "取消安装。"
        exit 0
    fi
    rm -rf "$TARGET_DIR"
    echo "✓ 已删除旧版本"
fi

# 复制文件
echo "正在安装..."
cp -r "$SCRIPT_DIR" "$TARGET_DIR"

# 删除不需要的文件
rm -rf "$TARGET_DIR/.git" 2>/dev/null || true
rm -f "$TARGET_DIR/install.sh" 2>/dev/null || true

echo "✓ 文件已复制到: $TARGET_DIR"

# 统计
FILE_COUNT=$(find "$TARGET_DIR" -name "*.md" -type f | wc -l)
LINE_COUNT=$(find "$TARGET_DIR" -name "*.md" -type f -exec cat {} + | wc -l)

echo ""
echo "=========================================="
echo "  安装完成！"
echo "=========================================="
echo ""
echo "  📁 安装位置: $TARGET_DIR"
echo "  📄 文件数量: $FILE_COUNT 个 Markdown 文件"
echo "  📝 总行数:   $LINE_COUNT 行"
echo ""
echo "  使用方法: 重启 Claude Code，然后说："
echo "    - '帮我写一篇IEEE论文'"
echo "    - '搜索交通预测论文'"
echo "    - '审稿一下我的论文'"
echo ""
echo "  更多用法请查看: $TARGET_DIR/README.md"
echo ""
