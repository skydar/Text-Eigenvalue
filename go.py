# -*- coding: utf-8 -*-
import os, sys
from word.prepro_file import prepro_file
from word.TF_IDF_Compute import TF_IDF_Compute


def curDir():
    #运行目录
    #CurrentPath = os.getcwd()
    #return CurrentPath
    #当前脚本
    #return sys.argv[0]
    #当前脚本目录
    ScriptPath = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
    print ScriptPath
    return ScriptPath

#预处理文件目录
PreprocessResultDir = os.path.join(os.getcwd(), "test")
#预处理文件名
PreprocessResultName = "pro_res.txt"
#搜索结果文件目录
ResultFileNameDir = os.path.join(os.getcwd(), "test")
#搜索结果文件名
ResultFileName = "result.txt"

def Preprocess(file_url):
    PreResUrl = os.path.join(PreprocessResultDir, PreprocessResultName)
    prepro_file(file_url,PreResUrl)

def TF_IDF(*words):
    PreResUrl = os.path.join(PreprocessResultDir, PreprocessResultName)
    ResFileUrl = os.path.join(ResultFileNameDir, ResultFileName)
    return TF_IDF_Compute(PreResUrl,ResFileUrl,*words)

path = os.path.join(os.getcwd(), 'test', 'doc')

if __name__ == '__main__':
    Preprocess(path)
    # 查找关键字所在的文档名
    print TF_IDF("JAVA")