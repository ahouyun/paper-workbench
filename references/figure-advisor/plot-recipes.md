# 七类图配方

每一节给一份**可直接运行的 Python 代码**——直接复制改数据就能出图。

---

## 通用前置

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Okabe-Ito 8 色（色盲安全）
OKABE = ['#000000', '#E69F00', '#56B4E9', '#009E73',
         '#F0E442', '#0072B2', '#D55E00', '#CC79A7']
# 也可直接用 seaborn 的 colorblind
PAL = sns.color_palette('colorblind')
```

---

## 1. 折线图（含误差阴影）

**何时用**：时间序列、x 是连续变量、需要展示均值±误差。

```python
def lineplot_with_band(ax, x, y_mean, y_err, label, color, ls='-'):
    """y_err 可以是 SD/SEM/95%CI，图注里务必交代。"""
    ax.plot(x, y_mean, color=color, linewidth=1.0, linestyle=ls, label=label)
    ax.fill_between(x, y_mean - y_err, y_mean + y_err,
                    color=color, alpha=0.2, linewidth=0)

# --- 示例 ---
rng = np.random.default_rng(42)
x = np.linspace(0, 10, 100)
# 假装 n=12 只小鼠，对每个 x 算 mean ± SEM
n = 12
y1_samples = np.sin(x)[:, None] + rng.normal(0, 0.3, (100, n))
y2_samples = np.cos(x)[:, None] + rng.normal(0, 0.3, (100, n))
y1_mean, y1_sem = y1_samples.mean(1), y1_samples.std(1, ddof=1) / np.sqrt(n)
y2_mean, y2_sem = y2_samples.mean(1), y2_samples.std(1, ddof=1) / np.sqrt(n)

fig, ax = plt.subplots(figsize=(3.5, 2.625))
lineplot_with_band(ax, x, y1_mean, y1_sem, 'Condition A',
                   color=OKABE[2], ls='-')
lineplot_with_band(ax, x, y2_mean, y2_sem, 'Condition B',
                   color=OKABE[6], ls='--')   # 第二条用虚线 -> 黑白可读
ax.set_xlabel('Time (s)')
ax.set_ylabel('Response (a.u.)')
ax.legend(frameon=False, loc='lower right')

# 图注必须写: shaded band = SEM, n = 12 mice per group.
plt.tight_layout()
plt.savefig('figs/01_line.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- `fill_between` 必须显式 `linewidth=0`，否则 PDF 里阴影边缘会有细线
- 不同曲线**必须**有除颜色之外的区分（线型 / marker），否则灰度下不可读

---

## 2. 柱状图（分组 + 误差棒）

**何时用**：分类变量的均值对比、组间比较。

```python
# 数据：3 组 × 2 条件 × n=10 重复
rng = np.random.default_rng(0)
groups = ['Control', 'Drug A', 'Drug B']
conditions = ['Before', 'After']
data = pd.DataFrame({
    'group': np.repeat(groups, 2 * 10),
    'condition': np.tile(np.repeat(conditions, 10), 3),
    'value': np.concatenate([
        rng.normal(loc, 1.0, 10)
        for loc in [1, 2, 3, 4, 2, 3]   # 6 组合
    ]),
})

# 用 seaborn barplot——默认就是 mean + 95%CI（bootstrap）
# 想要 SD/SEM 改 errorbar 参数
fig, ax = plt.subplots(figsize=(3.5, 2.625))
sns.barplot(
    data=data, x='group', y='value', hue='condition',
    palette=[OKABE[2], OKABE[6]],
    errorbar='se',          # 'sd' | 'se' | ('ci', 95) | None
    capsize=0.15,
    err_kws={'linewidth': 0.8},
    ax=ax,
)
# 叠加原始点显示数据分布——审稿人喜欢看分布而非只看均值
sns.stripplot(
    data=data, x='group', y='value', hue='condition',
    palette=[OKABE[2], OKABE[6]],
    dodge=True, size=2, alpha=0.6, edgecolor='black', linewidth=0.3,
    ax=ax, legend=False,
)
ax.set_xlabel(''); ax.set_ylabel('Score (a.u.)')
ax.legend(title='', frameon=False, loc='upper left')

# 图注: bars = mean ± SEM; dots = individual replicates; n = 10 per group.
plt.tight_layout()
plt.savefig('figs/02_bar.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- 柱状图**不要**用没有误差棒的纯柱——审稿人会怀疑没做重复
- 多组比较时配色保持类别一致（同一个条件在不同图里同色）
- `barplot` 默认 95% CI 是 bootstrap，**速度慢**，明确写 `errorbar='se'` 或 `'sd'` 更快也更明确

---

## 3. 散点图（多语义映射 + 回归线）

**何时用**：相关性、双变量关系；可以同时映射 hue（颜色）+ style（marker）+ size。

```python
# 模拟数据：N 个样本，x 和 y 有相关性，分两组
rng = np.random.default_rng(1)
N = 80
df = pd.DataFrame({
    'x': rng.normal(0, 1, N),
    'group': rng.choice(['A', 'B'], N),
})
df['y'] = 0.6 * df['x'] + np.where(df['group']=='B', 0.5, 0) + rng.normal(0, 0.5, N)

fig, ax = plt.subplots(figsize=(3.5, 3.0))
sns.scatterplot(
    data=df, x='x', y='y',
    hue='group', style='group',     # 颜色 + marker 形状双重编码
    palette=[OKABE[2], OKABE[6]],
    s=25, alpha=0.85, edgecolor='black', linewidth=0.3,
    ax=ax,
)
# 分组回归线 + 95% CI
sns.regplot(data=df[df.group=='A'], x='x', y='y',
            scatter=False, color=OKABE[2], line_kws={'lw': 1.0}, ax=ax)
sns.regplot(data=df[df.group=='B'], x='x', y='y',
            scatter=False, color=OKABE[6], line_kws={'lw': 1.0}, ax=ax)

# 在图里标 Pearson r 和 p
from scipy.stats import pearsonr
for g, c in zip(['A', 'B'], [OKABE[2], OKABE[6]]):
    sub = df[df.group == g]
    r, p = pearsonr(sub.x, sub.y)
    ax.text(0.05 if g=='A' else 0.05, 0.95 if g=='A' else 0.88,
            f'{g}: r={r:.2f}, p={p:.1e}',
            transform=ax.transAxes, fontsize=6, color=c, va='top')

ax.set_xlabel('Predictor x'); ax.set_ylabel('Response y')
ax.legend(title='Group', frameon=False, loc='lower right')

plt.tight_layout()
plt.savefig('figs/03_scatter.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- 散点图样本量很大（>1000）时，alpha 调到 0.2-0.3 防止 over-plotting，或用 `sns.jointplot` 加边缘密度
- 把 r 和 p 标在图里**很省审稿人时间**，加分项
- regplot 的 `scatter=False` 必须，否则散点会被画两遍

---

## 4. 箱线图 / 小提琴图（叠 stripplot）

**何时用**：组间分布对比；箱线图看四分位，小提琴图看密度。**最佳实践**：箱线图/小提琴图 + stripplot 叠加显示原始点。

```python
fig, ax = plt.subplots(figsize=(3.5, 2.625))
sns.boxplot(
    data=data, x='group', y='value', hue='condition',
    palette=[OKABE[2], OKABE[6]],
    showfliers=False,        # 不画异常点，由 stripplot 显示全部点
    width=0.6,
    ax=ax,
)
sns.stripplot(
    data=data, x='group', y='value', hue='condition',
    palette=[OKABE[2], OKABE[6]],
    dodge=True, size=2, alpha=0.6, edgecolor='black', linewidth=0.3,
    ax=ax, legend=False,
)
ax.set_xlabel(''); ax.set_ylabel('Score (a.u.)')
ax.legend(title='', frameon=False, loc='upper left')

# 图注: box = median + IQR; whiskers = 1.5×IQR; dots = individual replicates
plt.tight_layout()
plt.savefig('figs/04_box.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- n<10 时箱线的四分位估计不可靠，优先用 stripplot
- `showfliers=False` 因为 stripplot 已经显示了所有点
- 多组时 `dodge=True` 让点和箱对齐

---

## 5. 热力图（感知均匀色图）

**何时用**：矩阵型数据、相关性矩阵、混淆矩阵。

```python
# 相关性矩阵
rng = np.random.default_rng(42)
df_corr = pd.DataFrame(rng.normal(0, 1, (100, 5)),
                       columns=['A', 'B', 'C', 'D', 'E'])
corr = df_corr.corr()

fig, ax = plt.subplots(figsize=(4, 3.5))
sns.heatmap(
    corr, annot=True, fmt='.2f',
    cmap='RdBu_r', center=0,    # 双向数据用发散色图
    vmin=-1, vmax=1,
    square=True,
    linewidths=0.5,
    cbar_kws={'label': 'Pearson r'},
    ax=ax,
)
ax.set_title('Correlation Matrix')

plt.tight_layout()
plt.savefig('figs/05_heatmap.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- 双向数据必须用发散色图 + `center=0`
- 单向数据用 viridis / magma / inferno
- **永远不用** rainbow / jet / hsv

---

## 6. 误差棒图

**何时用**：需要精确展示均值±误差。

```python
# 数据：3 组 × n=10
rng = np.random.default_rng(42)
groups = ['Control', 'Drug A', 'Drug B']
means = [1.0, 2.5, 3.2]
sems = [0.2, 0.3, 0.25]

fig, ax = plt.subplots(figsize=(3.5, 2.625))
x_pos = np.arange(len(groups))
ax.errorbar(x_pos, means, yerr=sems, fmt='o', color='black',
            capsize=5, capthick=1.5, markersize=8, linewidth=1.5)
ax.set_xticks(x_pos)
ax.set_xticklabels(groups)
ax.set_ylabel('Response (a.u.)')
ax.set_xlim(-0.5, len(groups) - 0.5)

# 图注: error bars = SEM, n = 10 per group
plt.tight_layout()
plt.savefig('figs/06_errorbar.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- 必须在图注写清误差类型（SD / SEM / 95% CI）
- n<10 时优先用 stripplot 而非误差棒

---

## 7. 分布图（直方图 / KDE）

**何时用**：看单个连续变量的分布。

```python
rng = np.random.default_rng(42)
data_dist = rng.normal(0, 1, 200)

fig, axes = plt.subplots(1, 2, figsize=(7, 2.625))

# 直方图
axes[0].hist(data_dist, bins=30, color=OKABE[2], edgecolor='white',
             linewidth=0.5, alpha=0.8)
axes[0].set_xlabel('Value'); axes[0].set_ylabel('Count')
axes[0].set_title('Histogram')

# KDE
sns.kdeplot(data=data_dist, color=OKABE[6], linewidth=1.5, ax=axes[1])
axes[1].set_xlabel('Value'); axes[1].set_ylabel('Density')
axes[1].set_title('KDE')

plt.tight_layout()
plt.savefig('figs/07_distribution.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- n<5 时所有"分布"图都不可靠，直接列点
- 直方图的 bins 数量影响观感，尝试不同值

---

## 8. 相关性矩阵 / 散点矩阵

**何时用**：多变量相关性分析。

```python
rng = np.random.default_rng(42)
df_pair = pd.DataFrame(rng.normal(0, 1, (100, 4)),
                       columns=['A', 'B', 'C', 'D'])

# 相关性热力图（推荐）
fig, ax = plt.subplots(figsize=(4, 3.5))
sns.heatmap(df_pair.corr(), annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, ax=ax)
plt.tight_layout()
plt.savefig('figs/08_corr_heatmap.pdf', dpi=300, bbox_inches='tight')

# 散点矩阵（pairplot）—— 变量少时可用
# g = sns.pairplot(df_pair, diag_kind='kde')
# g.savefig('figs/08_pairplot.pdf', dpi=300)
```

**坑**：
- 变量 > 8 时 pairplot 满屏，改用热力图
- 大矩阵（>20 列）+ hierarchical clustering 重排行列

---

## 9. 多面板组合图

**何时用**：一张图讲多个相关子图。

```python
fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.4))

# Panel a: 折线
x = np.linspace(0, 10, 50)
axes[0, 0].plot(x, np.sin(x), color=OKABE[2])
axes[0, 0].set_title('a', fontweight='bold', loc='left')
axes[0, 0].set_xlabel('Time'); axes[0, 0].set_ylabel('sin(x)')

# Panel b: 散点
rng = np.random.default_rng(42)
axes[0, 1].scatter(rng.normal(0, 1, 50), rng.normal(0, 1, 50),
                   color=OKABE[6], s=20)
axes[0, 1].set_title('b', fontweight='bold', loc='left')
axes[0, 1].set_xlabel('x'); axes[0, 1].set_ylabel('y')

# Panel c: 柱状
groups = ['A', 'B', 'C']
values = [2, 3, 1]
axes[1, 0].bar(groups, values, color=[OKABE[2], OKABE[6], OKABE[4]])
axes[1, 0].set_title('c', fontweight='bold', loc='left')
axes[1, 0].set_ylabel('Value')

# Panel d: 箱线
data_box = [rng.normal(0, 1, 30) for _ in range(3)]
axes[1, 1].boxplot(data_box, labels=groups)
axes[1, 1].set_title('d', fontweight='bold', loc='left')
axes[1, 1].set_ylabel('Value')

plt.tight_layout()
plt.savefig('figs/09_multipanel.pdf', dpi=300, bbox_inches='tight')
```

**坑**：
- 子图标签 a/b/c/d 要统一位置（左上角）和风格（加粗）
- 同一个变量在多个子图里要同色
- 共享含义的坐标轴范围要一致

---

## 10. Plotly 交互图

**何时用**：需要交互探索数据。

```python
import plotly.express as px

# 散点图
fig = px.scatter(df, x='x', y='y', color='group',
                 title='Interactive Scatter Plot')
fig.show()

# 折线图
fig = px.line(df, x='time', y='value', color='group',
              title='Interactive Line Plot')
fig.show()
```

**坑**：
- 交互图不适合投稿（期刊要静态图）
- 适合探索数据、做报告、网页展示
