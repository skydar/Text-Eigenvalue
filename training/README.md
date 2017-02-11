# training idf

```bash
$ idf.py
```

CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵，矩阵元素weight[i][j] 表示j词在第i个文本下的词频，即各个词语出现的次数；通过get_feature_names()可看到所有文本的关键字，通过toarray()可看到词频矩阵的结果。TfidfTransformer也有个fit_transform函数，它的作用是计算tf-idf值
许多同学可能在使用Python进行科学计算时用过稀疏矩阵的构造，而python的科学计算包scipy.sparse是很好的一个解决稀疏矩阵构造/计算的包。
下面我介绍一下scipy.sparse包中csc/csr矩阵的构造中一个比较难理解的构造方法：
官方文档（http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html）中对csc矩阵的构造方法中最后一种：

此外熟悉下scikit-learn，文章很多，列一篇：
http://www.cnblogs.com/focusonepoint/p/5838768.html

然后再看代码中的注释就很清晰了