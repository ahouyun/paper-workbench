# 数据可用性声明指南

## 核心原则

### 1. FAIR 原则

**F**indable (可发现)：
- 数据有持久标识符 (DOI, Handle)
- 元数据完整且可搜索
- 在注册仓库中索引

**A**ccessible (可访问)：
- 通过标准协议访问 (HTTP, FTP)
- 有明确的访问条件
- 提供访问说明

**I**nteroperable (可互操作)：
- 使用标准格式
- 有完整的数据字典
- 与其他数据源兼容

**R**eusable (可重用)：
- 明确的使用许可
- 详细的来源信息
- 清晰的引用方式

### 2. 透明性

**要求**：
- 所有支持结论的数据必须可访问
- 限制访问需说明原因
- 提供替代访问方式

### 3. 持久性

**要求**：
- 使用持久标识符
- 选择可靠仓库
- 提供长期保存承诺

---

## 数据类型

### 1. 原始数据

**定义**：直接从实验或观察获得的数据

**存储建议**：
- 学科专用仓库
- 通用仓库 (Figshare, Dryad)
- 机构仓库

**示例**：
```
基因表达数据 → GEO, SRA
蛋白质结构 → PDB
临床数据 → ClinicalTrials.gov
```

### 2. 处理数据

**定义**：经过清洗、转换或分析的数据

**存储建议**：
- 与原始数据同仓库
- 提供处理说明
- 保留处理脚本

### 3. 代码

**定义**：数据分析、处理或生成结果的代码

**存储建议**：
- GitHub + Zenodo
- 软件仓库 (PyPI, CRAN)
- 机构仓库

### 4. 文档

**定义**：数据字典、README、使用说明

**存储建议**：
- 与数据同仓库
- Markdown 格式
- 版本控制

---

## 声明模板

### 1. 完全开放

```
Data availability

The data that support the findings of this study are available in [Repository Name] 
at [URL/DOI]. The code is available at [GitHub URL].

All data are freely available without restrictions.
```

### 2. 限制访问

```
Data availability

The data that support the findings of this study are available from [Repository Name] 
at [URL/DOI] with the identifier [Accession Number]. Access is restricted due to 
[reason, e.g., patient privacy, commercial sensitivity] and requires approval from 
[approving body].

Requests should be directed to [contact information].
```

### 3. 按请求提供

```
Data availability

The data that support the findings of this study are available from the corresponding 
author upon reasonable request. Requests should be directed to [email/contact].

Data will be shared within [timeframe, e.g., 30 days] of request.
```

### 4. 已发表数据

```
Data availability

The data that support the findings of this study are available in [Previous Study] 
at [DOI]. No new data were generated in this study.
```

### 5. 公开数据库

```
Data availability

The data that support the findings of this study are available in [Public Database] 
at [URL/DOI]. The accession numbers are [list of accessions].

All data are publicly available.
```

---

## 仓库选择

### 1. 学科专用仓库

**生命科学**：
- GEO (Gene Expression Omnibus)
- SRA (Sequence Read Archive)
- PDB (Protein Data Bank)
- ArrayExpress

**物理学**：
- arXiv
- INSPIRE-HEP
- PANGAEA

**社会科学**：
- ICPSR
- UK Data Service
- OpenICPSR

**化学**：
- PubChem
- ChemSpider
- CCDC

### 2. 通用仓库

**推荐**：
- Figshare
- Dryad
- Zenodo
- Mendeley Data

**特点**：
- 免费使用
- 提供 DOI
- 长期保存
- 支持多种格式

### 3. 机构仓库

**优势**：
- 机构支持
- 长期保存
- 符合政策要求

**示例**：
- 大学机构库
- 研究所数据库
- 政府数据中心

---

## 元数据要求

### 1. 必需元数据

**数据描述**：
- 标题
- 作者
- 摘要
- 关键词
- 创建日期

**技术信息**：
- 文件格式
- 文件大小
- 软件要求
- 系统要求

**来源信息**：
- 数据来源
- 收集方法
- 处理步骤
- 质量控制

### 2. 推荐元数据

**使用信息**：
- 许可证
- 引用方式
- 联系方式
- 更新计划

**关联信息**：
- 相关数据集
- 相关出版物
- 资助信息
- 伦理批准

### 3. 数据字典

**内容**：
- 变量名称
- 变量定义
- 数据类型
- 取值范围
- 缺失值说明

**格式**：
```
Variable: age
Definition: Age of participant at enrollment
Type: Integer
Range: 18-100
Missing: -99
```

---

## 访问限制

### 1. 限制类型

**隐私限制**：
- 患者数据
- 个人身份信息
- 敏感信息

**商业限制**：
- 商业机密
- 专利申请中
- 合作协议限制

**安全限制**:
- 国家安全
- 生物安全
- 双重用途研究

### 2. 限制说明

**必须说明**：
- 限制原因
- 限制范围
- 访问条件
- 审批流程

**示例**：
```
Access is restricted due to patient privacy concerns. Data contain potentially 
identifying information and cannot be shared publicly. Access requires approval 
from the Institutional Review Board and a data use agreement.

Requests should be directed to the corresponding author at [email].
```

### 3. 替代方案

**合成数据**：
- 提供模拟数据
- 保持统计特性
- 说明合成方法

**汇总数据**：
- 提供汇总统计
- 保护个体隐私
- 支持验证分析

**安全计算**：
- 提供计算环境
- 远程访问数据
- 结果导出审核

---

## 代码可用性

### 1. 代码存储

**推荐平台**：
- GitHub + Zenodo (DOI)
- GitLab + Zenodo
- Bitbucket + Zenodo

**版本控制**：
- 使用 Git
- 语义化版本号
- 发布说明

### 2. 代码文档

**README 内容**：
- 项目描述
- 安装说明
- 使用示例
- 依赖说明

**注释要求**：
- 函数说明
- 参数说明
- 返回值说明
- 示例代码

### 3. 可重复性

**环境管理**：
- requirements.txt
- environment.yml
- Dockerfile

**数据路径**：
- 相对路径
- 配置文件
- 环境变量

**随机种子**：
- 固定随机种子
- 记录种子值
- 提供复现脚本

---

## 声明写作

### 1. 结构

**段落 1**：数据位置和标识符

**段落 2**：访问条件（如有限制）

**段落 3**：代码和补充材料

**段落 4**：联系方式

### 2. 语言

**正式但清晰**：
- 避免法律术语
- 使用主动语态
- 说明具体步骤

**示例**：
```
✅ The data are available in GEO under accession GSE12345.
❌ The data may be available upon request to the authors.
```

### 3. 完整性

**必须包含**：
- 数据位置
- 访问条件
- 标识符
- 联系方式

**可选包含**：
- 代码位置
- 补充材料
- 致谢信息

---

## 自检清单

### 内容检查

- [ ] 所有支持结论的数据都有说明
- [ ] 数据位置明确
- [ ] 标识符正确
- [ ] 访问条件清晰

### 格式检查

- [ ] 符合期刊要求
- [ ] 语言正式清晰
- [ ] 结构完整
- [ ] 无拼写错误

### 技术检查

- [ ] DOI/URL 有效
- [ ] 访问权限正确
- [ ] 元数据完整
- [ ] 数据字典齐全

### 伦理检查

- [ ] 隐私保护到位
- [ ] 伦理批准说明
- [ ] 利益冲突声明
- [ ] 资助信息完整
