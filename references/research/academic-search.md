# 学术文献搜索参考手册

本文档提供一套可操作的学术论文搜索流程，以交通流预测（traffic flow prediction）为核心领域，但方法论适用于其他计算机科学方向。

---

## 1. 搜索源优先级 (Search Source Priority)

### T1: Semantic Scholar API

- **地址**: https://api.semanticscholar.org
- **覆盖范围**: 约2亿篇论文，涵盖所有学科，包含引用关系、作者信息、论文摘要
- **免费额度**: 未认证用户 100 次/5分钟；注册 API Key 后 1 次/秒（约 1000 次/5分钟）
- **API 文档**: https://api.semanticscholar.org/api-docs/graph
- **优势**:
  - 提供结构化 JSON 返回，字段丰富（标题、作者、年份、引用数、DOI、摘要、venue）
  - 支持引用图谱查询（citations / references）
  - 支持批量查询（paper/batch）
  - 有 relevance score 和 citation count 排序
- **局限**:
  - 2020年前的部分中文期刊覆盖不全
  - 预印本论文有时缺少 venue 信息
  - 高频调用需要申请 API Key（https://www.semanticscholar.org/product/api#api-key）

### T2: DBLP

- **地址**: https://dblp.org
- **覆盖范围**: 计算机科学领域的主要期刊和会议论文元数据（标题、作者、venue、年份）
- **免费额度**: 无严格限制，但建议不超过 1 次/秒
- **API 文档**: https://dblp.org/faq/13501473.html
- **优势**:
  - 计算机科学领域最权威的文献索引
  - 数据质量极高，无噪声
  - 支持按 venue（期刊/会议）精确筛选
  - 提供作者主页和发表记录
- **局限**:
  - 不提供摘要、引用数
  - 仅覆盖计算机科学及相关领域
  - 不含 DOI（部分条目有）

### T3: arXiv

- **地址**: https://arxiv.org
- **覆盖范围**: 预印本论文，物理、数学、计算机科学、统计学等
- **免费额度**: 无限制（但建议间隔 3 秒以上）
- **API 文档**: https://info.arxiv.org/help/api/index.html
- **优势**:
  - 最新研究最快出现在 arXiv
  - 提供完整摘要和 PDF 链接
  - 支持按分类（cs.LG, cs.AI, eess.SP 等）筛选
- **局限**:
  - 未经同行评审，质量参差不齐
  - 不提供引用数
  - API 返回 XML 格式，解析稍复杂

### T4: CrossRef API

- **地址**: https://api.crossref.org
- **覆盖范围**: 约1.5亿条 DOI 记录，涵盖所有有 DOI 的学术出版物
- **免费额度**: 无限制（Polite Pool 需提供邮箱，速率更高）
- **API 文档**: https://api.crossref.org/swagger-ui/index.html
- **优势**:
  - DOI 解析的权威来源
  - 支持按 ISSN（期刊编号）精确筛选期刊
  - 提供引用数（通过 Crossref Cited-by）
  - 可获取完整的出版元数据
- **局限**:
  - 搜索功能较弱，不如 Semantic Scholar 智能
  - 不提供摘要（部分条目有）
  - 返回数据量大时响应较慢

### T5: Google Scholar

- **地址**: https://scholar.google.com
- **覆盖范围**: 最广泛的学术搜索引擎，包含期刊、会议、预印本、学位论文、专利
- **免费额度**: 无官方 API，需通过爬虫或第三方工具（scholarly、serpapi）
- **优势**:
  - 覆盖面最广
  - 引用数最准确
  - 支持"被引用次数"和"相关文章"推荐
- **局限**:
  - 无官方 API，爬虫容易被封 IP
  - 使用代理或 SerpAPI（付费）才能稳定调用
  - 返回数据非结构化，需要解析 HTML

### 优先级使用建议

```
日常文献搜索流程:
1. 先用 Semantic Scholar API 做关键词搜索，获取标题、摘要、引用数
2. 用 DBLP 补充计算机科学会议/会议论文的精确 venue 信息
3. 用 arXiv 搜索最新预印本（近 3-6 个月）
4. 用 CrossRef 解析已知 DOI 的论文元数据
5. Google Scholar 仅作为人工验证和补充，不用于批量自动化
```

---

## 2. 搜索策略模板 (Search Strategy Templates)

### 2.1 核心主题搜索

**交通流预测（基础）**:
```
"traffic flow prediction" OR "traffic forecasting" OR "traffic flow forecasting"
```

**时空图网络（方法论）**:
```
"spatiotemporal graph" AND ("traffic" OR "transportation")
```

**图神经网络 + 交通**:
```
"graph neural network" AND ("traffic flow" OR "traffic prediction" OR "traffic forecasting")
```

**Transformer + 交通**:
```
"transformer" AND ("traffic" OR "transportation") AND ("prediction" OR "forecasting")
```

**扩散模型 + 交通**:
```
("diffusion model" OR "score-based" OR "denoising diffusion") AND ("traffic" OR "spatiotemporal")
```

**大语言模型 + 交通**:
```
("large language model" OR "LLM" OR "foundation model") AND ("traffic" OR "transportation")
```

### 2.2 数据集搜索

**标准基准数据集**:
```
"METR-LA" OR "PEMS-BAY" OR "PEMS04" OR "PEMS08" OR "PEMSD7" OR "METR-LA"
```

**交通数据集论文**:
```
"traffic dataset" AND ("benchmark" OR "benchmarking")
```

### 2.3 方法名称搜索

**经典方法**:
```
"STGCN" OR "DCRNN" OR "Graph WaveNet" OR "STAEformer" OR "ASTGCN" OR "GWNET"
```

**近期方法（2024-2026）**:
```
("spatiotemporal" OR "spatial-temporal") AND ("transformer" OR "attention") AND "traffic" AND 2024..2026
```

### 2.4 Boolean 运算符说明

| 运算符 | 含义 | 示例 |
|--------|------|------|
| AND | 同时包含 | "graph" AND "traffic" |
| OR | 包含任一 | "prediction" OR "forecasting" |
| NOT | 排除 | "traffic" NOT "internet" |
| "..." | 精确短语 | "traffic flow prediction" |
| ( ) | 分组 | ("deep learning" OR "neural network") AND "traffic" |

### 2.5 字段限定搜索

**Semantic Scholar 字段限定**:
```
title:"traffic flow" AND abstract:"graph neural"
```

**DBLP 字段限定**:
```
venue:KDD 2024 traffic
```

**arXiv 分类限定**:
```
cat:cs.LG AND ti:traffic
```

---

## 3. API 调用模式 (API Usage Patterns)

### 3.1 Semantic Scholar API

**基础搜索**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=traffic+flow+prediction&limit=10&fields=title,authors,year,venue,citationCount,externalIds,abstract"
```

**带分页的搜索**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=graph+neural+network+traffic&limit=100&offset=0&fields=title,authors,year,venue,citationCount,externalIds,abstract"
```

**按引用数排序**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=traffic+prediction&sort=citationCount:desc&limit=50&fields=title,authors,year,venue,citationCount"
```

**按年份筛选（2024-2026）**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=traffic+flow+prediction&year=2024-2026&fields=title,authors,year,venue,citationCount"
```

**按 venue 筛选**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=traffic&fields=title,authors,year,venue,citationCount&venue=TITS,TKDE,TPAMI,KDD,AAAI,NeurIPS"
```

**获取论文详情（by Paper ID）**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/204e3073870fae3d05bcbc2f6a8e263d9b72e776?fields=title,authors,year,venue,citationCount,references,citations"
```

**批量获取论文（by DOI）**:
```bash
curl -X POST "https://api.semanticscholar.org/graph/v1/paper/batch" \
  -H "Content-Type: application/json" \
  -d '{"ids":["DOI:10.1109/TITS.2020.2995533","DOI:10.1145/3292500.3330891"]}'
```

**返回字段说明**:
| 字段 | 类型 | 说明 |
|------|------|------|
| paperId | string | Semantic Scholar 内部 ID |
| title | string | 论文标题 |
| authors | array | 作者列表 [{name, authorId}] |
| year | int | 发表年份 |
| venue | string | 期刊/会议名称 |
| citationCount | int | 被引用次数 |
| externalIds | object | 外部 ID（DOI, ArXiv 等） |
| abstract | string | 摘要 |
| references | array | 参考文献列表 |
| citations | array | 被引用论文列表 |

### 3.2 DBLP API

**搜索论文**:
```bash
curl "https://dblp.org/search/publ/api?q=traffic+flow+prediction&format=json&h=30"
```

**按 venue 搜索**:
```bash
curl "https://dblp.org/search/publ/api?q=traffic+venue:KDD&format=json&h=50"
```

**搜索作者**:
```bash
curl "https://dblp.org/search/author/api?q=traffic+prediction&format=json"
```

**获取 venue 下的所有论文**:
```bash
curl "https://dblp.org/publ/api?q=venue:KDD:2024&format=json&h=100"
```

**返回字段说明**:
| 字段 | 类型 | 说明 |
|------|------|------|
| title | string | 论文标题 |
| authors | object | 作者信息（author 字段，可能是字符串或数组） |
| venue | string | 期刊/会议缩写 |
| year | string | 发表年份 |
| url | string | DBLP 页面链接 |
| doi | string | DOI（如有） |
| type | string | 类型（Journal, Conference, ...） |

### 3.3 CrossRef API

**基础搜索**:
```bash
curl "https://api.crossref.org/works?query=traffic+flow+prediction&rows=20"
```

**带过滤的搜索（期刊 ISSN）**:
```bash
curl "https://api.crossref.org/works?query=traffic+prediction&filter=issn:1524-9050&rows=20"
```
（1524-9050 是 IEEE TITS 的 ISSN）

**按时间范围筛选**:
```bash
curl "https://api.crossref.org/works?query=traffic+prediction&filter=from-pub-date:2024-01-01,until-pub-date:2026-12-31&rows=50"
```

**按引用数排序**:
```bash
curl "https://api.crossref.org/works?query=traffic+prediction&sort=is-referenced-by-count&order=desc&rows=20"
```

**按 DOI 获取元数据**:
```bash
curl "https://api.crossref.org/works/10.1109/TITS.2020.2995533"
```

**Polite Pool（提供邮箱提高速率）**:
```bash
curl "https://api.crossref.org/works?query=traffic&mailto=your@email.com&rows=50"
```

**常用期刊 ISSN**:
| 期刊 | ISSN |
|------|------|
| IEEE TITS | 1524-9050 |
| IEEE TKDE | 1041-4347 |
| IEEE TNNLS | 2162-237X |
| IEEE TPAMI | 0162-8828 |
| IEEE TCSVT | 1051-8215 |
| ACM TKDD | 1556-4681 |
| Transportation Research Part C | 0968-090X |

### 3.4 arXiv API

**基础搜索**:
```bash
curl "http://export.arxiv.org/api/query?search_query=all:traffic+flow+prediction&start=0&max_results=20"
```

**按分类搜索（cs.LG = 机器学习）**:
```bash
curl "http://export.arxiv.org/api/query?search_query=cat:cs.LG+AND+ti:traffic&start=0&max_results=30"
```

**按标题搜索**:
```bash
curl "http://export.arxiv.org/api/query?search_query=ti:spatiotemporal+AND+ti:traffic+AND+ti:prediction&start=0&max_results=20"
```

**按时间排序（最新优先）**:
```bash
curl "http://export.arxiv.org/api/query?search_query=all:traffic+prediction&sortBy=submittedDate&sortOrder=descending&max_results=30"
```

**返回格式**: XML（Atom feed），包含标题、作者、摘要、发布日期、arXiv ID、PDF 链接

**arXiv 分类常用**:
| 分类代码 | 含义 |
|----------|------|
| cs.LG | 机器学习 |
| cs.AI | 人工智能 |
| cs.CV | 计算机视觉 |
| eess.SP | 信号处理 |
| stat.ML | 统计机器学习 |
| cs.SI | 社交网络 |

---

## 4. 论文筛选标准 (Paper Selection Criteria)

### 4.1 期刊筛选（按交通流预测领域相关性）

**T1 - 核心期刊（必须搜索）**:
- IEEE Transactions on Intelligent Transportation Systems (TITS)
- IEEE Transactions on Knowledge and Data Engineering (TKDE)
- IEEE Transactions on Neural Networks and Learning Systems (TNNLS)
- IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
- IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)

**T2 - 高质量期刊**:
- ACM Transactions on Knowledge Discovery from Data (TKDD)
- Transportation Research Part C: Emerging Technologies
- Information Sciences
- Knowledge-Based Systems
- Neural Networks
- Expert Systems with Applications

**T3 - 补充期刊**:
- Applied Intelligence
- Neurocomputing
- IEEE Access（注意质量筛选）
- Sensors（注意质量筛选）

### 4.2 会议筛选

**T1 - 顶级会议（CCF-A）**:
- KDD (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- AAAI (AAAI Conference on Artificial Intelligence)
- NeurIPS (Conference on Neural Information Processing Systems)
- ICLR (International Conference on Learning Representations)
- ICML (International Conference on Machine Learning)
- WWW (The Web Conference)
- SIGIR (ACM SIGIR Conference on Research and Development in Information Retrieval)

**T2 - 高质量会议（CCF-B）**:
- CIKM (ACM International Conference on Information and Knowledge Management)
- ICDM (IEEE International Conference on Data Mining)
- SDM (SIAM International Conference on Data Mining)
- ECML-PKDD (European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases)
- AISTATS (International Conference on Artificial Intelligence and Statistics)
- WSDM (ACM International Conference on Web Search and Data Mining)

**T3 - 领域会议**:
- ITSC (IEEE International Conference on Intelligent Transportation Systems)
- TRB (Transportation Research Board Annual Meeting)
- ACM SIGSPATIAL

### 4.3 时间筛选策略

```
最新研究（2025-2026）: 用于了解前沿方向和最新方法
  - 搜索 arXiv 近 6 个月预印本
  - 搜索 Semantic Scholar year=2025-2026

成熟研究（2023-2025）: 用于方法对比和实验复现
  - 搜索 Semantic Scholar year=2023-2025
  - 按引用数排序，选择引用最高的

经典研究（2018-2023）: 用于理解领域发展脉络
  - 搜索 STGCN, DCRNN, Graph WaveNet 等奠基论文
  - 按引用数排序，选择引用最高的前 20 篇
```

### 4.4 引用数筛选

```
引用数阈值参考（交通流预测领域）:
- > 500 次: 经典论文，必读
- 100-500 次: 重要论文，应该了解
- 50-100 次: 有影响力的论文，可选阅读
- 10-50 次: 新论文或小领域论文，按需阅读
- < 10 次: 新论文，关注是否来自顶级 venue

注意: arXiv 预印本引用数偏低，需结合发表 venue 判断
```

### 4.5 相关性筛选

**关键词匹配规则**:
```
标题必须包含以下至少一项:
  - traffic flow
  - traffic prediction
  - traffic forecasting
  - spatiotemporal + traffic
  - graph + traffic

摘要必须包含以下至少一项:
  - METR-LA / PEMS-BAY / PEMS04 / PEMS08
  - speed prediction / flow prediction
  - spatiotemporal / spatial-temporal
  - graph neural network / GNN
```

---

## 5. 去重与合并 (Deduplication)

### 5.1 基于 DOI 去重

**策略**: 从多个数据源收集论文后，以 DOI 为唯一标识符进行去重。

**实现逻辑**:
```python
def deduplicate_by_doi(papers):
    seen_dois = set()
    unique_papers = []
    for paper in papers:
        doi = paper.get('doi', '').strip().lower()
        if doi and doi in seen_dois:
            continue
        if doi:
            seen_dois.add(doi)
        unique_papers.append(paper)
    return unique_papers
```

**注意事项**:
- Semantic Scholar 返回的 DOI 在 `externalIds.DOI` 字段
- CrossRef 返回的 DOI 在 `DOI` 字段（注意大小写）
- DBLP 部分条目有 DOI，在 `doi` 字段
- arXiv 不直接提供 DOI，但可通过 Semantic Scholar 交叉查询获取

### 5.2 基于标题相似度去重

**策略**: 对于没有 DOI 的论文（如 arXiv 预印本），通过标题相似度判断是否重复。

**实现逻辑**:
```python
from difflib import SequenceMatcher

def normalize_title(title):
    """标准化标题: 小写、去除标点和多余空格"""
    import re
    title = title.lower().strip()
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title

def title_similarity(t1, t2):
    """计算两个标题的相似度 (0-1)"""
    return SequenceMatcher(None, normalize_title(t1), normalize_title(t2)).ratio()

def deduplicate_by_title(papers, threshold=0.85):
    """基于标题相似度去重"""
    unique = []
    for paper in papers:
        is_dup = False
        for existing in unique:
            if title_similarity(paper['title'], existing['title']) > threshold:
                # 保留信息更丰富的那篇（有摘要 > 无摘要）
                if len(paper.get('abstract', '')) > len(existing.get('abstract', '')):
                    unique.remove(existing)
                    unique.append(paper)
                is_dup = True
                break
        if not is_dup:
            unique.append(paper)
    return unique
```

**相似度阈值选择**:
- 0.95: 仅去除完全相同的标题（如大小写差异）
- 0.85: 推荐阈值，能处理微小的措辞差异
- 0.70: 激进阈值，可能误合并不同论文

### 5.3 合并多源结果

**合并策略**:
```python
def merge_paper_info(primary, secondary):
    """合并两个来源的同一篇论文信息，primary 优先"""
    merged = dict(primary)
    for key, value in secondary.items():
        if key not in merged or not merged[key]:
            merged[key] = value
        elif key == 'citationCount':
            # 引用数取较大值
            merged[key] = max(merged.get(key, 0), value or 0)
        elif key == 'abstract':
            # 摘要取较长的
            if len(str(value)) > len(str(merged.get(key, ''))):
                merged[key] = value
    return merged
```

**合并优先级**:
```
元数据完整性: Semantic Scholar > CrossRef > DBLP > arXiv
引用数准确性: Google Scholar > Semantic Scholar > CrossRef
最新预印本: arXiv > Semantic Scholar
venue 信息: DBLP > Semantic Scholar > CrossRef
```

### 5.4 完整去重流程

```
1. 从 Semantic Scholar 收集论文列表
2. 从 DBLP 补充 venue 信息
3. 从 arXiv 获取最新预印本
4. 按 DOI 去重（以 Semantic Scholar 为主，补充 CrossRef 的 DOI）
5. 对无 DOI 的条目按标题相似度去重
6. 合并多源元数据（引用数取大值，摘要取长值，venue 取最权威值）
7. 输出去重后的论文列表
```

---

## 6. 搜索结果模板 (Output Template)

### 6.1 单篇论文信息

```yaml
title: "Spatio-Temporal Graph Convolutional Networks: A Deep Learning Framework for Traffic Forecasting"
authors:
  - Yu, Bing
  - Yin, Haoteng
  - Zhu, Zhanxing
journal_conference: "IJCAI 2018"  # 或期刊名如 "IEEE TITS"
year: 2018
doi: "10.24963/ijcai.2018/505"
citations: 2150  # 截至搜索时的引用数
abstract: "Timely accurate traffic forecasting is crucial for urban traffic control..."
key_innovation: "首次提出纯图卷积架构处理交通时空数据，设计门控时间卷积层"
dataset:
  - METR-LA
  - PEMS-BAY
code_url: "https://github.com/hazdzz/STGCN"
```

### 6.2 批量结果排序

**排序维度**:
```
1. 按引用数降序: 找到领域内最有影响力的论文
2. 按时间降序: 找到最新的研究进展
3. 按相关性降序: 找到与查询最匹配的论文
4. 综合排序: citationCount * 0.4 + recency * 0.3 + relevance * 0.3
```

**综合排序实现**:
```python
import time

def compute_score(paper, query_year=2026):
    """计算综合排序分数"""
    # 引用数分数（对数归一化）
    import math
    citations = paper.get('citationCount', 0) or 0
    cite_score = math.log1p(citations) / math.log1p(5000)  # 假设 5000 为上限
    cite_score = min(cite_score, 1.0)

    # 时间分数（越新越高）
    year = paper.get('year', 2020) or 2020
    recency_score = max(0, (year - 2018) / (query_year - 2018))  # 2018 为起点
    recency_score = min(recency_score, 1.0)

    # 相关性分数（基于关键词匹配，0-1）
    relevance_score = paper.get('relevance', 0.5)

    return cite_score * 0.4 + recency_score * 0.3 + relevance_score * 0.3
```

### 6.3 输出格式（Markdown）

```markdown
## 搜索结果: Traffic Flow Prediction

**搜索时间**: 2026-06-19
**搜索关键词**: "traffic flow prediction" OR "traffic forecasting"
**时间范围**: 2024-2026
**共找到**: 47 篇论文（去重后）

---

### 1. [STAEformer: Spatio-Temporal Adaptive Embedding for Traffic Forecasting]

- **作者**: Junfeng Hu, Yuxuan Liang, Zhencheng Fan, Hongyang Chen, Yu Zheng
- **发表**: AAAI 2024
- **DOI**: 10.1609/aaai.v38i8.28725
- **引用数**: 85
- **关键创新**: 自适应时空嵌入，无需预定义图结构
- **数据集**: METR-LA, PEMS-BAY, PEMS04, PEMS08
- **代码**: https://github.com/XDZhelheim/STAEformer

### 2. [TrafficBERT: ...]

...
```

---

## 7. 交通流预测专用搜索 (Traffic-Specific Search)

### 7.1 标准数据集搜索

**数据集论文**:
```bash
# Semantic Scholar
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=METR-LA+PEMS-BAY+traffic+dataset&limit=20&fields=title,authors,year,venue,citationCount,abstract"
```

**按数据集名称搜索引用该数据集的论文**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22METR-LA%22+traffic+prediction&limit=50&fields=title,year,venue,citationCount"
```

**常用数据集**:
| 数据集 | 说明 | 论文 |
|--------|------|------|
| METR-LA | 洛杉矶高速公路 207 个传感器，4 个月 | DCRNN (Li et al., 2018) |
| PEMS-BAY | 湾区 325 个传感器，6 个月 | DCRNN (Li et al., 2018) |
| PEMS04 | 加州 307 个传感器 | STSGCN (Song et al., 2020) |
| PEMS08 | 加州 170 个传感器 | STSGCN (Song et al., 2020) |
| PEMSD7(M) | 加州 228 个传感器 | ASTGCN (Guo et al., 2019) |
| PEMS03 | 加州 358 个传感器 | TOCGCN (Ji et al., 2022) |
| PEMS07 | 加州 883 个传感器 | STAEformer (Hu et al., 2024) |

### 7.2 方法名称搜索

**经典方法论文**:
```bash
# STGCN
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=STGCN+spatio-temporal+graph+convolutional&limit=5&fields=title,authors,year,venue,citationCount,externalIds"

# DCRNN
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=DCRNN+diffusion+convolutional+recurrent&limit=5&fields=title,authors,year,venue,citationCount,externalIds"

# Graph WaveNet
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=Graph+WaveNet+traffic&limit=5&fields=title,authors,year,venue,citationCount,externalIds"
```

**方法名称与年份对应**:
| 方法 | 年份 | 会议/期刊 | 核心思想 |
|------|------|-----------|----------|
| STGCN | 2018 | IJCAI | 图卷积 + 门控时间卷积 |
| DCRNN | 2018 | ICLR | 扩散卷积 + 编码器-解码器 |
| Graph WaveNet | 2019 | IJCAI | 自适应图 + 扩展因果卷积 |
| ASTGCN | 2019 | AAAI | 注意力时空图卷积 |
| STSGCN | 2020 | AAAI | 时空同步图卷积 |
| GWNET | 2019 | IJCAI | Graph WaveNet |
| AGCRN | 2020 | NeurIPS | 自适应图卷积循环网络 |
| STAEformer | 2024 | AAAI | 自适应嵌入 Transformer |
| PDFormer | 2023 | AAAI | 传播延迟感知 Transformer |
| DGCRN | 2023 | ICLR | 动态图卷积循环网络 |
| STID | 2023 | AAAI | 纯 MLP 时空嵌入 |
| LargeST | 2024 | NeurIPS | 大规模时空预训练 |

### 7.3 任务类型搜索

**交通速度预测**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22traffic+speed+prediction%22&year=2023-2026&limit=30&fields=title,year,venue,citationCount"
```

**交通流量预测**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22traffic+flow+forecasting%22&year=2023-2026&limit=30&fields=title,year,venue,citationCount"
```

**交通需求预测**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22ride-hailing+demand+prediction%22+OR+%22taxi+demand+forecasting%22&limit=20&fields=title,year,venue,citationCount"
```

**出行时间预测**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22travel+time+estimation%22+OR+%22ETA+prediction%22+graph&limit=20&fields=title,year,venue,citationCount"
```

### 7.4 新方法趋势搜索（2024-2026）

**大模型 + 交通**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22large+language+model%22+AND+%22traffic%22&year=2024-2026&limit=20&fields=title,year,venue,citationCount,abstract"
```

**扩散模型 + 交通**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22diffusion+model%22+AND+%22traffic%22&year=2024-2026&limit=20&fields=title,year,venue,citationCount,abstract"
```

**Mamba / 状态空间模型 + 交通**:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=%22state+space+model%22+AND+%22traffic%22+OR+%22Mamba%22+AND+%22spatiotemporal%22&year=2024-2026&limit=15&fields=title,year,venue,citationCount,abstract"
```

---

## 8. 代码实现模板 (Code Templates)

### 8.1 调用 Semantic Scholar API

```python
"""
Semantic Scholar API 搜索模块
"""
import requests
import time
from typing import List, Dict, Optional


SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1"
DEFAULT_FIELDS = "title,authors,year,venue,citationCount,externalIds,abstract,url"


def search_semantic_scholar(
    query: str,
    limit: int = 100,
    offset: int = 0,
    year: Optional[str] = None,
    venue: Optional[str] = None,
    sort: Optional[str] = None,
    fields: str = DEFAULT_FIELDS,
    api_key: Optional[str] = None,
) -> List[Dict]:
    """
    搜索 Semantic Scholar

    Args:
        query: 搜索关键词
        limit: 返回数量（最大 100）
        offset: 偏移量（分页用）
        year: 年份范围，如 "2024-2026"
        venue: 期刊/会议，如 "TITS,TKDE,KDD"
        sort: 排序，如 "citationCount:desc"
        fields: 返回字段
        api_key: API Key（可选）

    Returns:
        论文列表
    """
    url = f"{SEMANTIC_SCHOLAR_BASE}/paper/search"
    params = {
        "query": query,
        "limit": min(limit, 100),
        "offset": offset,
        "fields": fields,
    }
    if year:
        params["year"] = year
    if venue:
        params["venue"] = venue
    if sort:
        params["sort"] = sort

    headers = {}
    if api_key:
        headers["x-api-key"] = api_key

    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()

    return data.get("data", [])


def search_all_semantic_scholar(
    query: str,
    max_results: int = 200,
    year: Optional[str] = None,
    venue: Optional[str] = None,
    api_key: Optional[str] = None,
) -> List[Dict]:
    """搜索所有结果（自动分页）"""
    all_papers = []
    offset = 0
    batch_size = 100

    while len(all_papers) < max_results:
        remaining = max_results - len(all_papers)
        batch = search_semantic_scholar(
            query=query,
            limit=min(batch_size, remaining),
            offset=offset,
            year=year,
            venue=venue,
            api_key=api_key,
        )
        if not batch:
            break
        all_papers.extend(batch)
        offset += len(batch)
        time.sleep(1)  # 速率限制

    return all_papers[:max_results]


# 使用示例
if __name__ == "__main__":
    papers = search_semantic_scholar(
        query="traffic flow prediction graph neural network",
        limit=50,
        year="2024-2026",
        sort="citationCount:desc",
    )
    for p in papers[:5]:
        print(f"[{p.get('year')}] {p['title']} (citations: {p.get('citationCount', 0)})")
```

### 8.2 调用 DBLP API

```python
"""
DBLP API 搜索模块
"""
import requests
from typing import List, Dict


DBLP_BASE = "https://dblp.org/search/publ/api"


def search_dblp(
    query: str,
    limit: int = 30,
    format: str = "json",
) -> List[Dict]:
    """
    搜索 DBLP

    Args:
        query: 搜索关键词（支持 venue:KDD 等限定）
        limit: 返回数量
        format: 返回格式 ("json" 或 "xml")

    Returns:
        论文列表
    """
    params = {
        "q": query,
        "h": min(limit, 1000),
        "format": format,
    }

    response = requests.get(DBLP_BASE, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    result = data.get("result", {})
    hits = result.get("hits", {})
    if isinstance(hits, int):
        return []

    return hits.get("hit", [])


def extract_dblp_info(hit: Dict) -> Dict:
    """从 DBLP 结果中提取标准化信息"""
    info = hit.get("info", {})
    authors_raw = info.get("authors", {})
    author_list = authors_raw.get("author", [])
    if isinstance(author_list, dict):
        author_list = [author_list]
    authors = [a.get("text", a) if isinstance(a, dict) else str(a) for a in author_list]

    return {
        "title": info.get("title", ""),
        "authors": authors,
        "venue": info.get("venue", ""),
        "year": info.get("year", ""),
        "doi": info.get("doi", ""),
        "url": info.get("url", ""),
        "type": info.get("type", ""),
    }


# 使用示例
if __name__ == "__main__":
    hits = search_dblp("traffic flow prediction venue:KDD", limit=20)
    for hit in hits:
        info = extract_dblp_info(hit)
        print(f"[{info['year']}] {info['title']} @ {info['venue']}")
```

### 8.3 调用 CrossRef API

```python
"""
CrossRef API 搜索模块
"""
import requests
from typing import List, Dict, Optional


CROSSREF_BASE = "https://api.crossref.org/works"
CONTACT_EMAIL = "your@email.com"  # 用于 Polite Pool


def search_crossref(
    query: str,
    rows: int = 20,
    issn: Optional[str] = None,
    from_date: Optional[str] = None,
    until_date: Optional[str] = None,
    sort: Optional[str] = None,
) -> List[Dict]:
    """
    搜索 CrossRef

    Args:
        query: 搜索关键词
        rows: 返回数量
        issn: 期刊 ISSN
        from_date: 起始日期 (YYYY-MM-DD)
        until_date: 截止日期 (YYYY-MM-DD)
        sort: 排序 ("is-referenced-by-count", "published", "relevance")

    Returns:
        论文列表
    """
    params = {
        "query": query,
        "rows": min(rows, 1000),
        "mailto": CONTACT_EMAIL,
    }

    filters = []
    if issn:
        filters.append(f"issn:{issn}")
    if from_date:
        filters.append(f"from-pub-date:{from_date}")
    if until_date:
        filters.append(f"until-pub-date:{until_date}")
    if filters:
        params["filter"] = ",".join(filters)

    if sort:
        params["sort"] = sort
        params["order"] = "desc"

    response = requests.get(CROSSREF_BASE, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    items = data.get("message", {}).get("items", [])
    return items


def extract_crossref_info(item: Dict) -> Dict:
    """从 CrossRef 结果中提取标准化信息"""
    authors = []
    for author in item.get("author", []):
        name = f"{author.get('given', '')} {author.get('family', '')}".strip()
        if name:
            authors.append(name)

    # 提取年份
    pub_date = item.get("published-print", item.get("published-online", {}))
    year = None
    if pub_date and "date-parts" in pub_date:
        date_parts = pub_date["date-parts"][0]
        if date_parts:
            year = date_parts[0]

    # 提取期刊名
    container = item.get("container-title", [])
    journal = container[0] if container else ""

    return {
        "title": item.get("title", [""])[0] if item.get("title") else "",
        "authors": authors,
        "journal": journal,
        "year": year,
        "doi": item.get("DOI", ""),
        "citations": item.get("is-referenced-by-count", 0),
        "url": item.get("URL", ""),
        "type": item.get("type", ""),
    }


# 使用示例
if __name__ == "__main__":
    # 搜索 IEEE TITS 期刊的交通预测论文
    items = search_crossref(
        query="traffic flow prediction",
        rows=20,
        issn="1524-9050",  # IEEE TITS
        from_date="2024-01-01",
        sort="is-referenced-by-count",
    )
    for item in items:
        info = extract_crossref_info(item)
        print(f"[{info['year']}] {info['title']} (cited: {info['citations']})")
```

### 8.4 调用 arXiv API

```python
"""
arXiv API 搜索模块
"""
import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional


ARXIV_BASE = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def search_arxiv(
    query: str,
    max_results: int = 20,
    start: int = 0,
    sort_by: str = "submittedDate",
    sort_order: str = "descending",
) -> List[Dict]:
    """
    搜索 arXiv

    Args:
        query: 搜索查询（支持 cat:cs.LG, ti:xxx 等限定）
        max_results: 返回数量
        start: 偏移量
        sort_by: 排序字段 ("relevance", "lastUpdatedDate", "submittedDate")
        sort_order: 排序方向 ("ascending", "descending")

    Returns:
        论文列表
    """
    params = {
        "search_query": query,
        "start": start,
        "max_results": min(max_results, 200),
        "sortBy": sort_by,
        "sortOrder": sort_order,
    }

    response = requests.get(ARXIV_BASE, params=params, timeout=30)
    response.raise_for_status()

    return parse_arxiv_xml(response.text)


def parse_arxiv_xml(xml_text: str) -> List[Dict]:
    """解析 arXiv XML 响应"""
    root = ET.fromstring(xml_text)
    papers = []

    for entry in root.findall(f"{ATOM_NS}entry"):
        # 提取 arXiv ID
        entry_id = entry.findtext(f"{ATOM_NS}id", "")
        arxiv_id = entry_id.split("/abs/")[-1] if "/abs/" in entry_id else entry_id

        # 提取作者
        authors = []
        for author_elem in entry.findall(f"{ATOM_NS}author"):
            name = author_elem.findtext(f"{ATOM_NS}name", "")
            if name:
                authors.append(name)

        # 提取分类
        categories = []
        for cat_elem in entry.findall(f"{ARXIV_NS}primary_category"):
            term = cat_elem.get("term", "")
            if term:
                categories.append(term)

        papers.append({
            "title": entry.findtext(f"{ATOM_NS}title", "").strip().replace("\n", " "),
            "authors": authors,
            "abstract": entry.findtext(f"{ATOM_NS}summary", "").strip(),
            "published": entry.findtext(f"{ATOM_NS}published", "")[:10],
            "updated": entry.findtext(f"{ATOM_NS}updated", "")[:10],
            "arxiv_id": arxiv_id,
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
            "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
            "categories": categories,
        })

    return papers


# 使用示例
if __name__ == "__main__":
    papers = search_arxiv(
        query="ti:traffic AND ti:prediction AND cat:cs.LG",
        max_results=20,
        sort_by="submittedDate",
        sort_order="descending",
    )
    for p in papers[:5]:
        print(f"[{p['published']}] {p['title']}")
        print(f"  arXiv: {p['arxiv_id']}")
        print(f"  Authors: {', '.join(p['authors'][:3])}...")
        print()
```

### 8.5 完整搜索 + 去重 + 输出流程

```python
"""
完整学术论文搜索流程
整合 Semantic Scholar、DBLP、arXiv、CrossRef 四个数据源
包含去重、合并、排序、输出
"""
import requests
import time
import math
import re
from datetime import datetime
from difflib import SequenceMatcher
from typing import List, Dict, Optional


# ============================================================
# 搜索函数（简化版，仅保留核心逻辑）
# ============================================================

def search_semantic_scholar(query, limit=100, year=None, api_key=None):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": min(limit, 100),
        "fields": "title,authors,year,venue,citationCount,externalIds,abstract,url",
    }
    if year:
        params["year"] = year
    headers = {"x-api-key": api_key} if api_key else {}
    resp = requests.get(url, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get("data", [])


def search_arxiv(query, max_results=20):
    import xml.etree.ElementTree as ET
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "max_results": min(max_results, 100),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    ns = "{http://www.w3.org/2005/Atom}"
    papers = []
    for entry in root.findall(f"{ns}entry"):
        entry_id = entry.findtext(f"{ns}id", "")
        arxiv_id = entry_id.split("/abs/")[-1] if "/abs/" in entry_id else ""
        authors = [a.findtext(f"{ns}name", "") for a in entry.findall(f"{ns}author")]
        papers.append({
            "title": entry.findtext(f"{ns}title", "").strip().replace("\n", " "),
            "authors": authors,
            "abstract": entry.findtext(f"{ns}summary", "").strip(),
            "year": int(entry.findtext(f"{ns}published", "")[:4]) if entry.findtext(f"{ns}published") else None,
            "venue": "arXiv",
            "citationCount": 0,
            "doi": None,
            "arxiv_id": arxiv_id,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "source": "arxiv",
        })
    return papers


# ============================================================
# 去重与合并
# ============================================================

def normalize_title(title):
    title = title.lower().strip()
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title


def title_similarity(t1, t2):
    return SequenceMatcher(None, normalize_title(t1), normalize_title(t2)).ratio()


def deduplicate_papers(papers, title_threshold=0.85):
    """DOI 去重 + 标题相似度去重"""
    doi_map = {}
    no_doi = []
    for p in papers:
        doi = (p.get("doi") or "").strip().lower()
        if doi:
            if doi not in doi_map:
                doi_map[doi] = p
            else:
                # 合并信息
                existing = doi_map[doi]
                if (p.get("citationCount") or 0) > (existing.get("citationCount") or 0):
                    doi_map[doi] = p
        else:
            no_doi.append(p)

    # 对无 DOI 的论文按标题去重
    unique_no_doi = []
    for p in no_doi:
        is_dup = False
        for existing in unique_no_doi:
            if title_similarity(p["title"], existing["title"]) > title_threshold:
                is_dup = True
                break
        if not is_dup:
            # 也和 DOI 列表去重
            for doi_p in doi_map.values():
                if title_similarity(p["title"], doi_p["title"]) > title_threshold:
                    is_dup = True
                    break
        if not is_dup:
            unique_no_doi.append(p)

    return list(doi_map.values()) + unique_no_doi


# ============================================================
# 排序
# ============================================================

def compute_score(paper, query_year=2026):
    citations = paper.get("citationCount") or 0
    cite_score = min(math.log1p(citations) / math.log1p(5000), 1.0)
    year = paper.get("year") or 2020
    recency_score = min(max(0, (year - 2018) / (query_year - 2018)), 1.0)
    return cite_score * 0.5 + recency_score * 0.5


def sort_papers(papers, method="score"):
    if method == "score":
        return sorted(papers, key=lambda p: compute_score(p), reverse=True)
    elif method == "citations":
        return sorted(papers, key=lambda p: p.get("citationCount") or 0, reverse=True)
    elif method == "year":
        return sorted(papers, key=lambda p: p.get("year") or 0, reverse=True)
    return papers


# ============================================================
# 输出
# ============================================================

def format_papers_markdown(papers, title="搜索结果", query=""):
    lines = [f"## {title}", ""]
    lines.append(f"**搜索时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**搜索关键词**: {query}")
    lines.append(f"**共找到**: {len(papers)} 篇论文（去重后）")
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, p in enumerate(papers, 1):
        authors = p.get("authors", [])
        if isinstance(authors, list) and authors and isinstance(authors[0], dict):
            authors = [a.get("name", "") for a in authors]
        author_str = ", ".join(authors[:4])
        if len(authors) > 4:
            author_str += " et al."

        lines.append(f"### {i}. [{p['title']}]")
        lines.append("")
        lines.append(f"- **作者**: {author_str}")
        lines.append(f"- **发表**: {p.get('venue', 'N/A')} {p.get('year', '')}")
        doi = p.get('doi', '')
        if doi:
            lines.append(f"- **DOI**: {doi}")
        lines.append(f"- **引用数**: {p.get('citationCount', 0)}")
        abstract = p.get("abstract", "")
        if abstract:
            lines.append(f"- **摘要**: {abstract[:200]}...")
        lines.append("")

    return "\n".join(lines)


# ============================================================
# 主搜索流程
# ============================================================

def full_search(
    query_ss: str,
    query_arxiv: str,
    year_range: str = "2024-2026",
    max_per_source: int = 100,
    sort_method: str = "score",
    output_file: Optional[str] = None,
):
    """
    完整搜索流程

    Args:
        query_ss: Semantic Scholar 查询语句
        query_arxiv: arXiv 查询语句
        year_range: 年份范围
        max_per_source: 每个数据源最大结果数
        sort_method: 排序方法 ("score", "citations", "year")
        output_file: 输出文件路径（可选）
    """
    print(f"[1/4] 搜索 Semantic Scholar: {query_ss}")
    ss_papers = search_semantic_scholar(query_ss, limit=max_per_source, year=year_range)
    for p in ss_papers:
        p["source"] = "semantic_scholar"
    print(f"  -> 找到 {len(ss_papers)} 篇")

    time.sleep(1)

    print(f"[2/4] 搜索 arXiv: {query_arxiv}")
    arxiv_papers = search_arxiv(query_arxiv, max_results=min(max_per_source, 100))
    print(f"  -> 找到 {len(arxiv_papers)} 篇")

    time.sleep(1)

    # 合并所有结果
    all_papers = ss_papers + arxiv_papers
    print(f"[3/4] 去重: 合并前 {len(all_papers)} 篇")
    unique_papers = deduplicate_papers(all_papers)
    print(f"  -> 去重后 {len(unique_papers)} 篇")

    # 排序
    sorted_papers = sort_papers(unique_papers, method=sort_method)
    print(f"[4/4] 排序完成 (方法: {sort_method})")

    # 输出
    md = format_papers_markdown(
        sorted_papers,
        title="Traffic Flow Prediction 论文搜索结果",
        query=f"{query_ss} | {query_arxiv}",
    )

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"结果已保存至: {output_file}")
    else:
        print(md)

    return sorted_papers


# ============================================================
# 使用示例
# ============================================================

if __name__ == "__main__":
    papers = full_search(
        query_ss="traffic flow prediction graph neural network",
        query_arxiv="ti:traffic AND ti:prediction AND (cat:cs.LG OR cat:cs.AI)",
        year_range="2024-2026",
        max_per_source=50,
        sort_method="score",
        output_file="traffic_prediction_papers.md",
    )

    # 打印前 10 篇
    print("\n--- Top 10 ---\n")
    for i, p in enumerate(papers[:10], 1):
        cite = p.get("citationCount", 0)
        year = p.get("year", "?")
        venue = p.get("venue", "?")
        print(f"{i}. [{year}] [{venue}] {p['title']} (citations: {cite})")
```

---

## 附录: 常用查询速查表

| 搜索目标 | Semantic Scholar 查询 | arXiv 查询 |
|----------|----------------------|------------|
| 交通流预测基础 | `traffic flow prediction` | `ti:traffic AND ti:flow AND ti:prediction` |
| 图神经网络+交通 | `graph neural network traffic` | `ti:graph AND ti:traffic AND cat:cs.LG` |
| Transformer+交通 | `transformer traffic prediction` | `ti:transformer AND ti:traffic` |
| 扩散模型+交通 | `diffusion model traffic` | `ti:diffusion AND ti:traffic` |
| 时空预测 | `spatiotemporal prediction` | `ti:spatiotemporal AND ti:prediction` |
| 交通数据集 | `METR-LA PEMS-BAY benchmark` | `ti:METR-LA OR ti:PEMS-BAY` |
| 大模型+交通 | `large language model traffic` | `ti:LLM AND ti:traffic` |
| 最新综述 | `survey traffic prediction deep learning` | `ti:survey AND ti:traffic AND ti:learning` |

---

## 附录: API 速率限制速查

| 数据源 | 未认证速率 | 认证后速率 | 建议间隔 |
|--------|-----------|-----------|----------|
| Semantic Scholar | 100次/5分钟 | 1次/秒 | 3-5 秒 |
| DBLP | 无硬限制 | N/A | 1 秒 |
| CrossRef | 无硬限制 | Polite Pool 更快 | 1 秒 |
| arXiv | 无硬限制 | N/A | 3 秒 |
| Google Scholar | 无 API | N/A | 10-30 秒（爬虫） |
