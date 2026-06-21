"""
IEEE论文图表代码模板
用法: 直接复制需要的函数，修改数据即可

依赖: pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

# ===== 全局设置 =====
def set_ieee_style():
    """设置IEEE论文图表样式"""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman'],
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': False,
        'legend.frameon': False,
    })

set_ieee_style()

# ===== 1. 多数据集对比柱状图 =====
def plot_comparison_bar(datasets, methods, results, metric="MAE",
                        save_path="comparison_bar.pdf"):
    """
    多数据集对比柱状图

    参数:
        datasets: 数据集名称列表, e.g., ['METR-LA', 'PEMS-BAY', 'PEMS04', 'PEMS08']
        methods: 方法名称列表, e.g., ['DCRNN', 'STGCN', 'GWNet', 'Ours']
        results: 结果矩阵 shape=(n_methods, n_datasets)
        metric: 指标名称
        save_path: 保存路径
    """
    n_datasets = len(datasets)
    n_methods = len(methods)

    fig, axes = plt.subplots(1, n_datasets, figsize=(3.5 * n_datasets, 3))

    if n_datasets == 1:
        axes = [axes]

    x = np.arange(n_methods)
    width = 0.6

    colors = ['#4C78A8'] * (n_methods - 1) + ['#E31A1C']  # 最后一个是ours

    for i, (ax, dataset) in enumerate(zip(axes, datasets)):
        bars = ax.bar(x, results[:, i], width, color=colors, edgecolor='white')
        ax.set_xlabel(dataset)
        ax.set_ylabel(metric)
        ax.set_xticks(x)
        ax.set_xticklabels(methods, rotation=45, ha='right')

        # 标注最佳值
        best_idx = np.argmin(results[:, i])
        ax.annotate(f'{results[best_idx, i]:.2f}',
                    xy=(best_idx, results[best_idx, i]),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 2. 多步预测折线图 =====
def plot_prediction_curve(time_steps, ground_truth, predictions,
                          method_names=None, sensor_id=0,
                          save_path="prediction_curve.pdf"):
    """
    多步预测折线图

    参数:
        time_steps: 时间步数组
        ground_truth: 真实值
        predictions: 预测值列表 (每个方法一个)
        method_names: 方法名称列表
        sensor_id: 传感器ID (用于标题)
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(7, 3))

    # 真实值
    ax.plot(time_steps, ground_truth, 'k-', linewidth=2, label='Ground Truth')

    # 预测值
    colors = ['#4C78A8', '#E8864A', '#59A14F', '#9D78B8', '#E31A1C']
    linestyles = ['--', '-.', ':', '--', '-.']

    for i, pred in enumerate(predictions):
        name = method_names[i] if method_names else f'Method {i+1}'
        ax.plot(time_steps, pred, color=colors[i % len(colors)],
                linestyle=linestyles[i % len(linestyles)],
                linewidth=1.5, label=name)

    ax.set_xlabel('Time Step')
    ax.set_ylabel('Traffic Speed (mph)')
    ax.set_title(f'Sensor {sensor_id}')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 3. 消融实验表格 =====
def plot_ablation_table(components, metrics, save_path="ablation.tex"):
    """
    生成消融实验LaTeX表格

    参数:
        components: 组件名称列表
        metrics: 指标字典 {'MAE': [...], 'RMSE': [...], 'MAPE': [...]}
        save_path: 保存路径
    """
    lines = []
    lines.append("\\begin{table}[!t]")
    lines.append("\\centering")
    lines.append("\\caption{Ablation study results.}")
    lines.append("\\label{tab:ablation}")
    lines.append("\\begin{tabular}{l" + "c" * len(metrics) + "}")
    lines.append("\\toprule")

    # 表头
    header = "Variant"
    for metric in metrics:
        header += f" & {metric}↓"
    header += " \\\\"
    lines.append(header)
    lines.append("\\midrule")

    # 数据行
    for i, comp in enumerate(components):
        row = comp
        for metric, values in metrics.items():
            val = values[i]
            if i == 0:  # Full Model
                row += f" & \\textbf{{{val}}}"
            else:
                row += f" & {val}"
        row += " \\\\"
        lines.append(row)

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")

    with open(save_path, 'w') as f:
        f.write('\n'.join(lines))

    print(f"LaTeX table saved to {save_path}")


# ===== 4. 注意力热力图 =====
def plot_attention_heatmap(attention_matrix, x_labels=None, y_labels=None,
                           title="Attention Weights",
                           save_path="attention_heatmap.pdf"):
    """
    注意力权重热力图

    参数:
        attention_matrix: 注意力矩阵
        x_labels: X轴标签
        y_labels: Y轴标签
        title: 标题
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    im = ax.imshow(attention_matrix, cmap='YlOrRd', aspect='auto')

    if x_labels:
        ax.set_xticks(range(len(x_labels)))
        ax.set_xticklabels(x_labels, rotation=45, ha='right')
    if y_labels:
        ax.set_yticks(range(len(y_labels)))
        ax.set_yticklabels(y_labels)

    ax.set_xlabel('Key Position')
    ax.set_ylabel('Query Position')
    ax.set_title(title)

    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 5. 消融柱状图 =====
def plot_ablation_bar(components, values, metric="MAE",
                      save_path="ablation_bar.pdf"):
    """
    消融实验柱状图

    参数:
        components: 组件名称列表
        values: 对应的指标值
        metric: 指标名称
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(6, 3.5))

    colors = ['#E31A1C'] + ['#4C78A8'] * (len(components) - 1)  # 第一个是Full Model
    bars = ax.bar(range(len(components)), values, color=colors, edgecolor='white')

    ax.set_xticks(range(len(components)))
    ax.set_xticklabels(components, rotation=45, ha='right')
    ax.set_ylabel(metric)

    # 标注数值
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f'{val:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 6. 预测区间图 =====
def plot_prediction_interval(time_steps, ground_truth, mean_pred,
                             lower_bound, upper_bound,
                             save_path="prediction_interval.pdf"):
    """
    概率预测区间图

    参数:
        time_steps: 时间步
        ground_truth: 真实值
        mean_pred: 预测均值
        lower_bound: 下界
        upper_bound: 上界
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(7, 3))

    ax.plot(time_steps, ground_truth, 'k-', linewidth=2, label='Ground Truth')
    ax.plot(time_steps, mean_pred, 'r--', linewidth=1.5, label='Prediction')
    ax.fill_between(time_steps, lower_bound, upper_bound,
                    alpha=0.3, color='#4C78A8', label='90% CI')

    ax.set_xlabel('Time Step')
    ax.set_ylabel('Traffic Speed (mph)')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 7. 效率散点图 =====
def plot_efficiency_scatter(methods, params, mae, fps=None,
                            save_path="efficiency_scatter.pdf"):
    """
    参数量 vs 性能散点图

    参数:
        methods: 方法名称列表
        params: 参数量列表 (M)
        mae: MAE列表
        fps: FPS列表 (可选, 用于气泡大小)
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(5, 4))

    if fps:
        sizes = [f / max(fps) * 500 for f in fps]
    else:
        sizes = [100] * len(methods)

    colors = ['#4C78A8'] * (len(methods) - 1) + ['#E31A1C']

    for i, (p, m, s, c) in enumerate(zip(params, mae, sizes, colors)):
        ax.scatter(p, m, s=s, c=c, alpha=0.7, edgecolors='white', linewidth=1)
        ax.annotate(methods[i], (p, m), xytext=(5, 5),
                    textcoords='offset points', fontsize=8)

    ax.set_xlabel('Parameters (M)')
    ax.set_ylabel('MAE ↓')
    ax.set_xscale('log')

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


# ===== 使用示例 =====
if __name__ == "__main__":
    # 示例1: 多数据集对比
    datasets = ['METR-LA', 'PEMS-BAY', 'PEMS04', 'PEMS08']
    methods = ['DCRNN', 'STGCN', 'GWNet', 'STAEformer', 'Ours']
    results = np.array([
        [3.17, 1.74, 19.47, 18.76],  # DCRNN
        [3.47, 1.69, 19.32, 15.74],  # STGCN
        [2.69, 1.58, 17.86, 16.88],  # GWNet
        [2.49, 1.48, 17.35, 16.50],  # STAEformer
        [2.38, 1.32, 16.85, 15.92],  # Ours
    ])
    plot_comparison_bar(datasets, methods, results, metric="MAE")

    # 示例2: 消融实验
    components = ['Full Model', 'w/o Spatial', 'w/o Temporal', 'w/o Adaptive']
    metrics = {
        'MAE': [2.98, 3.12, 3.18, 3.05],
        'RMSE': [5.85, 6.15, 6.28, 5.98],
    }
    plot_ablation_bar(components, metrics['MAE'], metric="MAE")
