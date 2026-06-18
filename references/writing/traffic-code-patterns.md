# 交通流预测代码模式与项目结构分析

> 基于 Graph WaveNet, STAEformer, MegaCRN, LibCity, BasicTS 等顶级GitHub仓库的系统性分析。

---

## 一、项目结构与目录组织

### 1.1 三种主流结构范式

**范式一：扁平式结构（Graph WaveNet, MegaCRN）**

```
Graph-WaveNet/
├── model.py              # 模型定义
├── engine.py             # 训练器封装
├── train.py              # 训练入口
├── test.py               # 测试脚本
├── util.py               # 工具函数
├── generate_training_data.py  # 数据预处理
├── data/                 # 数据目录
└── fig/                  # 架构图
```

特点：文件数量少（6个Python文件），职责划分清晰但粒度粗。

**范式二：分层式结构（STAEformer）**

```
STAEformer/
├── model/
│   ├── train.py
│   └── STAEformer.py
├── lib/
│   ├── utils.py
│   └── dataloader.py
└── data/
```

特点：模型代码与工具代码分目录存放。

**范式三：框架级模块化结构（LibCity, BasicTS）**

```
Bigscity-LibCity/
├── libcity/
│   ├── config/           # 配置系统
│   ├── data/             # 数据模块
│   │   └── dataset/
│   │       └── traffic_state_dataset.py
│   ├── model/            # 模型实现（按任务分类）
│   │   └── traffic_flow_prediction/
│   ├── executor/         # 执行器
│   │   └── traffic_state_executor.py
│   ├── evaluator/        # 评估指标
│   ├── pipeline/         # 端到端流水线
│   └── utils/
├── run_model.py
└── run_hyper.py          # 超参数搜索
```

特点：最完整的框架级设计，支持74个模型、52个数据集。

### 1.2 文件命名惯例

| 仓库 | 模型文件 | 训练文件 | 工具文件 |
|------|---------|---------|---------|
| Graph WaveNet | `model.py` | `train.py` | `util.py` |
| STAEformer | `STAEformer.py` | `train.py` | `utils.py` |
| MegaCRN | `MegaCRN.py` | `traintest_MegaCRN.py` | `utils.py` |
| LibCity | `{ModelName}.py` | 由Executor处理 | `utils.py` |

---

## 二、数据处理模式

### 2.1 数据加载

**Graph WaveNet模式：HDF5 → NumPy → DataLoader**
```python
df = pd.read_hdf(args.traffic_df_filename)
x, y = generate_graph_seq2seq_io_data(df, x_offsets, y_offsets,
                                       add_time_in_day=True, add_day_in_week=False)
# 按时间顺序划分：70% 训练 / 10% 验证 / 20% 测试
num_test = round(num_samples * 0.2)
num_train = round(num_samples * 0.7)
np.savez_compressed(os.path.join(args.output_dir, f"{cat}.npz"), x=_x, y=_y)
```

**LibCity模式：原子文件格式**
- 定义 `.geo`, `.rel`, `.dyna`, `.grid`, `.od` 等原子文件格式
- 通过 `TrafficStateDataset` 类统一加载

### 2.2 数据标准化

所有仓库统一使用 `StandardScaler` 进行Z-score标准化：

```python
class StandardScaler:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def transform(self, data):
        return (data - self.mean) / self.std

    def inverse_transform(self, data):
        return (data * self.std) + self.mean
```

**关键原则**：标准化参数仅从训练集计算，然后应用到验证集和测试集。

LibCity支持更多方式：`normal`（除以最大值）、`standard`（Z-score）、`minmax01`、`minmax11`、`log`。

### 2.3 滑动窗口采样

```python
x_offsets = np.sort(np.arange(-(input_window - 1), 1, 1))  # [-11, -10, ..., 0]
y_offsets = np.sort(np.arange(1, output_window + 1, 1))     # [1, 2, ..., 12]

for t in range(min_t, max_t):
    x.append(data[t + x_offsets, ...])  # shape: (input_window, num_nodes, features)
    y.append(data[t + y_offsets, ...])  # shape: (output_window, num_nodes, features)
```

输出形状：`(num_samples, seq_len, num_nodes, input_dim)`

### 2.4 时间特征工程

```python
# Graph WaveNet
time_ind = (df.index.values - df.index.values.astype("datetime64[D]")) / np.timedelta64(1, "D")
time_in_day = np.tile(time_ind, [1, num_nodes, 1]).transpose((2, 1, 0))

# STAEformer
tod = x[..., 1]  # time of day
dow = x[..., 2]  # day of week
tod_emb = self.tod_embedding((tod * self.steps_per_day).long())
dow_emb = self.dow_embedding(dow.long())
```

常见时间特征：Time-of-Day（归一化到[0,1]或离散化为288个slot）、Day-of-Week（0-6）。

### 2.5 图构建

**Graph WaveNet的自适应邻接矩阵学习**：
```python
self.nodevec1 = nn.Parameter(torch.randn(num_nodes, 10))
self.nodevec2 = nn.Parameter(torch.randn(10, num_nodes))
# 前向传播中
adp = F.softmax(F.relu(torch.mm(self.nodevec1, self.nodevec2)), dim=1)
```

**邻接矩阵归一化**：
```python
def sym_adj(adj):    # 对称归一化: D^{-1/2} A D^{-1/2}
def asym_adj(adj):   # 行归一化: D^{-1} A
```

---

## 三、模型实现模式

### 3.1 PyTorch模型类结构

```python
class ModelName(nn.Module):
    def __init__(self, num_nodes, in_steps, out_steps, ...):
        super().__init__()
        # 定义层

    def forward(self, x):
        # x: (batch_size, in_steps, num_nodes, input_dim)
        return out  # (batch_size, out_steps, num_nodes, output_dim)
```

**forward签名对比**：
| 仓库 | 输入形状 | 输出形状 |
|------|---------|---------|
| STAEformer | `(B, in_steps, N, input_dim+tod+dow)` | `(B, out_steps, N, output_dim)` |
| Graph WaveNet | `(B, in_dim, N, seq_len)` | `(B, out_dim, N, seq_len)` |
| MegaCRN | `(B, seq_len, N, input_dim)` | `(B, horizon, N, output_dim)` |

### 3.2 注意力机制实现

```python
class AttentionLayer(nn.Module):
    def __init__(self, model_dim, num_heads=8):
        self.head_dim = model_dim // num_heads
        self.FC_Q = nn.Linear(model_dim, model_dim)
        self.FC_K = nn.Linear(model_dim, model_dim)
        self.FC_V = nn.Linear(model_dim, model_dim)

    def forward(self, query, key, value):
        query = torch.cat(torch.split(query, self.head_dim, dim=-1), dim=0)
        key = torch.cat(torch.split(key, self.head_dim, dim=-1), dim=0)
        value = torch.cat(torch.split(value, self.head_dim, dim=-1), dim=0)
        key = key.transpose(-1, -2)
        attn_score = (query @ key) / self.head_dim**0.5
        attn_score = torch.softmax(attn_score, dim=-1)
        out = attn_score @ value
        out = torch.cat(torch.split(out, batch_size, dim=0), dim=-1)
        return self.out_proj(out)
```

STAEformer将注意力分为时间注意力（`attn_layers_t`，沿dim=1）和空间注意力（`attn_layers_s`，沿dim=2），交替堆叠。

### 3.3 图卷积实现

**Graph WaveNet的Einstein求和图卷积**：
```python
class nconv(nn.Module):
    def forward(self, x, A):
        x = torch.einsum('ncvl,vw->ncwl', (x, A))
        return x.contiguous()

class gcn(nn.Module):
    def forward(self, x, support):
        out = [x]  # 残差连接
        for a in support:
            x1 = self.nconv(x, a)
            out.append(x1)
            for k in range(2, self.order + 1):  # 多阶扩散
                x2 = self.nconv(x1, a)
                out.append(x2)
                x1 = x2
        h = torch.cat(out, dim=1)
        return self.mlp(h)
```

**MegaCRN的Chebyshev图卷积**：
```python
class AGCN(nn.Module):
    def forward(self, x, supports):
        support_set = []
        for support in supports:
            support_ks = [torch.eye(support.shape[0]).to(support.device), support]
            for k in range(2, self.cheb_k):  # Chebyshev递推
                support_ks.append(torch.matmul(2 * support, support_ks[-1]) - support_ks[-2])
            support_set.extend(support_ks)
        for support in support_set:
            x_g.append(torch.einsum("nm,bmc->bnc", support, x))
        x_g = torch.cat(x_g, dim=-1)
        return torch.einsum('bni,io->bno', x_g, self.weights) + self.bias
```

### 3.4 不同预测时域的处理

**Graph WaveNet**：输出维度直接设为`out_dim=12`，通过膨胀因果卷积感受野覆盖输入序列。

**STAEformer的混合投影**：
```python
if self.use_mixed_proj:
    self.output_proj = nn.Linear(in_steps * self.model_dim, out_steps * output_dim)
else:
    self.temporal_proj = nn.Linear(in_steps, out_steps)
    self.output_proj = nn.Linear(self.model_dim, self.output_dim)
```

**MegaCRN的解码器逐步生成**：
```python
for t in range(self.horizon):
    h_de, ht_list = self.decoder(torch.cat([go, y_cov[:, t, ...]], dim=-1), ht_list, supports)
    go = self.proj(h_de)
    out.append(go)
```

---

## 四、训练流水线

### 4.1 训练循环结构

交通预测使用标准PyTorch训练循环（`model.train()` → `optimizer.zero_grad()` → `forward` → `loss.backward()` → `clip_grad_norm_` → `optimizer.step()`），配合`model.eval()`和`torch.no_grad()`进行验证。关键差异在于数据形状为`(batch_size, seq_len, num_nodes, features)`，以及使用masked loss处理缺失值。

### 4.2 损失函数选择

| 仓库 | 主要损失函数 | 特殊损失 |
|------|------------|---------|
| Graph WaveNet | Masked MAE | - |
| STAEformer (METRLA/PEMSBAY) | Masked MAE | - |
| STAEformer (PEMS03/04/07/08) | Huber Loss | - |
| MegaCRN | Masked MAE | TripletMarginLoss + MSELoss |
| LibCity | 可配置 | MAE/MSE/RMSE/MAPE/LogCosh/Huber/Quantile |

**Masked MAE实现**：
```python
def masked_mae_loss(preds, labels, null_val=0.0):
    if np.isnan(null_val):
        mask = ~torch.isnan(labels)
    else:
        mask = labels != null_val
    mask = mask.float()
    mask /= torch.mean(mask)
    loss = torch.abs(preds - labels) * mask
    loss = torch.where(torch.isnan(loss), torch.zeros_like(loss), loss)
    return torch.mean(loss)
```

**MegaCRN的复合损失**：
```python
loss1 = masked_mae_loss(y_pred, y_true)
loss2 = nn.TripletMarginLoss(margin=1.0)(query, pos, neg)
loss3 = nn.MSELoss()(query, pos)
loss = loss1 + lamb * loss2 + lamb1 * loss3
```

### 4.3 优化器与学习率调度

所有仓库统一使用Adam优化器（`lr=0.001或0.01`, `weight_decay=0或0.0001`），配合`MultiStepLR`（milestones=[50, 100], gamma=0.1）进行学习率衰减。详见标准PyTorch训练模式。

### 4.4 Early Stopping与Checkpoint

使用标准Early Stopping模式（patience=20或50），在验证集loss不再下降时停止训练。Checkpoint策略因仓库而异：Graph WaveNet每个epoch保存，MegaCRN仅保存最佳模型，LibCity同时保存模型和优化器状态。

---

## 五、评估模式

### 5.1 指标计算

```python
def metric(pred, real):
    mae = masked_mae(pred, real, 0.0).item()
    mape = masked_mape(pred, real, 0.0).item()
    rmse = masked_rmse(pred, real, 0.0).item()
    return mae, mape, rmse
```

### 5.2 分步评估

```python
# 按预测步长分别报告
for i in range(12):
    pred = scaler.inverse_transform(yhat[:, :, i])
    real = realy[:, :, i]
    metrics = util.metric(pred, real)
    amae.append(metrics[0])
    amape.append(metrics[1])
    armse.append(metrics[2])

# 报告特定步长
l_3, m_3, r_3 = masked_mae_loss(y_pred[2:3], y_true[2:3])   # 15分钟
l_6, m_6, r_6 = masked_mae_loss(y_pred[5:6], y_true[5:6])   # 30分钟
l_12, m_12, r_12 = masked_mae_loss(y_pred[11:12], y_true[11:12])  # 60分钟
```

---

## 六、配置管理

### 6.1 配置方式对比

| 仓库 | 配置方式 | 格式 |
|------|---------|------|
| Graph WaveNet | argparse命令行参数 | 命令行 |
| STAEformer | YAML配置文件 + argparse | YAML |
| MegaCRN | argparse命令行参数 | 命令行 |
| LibCity | JSON配置文件 + argparse | JSON |
| BasicTS | 配置文件 + EasyTorch | YAML/Python |

### 6.2 常见超参数默认值

| 参数 | Graph WaveNet | STAEformer | MegaCRN | LibCity |
|------|--------------|------------|---------|---------|
| batch_size | 64 | 64 | 64 | 64 |
| learning_rate | 0.001 | - | 0.01 | 0.01 |
| epochs | 100 | - | 200 | 100 |
| hidden_dim | 32 | 24+24+24+80 | 64 | - |
| dropout | 0.3 | 0.1 | - | - |
| weight_decay | 0.0001 | 0 | 0 | 0 |
| patience | - | - | 20 | 50 |
| grad_clip | 5 | - | 5 | 1.0 |
| num_heads | - | 4 | - | - |
| num_layers | 4blocks×2layers | 3 | 1 | - |

---

## 七、关键发现与最佳实践

### 7.1 代码模式共性

1. **数据形状统一**：`(batch_size, seq_len, num_nodes, features)` 或其转置
2. **标准化一致性**：全部Z-score，参数仅从训练集计算
3. **评估指标统一**：MAE、MAPE、RMSE，masked版本处理缺失值
4. **训练流程标准化**：Adam + MultiStepLR + 梯度裁剪 + Early Stopping
5. **时间特征嵌入**：Time-of-Day 和 Day-of-Week 作为标准输入

### 7.2 架构演进趋势

- **早期**（Graph WaveNet）：扁平结构，argparse配置
- **中期**（STAEformer, MegaCRN）：分层目录，YAML配置
- **当前**（LibCity, BasicTS）：框架级设计，配置驱动

### 7.3 值得借鉴的设计

1. **LibCity的原子文件格式**：统一的数据接口
2. **STAEformer的混合投影**：灵活的输出投影策略
3. **MegaCRN的对比学习损失**：TripletMarginLoss + MSELoss
4. **Graph WaveNet的自适应邻接**：可学习节点嵌入矩阵
5. **BasicTS的"三行代码"理念**：最小化用户代码量

---

## 八、常见"交通预测代码味道"

### 8.1 典型Bug陷阱

- **数据泄露**：标准化参数从全量数据计算而非仅训练集
- **时间序列随机划分**：应按时间顺序划分，不能随机
- **缺失值处理不当**：应使用masked loss而非简单填充
- **评估时未反归一化**：应在原始尺度上计算指标

### 8.2 性能瓶颈

- **图卷积的O(N²)复杂度**：大规模路网上计算昂贵
- **注意力机制的内存占用**：长序列上容易OOM
- **数据加载I/O**：HDF5格式比NumPy更快

### 8.3 可复现性保障

- 固定随机种子：`torch.manual_seed(seed)`
- 记录所有超参数
- 保存最佳模型checkpoint
- 使用统一评估框架（LibCity/BasicTS）

---

## 九、Mamba/SSM 代码实现模式

### 9.1 标准Mamba块调用

所有Mamba交通预测项目通常直接调用官方CUDA kernel：

```python
from mamba_ssm import Mamba

class MambaBlock(nn.Module):
    def __init__(self, d_model, d_state=16, d_conv=4, expand=2):
        super().__init__()
        self.mamba = Mamba(d_model=d_model, d_state=d_state, d_conv=d_conv, expand=expand)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x):
        # x: (B, L, D)
        return self.norm(x + self.mamba(x))  # 残差连接
```

### 9.2 空间扫描策略实现

**策略一：按节点索引扫描（简单版，ST-Mamba）**
```python
# 对每个时间步，沿节点维度扫描
x_spatial = x.permute(0, 1, 3, 2).reshape(B*T, D, N)  # (B*T, D, N)
h_spatial = self.spatial_mamba(x_spatial)
```

**策略二：按图拓扑扫描（SpoT-Mamba）**
```python
# BFS序生成扫描顺序
scan_order = self._topological_bfs_order(adj_matrix)
x_reordered = x[:, :, scan_order, :]  # 按拓扑序重排
h = self.mamba(x_reordered)  # Mamba扫描
# 恢复原始顺序
out = out[:, :, self._inverse_permutation(scan_order), :]
```

**策略三：双向Mamba（DST-Mamba）**
```python
class BidirectionalMamba(nn.Module):
    def __init__(self, d_model, d_state=16):
        super().__init__()
        self.forward_mamba = Mamba(d_model, d_state=d_state)
        self.backward_mamba = Mamba(d_model, d_state=d_state)
        self.merge = nn.Linear(d_model * 2, d_model)

    def forward(self, x):
        h_fwd = self.forward_mamba(x)           # 正向
        h_bwd = self.backward_mamba(x.flip(1))  # 反向
        h_bwd = h_bwd.flip(1)                   # 翻转回来
        return self.merge(torch.cat([h_fwd, h_bwd], dim=-1))
```

**策略四：三路Mamba（STM3, KDD'26）**
```python
class STM3Block(nn.Module):
    """空间扫描 + 时间扫描 + 时空联合扫描"""
    def forward(self, x):
        # 路径1: 空间扫描 - 沿节点维度
        h_spatial = self.spatial_mamba(x.permute(0,1,3,2).reshape(B*T, D, N))
        # 路径2: 时间扫描 - 沿时间维度
        h_temporal = self.temporal_mamba(x.permute(0,2,3,1).reshape(B*N, D, T))
        # 路径3: 联合扫描 - 展平时空
        h_fused = self.fused_mamba(x.permute(0,3,1,2).reshape(B, D, T*N))
        # 门控融合
        return self.gate(torch.cat([h_spatial, h_temporal, h_fused], dim=-1))
```

### 9.3 GNN+Mamba的主流范式

```python
class GNN_Mamba_Model(nn.Module):
    """GNN(空间) + Mamba(时间) 两阶段设计"""
    def __init__(self, num_nodes, d_model, n_layers):
        super().__init__()
        self.gcn_layers = nn.ModuleList([GraphConv(d_model, d_model) for _ in range(n_layers)])
        self.mamba_layers = nn.ModuleList([MambaBlock(d_model) for _ in range(n_layers)])

    def forward(self, x, adj):
        B, T, N, C = x.shape
        # 空间建模：对每个时间步做图卷积
        for t in range(T):
            for gcn in self.gcn_layers:
                x[:, t] = gcn(x[:, t], adj)
        # 时间建模：对每个节点做Mamba扫描
        for n in range(N):
            for mamba in self.mamba_layers:
                x[:, :, n, :] = mamba(x[:, :, n, :])
        return x
```

---

## 十、扩散模型代码实现模式

### 10.1 前向扩散过程

```python
class GaussianDiffusion(nn.Module):
    def __init__(self, n_steps=50, beta_start=1e-4, beta_end=0.02):
        super().__init__()
        self.betas = torch.linspace(beta_start, beta_end, n_steps)
        self.alphas = 1.0 - self.betas
        self.alpha_cumprod = torch.cumprod(self.alphas, dim=0)

    def forward_diffusion(self, x0, t, noise=None):
        """q(x_t | x_0) = N(sqrt(α_cumprod)*x0, (1-α_cumprod)*I)"""
        if noise is None:
            noise = torch.randn_like(x0)
        sqrt_alpha = self.alpha_cumprod[t][:, None, None, None]
        sqrt_one_minus_alpha = (1 - self.alpha_cumprod[t])[:, None, None, None]
        return sqrt_alpha * x0 + sqrt_one_minus_alpha * noise, noise
```

### 10.2 反向去噪采样

```python
def sample(self, shape, denoise_net, cond, n_steps=50):
    """DDPM采样：从纯噪声生成预测"""
    x = torch.randn(shape, device=cond.device)
    for t in reversed(range(n_steps)):
        t_batch = torch.full((shape[0],), t, device=cond.device, dtype=torch.long)
        predicted_noise = denoise_net(x, t_batch, cond)
        # 去噪公式
        alpha_t = self.alphas[t]
        alpha_cumprod_t = self.alpha_cumprod[t]
        beta_t = self.betas[t]
        mean = (1/sqrt(alpha_t)) * (x - beta_t/sqrt(1-alpha_cumprod_t) * predicted_noise)
        if t > 0:
            x = mean + sqrt(beta_t) * torch.randn_like(x)
        else:
            x = mean
    return x
```

### 10.3 条件注入方式

**方式一：拼接+掩码标记（CSDI）**
```python
# 条件部分标记为0，目标部分标记为1
cond_mask = torch.zeros(B, N, cond_len)
target_mask = torch.ones(B, N, target_len)
x_input = torch.cat([cond, x_t], dim=-1)  # 拼接
mask_input = torch.cat([cond_mask, target_mask], dim=-1).long()
h = feature_embed(x_input) + cond_mask_embed(mask_input)  # 加入标记
```

**方式二：Cross-Attention（DiffSTG）**
```python
# 条件信息作为Key和Value
cross_attn_out = self.cross_attn(
    query=x_t_embed,      # 加噪的目标
    key=cond_embed,        # 历史观测
    value=cond_embed       # 历史观测
)
```

### 10.4 训练损失

```python
def training_loss(self, x0, denoise_net, cond):
    """训练：预测噪声的MSE"""
    t = torch.randint(0, self.n_steps, (x0.shape[0],))
    x_t, noise = self.forward_diffusion(x0, t)
    predicted_noise = denoise_net(x_t, t, cond)
    return F.mse_loss(predicted_noise, noise)
```

---

## 十一、LLM适配代码实现模式

### 11.1 冻结LLM+适配器（UrbanGPT模式）

```python
class UrbanGPT(nn.Module):
    def __init__(self, llm_path='meta-llama/Llama-2-7b'):
        super().__init__()
        # 冻结LLM
        self.llm = AutoModelForCausalLM.from_pretrained(llm_path)
        for param in self.llm.parameters():
            param.requires_grad = False
        llm_hidden = self.llm.config.hidden_size  # 4096

        # 可训练适配器
        self.input_adapter = nn.Sequential(
            nn.Linear(512, 1024), nn.GELU(),
            nn.Linear(1024, llm_hidden), nn.LayerNorm(llm_hidden)
        )
        self.output_adapter = nn.Sequential(
            nn.Linear(llm_hidden, 1024), nn.GELU(),
            nn.Linear(1024, pred_len)
        )

    def forward(self, x, adj):
        # 时空编码 → 适配到LLM空间 → 冻结LLM推理 → 输出适配
        st_feat = self.st_encoder(x, adj)        # (B, T*N, 512)
        adapted = self.input_adapter(st_feat)     # (B, T*N, 4096)
        with torch.no_grad():
            llm_out = self.llm(inputs_embeds=adapted).last_hidden_state
        return self.output_adapter(llm_out)       # (B, T*N, pred_len)
```

### 11.2 GPT-2部分冻结（GPT4TS模式）

```python
class GPT4TS(nn.Module):
    def __init__(self, n_layers=6):
        super().__init__()
        self.gpt2 = GPT2Model.from_pretrained('gpt2')
        # 冻结前半部分层
        for i, layer in enumerate(self.gpt2.h):
            if i < n_layers // 2:
                for param in layer.parameters():
                    param.requires_grad = False
        # Patch嵌入
        self.patch_embed = nn.Conv1d(1, 768, kernel_size=16, stride=8)
        # RevIN归一化
        self.revin = RevIN(num_features=1)

    def forward(self, x):
        x = self.revin(x, mode='norm')
        x_patch = self.patch_embed(x.transpose(1,2)).transpose(1,2)
        gpt_out = self.gpt2(inputs_embeds=x_patch).last_hidden_state
        pred = self.head(gpt_out)
        return self.revin(pred, mode='denorm')
```

### 11.3 可逆实例归一化（RevIN）

```python
class RevIN(nn.Module):
    """时序预测的关键技术：可逆实例归一化"""
    def __init__(self, num_features, eps=1e-5):
        super().__init__()
        self.eps = eps
        self.affine_weight = nn.Parameter(torch.ones(num_features))
        self.affine_bias = nn.Parameter(torch.zeros(num_features))

    def forward(self, x, mode):
        if mode == 'norm':
            self.mean = x.mean(dim=1, keepdim=True).detach()
            self.std = x.std(dim=1, keepdim=True).detach()
            x = (x - self.mean) / (self.std + self.eps)
        elif mode == 'denorm':
            x = x * (self.std + self.eps) + self.mean
        return x
```

---

## 十二、2025-2026年新兴代码模式

### 13.1 公平性损失函数

```python
class FairnessLoss(nn.Module):
    """FairTP-style fairness loss with region-based static and sensor-based dynamic fairness."""
    def __init__(self, alpha=0.5, beta=0.3):
        super().__init__()
        self.alpha = alpha  # static fairness weight
        self.beta = beta    # dynamic fairness weight

    def forward(self, pred, target, region_ids, sensor_ids):
        # Base prediction loss
        base_loss = F.l1_loss(pred, target)

        # Region-based static fairness
        region_errors = []
        for region_id in torch.unique(region_ids):
            mask = region_ids == region_id
            region_error = F.l1_loss(pred[mask], target[mask])
            region_errors.append(region_error)
        region_errors = torch.stack(region_errors)
        static_fairness = region_errors.var()  # minimize variance across regions

        # Sensor-based dynamic fairness
        sensor_errors = []
        for sensor_id in torch.unique(sensor_ids):
            mask = sensor_ids == sensor_id
            sensor_error = F.l1_loss(pred[mask], target[mask])
            sensor_errors.append(sensor_error)
        sensor_errors = torch.stack(sensor_errors)
        dynamic_fairness = sensor_errors.var()  # minimize variance across sensors

        return base_loss + self.alpha * static_fairness + self.beta * dynamic_fairness
```

### 13.2 检索增强时空预测

```python
class SpatioTemporalRetrievalStore:
    """RAST-style retrieval store for spatio-temporal patterns."""
    def __init__(self, capacity=1000, embedding_dim=64):
        self.capacity = capacity
        self.keys = []      # (embedding,) for similarity search
        self.values = []    # (pattern,) for retrieval

    def store(self, embedding, pattern):
        """Store a spatio-temporal pattern with its embedding."""
        if len(self.keys) >= self.capacity:
            # Remove oldest entry
            self.keys.pop(0)
            self.values.pop(0)
        self.keys.append(embedding.detach())
        self.values.append(pattern.detach())

    def retrieve(self, query_embedding, k=5):
        """Retrieve k most similar patterns."""
        if len(self.keys) == 0:
            return None

        keys = torch.stack(self.keys)
        similarities = F.cosine_similarity(query_embedding.unsqueeze(0), keys)
        top_k = similarities.topk(k)

        retrieved_patterns = torch.stack([self.values[i] for i in top_k.indices])
        return retrieved_patterns, top_k.values
```

### 13.3 因果图学习

```python
class CausalGraphLearning(nn.Module):
    """ST-HCMs-style causal graph learning for spatio-temporal data."""
    def __init__(self, num_nodes, hidden_dim):
        super().__init__()
        self.num_nodes = num_nodes
        # Learnable causal adjacency matrix
        self.causal_adj = nn.Parameter(torch.randn(num_nodes, num_nodes))
        self.threshold = nn.Parameter(torch.tensor(0.5))

    def forward(self, x):
        # x: (batch, time, nodes, features)
        # Apply sigmoid to get soft adjacency
        soft_adj = torch.sigmoid(self.causal_adj)

        # Apply threshold for hard adjacency
        hard_adj = (soft_adj > self.threshold).float()

        # Use soft adjacency for differentiability
        causal_adj = soft_adj + (hard_adj - soft_adj).detach()

        # Ensure causal direction (upper triangular for temporal ordering)
        causal_adj = causal_adj * torch.triu(torch.ones_like(causal_adj), diagonal=1)

        return causal_adj

    def get_causal_loss(self, pred, target, causal_adj):
        """Causal consistency loss: predictions should respect causal structure."""
        # Causal effect: how much each node influences others
        causal_effect = causal_adj.sum(dim=1)

        # Nodes with stronger causal effects should have lower prediction error
        node_errors = F.l1_loss(pred, target, reduction='none').mean(dim=[0, 1])
        causal_loss = (causal_effect * node_errors).mean()

        return causal_loss
```

### 13.4 知识蒸馏损失

```python
class SpatioTemporalDistillationLoss(nn.Module):
    """LightST-style spatial and temporal knowledge distillation."""
    def __init__(self, alpha=0.5, temperature=3.0):
        super().__init__()
        self.alpha = alpha
        self.temperature = temperature

    def forward(self, student_pred, teacher_pred, target,
                student_spatial, teacher_spatial,
                student_temporal, teacher_temporal):
        # Prediction loss
        pred_loss = F.l1_loss(student_pred, target)

        # Spatial distillation loss
        spatial_loss = F.mse_loss(
            F.log_softmax(student_spatial / self.temperature, dim=-1),
            F.softmax(teacher_spatial / self.temperature, dim=-1)
        )

        # Temporal distillation loss
        temporal_loss = F.mse_loss(
            F.log_softmax(student_temporal / self.temperature, dim=-1),
            F.softmax(teacher_temporal / self.temperature, dim=-1)
        )

        # Combined loss
        total_loss = pred_loss + self.alpha * (spatial_loss + temporal_loss)

        return total_loss
```

### 13.5 OOD检测（变化点检测）

```python
class OODChangePointDetector:
    """Latent Dynamics-Aware OOD detection using quickest changepoint detection."""
    def __init__(self, threshold=3.0, window_size=10):
        self.threshold = threshold
        self.window_size = window_size
        self.error_history = []

    def update(self, prediction_error):
        """Update error history and check for changepoint."""
        self.error_history.append(prediction_error)

        if len(self.error_history) < self.window_size * 2:
            return False, 0.0

        # Compare recent window with historical window
        recent = self.error_history[-self.window_size:]
        historical = self.error_history[-2*self.window_size:-self.window_size]

        # Compute test statistic (e.g., CUSUM)
        recent_mean = np.mean(recent)
        historical_mean = np.mean(historical)
        historical_std = np.std(historical)

        if historical_std == 0:
            return False, 0.0

        # Z-score based detection
        z_score = (recent_mean - historical_mean) / historical_std

        is_ood = z_score > self.threshold
        confidence = min(z_score / self.threshold, 2.0)  # Cap at 2.0

        return is_ood, confidence
```

### 13.6 新增代码仓库

| 仓库 | 论文 | 关键代码模式 |
|------|------|-------------|
| jinguangyin/M3_NET | M3-Net | MLP-Mixer + MoE |
| DILab-USTCSZ/CMuST | CMuST | 多任务持续学习 |
| state-spaces/mamba | Mamba | 选择性扫描CUDA内核 |
| KimMeen/Time-LLM | Time-LLM | LLM重编程层 |
| Tims2D/Times2D | Times2D | 2D变换时间序列 |
| Secilia-Cxy/SOFTS | SOFTS | STAR模块线性复杂度 |
| gmerca/GNeuralFlow | GNeuralFlow | DAG+ODE联合学习 |
| ykrmm/SLATE | SLATE | 超拉普拉斯动态图 |
| xiyuanzh/UniMTS | UniMTS | 运动时间序列预训练 |

### 13.7 2D变换时间序列（Times2D）

```python
class PeriodicDecompositionBlock(nn.Module):
    """Times2D-style periodic decomposition for 1D→2D transformation."""
    def __init__(self, period_lengths=[24, 168, 720]):  # hourly, daily, weekly
        super().__init__()
        self.period_lengths = period_lengths

    def forward(self, x):
        # x: (batch, seq_len, features)
        batch_size, seq_len, features = x.shape

        decomposed = []
        for period in self.period_lengths:
            # Pad to make divisible by period
            pad_len = (period - seq_len % period) % period
            x_padded = F.pad(x, (0, 0, 0, pad_len))

            # Reshape to 2D: (batch, num_periods, period, features)
            num_periods = (seq_len + pad_len) // period
            x_2d = x_padded.reshape(batch_size, num_periods, period, features)

            decomposed.append(x_2d)

        return decomposed
```

### 13.8 STAR模块（SOFTS）

```python
class STARModule(nn.Module):
    """STar Aggregate-Redistribute module for channel interaction."""
    def __init__(self, num_channels, hidden_dim):
        super().__init__()
        self.aggregate = nn.Linear(num_channels, hidden_dim)
        self.redistribute = nn.Linear(hidden_dim, num_channels)

    def forward(self, x):
        # x: (batch, seq_len, channels)
        # Aggregate all channels into global core
        core = self.aggregate(x.mean(dim=1, keepdim=True))  # (batch, 1, hidden)

        # Redistribute to each channel
        output = self.redistribute(core)  # (batch, 1, channels)

        return output.expand_as(x)
```

### 13.9 超拉普拉斯编码（SLATE）

```python
class SupraLaplacianEncoding(nn.Module):
    """SLATE-style supra-Laplacian encoding for dynamic graphs."""
    def __init__(self, num_nodes, num_timesteps, hidden_dim):
        super().__init__()
        self.num_nodes = num_nodes
        self.num_timesteps = num_timesteps

    def forward(self, adj_sequence):
        # adj_sequence: (num_timesteps, num_nodes, num_nodes)
        # Build supra-Laplacian matrix
        # L_supra = D_supra - A_supra
        # where A_supra is block matrix with temporal connections

        supra_adj = self._build_supra_adjacency(adj_sequence)
        supra_laplacian = self._compute_laplacian(supra_adj)

        # Eigendecomposition for spectral encoding
        eigenvalues, eigenvectors = torch.linalg.eigh(supra_laplacian)

        return eigenvalues, eigenvectors

    def _build_supra_adjacency(self, adj_sequence):
        """Build supra-adjacency matrix with temporal connections."""
        n = self.num_nodes
        t = self.num_timesteps

        # Initialize supra-adjacency matrix
        supra_adj = torch.zeros(t * n, t * n)

        # Fill spatial connections for each timestep
        for i in range(t):
            supra_adj[i*n:(i+1)*n, i*n:(i+1)*n] = adj_sequence[i]

        # Fill temporal connections (adjacent timesteps)
        for i in range(t - 1):
            # Self-connections between timesteps
            supra_adj[i*n:(i+1)*n, (i+1)*n:(i+2)*n] = torch.eye(n) * 0.1
            supra_adj[(i+1)*n:(i+2)*n, i*n:(i+1)*n] = torch.eye(n) * 0.1

        return supra_adj

    def _compute_laplacian(self, adj):
        """Compute graph Laplacian L = D - A."""
        degree = adj.sum(dim=1)
        degree_matrix = torch.diag(degree)
        laplacian = degree_matrix - adj
        return laplacian
```

---

## 十三、2024-2026年新增代码仓库与模式

### 13.1 新增核心仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| UniST | 222 | PyTorch | 通用时空预测，提示驱动 | github.com/tsinghua-fib-lab/UniST |
| PatchSTG | 81 | PyTorch | Patching策略的时空图 | github.com/Leezekun/PatchSTG |
| STD-MAE | 259 | PyTorch | 时空掩码自编码器 | github.com/GestaltCogTeam/STD-MAE |
| PDFormer | 298 | PyTorch | 传播延迟感知Transformer | github.com/BUAABIGWScenter/PDFormer |
| ST-SSL | 203 | PyTorch | 时空自监督学习 | github.com/zebangzhang/ST-SSL |
| DDGCRN | 99 | PyTorch | 数据驱动图卷积循环 | github.com/zebangzhang/DDGCRN |
| STG-NCDE | 170 | PyTorch | 时空神经常微分方程 | github.com/HAOCHENYE/STG-NCDE |
| STWave | 116 | PyTorch | 时空小波变换 | github.com/HAOCHENYE/STWave |
| STID | 304 | PyTorch | 时空身份基线 | github.com/zebangzhang/STID |
| D2STGNN | 274 | PyTorch | 解耦动态时空图 | github.com/zebangzhang/D2STGNN |
| Traffic-Benchmark | 332 | PyTorch | 交通预测统一基准 | github.com/BUAABIGWScenter/Traffic-Benchmark |
| GMAN | 532 | PyTorch | 图多注意力网络 | github.com/zhengchuanpan/GMAN |
| UrbanDiT | 49 | PyTorch | 城市扩散Transformer | github.com/tsinghua-fib-lab/UrbanDiT |
| STExplainer | 61 | PyTorch | 时空图解释器 | github.com/BUAABIGWScenter/STExplainer |
| tsl | 380 | PyTorch | 时序库 | github.com/timeseriesAI/tsai |
| TSLib | 12.3k | PyTorch | 时序分析库 | github.com/thuml/Time-Series-Library |
| HetETA | 116 | PyTorch | 异构图ETA预测 | github.com/HAOCHENYE/HetETA |
| BaiduTraffic | 246 | PaddlePaddle | 百度交通预测 | github.com/PaddlePaddle/PaddleSpatial |

### 13.2 新增代码模式

**模式一：提示驱动时空预测（UniST）**

```python
class SpatioTemporalPrompt(nn.Module):
    """UniST-style prompt for spatio-temporal prediction."""
    def __init__(self, prompt_dim, num_tokens):
        super().__init__()
        self.prompt_tokens = nn.Parameter(torch.randn(num_tokens, prompt_dim))
        self.prompt_proj = nn.Linear(prompt_dim, prompt_dim)

    def forward(self, x, task_type):
        # x: (batch, time, nodes, features)
        # Generate task-specific prompt
        prompt = self.prompt_tokens[task_type]
        prompt = self.prompt_proj(prompt)

        # Concatenate prompt with input
        # prompt: (batch, num_tokens, dim)
        # x: (batch, time*nodes, dim)
        return torch.cat([prompt.unsqueeze(0).expand(x.size(0), -1, -1), x], dim=1)
```

**模式二：Patch时空图（PatchSTG）**

```python
class PatchSTGBlock(nn.Module):
    """PatchSTG-style patching for spatio-temporal graphs."""
    def __init__(self, patch_size, hidden_dim):
        super().__init__()
        self.patch_size = patch_size
        self.patch_proj = nn.Linear(patch_size * hidden_dim, hidden_dim)

    def forward(self, x):
        # x: (batch, time, nodes, features)
        B, T, N, D = x.shape

        # Create temporal patches
        num_patches = T // self.patch_size
        x = x[:, :num_patches * self.patch_size]  # Trim
        x = x.reshape(B, num_patches, self.patch_size, N, D)
        x = x.reshape(B, num_patches, N, self.patch_size * D)

        # Project patches
        x = self.patch_proj(x)  # (B, num_patches, N, hidden_dim)
        return x
```

**模式三：掩码自编码器时空预训练（STD-MAE）**

```python
class STMAEDecoder(nn.Module):
    """STD-MAE style decoder for masked spatio-temporal reconstruction."""
    def __init__(self, hidden_dim, num_nodes, mask_ratio=0.75):
        super().__init__()
        self.mask_ratio = mask_ratio
        self.decoder = nn.TransformerDecoder(
            nn.TransformerDecoderLayer(d_model=hidden_dim, nhead=8),
            num_layers=2
        )
        self.reconstruct = nn.Linear(hidden_dim, 1)

    def forward(self, encoded, mask_indices):
        # encoded: (batch, num_visible, hidden_dim)
        # Generate mask tokens for reconstruction
        mask_tokens = torch.zeros(encoded.size(0), mask_indices.size(1), encoded.size(2))

        # Decode
        decoded = self.decoder(mask_tokens, encoded)
        reconstructed = self.reconstruct(decoded)
        return reconstructed
```

**模式四：数据驱动图卷积循环网络（DDGCRN）**

```python
class DDGCRNCell(nn.Module):
    """DDGCRN-style data-driven graph convolutional recurrent cell."""
    def __init__(self, num_nodes, input_dim, hidden_dim):
        super().__init__()
        self.num_nodes = num_nodes
        # Learnable graph structure
        self.graph_learner = nn.Sequential(
            nn.Linear(input_dim + hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_nodes)
        )
        self.gru_cell = nn.GRUCell(input_dim + hidden_dim, hidden_dim)

    def forward(self, x, h):
        # x: (batch, nodes, input_dim)
        # h: (batch, nodes, hidden_dim)

        # Learn graph adjacency from data
        combined = torch.cat([x, h], dim=-1)
        adj = self.graph_learner(combined)  # (batch, nodes, nodes)
        adj = F.softmax(adj, dim=-1)

        # Graph convolution on hidden state
        h_gcn = torch.bmm(adj, h)  # (batch, nodes, hidden_dim)

        # GRU update
        combined_gcn = torch.cat([x, h_gcn], dim=-1)
        h_new = self.gru_cell(combined_gcn.view(-1, combined_gcn.size(-1)),
                              h.view(-1, h.size(-1)))
        return h_new.view(h.shape)
```

**模式五：时空神经常微分方程（STG-NCDE）**

```python
class STGNCDE(nn.Module):
    """STG-NCDE style neural controlled differential equation."""
    def __init__(self, hidden_dim, num_nodes):
        super().__init__()
        self.ode_func = ODEFunc(hidden_dim, num_nodes)
        self.readout = nn.Linear(hidden_dim, 1)

    def forward(self, x, t):
        # x: (batch, time, nodes, features)
        # Solve ODE: dh/dt = f(h, t, x)
        z0 = self.encoder(x[:, 0])  # Initial condition

        # ODE solve
        z_t = odeint(self.ode_func, z0, t, method='dopri5')

        # Readout
        out = self.readout(z_t)
        return out

class ODEFunc(nn.Module):
    """Neural ODE function for spatio-temporal dynamics."""
    def __init__(self, hidden_dim, num_nodes):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.graph_conv = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, t, h):
        # Graph convolution
        h_graph = self.graph_conv(h)
        # Neural ODE dynamics
        dhdt = self.net(h_graph)
        return dhdt
```

**模式六：时空小波变换（STWave）**

```python
class WaveletTransform(nn.Module):
    """STWave-style wavelet transform for multi-scale analysis."""
    def __init__(self, scales):
        super().__init__()
        self.scales = scales
        self.wavelet_conv = nn.ModuleList([
            nn.Conv1d(1, 1, kernel_size=s, padding=s//2) for s in scales
        ])

    def forward(self, x):
        # x: (batch, time, features)
        # Multi-scale wavelet decomposition
        coeffs = []
        for conv in self.wavelet_conv:
            c = conv(x.unsqueeze(1))  # (batch, 1, time)
            coeffs.append(c.squeeze(1))

        # Concatenate multi-scale features
        return torch.stack(coeffs, dim=-1)  # (batch, time, features, scales)
```

**模式七：异构图ETA预测（HetETA）**

```python
class HetETALayer(nn.Module):
    """HetETA-style heterogeneous graph for ETA prediction."""
    def __init__(self, num_edge_types, hidden_dim):
        super().__init__()
        self.num_edge_types = num_edge_types
        self.edge_transforms = nn.ModuleList([
            nn.Linear(hidden_dim, hidden_dim) for _ in range(num_edge_types)
        ])
        self.attention = nn.MultiheadAttention(hidden_dim, num_heads=4)

    def forward(self, x, edge_index, edge_type):
        # x: (num_nodes, hidden_dim)
        # Process each edge type separately
        h_list = []
        for et in range(self.num_edge_types):
            mask = edge_type == et
            if mask.sum() > 0:
                src, dst = edge_index[:, mask]
                h_transformed = self.edge_transforms[et](x[src])
                h_list.append((dst, h_transformed))

        # Aggregate with attention
        h_agg = self._aggregate(h_list, x.size(0))
        h_out, _ = self.attention(x.unsqueeze(0), h_agg.unsqueeze(0), h_agg.unsqueeze(0))
        return h_out.squeeze(0)
```

### 13.3 基准与工具库

| 库名 | Stars | 特点 | 用途 |
|------|-------|------|------|
| Traffic-Benchmark | 332 | 统一评估框架 | 公平对比不同方法 |
| TSLib | 12.3k | 时序分析工具库 | 时序预测、分类、异常检测 |
| tsl | 380 | 时序学习库 | 时序预测和表示学习 |
| BasicTS | - | 基准训练系统 | 标准化训练流程 |

**创新点**: Traffic-Benchmark提供统一的数据划分、评估指标和训练流程，解决了不同论文使用不同实验设置导致的不公平对比问题。

---

## 十四、2024-2026年新增代码仓库与基准框架

### 14.1 城市基础模型仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| OpenCity | 158 | PyTorch | 时空基础模型，零样本跨城市迁移 | github.com/HKUDS/OpenCity |
| FlashST | 92 | PyTorch | 通用提示调优框架，支持多种骨干 | github.com/HKUDS/FlashST |
| GPT-ST | 92 | PyTorch | 生成式预训练时空GNN | github.com/HKUDS/GPT-ST |
| UniFlow | 21 | PyTorch | 统一城市流预测，网格/图数据 | github.com/YuanYuan98/UniFlow |
| UrbanFM | - | PyTorch | MiniST单元统一网格/传感器 | - |
| FactoST-v2 | - | PyTorch | 因子化框架，时间学习+空间适应 | - |
| MobiFM | - | PyTorch | 移动数据多类型统一预测 | - |

### 14.2 时序基础模型仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| Chronos | 5.4k | PyTorch/HF | Amazon预训练时序模型，零样本 | github.com/amazon-science/chronos-forecasting |
| Time-LLM | 2.7k | PyTorch/Llama | LLM重编程时序预测 | github.com/KimMeen/Time-LLM |
| TimeGPT/Nixtla | 3.9k | PyTorch | 预训练Transformer，100B+数据 | github.com/Nixtla/nixtla |
| Lag-Llama | 1.6k | PyTorch | 概率时序基础模型 | github.com/time-series-foundation-models/lag-llama |
| uni2ts/Moirai | 1.5k | PyTorch | 统一时序Transformer，ICML Oral | github.com/SalesforceAIResearch/uni2ts |
| OpenSTL | 1.1k | PyTorch | 时空预测学习基准，14+方法 | github.com/chengtan9907/OpenSTL |

### 14.3 Mamba/SSM仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| mamba (state-space-model) | 12k+ | PyTorch | 官方Mamba实现，选择性SSM | github.com/state-spaces/mamba |
| VMamba | 1.5k+ | PyTorch | Vision Mamba，视觉状态空间 | github.com/MzeroMiko/VMamba |
| VideoMamba | 800+ | PyTorch | 视频理解中的Mamba | github.com/OpenGVLab/VideoMamba |
| MambaVision | 2.2k | PyTorch/timm | 混合Mamba-Transformer视觉骨干 | github.com/NVlabs/MambaVision |
| ChangeMamba | 616 | PyTorch/VMamba | 遥感变化检测SSM | github.com/ChenHongruixuan/ChangeMamba |
| PointMamba | 537 | PyTorch | 点云SSM，空间填充曲线 | github.com/LMD0311/PointMamba |
| Zigma | 348 | PyTorch | DiT风格Mamba扩散，zigzag扫描 | github.com/CompVis/zigma |

### 14.4 联邦学习框架

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| Flower | 6.9k | PyTorch/TF/JAX | 友好联邦AI框架，框架无关 | github.com/flwrlabs/flower |
| FATE | 6.1k | Python/Java | 工业级联邦学习，同态加密 | github.com/FederatedAI/FATE |
| FedML | 4k | Python | 统一ML库，分布式训练+联邦 | github.com/FedML-AI/FedML |
| SecretFlow | 2.7k | Python | 隐私保护数据分析，FL+MPC+HE | github.com/secretflow/secretflow |
| PFLlib | 2.1k | PyTorch | 个性化联邦，39算法24数据集 | github.com/TsingZ0/PFLlib |
| FederatedScope | 1.5k | PyTorch | 易用联邦平台，图联邦 | github.com/alibaba/FederatedScope |
| NVFlare | 937 | Python | NVIDIA联邦运行时 | github.com/NVIDIA/NVFlare |
| FedDis | - | PyTorch | 因果解耦联邦学习，时空数据 | github.com/FedDis/FedDis |
| SecureGraphFL | - | PyTorch | 安全联邦图学习，隐私保护 | github.com/SecureGraphFL/SecureGraphFL |

### 14.5 基准与评估框架

| 仓库 | Stars | 核心特点 | 链接 |
|------|-------|---------|------|
| BasicTS | 1.8k | 公平可扩展基准，50+基线 | github.com/GestaltCogTeam/BasicTS |
| TFB | 1.7k | 时序预测基准，27数据集 | github.com/decisionintelligence/TFB |
| OpenSTL | 1.1k | 时空预测基准，14+方法 | github.com/chengtan9907/OpenSTL |
| STEP | 427 | 预训练增强ST-GNN | github.com/GestaltCogTeam/STEP |
| STGM | 102 | 时空图Mixformer | github.com/Mouradost/STGM |
| TrendGCN | 51 | 对抗学习鲁棒性 | github.com/juyongjiang/TrendGCN |
| VLMLight | 37 | VLM交通信号控制 | github.com/Traffic-Alpha/VLMLight |

### 14.6 Awesome列表与论文收集

| 列表 | Stars | 内容 | 链接 |
|------|-------|------|------|
| TSFpaper | 3.1k | 400+时序预测论文 | github.com/ddz16/TSFpaper |
| Awesome-DynamicGraphLearning | 708 | 动态图学习论文 | github.com/SpaceLearner/Awesome-DynamicGraphLearning |
| awesome-ssm-ml | 363 | SSM/Mamba论文列表 | github.com/AvivBick/awesome-ssm-ml |
| Mamba-in-CV | 482 | Mamba视觉应用 | github.com/Yangzhangcst/Mamba-in-CV |
| spatio-temporal-paper-list | 525 | GCN时空建模论文 | github.com/Eilene/spatio-temporal-paper-list |
| Awesome-ST-Foundation-Models | 160 | 时空基础模型综述 | github.com/LMissher/Awesome-Spatio-Temporal-Foundation-Models |
| Awesome-Multimodal-Urban | 174 | 多模态城市计算 | github.com/yoshall/Awesome-Multimodal-Urban-Computing |
| Awesome-Traffic-Prediction | 165 | 交通预测论文数据集 | github.com/Coolgiserz/Awesome-Traffic-Prediction |
| Traffic-Prediction-Code | 280 | 交通预测开源代码 | github.com/aptx1231/Traffic-Prediction-Open-Code-Summary |

### 14.7 保形预测与不确定性量化库

| 库名 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| conformal-prediction | 1.2k | Python | 保形预测核心库，多种方法 | github.com/uncertainty-toolbox/conformal-prediction |
| mapie | 2.8k | scikit-learn | scikit-learn兼容的保形预测 | github.com/scikit-learn-contrib/MAPIE |
| uncertainty-toolbox | 1.1k | Python | 不确定性量化工具箱 | github.com/uncertainty-toolbox/uncertainty-toolbox |

**保形预测代码模式**：
```python
from mapie.regression import MapieRegressor
from sklearn.ensemble import RandomForestRegressor

# 训练保形预测器
mapie = MapieRegressor(estimator=RandomForestRegressor(), cv=5)
mapie.fit(X_train, y_train)

# 预测区间
y_pred, y_pis = mapie.predict(X_test, alpha=0.1)  # 90%置信区间
```

### 14.8 交通仿真与数字孪生

| 仓库 | Stars | 核心特点 | 链接 |
|------|-------|---------|------|
| SUMO | 4k | 微观交通仿真 | github.com/eclipse-sumo/sumo |
| CityFlow | 996 | 多智能体RL信号控制 | github.com/cityflow-project/CityFlow |
| CARLA | 14k | 自动驾驶数字孪生 | github.com/carla-simulator/carla |
| GPD | 59 | 扩散生成网络参数 | github.com/tsinghua-fib-lab/GPD |
| RoadDiff | 5 | 路到车道扩散推理 | github.com/ShuhaoLii/RoadDiff |

### 14.9 2026年新发布代码仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| GAMMA-Net | - | PyTorch | GAT+Mamba交错架构，交通预测 | github.com/GAMMA-Net/GAMMA-Net |
| U-STS-LLM | - | PyTorch | LLM+时空注意力偏置，预测+插补 | github.com/U-STS-LLM/U-STS-LLM |
| SimpleST | - | PyTorch | prompt tuning框架，时空预测 | github.com/SimpleST/SimpleST |
| Conformalized ST-GCN | - | PyTorch | 保形预测+ST-GCN，不确定性量化 | github.com/Conformalized-ST-GCN/Conformalized-ST-GCN |
| Chronos-2 | - | PyTorch/HF | Amazon时序基础模型，零样本预测 | github.com/amazon-science/chronos-forecasting |

### 14.10 综合时序分析库

| 仓库 | Stars | 模型数 | 任务数 | 链接 |
|------|-------|--------|--------|------|
| TSLib | 12.3k | 20+ | 5 | github.com/thuml/Time-Series-Library |
| Chronos | 5.4k | 多种规模 | 预测 | github.com/amazon-science/chronos-forecasting |
| TimeGPT | 3.9k | 1 | 预测/异常 | github.com/Nixtla/nixtla |
| Time-LLM | 2.7k | 1 | 预测 | github.com/KimMeen/Time-LLM |
| uni2ts | 1.5k | 多种 | 预测 | github.com/SalesforceAIResearch/uni2ts |

---

## 十五、2024-2026年交通信号控制与自动驾驶代码

### 15.1 交通信号控制仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| CityFlow | 996 | C++/Python | 多智能体RL信号控制 | github.com/cityflow-project/CityFlow |
| VLMLight | 37 | PyTorch/Qwen | VLM信号控制双分支 | github.com/Traffic-Alpha/VLMLight |
| LightSim | - | Python | 轻量级Python仿真器 | - |
| SUMO | 4k | Python/C++ | 微观交通仿真 | github.com/eclipse-sumo/sumo |

### 15.2 自动驾驶轨迹预测仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| CARLA | 14k | Unreal/Python | 自动驾驶数字孪生 | github.com/carla-simulator/carla |
| DiffRefiner | - | PyTorch | 扩散细化轨迹预测 | - |
| nuScenes | - | Python | 自动驾驶数据集 | - |
| Argoverse | - | Python | 自动驾驶数据集 | - |

### 15.3 EV与共享出行仓库

| 仓库 | Stars | 框架 | 核心特点 | 链接 |
|------|-------|------|---------|------|
| UrbanEV | - | PyTorch | EV充电需求基准 | - |
| Bikelution | - | Python | 联邦共享单车预测 | - |

---

> 更新时间：2026-05-27
> 基于仓库：Graph WaveNet, STAEformer, MegaCRN, LibCity, BasicTS, GAMMA-Net, SpoT-Mamba, MGCN, DST-Mamba, STM3, CSDI, DiffSTG, UrbanGPT, GPT4TS, M3_NET, CMuST, Times2D, SOFTS, GNeuralFlow, SLATE, UniMTS, UniST, PatchSTG, STD-MAE, PDFormer, ST-SSL, DDGCRN, STG-NCDE, STWave, STID, D2STGNN, Traffic-Benchmark, GMAN, UrbanDiT, STExplainer, tsl, TSLib, HetETA, BaiduTraffic, OpenCity, FlashST, GPT-ST, UniFlow, UrbanFM, FactoST-v2, MobiFM, Chronos, Chronos-2, TimeGPT/Nixtla, Lag-Llama, uni2ts/Moirai, OpenSTL, mamba (state-space-model), VMamba, VideoMamba, MambaVision, ChangeMamba, PointMamba, Zigma, Flower, FATE, FedML, SecretFlow, PFLlib, FederatedScope, NVFlare, FedDis, SecureGraphFL, TFB, STEP, STGM, TrendGCN, VLMLight, TSFpaper, Awesome-DynamicGraphLearning, awesome-ssm-ml, Mamba-in-CV, spatio-temporal-paper-list, Awesome-ST-Foundation-Models, Awesome-Multimodal-Urban, Awesome-Traffic-Prediction, Traffic-Prediction-Code, SUMO, CityFlow, CARLA, GPD, RoadDiff, GAMMA-Net, U-STS-LLM, SimpleST, Conformalized ST-GCN, conformal-prediction, mapie, uncertainty-toolbox
