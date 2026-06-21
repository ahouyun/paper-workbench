# 代码复现指南 (Reproducibility Guide)

> 确保论文实验可复现，满足IEEE期刊的可复现性要求。

---

## 一、为什么可复现性重要

**编辑的原话：** "论文被接收的前提之一是可复现性。该技能没有任何关于代码组织、实验配置文件、随机种子控制、结果日志记录的指导。"

**IEEE要求：**
- IEEE鼓励作者公开代码和数据
- 审稿人可能要求查看代码验证结果
- 可复现性是论文质量的重要指标

---

## 二、随机种子控制（必须）

### PyTorch随机种子设置

```python
import torch
import numpy as np
import random
import os

def set_seed(seed: int = 42):
    """设置所有随机种子，确保实验可复现"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ['PYTHONHASHSEED'] = str(seed)

# 在训练开始时调用
set_seed(42)
```

### 多次运行报告均值和标准差

```python
def run_multiple_seeds(train_fn, seeds=[42, 43, 44, 45, 46]):
    """多次运行实验，报告均值和标准差"""
    results = []
    for seed in seeds:
        set_seed(seed)
        result = train_fn()
        results.append(result)
    
    # 计算均值和标准差
    mean = np.mean(results)
    std = np.std(results)
    print(f"Result: {mean:.4f} ± {std:.4f}")
    return mean, std
```

**报告格式：**
- MAE: 2.49 ± 0.03 (5次运行)
- RMSE: 4.99 ± 0.05 (5次运行)

---

## 三、项目目录结构

```
project/
├── configs/                  # 配置文件
│   ├── default.yaml          # 默认配置
│   ├── metr-la.yaml          # METR-LA数据集配置
│   ├── pems-bay.yaml         # PEMS-BAY数据集配置
│   └── pems04.yaml           # PEMS04数据集配置
├── src/                      # 源代码
│   ├── data/                 # 数据处理
│   │   ├── dataset.py        # 数据集类
│   │   ├── preprocessor.py   # 数据预处理
│   │   └── utils.py          # 数据工具
│   ├── models/               # 模型定义
│   │   ├── staeformer.py     # 模型实现
│   │   └── layers.py         # 网络层
│   ├── training/             # 训练逻辑
│   │   ├── trainer.py        # 训练器
│   │   └── optimizer.py      # 优化器
│   └── utils/                # 工具函数
│       ├── seed.py           # 随机种子
│       ├── metrics.py        # 评估指标
│       └── logger.py         # 日志
├── scripts/                  # 运行脚本
│   ├── train.py              # 训练脚本
│   ├── evaluate.py           # 评估脚本
│   └── run_all.sh            # 批量运行
├── data/                     # 数据（DVC管理或说明下载方式）
├── checkpoints/              # 模型检查点
├── logs/                     # 实验日志
├── results/                  # 实验结果
├── requirements.txt          # 依赖
├── README.md                 # 项目说明
├── CITATION.cff              # 引用信息
└── LICENSE                   # 许可证
```

---

## 四、配置文件管理

### YAML配置文件示例

```yaml
# configs/default.yaml
data:
  dataset: "METR-LA"
  data_dir: "./data/METR-LA"
  seq_len: 12          # 输入序列长度（12步 = 1小时）
  pred_len: 12         # 预测序列长度（12步 = 1小时）
  train_ratio: 0.7
  val_ratio: 0.1
  test_ratio: 0.2
  normalizer: "z-score"

model:
  name: "STAEformer"
  d_model: 512
  n_heads: 8
  n_layers: 3
  dropout: 0.1

training:
  seed: 42
  batch_size: 64
  learning_rate: 0.001
  weight_decay: 0.0001
  epochs: 100
  patience: 20
  optimizer: "Adam"
  scheduler: "CosineAnnealingLR"

evaluation:
  metrics: ["MAE", "RMSE", "MAPE"]
  horizons: [3, 6, 12]  # 15min, 30min, 60min
```

---

## 五、实验结果记录

### 必须记录的信息

| 信息 | 说明 | 示例 |
|------|------|------|
| 随机种子 | 所有随机种子 | seed=42 |
| 超参数 | 所有超参数值 | lr=0.001, batch_size=64 |
| 数据划分 | 训练/验证/测试比例 | 7:1:2 |
| 归一化方法 | 数据归一化方式 | Z-score |
| 硬件环境 | GPU型号、内存 | NVIDIA A100 40GB |
| 软件版本 | PyTorch、CUDA版本 | PyTorch 2.0, CUDA 11.8 |
| 训练时间 | 总训练时间 | 6.5 hours |
| 最佳epoch | 早停时的epoch | epoch 67 |

### 结果日志模板

```markdown
## 实验结果日志

**实验名称**: STAEformer on METR-LA
**日期**: 2026-06-20
**随机种子**: 42, 43, 44, 45, 46

### 环境
- GPU: NVIDIA A100 40GB
- PyTorch: 2.0.1
- CUDA: 11.8
- Python: 3.10

### 超参数
- Learning rate: 0.001
- Batch size: 64
- Epochs: 100 (early stop at 67)
- Optimizer: Adam

### 结果 (5次运行)
| Horizon | MAE | RMSE | MAPE |
|---------|-----|------|------|
| 15min | 2.49 ± 0.03 | 4.99 ± 0.05 | 6.50% ± 0.12% |
| 30min | 2.78 ± 0.04 | 5.55 ± 0.06 | 7.80% ± 0.15% |
| 60min | 3.15 ± 0.05 | 6.35 ± 0.07 | 9.80% ± 0.18% |

### 训练时间
- 平均每个epoch: 5.8分钟
- 总训练时间: 6.5小时
```

---

## 六、README模板

```markdown
# [Model Name]

This repository contains the implementation of [Model Name] for 
traffic flow prediction, as described in our paper "[Paper Title]".

## Requirements

- Python 3.8+
- PyTorch 2.0+
- numpy, pandas, scipy

## Installation

```bash
pip install -r requirements.txt
```

## Data

Download the datasets from [link] and place them in `data/` directory.

## Training

```bash
# Train on METR-LA
python scripts/train.py --config configs/metr-la.yaml

# Train on PEMS-BAY
python scripts/train.py --config configs/pems-bay.yaml
```

## Evaluation

```bash
python scripts/evaluate.py --config configs/metr-la.yaml --checkpoint checkpoints/best.pt
```

## Results

| Dataset | Horizon | MAE | RMSE | MAPE |
|---------|---------|-----|------|------|
| METR-LA | 15min | 2.49 ± 0.03 | 4.99 ± 0.05 | 6.50% |
| METR-LA | 30min | 2.78 ± 0.04 | 5.55 ± 0.06 | 7.80% |
| METR-LA | 60min | 3.15 ± 0.05 | 6.35 ± 0.07 | 9.80% |

## Citation

```bibtex
@article{yourpaper2026,
  title={Your Paper Title},
  author={Your Name},
  journal={IEEE TITS},
  year={2026}
}
```

## License

MIT License
```

---

## 七、自查清单

- [ ] 所有随机种子已设置（Python, NumPy, PyTorch, CUDA）
- [ ] 实验结果报告均值±标准差（至少3次运行）
- [ ] 配置文件已保存（YAML/JSON格式）
- [ ] 依赖已锁定（requirements.txt或environment.yml）
- [ ] 数据下载/预处理步骤已文档化
- [ ] README包含完整的训练和评估命令
- [ ] 结果与论文中报告的数字一致
- [ ] 代码在干净环境中可以运行

---

> 来源：PyTorch Lightning, lightning-hydra-template, The Turing Way
> 更新时间：2026-06-20
