# coding: utf-8
import os
import sys
import re
import string

reload(sys)
sys.setdefaultencoding('utf8')

#sO = set(['uv', 'vd', 'ad', 'ag', 'vg', 'nrfg', 'zg', 'vn', 'an', 'vq', 'rr', 'ul', 'ud', 'rz', 'ng', 'nz', 'rg', 'vi', 'u', 'nr', 'ns', 'nt', 'df', 'dg', 'uj', 'mg', 'uz', 'tg', 'nrt', 'a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'mq', 't', 'v', 'y', 'x', 'ug', 'z'])
#s360 = set(['nhd', 'vd', 'ad', 'vf', 'gp', 'nhm', 'vi', 'nnd', 'vl', 'al', 'vn', 'an', 'gg', 'vq', 'gc', 'gb', 'nba', 'nbc', 'nr2', 'gm', 'nnt', 'udh', 'gi', 'rr', 'rzv', 'nrfg', 'ntcf', 'ntcb', 'nf', 'nr1', 'nz', 'rzt', 'rz', 'ntch', 'h', 'ryv', 'mq', 'nr', 'ns', 'nt', 'nw', 'nrj', 'dl', 'bl', 'nts', 'ntu', 'nrf', 'na', 'nth', 'nrt', 'nsf', 'nto', 'nis', 'ntc', 'comb', 'jn', 'nit', 'qt', 'a', 'ry', 'c', 'b', 'e', 'd', 'f', 'i', 'uls', 'j', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'v', 'y', 'rzs', 'z', 'nmc'])
# 比较两个set
def diff(s1, s2):
    left = set([])
    while not len(s1) == 0:
        c = s1.pop()
        if not c in s2:
            left.add(c)
        s2.discard(c)
    print "s1:\t",left
    print "s2:\t",s2

origin_dict = {}

def switch_pos(pos):
    if isinstance(pos, list):
        pos = pos[0]
    if not pos :
        return ''
    elif pos =='N':
        return 'n'
    elif pos =='V':
        return 'v'
    elif pos =='ADJ':
        return 'a'
    elif pos =='ADV':
        return 'd'
    elif pos =='CLAS':
        return 'q'
    elif pos =='ECHO':
        return 'o'
    elif pos =='STRU':
        return 'u'
    elif pos =='AUX':
        return 'u'
    elif pos =='COOR':
        return 'c'
    elif pos =='CONJ':
        return 'c'
    elif pos =='SUFFIX':
        return ''
    elif pos =='PREFIX':
        return ''
    elif pos =='PREP':
        return 'p'
    elif pos =='PRON':
        return 'r'
    elif pos =='QUES':
        return 'd'
    elif pos =='NUM':
        return 'm'
    elif pos =='IDIOM':
        return 'i'
    else:
        return ''

def read_sougou(file_in):
    fd = open(file_in, 'r')
    for line in fd:
        content = line.replace('\n', '').split('\t')
        word = content[0]
        pos = content[2].split(',')[0]
        pos_standard = switch_pos(pos)
        if not freq_dict.has_key(word):
            freq_dict[word] = ''
            pos_dict[word] = pos_standard
    fd.close()

def write_comb_dict(file_out):
    freq_dict_ = sorted(freq_dict.iteritems(), key=lambda d:d[1], reverse=True)
    f = open(file_out, 'w')
    for i in freq_dict_:
        tag = pos_dict[i[0]] if pos_dict.has_key(i[0]) else ''
        f.write(i[0] + ' ' + i[1] + ' ' + tag + '\n')
    f.close()

re_userdict = re.compile('^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)
freq_dict = {}
pos_dict = {}

def default_dict(file_default):
    f = open(file_default, 'rb')
    for line in f:
        word, freq, tag = re_userdict.match(line).groups()
        if freq is not None:
            freq = freq.strip()
        else:
            freq = ''
        if tag is not None:
            tag = tag.strip()
        else:
            tag = ''
        freq_dict[word] = freq
        pos_dict[word] = tag

    f.close()

if __name__ == "__main__" :

    file_default = os.path.join(os.getcwd(), os.path.pardir, 'origin', 'dict.txt')
    file_sogou = os.path.join(os.getcwd(), "SogouLabDic.dic")
    file_out = os.path.join(os.getcwd(), os.path.pardir, "dict_comb.txt")

    default_dict(file_default)
    read_sougou(file_sogou)
    write_comb_dict(file_out)
