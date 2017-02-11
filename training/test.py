# coding:utf-8
import string
import jieba
import jieba.analyse
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    corpus=["我们 来到 北京 清华大学",
            "他们 来到 网易 杭研 大厦",
            "小明 硕士 毕业 与 中国 科学院",
            "我们 爱 北京 天安门"]

    #该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer=CountVectorizer()
    #将文本转为词频矩阵
    freq_term_matrix = vectorizer.fit_transform(corpus)
    # 稀疏变密集
    #print freq_term_matrix.todense()

    #该类会统计每个词语的tf-idf权值
    tfidf=TfidfTransformer(norm="l2")
    #Now that fit() method has calculated the idf for the matrix
    tfidf.fit(freq_term_matrix)
    idf = tfidf.idf_.tolist()
    #计算tfidf
    tf_idf_matrix = tfidf.transform(freq_term_matrix)
    #print tf_idf_matrix.todense()

    #获取词袋模型中的所有词语
    word=vectorizer.get_feature_names()
    #将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    weight=tf_idf_matrix.toarray()


    #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        print u"-------这里输出第",i,u"类文本的词语tf-idf权重------"
        for j in range(len(word)):
            print word[j],weight[i][j]


    idfdict = {}
    for index, v in enumerate(idf):
        getword = word[index]
        getvalue = v
        if idfdict.has_key(getword):  #更新全局TFIDF值
            idfdict[getword] += string.atof(getvalue)
        else:
            idfdict.update({getword:getvalue})
    sorted_tfidf = sorted(idfdict.iteritems(), key=lambda d:d[1],  reverse=True)

    file = os.path.join(os.getcwd(), r'idf.txt')
    f = open(file,'w+')
    for i in sorted_tfidf:
        content = i[0]+' '+str(i[1])+"\n"
        f.write(content)
    f.close()

    jieba.analyse.set_idf_path(file)
    for ws in corpus:
        cut_content = jieba.analyse.extract_tags(ws, 10)
        print ','.join(cut_content)
