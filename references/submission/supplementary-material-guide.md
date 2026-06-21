# 补充材料指南 (Supplementary Material Guide)

> 什么放主文，什么放补充材料，如何组织补充材料。

---

## 一、主文 vs 补充材料

### 放在主文的内容

| 内容 | 原因 |
|------|------|
| 核心方法描述 | 审稿人需要理解你的方法 |
| 主要实验结果 | 支撑你的核心贡献 |
| 关键消融实验 | 验证设计选择 |
| 标准数据集描述 | 审稿人需要了解实验设置 |
| 与主要基线的对比 | 支撑性能声明 |

### 放在补充材料的内容

| 内容 | 原因 |
|------|------|
| 额外数据集结果 | 主文空间有限 |
| 超参数敏感性分析 | 细节性分析 |
| 额外的消融实验 | 补充验证 |
| 算法伪代码 | 实现细节 |
| 证明和推导 | 数学细节 |
| 可视化补充 | 额外的图和表 |
| 代码和数据说明 | 可复现性 |

---

## 二、补充材料结构

### 推荐结构

```
Supplementary Material

S1. Dataset Details
    S1.1 Dataset Statistics
    S1.2 Data Preprocessing
    S1.3 Train/Validation/Test Split

S2. Model Architecture Details
    S2.1 Layer Configuration
    S2.2 Hyperparameter Settings
    S2.3 Computational Complexity Analysis

S3. Additional Experimental Results
    S3.1 Results on Additional Datasets
    S3.2 Results with Different Prediction Horizons
    S3.3 Results with Different Training Sizes

S4. Ablation Studies
    S4.1 Component Ablation
    S4.2 Hyperparameter Sensitivity
    S4.3 Design Choice Analysis

S5. Visualization
    S5.1 Attention Visualization
    S5.2 Prediction Examples
    S5.3 Error Analysis

S6. Reproducibility
    S6.1 Code Repository
    S6.2 Random Seed Settings
    S6.3 Hardware and Software Environment
```

---

## 三、各部分写作要点

### S1. 数据集详情

```markdown
## S1. Dataset Details

### S1.1 Dataset Statistics

| Dataset | Sensors | Time Range | Sampling | Type |
|---------|---------|------------|----------|------|
| METR-LA | 207 | Mar-Jun 2012 | 5 min | Speed |
| PEMS-BAY | 325 | Jan-Jun 2017 | 5 min | Speed |
| PEMS04 | 307 | Jan-Feb 2018 | 5 min | Flow |
| PEMS08 | 170 | Jul-Aug 2016 | 5 min | Flow |

### S1.2 Data Preprocessing

- Missing values: Linear interpolation
- Normalization: Z-score (mean and std computed on training set)
- Input sequence length: 12 steps (1 hour)
- Prediction sequence length: 12 steps (1 hour)

### S1.3 Train/Validation/Test Split

| Dataset | Train | Validation | Test |
|---------|-------|------------|------|
| METR-LA | 70% | 10% | 20% |
| PEMS-BAY | 70% | 10% | 20% |
| PEMS04 | 60% | 20% | 20% |
| PEMS08 | 60% | 20% | 20% |
```

### S2. 模型架构细节

```markdown
## S2. Model Architecture Details

### S2.1 Layer Configuration

| Layer | Output Size | Parameters |
|-------|-------------|------------|
| Input Embedding | (B, T, N, D) | - |
| Spatial Attention | (B, T, N, D) | 4D² |
| Temporal Attention | (B, T, N, D) | 4D² |
| Feed-Forward | (B, T, N, D) | 8D² |
| Output Projection | (B, T', N, 1) | D |

Total parameters: 8.2M

### S2.2 Hyperparameter Settings

| Hyperparameter | Value | Search Range |
|---------------|-------|--------------|
| Learning rate | 0.001 | [0.0001, 0.01] |
| Batch size | 64 | [32, 64, 128] |
| Hidden dimension | 512 | [256, 512, 1024] |
| Number of heads | 8 | [4, 8, 16] |
| Number of layers | 3 | [2, 3, 4] |
| Dropout | 0.1 | [0.0, 0.1, 0.2] |
```

### S3. 额外实验结果

```markdown
## S3. Additional Experimental Results

### S3.1 Results on PEMS03 and PEMS07

| Model | PEMS03 MAE | PEMS03 RMSE | PEMS07 MAE | PEMS07 RMSE |
|-------|------------|-------------|------------|-------------|
| DCRNN | 18.76 | 29.18 | 22.93 | 35.22 |
| STGCN | 15.74 | 25.28 | 19.32 | 31.27 |
| GWNet | 16.88 | 27.36 | 18.24 | 30.48 |
| Ours | 15.12 | 24.56 | 17.38 | 28.95 |

### S3.2 Results with Different Training Sizes

| Training % | MAE | RMSE | MAPE |
|------------|-----|------|------|
| 20% | 2.85 | 5.62 | 7.45% |
| 40% | 2.68 | 5.35 | 7.12% |
| 60% | 2.55 | 5.15 | 6.85% |
| 80% | 2.52 | 5.08 | 6.72% |
| 100% | 2.49 | 4.99 | 6.50% |
```

### S4. 消融实验

```markdown
## S4. Ablation Studies

### S4.1 Component Ablation

| Variant | MAE | RMSE | MAPE | ΔMAE |
|---------|-----|------|------|------|
| Full Model | 2.49 | 4.99 | 6.50% | - |
| w/o Spatial Attention | 2.58 | 5.12 | 6.72% | +0.09 |
| w/o Temporal Attention | 2.62 | 5.18 | 6.85% | +0.13 |
| w/o Adaptive Embedding | 2.55 | 5.08 | 6.68% | +0.06 |
| w/o Delay Modeling | 2.71 | 5.35 | 7.12% | +0.22 |

### S4.2 Hyperparameter Sensitivity

| Hidden Dim | MAE | Params | Training Time |
|------------|-----|--------|---------------|
| 256 | 2.58 | 2.1M | 3.2h |
| 512 | 2.49 | 8.2M | 6.5h |
| 1024 | 2.47 | 32.8M | 14.2h |
```

---

## 四、补充材料格式要求

### 4.1 文件格式

- PDF格式（便于阅读）
- 包含页码和页眉
- 包含目录

### 4.2 图表要求

- 与主文相同的图表规范
- 图表编号以"S"开头（Figure S1, Table S1）
- 图表标题完整清晰

### 4.3 引用规范

- 从主文引用补充材料："See Supplementary Material, Section S3.1"
- 从补充材料引用主文："See main paper, Table 1"

---

## 五、自查清单

- [ ] 补充材料包含完整的数据集描述
- [ ] 补充材料包含完整的超参数设置
- [ ] 补充材料包含额外的实验结果
- [ ] 补充材料包含详细的消融实验
- [ ] 补充材料包含可复现性信息
- [ ] 图表编号以"S"开头
- [ ] 主文正确引用了补充材料
- [ ] 补充材料格式符合期刊要求

---

> 更新时间：2026-06-20
