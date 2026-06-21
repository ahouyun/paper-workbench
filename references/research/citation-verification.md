# 文献引用验证指南 (Citation Verification Guide)

> 解决AI生成论文中最致命的问题：幻觉引用（hallucinated citations）。

---

## 一、为什么必须验证引用

**编辑的原话：** "AI 生成的文献引用有极高的幻觉率。TITS 的审稿人会对每条关键引用进行核实。如果你引用了一篇不存在的论文，或错误描述了前人工作的结论，这是学术不端，不是润色能解决的。"

**常见幻觉类型：**
- 编造不存在的论文标题
- 编造不存在的作者
- 编造不存在的DOI
- 错误描述论文的实际内容
- 引用存在但年份/期刊/会议错误

---

## 二、验证流程（必须执行）

### ⚠️ 强制验证要求

**在提交论文前，必须完成以下验证：**

1. 所有引用的论文必须通过至少1个API验证存在
2. 所有引用的DOI必须是真实的（不是Phantom ID）
3. 所有引用的创新描述必须与原文一致
4. 所有引用的数字必须从原文表格中复制

**不执行验证 = 潜在的学术不端**

### 步骤1：验证论文存在性

对每条引用，必须通过以下至少1个来源验证：

| 来源 | API | 验证内容 |
|------|-----|---------|
| Semantic Scholar | `api.semanticscholar.org` | 标题、作者、年份、DOI |
| CrossRef | `api.crossref.org` | DOI解析、元数据 |
| DBLP | `dblp.org` | CS会议/期刊论文 |
| arXiv | `arxiv.org` | 预印本 |

**验证代码：**
```python
import requests

def verify_citation(title, authors=None, year=None):
    """验证论文是否存在，返回验证结果"""
    # 1. Semantic Scholar验证
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": title, "limit": 3, "fields": "title,authors,year,venue,externalIds"}
    resp = requests.get(url, params=params, timeout=10)
    
    if resp.status_code == 200:
        papers = resp.json().get("data", [])
        for p in papers:
            if p["title"].lower().strip() == title.lower().strip():
                return {"status": "verified", "paper": p}
            # 模糊匹配
            if title.lower()[:30] in p["title"].lower():
                return {"status": "possible_match", "paper": p}
    
    # 2. CrossRef验证
    url = "https://api.crossref.org/works"
    params = {"query": title, "rows": 3}
    resp = requests.get(url, params=params, timeout=10)
    
    if resp.status_code == 200:
        items = resp.json().get("message", {}).get("items", [])
        for item in items:
            item_title = item.get("title", [""])[0]
            if title.lower()[:30] in item_title.lower():
                return {"status": "verified", "source": "crossref", "doi": item.get("DOI")}
    
    return {"status": "NOT_FOUND", "warning": "可能为幻觉引用！"}
```

### 步骤2：验证内容准确性

即使论文存在，也必须验证：
- ✅ 作者是否正确
- ✅ 年份是否正确
- ✅ 期刊/会议是否正确
- ✅ 你描述的"核心创新"是否真的是论文的创新
- ✅ 你引用的数字是否来自该论文

**常见错误：**
- ❌ "PDFormer (AAAI 2023) 提出了自适应图学习" — 实际上PDFormer的核心是传播延迟感知，不是自适应图学习
- ❌ "STAEformer在METR-LA上MAE为2.49" — 需要核实具体数字

### 步骤3：Phantom ID检测

**什么是Phantom ID：** 格式正确但不存在的DOI/arXiv ID

```python
def check_phantom_id(doi=None, arxiv_id=None):
    """检测Phantom ID"""
    if doi:
        url = f"https://api.crossref.org/works/{doi}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            return {"status": "PHANTOM", "warning": f"DOI {doi} 不存在！可能是幻觉引用！"}
    
    if arxiv_id:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        resp = requests.get(url, timeout=10)
        if "<entry>" not in resp.text:
            return {"status": "PHANTOM", "warning": f"arXiv ID {arxiv_id} 不存在！"}
    
    return {"status": "ok"}
```

---

## 三、引用描述准确性检查

**规则：** 每次引用论文时，必须确保你的描述与论文实际内容一致。

| 检查项 | 正确做法 | 错误做法 |
|--------|---------|---------|
| 创新描述 | 描述论文的实际核心贡献 | 把A论文的创新说成B论文的 |
| 数字引用 | 直接从论文表格中复制数字 | 凭记忆或AI生成数字 |
| 方法描述 | 准确描述论文使用的方法 | 泛泛说"提出了新方法" |
| 结论描述 | 准确描述论文的实际结论 | 夸大或曲解论文结论 |

**验证清单：**
- [ ] 每条引用的论文标题已通过API验证存在
- [ ] 每条引用的作者已验证正确
- [ ] 每条引用的年份已验证正确
- [ ] 每条引用的创新描述已与原文核对
- [ ] 每条引用的数字已从原文表格中复制
- [ ] 没有Phantom ID（格式正确但不存在的DOI）

---

## 四、参考文献管理工具

### 推荐工具组合

| 工具 | 用途 | 优先级 |
|------|------|--------|
| **Zotero** | 文献管理、自动抓取元数据 | 高 |
| **Better BibTeX** | Zotero插件，自动生成BibTeX | 高 |
| **bibguard** | 检测幻觉引用 | 高 |
| **doi-mcp** | 9数据库验证引用 | 中 |

### BibTeX管理最佳实践

```bibtex
% 每条BibTeX必须包含DOI
@article{staeformer2024,
  title={STAEformer: Spatio-Temporal Adaptive Embedding Makes Better Traffic Forecasters},
  author={Shao, Zezhi and Zhang, Zhao and Wang, Fei and Xu, Yongjun},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2024},
  doi={10.1109/TITS.2024.XXXXXXX}  % 必须有DOI
}
```

---

## 五、自查清单

在提交论文前，逐项检查：

- [ ] 所有引用的论文都通过至少1个API验证存在
- [ ] 所有引用的DOI都是真实的（不是Phantom ID）
- [ ] 所有引用的创新描述都与原文一致
- [ ] 所有引用的数字都从原文表格中复制
- [ ] 没有凭记忆或AI生成的引用
- [ ] 参考文献格式统一（IEEE格式）
- [ ] 正文中引用的论文都在参考文献列表中
- [ ] 参考文献列表中的论文都在正文中被引用

---

> 来源：tfscharff/doi-mcp, GeoffreyWang1117/bibguard, ykangw/VeriExCiting
> 更新时间：2026-06-20
