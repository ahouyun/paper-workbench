#!/bin/bash
# Paper Workbench 安装脚本
# 支持多种 AI 编程工具
# 用法: bash install.sh [--tool claude|codex|cursor|windsurf|all]

set -e

echo "=========================================="
echo "  Paper Workbench 安装程序"
echo "  工具无关的论文写作工作台"
echo "=========================================="
echo ""

# 默认安装所有工具
TOOL="${1:-all}"
# 移除 --tool 前缀
TOOL="${TOOL#--tool }"

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 安装函数
install_to_tool() {
    local tool_name="$1"
    local skills_dir="$2"

    echo "📦 安装到 $tool_name..."

    # 创建目录（如果不存在）
    mkdir -p "$skills_dir"

    local target_dir="$skills_dir/paper-workbench"

    # 检查是否已安装
    if [ -d "$target_dir" ]; then
        echo "  ⚠ 已检测到已安装版本: $target_dir"
        read -p "  是否覆盖安装? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "  跳过 $tool_name。"
            return
        fi
        rm -rf "$target_dir"
        echo "  ✓ 已删除旧版本"
    fi

    # 复制文件
    cp -r "$SCRIPT_DIR" "$target_dir"

    # 删除不需要的文件
    rm -rf "$target_dir/.git" 2>/dev/null || true
    rm -f "$target_dir/install.sh" 2>/dev/null || true

    echo "  ✓ 已安装到: $target_dir"
}

# 根据参数安装
case "$TOOL" in
    claude)
        install_to_tool "Claude Code" "$HOME/.claude/skills"
        ;;
    codex)
        install_to_tool "Codex CLI" "$HOME/.codex/skills"
        ;;
    cursor)
        install_to_tool "Cursor" ".cursor/skills"
        ;;
    windsurf)
        install_to_tool "Windsurf" ".windsurf/skills"
        ;;
    all)
        echo "将安装到所有支持的工具..."
        echo ""

        # Claude Code
        if [ -d "$HOME/.claude" ] || [ "$1" = "--all" ]; then
            install_to_tool "Claude Code" "$HOME/.claude/skills"
            echo ""
        fi

        # Codex CLI
        if [ -d "$HOME/.codex" ] || [ "$1" = "--all" ]; then
            install_to_tool "Codex CLI" "$HOME/.codex/skills"
            echo ""
        fi

        # Cursor（当前目录）
        install_to_tool "Cursor" ".cursor/skills"
        echo ""

        # Windsurf（当前目录）
        install_to_tool "Windsurf" ".windsurf/skills"
        echo ""

        # 创建符号链接（可选）
        echo "💡 提示: 也可以使用符号链接共享同一个安装："
        echo "   ln -s $(pwd)/paper-workbench ~/.claude/skills/paper-workbench"
        echo "   ln -s $(pwd)/paper-workbench ~/.codex/skills/paper-workbench"
        echo ""
        ;;
    *)
        echo "❌ 未知工具: $TOOL"
        echo "用法: bash install.sh [--tool claude|codex|cursor|windsurf|all]"
        exit 1
        ;;
esac

# 统计
if [ -d "$TARGET_DIR" ]; then
    FILE_COUNT=$(find "$TARGET_DIR" -name "*.md" -type f | wc -l)
    LINE_COUNT=$(find "$TARGET_DIR" -name "*.md" -type f -exec cat {} + | wc -l)
fi

echo ""
echo "=========================================="
echo "  安装完成！"
echo "=========================================="
echo ""
echo "  📄 文件数量: $FILE_COUNT 个 Markdown 文件"
echo "  📝 总行数:   $LINE_COUNT 行"
echo ""
echo "  使用方法："
echo "    - Claude Code: 重启后直接使用"
echo "    - Codex CLI: 使用 /skill paper-workbench"
echo "    - Cursor/Windsurf: 在项目中使用"
echo ""
echo "  更多用法请查看: TOOL_COMPATIBILITY.md"
echo ""
