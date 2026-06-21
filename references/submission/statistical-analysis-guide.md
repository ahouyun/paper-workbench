# 统计分析指南 (Statistical Analysis Guide)

> TITS审稿人越来越关注实验的统计严谨性。

---

## 一、为什么需要统计分析

**编辑的原话：** "仅靠'均值±标准差'已经不够了。审稿人越来越关注统计检验、p值、置信区间、效应量。"

**常见审稿意见：**
- "The improvements are marginal. Are they statistically significant?"
- "How many runs were performed? What is the standard deviation?"
- "Please provide p-values for the ablation results."

---

## 二、必须报告的统计量

### 2.1 基本统计量

| 统计量 | 说明 | 报告格式 |
|--------|------|---------|
| 均值 (Mean) | 多次运行的平均值 | 2.49 |
| 标准差 (Std) | 多次运行的标准差 | ±0.03 |
| 运行次数 (N) | 实验重复次数 | N=5 |
| 置信区间 (CI) | 均值的置信区间 | 95% CI: [2.46, 2.52] |

**报告格式示例：**
```
Our method achieves MAE of 2.49 ± 0.03 (mean ± std, N=5) on METR-LA.
95% confidence interval: [2.46, 2.52].
```

### 2.2 显著性检验

**何时需要显著性检验：**
- 声称"我们的方法优于基线"时
- 消融实验中声称"组件X有效"时
- 改进幅度较小时（<5%）

**推荐的检验方法：**

| 场景 | 推荐检验 | 说明 |
|------|---------|------|
| 两组对比 | 配对t检验 (paired t-test) | 适用于正态分布数据 |
| 两组对比 | Wilcoxon符号秩检验 | 不假设正态分布 |
| 多组对比 | Friedman检验 | 非参数，适用于多数据集 |
| 多组对比后两两比较 | Nemenyi检验 | Friedman的事后检验 |

**报告格式示例：**
```
The improvement over STAEformer is statistically significant 
(paired t-test, p < 0.01, N=5).
```

### 2.3 效应量

**什么是效应量：** 衡量改进的实际大小，不受样本量影响。

**Cohen's d：**
```
d = (mean_ours - mean_baseline) / pooled_std

d ≈ 0.2: 小效应
d ≈ 0.5: 中等效应
d ≈ 0.8: 大效应
```

**报告格式示例：**
```
The improvement over STAEformer has a large effect size 
(Cohen's d = 1.2, p < 0.01).
```

---

## 三、消融实验的统计严谨性

### 3.1 公平消融设计

**规则：** 控制变量数量一致

**错误示例：**
```
Full Model: 8.2M params, MAE 2.49
w/o Module A: 5.1M params, MAE 2.58  ← 参数量不同！
```

**正确示例：**
```
Full Model: 8.2M params, MAE 2.49
w/o Module A: 8.2M params, MAE 2.58  ← 参数量相同
(replace Module A with same-size FFN)
```

### 3.2 消融实验的运行次数

**推荐：** 至少5次独立运行，报告均值±标准差

**报告格式：**
```
| Variant | MAE (mean ± std) | ΔMAE | p-value |
|---------|------------------|------|---------|
| Full Model | 2.49 ± 0.03 | - | - |
| w/o Module A | 2.58 ± 0.04 | +0.09 | < 0.01 |
| w/o Module B | 2.62 ± 0.05 | +0.13 | < 0.001 |
```

### 3.3 超参数搜索对消融的影响

**问题：** 如果Full Model和消融变体使用不同的超参数，消融结论不可靠。

**解决方案：**
- 所有变体使用相同的超参数搜索范围
- 报告超参数搜索的结果（如最佳学习率）
- 如果超参数差异很大，说明这一点

---

## 四、多数据集上的多重比较

### 4.1 问题

在4个数据集上比较5个方法，进行20次检验，即使所有方法相同，也有60%的概率至少有一次"显著"。

### 4.2 解决方案

**Bonferroni校正：**
```
校正后的显著性水平 = α / 比较次数
例：α = 0.05, 20次比较 → 校正后α = 0.0025
```

**Holm校正（更宽松）：**
```
将p值从小到大排序
第i个比较的显著性水平 = α / (n - i + 1)
```

**报告格式：**
```
After Holm correction for multiple comparisons (20 tests), 
the improvement remains significant on METR-LA (p < 0.01) 
and PEMS-BAY (p < 0.05), but not on PEMS04 (p = 0.12).
```

---

## 五、Python代码模板

### 5.1 配对t检验

```python
from scipy import stats
import numpy as np

def paired_t_test(ours, baseline, name="Method"):
    """配对t检验"""
    t_stat, p_value = stats.ttest_rel(ours, baseline)
    print(f"{name} vs Baseline:")
    print(f"  Ours: {np.mean(ours):.4f} ± {np.std(ours):.4f}")
    print(f"  Baseline: {np.mean(baseline):.4f} ± {np.std(baseline):.4f}")
    print(f"  t-statistic: {t_stat:.4f}")
    print(f"  p-value: {p_value:.6f}")
    print(f"  Significant (p < 0.05): {p_value < 0.05}")
    return t_stat, p_value

# 示例
ours = [2.49, 2.51, 2.48, 2.52, 2.47]  # 5次运行
baseline = [2.69, 2.71, 2.68, 2.72, 2.67]  # 5次运行
paired_t_test(ours, baseline, "STAEformer")
```

### 5.2 Wilcoxon符号秩检验

```python
def wilcoxon_test(ours, baseline, name="Method"):
    """Wilcoxon符号秩检验（不假设正态分布）"""
    stat, p_value = stats.wilcoxon(ours, baseline)
    print(f"{name} vs Baseline:")
    print(f"  Wilcoxon statistic: {stat:.4f}")
    print(f"  p-value: {p_value:.6f}")
    return stat, p_value
```

### 5.3 Cohen's d效应量

```python
def cohens_d(ours, baseline):
    """计算Cohen's d效应量"""
    n1, n2 = len(ours), len(baseline)
    var1, var2 = np.var(ours, ddof=1), np.var(baseline, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    d = (np.mean(ours) - np.mean(baseline)) / pooled_std
    
    if abs(d) < 0.2:
        effect = "negligible"
    elif abs(d) < 0.5:
        effect = "small"
    elif abs(d) < 0.8:
        effect = "medium"
    else:
        effect = "large"
    
    print(f"Cohen's d: {d:.4f} ({effect} effect)")
    return d
```

### 5.4 多数据集Friedman检验

```python
def friedman_test_multi_dataset(results_dict):
    """
    多数据集上的Friedman检验
    results_dict: {dataset_name: {method_name: [runs]}}
    """
    # 提取方法名
    methods = list(list(results_dict.values())[0].keys())
    n_datasets = len(results_dict)
    n_methods = len(methods)
    
    # 构建矩阵
    matrix = []
    for dataset, methods_results in results_dict.items():
        row = [np.mean(methods_results[m]) for m in methods]
        matrix.append(row)
    
    matrix = np.array(matrix)
    
    # Friedman检验
    stat, p_value = stats.friedmanchisquare(*[matrix[:, i] for i in range(n_methods)])
    
    print(f"Friedman test (χ² = {stat:.4f}, p = {p_value:.6f})")
    print(f"Significant (p < 0.05): {p_value < 0.05}")
    
    if p_value < 0.05:
        # Nemenyi事后检验
        print("\nSignificant differences found. Consider Nemenyi post-hoc test.")
    
    return stat, p_value
```

---

## 六、自查清单

- [ ] 实验结果报告了均值±标准差
- [ ] 实验至少运行5次
- [ ] 显著性检验已进行（配对t检验或Wilcoxon）
- [ ] p值已报告
- [ ] 效应量已计算（Cohen's d）
- [ ] 多数据集比较已校正（Bonferroni或Holm）
- [ ] 消融实验控制了变量数量
- [ ] 消融实验使用了相同的超参数搜索范围

---

> 更新时间：2026-06-20
