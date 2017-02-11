# coding: utf-8
import os, sys, string, shutil
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

reload(sys)
sys.setdefaultencoding('utf8')

def getFilelist(argv) :
    path = argv
    filelist = []
    files = os.listdir(path)
    for f in files :
        if(f[0] == '.') :
            pass
        if os.path.isfile(f):
            pass
        else :
            filelist.append(f)
    return filelist,path

#对文档进行分词处理
def fenci(argv,path,outdir) :
    filename = argv
    file = os.path.join(path, filename)

    #保存分词结果的目录
    sFilePath = os.path.join(path, outdir)
    if not os.path.exists(sFilePath) :
        os.mkdir(sFilePath)
    #读取文档
    f = open(file,'r+')
    file_list = f.read()
    f.close()

    #对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(file_list,cut_all=True)

    #对空格，换行符进行处理
    result = []
    for seg in seg_list :
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n") :
            result.append(seg)

    f = open(os.path.join(sFilePath, filename), "w+")
    f.write(' '.join(result))
    f.close()

#读取100份已分词好的文档，进行TF-IDF计算
def Tfidf(filelist, path, outdir = os.getcwd()) :
    corpus = []  #存取n份文档的分词结果
    for ff in filelist :
        fname = os.path.join(path, ff)
        f = open(fname,'r+')
        content = f.read()
        f.close()
        corpus.append(content)
    #该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer=CountVectorizer(analyzer='word', min_df=2)
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

    idfdict = {}
    for index, v in enumerate(idf):
        getword = word[index]
        getvalue = v
        if idfdict.has_key(getword):  #更新全局TFIDF值
            idfdict[getword] += string.atof(getvalue)
        else:
            idfdict.update({getword:getvalue})
    sorted_tfidf = sorted(idfdict.iteritems(), key=lambda d:d[1],  reverse=True)

    sFilePath = os.path.join(outdir, 'pre_tfidf')
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)

    f = open(os.path.join(os.getcwd(), r'idf.txt'),'w+')
    for i in sorted_tfidf:
        content = i[0]+' '+str(i[1])+"\n"
        f.write(content)
    f.close()

    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
    for i in range(len(weight)) :
        # n = string.zfill(i,5)+ filelist[i]
        n = filelist[i]
        print "output tf-idf weight file:\t", n
        f = open(os.path.join(sFilePath, n),'w+')
        for j in range(len(word)) :
            f.write(word[j]+"    "+str(weight[i][j])+"\n")
        f.close()

if __name__ == "__main__" :
    samples = os.path.join(os.getcwd(), os.path.pardir, 'sample_resumes')
    (allfile,path) = getFilelist(os.path.join(samples, 'zh'))
    pres = os.path.join(samples, 'pre_texts')
    if os.path.exists(pres):
        shutil.rmtree(pres)
    for ff in allfile :
        print "Using jieba on " + ff
        fenci(ff, path, pres)

    Tfidf(allfile, pres, pres)