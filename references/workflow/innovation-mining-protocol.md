# 创新点挖掘协议（Innovation Mining Protocol）

> 用于替代“先翻创新点库存再套用”的旧做法。目标不是背诵创新方向，而是针对**当前论文选题**，基于最新文献与最近两年的场馆信号，动态挖掘可辩护、可验证、可写进论文的创新点。

---

## 0. 核心立场

1. **先检索，再创新**：没有当前领域的 recent-paper 证据，不写强 novelty claim。
2. **创新点不是名词库**：`Mamba / Diffusion / Foundation Model / Causal / Physics-informed` 这类词只能算方法家族，不算创新点本身。
3. **创新点必须绑定证据包**：每个 innovation claim 都要同时回答：
   - 它相对谁新？
   - 它解决了什么已知瓶颈？
   - 它需要什么实验或分析才能站住？
4. **先做机会图，再做写作包装**：若最近工作已覆盖中心主张，优先做 rescue route，而不是强行夸大。
5. **动态优先于库存**：历史整理文件只能做启发，不能直接代替最近 12-24 个月的检索结果。

---

## 1. 适用触发

当用户出现以下意图时，优先进入本协议：

- “帮我找创新点 / 新意 / novelty”
- “这个方向还有没有机会”
- “最近这个领域前沿是什么”
- “这个 idea 会不会已经被做完了”
- “帮我做选题 / 改题 / 细化研究问题”
- `conference` 模式下需要明确 novelty claim
- `ieee_trans` / `english_research` 模式下需要做 contribution positioning

---

## 2. 最小执行主线

1. **界定问题**：明确任务、场景、目标数据、目标 venue、已知方法边界。
2. **做最近检索**：优先查近 12-24 个月的顶会/强刊/可信预印本。
3. **聚类 closest work**：把最接近的工作按问题、机制、证据路径分组。
4. **判断覆盖关系**：
   - `covered central claim`
   - `crowded but open`
   - `benchmark gap`
   - `mechanism gap`
   - `deployment/system gap`
   - `theory/analysis gap`
   - `negative-result opportunity`
5. **生成 3 类候选创新**：
   - 保守修复：保留原问题，缩窄主张
   - 高精度切口：换更窄但更可证的 bottleneck
   - 雄心重构：改问题 framing、证据类型或贡献类型
6. **给出证据包**：为每个候选创新绑定 baseline、ablation、stress test、failure analysis。
7. **只保留可辩护 claims**：不能明确写出“相对谁新、为什么新、怎么证”的候选，一律降级为想法备忘。

---

## 3. 检索与筛选规则

### 3.1 优先数据源

优先使用可核查来源：

- 官方 proceedings / publisher 页面
- arXiv 论文页
- OpenReview
- ACL Anthology / CVF / PMLR / ACM DL / IEEE Xplore / DBLP
- Semantic Scholar / OpenAlex / CrossRef

### 3.2 查询原则

- 先用**任务词 + 方法词 + benchmark/setting** 的公开关键词。
- 不把用户私有 draft 句子直接丢进搜索框，除非用户明确授权。
- 至少混合三类 query：
  - 问题导向：`<task> + <setting>`
  - 方法导向：`<method family> + <task>`
  - 风险导向：`<task> + robustness / generalization / missing data / efficiency / calibration / deployment`

### 3.3 检索输出的最小字段

每篇保留文献至少标注：

- 标题
- venue / year / source status
- paper type：`pure method` / `pure benchmark` / `method + benchmark` / `system/tool` / `survey` / `theory/proof`
- relevance rationale
- 是否直接威胁当前 idea

---

## 4. 机会图（Opportunity Map）写法

对每个 closest-work cluster，都输出以下四项：

1. **已经被覆盖了什么**
2. **还没被测或没被讲清楚什么**
3. **最可信的 rescue route**
4. **需要什么证据才能判断值不值得做**

建议使用如下紧凑模板：

```text
Cluster:
Covered:
Still weak:
Possible rescue route:
Evidence needed:
```

---

## 5. 创新点候选的合法形态

只有以下形态可以当“论文创新点”进入正式写作：

### A. 问题创新

- 新任务定义
- 新失败模式
- 新场景约束
- 新用户/系统目标

### B. 方法创新

- 明确机制的新模块或新训练范式
- 对已有范式的结构性重构，而非简单叠模块
- 有可解释设计动机的 hybrid mechanism

### C. 证据创新

- 新 benchmark / 新 protocol / 新 stress test
- 新评估维度：校准、OOD、效率、可部署性、隐私、安全
- 证明某个主流假设失效的负结果或诊断分析

### D. 系统/部署创新

- 真实延迟、算力、边缘、联邦、隐私、城市迁移等现实约束
- 从“离线 SOTA”转向“可部署最优”

### E. 理论/分析创新

- 机制解释
- 表达能力/稳定性/泛化分析
- 因果、物理、一致性或误差分解分析

---

## 6. 禁止把这些当创新点

以下内容只能算素材，不能单独算创新点：

- “用了 Transformer / Mamba / Diffusion / LLM”
- “融合多源数据”
- “做了消融实验”
- “精度更高”
- “构建了一个 framework”
- “更高效 / 更鲁棒 / 更泛化”但没有明确对照对象和机制解释

这些内容必须写成：

```text
旧瓶颈 → 新机制 → 为什么可能有效 → 如何验证
```

---

## 7. 与文献检索模块的衔接

若任务已涉及 `academic_search` / `deep_research` / `lit_review`，本协议必须复用这些结果，而不是重新拍脑袋产出创新点。

建议衔接顺序：

1. `academic_search` 先给出去重文献列表
2. 本协议做 closest-work clustering
3. 本协议输出 opportunity map
4. 再进入 outline / introduction / contribution drafting

---

## 8. 与写作模块的衔接

只有经过本协议筛选后的候选，才允许写进：

- Abstract contribution sentence
- Introduction contribution list
- Related Work positioning paragraph
- Method overview claims
- Conclusion takeaway

写作时必须保留以下映射：

```text
Innovation claim -> closest prior art -> differentiator -> required evidence -> section anchor
```

若映射写不出来，降级处理：

- 改写成 `motivation`
- 改写成 `hypothesis`
- 改写成 `future extension`
- 或直接删除

---

## 9. 推荐输出格式

```text
Problem and venue framing:
Search freshness:
Closest-work clusters:
Opportunity map:
Candidate innovation claims:
Evidence package for each claim:
High-risk novelty threats:
Best current route:
Claims that should not be written yet:
```

---

## 10. 2025-2026 前沿方向簇（仅作检索启发，不可直接当创新点）

以下方向在 2025-2026 仍值得优先检索，但只能作为**query seed**：

- foundation model / pretraining / universal spatiotemporal model
- Mamba / SSM for long-horizon spatiotemporal forecasting
- diffusion for probabilistic forecasting / imputation / parameter generation
- calibration / uncertainty / conformal prediction
- OOD / distribution shift / retrieval-augmented robustness
- causal / intervention / counterfactual spatiotemporal modeling
- physics-informed / conservation-aware / mechanistic constraints
- federated / edge / real-time / deployment-aware forecasting
- benchmark redesign / evaluation protocol / negative result / diagnostic analysis

写作时一律改写成“**这个方向下的具体未解问题**”，不能原样当贡献。

---

## 11. 失败保护

当检索结果显示“主张已高度覆盖”时，不输出虚高创新点，改输出：

- 缩窄版问题
- benchmark / protocol 版贡献
- deployment / system 版贡献
- analysis / negative-result 版贡献
- venue switch 建议

结论模板：

```text
Direct novelty is weak in the current framing.
Most defensible rescue route:
Minimum evidence needed:
What should not be claimed:
```
