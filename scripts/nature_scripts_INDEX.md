# Nature 相关脚本索引

## 概述

本目录包含支持 Nature 风格论文写作的脚本工具。

## 脚本列表

### 1. academic_search.py

**功能**：学术搜索工具

**能力**：
- 多数据库并行搜索（PubMed, CrossRef, arXiv）
- 结果去重
- 引用格式化
- 搜索策略文档生成

**依赖**：
- requests
- beautifulsoup4
- xml.etree.ElementTree

**使用**：
```bash
python scripts/academic_search.py --query "keyword1 keyword2" --databases pubmed crossref arxiv --limit 50 --output results.json
```

### 2. citation_converter.py

**功能**：引用格式转换

**能力**：
- 支持多种引用格式（APA, Nature, IEEE, Vancouver, Chicago, MLA）
- 批量转换
- 格式验证
- 错误检查

**依赖**：
- re
- json

**使用**：
```bash
python scripts/citation_converter.py --input references.bib --format nature --output references_nature.bib
```

### 3. figure_renderer_nature.py

**功能**：Nature 标准图表渲染

**能力**：
- 应用 Nature 图表标准
- 生成 matplotlib 配置
- 多面板图布局
- SVG/PDF 输出

**依赖**：
- matplotlib
- numpy
- pandas

**使用**：
```bash
python scripts/figure_renderer_nature.py --data data.csv --type bar --output figure1.svg
```

### 4. paper2ppt.py

**功能**：论文转 PPT

**能力**：
- 解析论文结构
- 生成幻灯片大纲
- 创建 .pptx 文件
- 添加演讲者备注

**依赖**：
- python-pptx
- re

**使用**：
```bash
python scripts/paper2ppt.py --input paper.md --output presentation.pptx --language zh
```

### 5. data_availability_checker.py

**功能**：数据可用性检查

**能力**：
- 检查数据可用性声明
- 验证 FAIR 原则
- 评估仓库合规性
- 生成检查报告

**依赖**：
- requests
- json
- re

**使用**：
```bash
python scripts/data_availability_checker.py --input paper.md --output report.json
```

## 安装依赖

```bash
pip install -r requirements_nature.txt
```

## 注意事项

1. 所有脚本遵循 Nature 风格规范
2. 输出格式符合 Nature 期刊要求
3. 错误处理完善
4. 日志记录详细

## 更新日志

- v1.0.0 (2024-01-01): 初始版本
  - academic_search.py
  - citation_converter.py
  - figure_renderer_nature.py
  - paper2ppt.py
  - data_availability_checker.py
