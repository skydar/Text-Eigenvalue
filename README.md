# Text-Eigenvalue

sample_resumes文件放的是简历样本，来源已经找不到了，请严格遵照里面的版权说明来使用

本实例展示 简历关键词的提取，用于相关性的搜索

## jieba分词

[项目介绍https://github.com/fxsjy/jieba](https://github.com/fxsjy/jieba)
jieba python项目中已经做了比较详细的使用说明了，jieba很简洁，适合需求不复杂的情况使用

### 词库融合

jieba分词是基于词库字典的（dic），所以，词库越大，越准确，分词的效果越好
这里做了jieba提供的词库和sogou流行词库的融合

### idf训练

idf权重是针对具体应用的，不同的应用，同一个词的权重显然不一样
作为tf-idf的一部分idf的准确度直接影响了最后的效果
jieba自带的idf文件适合普通新闻类摘要的应用，所以其他应用要自己训练，

训练过程：

* jieba对训练集各个文本进行分词，得到打散的文本
* 采用sklearn科学计算包，计算分词后的文本集对应的tf-idf矩阵
* 分离tf和idf，输出idf.txt

训练集就是上文提到的网络简历，训练集越大，测试的效果越好

### 测试

一般来说，训练集要包涵测试集，所以就拿训练集中的文本来测试

## 已知的问题：
*词库变动后要清除缓存，windows删除如下:c:\users\xxx\appdata\local\temp\jieba.cache*

*jieba 全模式下中英文混搭的词 比如QQ号 被分为了“QQ”和“号”*

因为jieba/__init__.py下
re_han_cut_all = re.compile("([\u4E00-\u9FD5]+)", re.U)
使得中文和英文被分隔开
(精确模式下没有这个问题，因为使用的是re_han_default，中英文还是连在一起的)

## TODO
* 增加行业分词库 *jieba._get_abs_path("computer.dict.txt")*
* 增加停词库（除非训练集很完善，否则还是很需要的） *jieba.analyse.set_stop_words("stop_words.txt")*