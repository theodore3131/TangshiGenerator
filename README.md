# 使用python生成唐诗
- 环境：python 3.6，anaconda管理架包
## 步骤
- 使用beautifulsoup4爬虫爬取古诗文网 http://www.gushiwen.org 上的全唐诗
- 使用正则表达式对爬取的数据进行处理（去除题目，作者，卷名）
- 使用jieba中文分词对处理后的唐诗进行分词并使用textRank算法分词性提取各个词性的高频词
- 根据字数，平仄，押韵等规则对得到的高频词进行排列组合。
