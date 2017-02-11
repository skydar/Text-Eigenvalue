# -*- coding: utf-8 -*-
'''
Created on 2014-10-26
@author: zhanghb
'''
import os
import jieba
from jieba.analyse import extract_tags
from word import GrobalParament
import re
def halfcut(content):
    word_list=[]
    k=GrobalParament.n
    f = jieba._get_abs_path(os.path.join('extra_dict', 'computer.dict.txt'))
    jieba.load_userdict(f)
    #jieba.analyse.set_stop_words("stop_words.txt")
    while True:
        cut_content = extract_tags(content, k)
        word_list_temp=cut_content
        if not GrobalParament.ruler_list:
            r=r'[^/\d]{2,}'
            temp='/'.join(word_list_temp)
            word_list=re.findall(r,temp)
        else:
            for word in word_list_temp:
                if word not in GrobalParament.ruler_list:
                    word_list.append(word)
            #print len(word_list)
        if (len(word_list)>=GrobalParament.n):
            break
        else:
            if k - GrobalParament.n > 5:
                break
            word_list=[]
            k+=1
    return word_list