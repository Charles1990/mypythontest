import jieba
import numpy as np 
import pandas as pd 
import xlrd

# #写入文字的形式可以导出词频
# text = "目前已经有不少部哲学史了，我的目的并不是要仅仅在它们之中再加上一部【1】。"

# item = text.strip('\n\r').split('\t')

# import jieba.analyse
# tags = jieba.analyse.extract_tags(item[0])

# word_lst = []
# for t in tags:
#    word_lst.append(t)

# word_dict = {}
# for item in word_lst:
#    if item not in word_dict:
#      word_dict[item] = 1
#    else:
#      word_dict[item] += 1   
# word_dict=pd.Series(word_dict)
# word_dict.to_csv('/Users/qingmo/Desktop/test/cccc.csv')

import jieba
import jieba.analyse
word_lst = []
key_lst = []
for line in open('/Users/qingmo/Desktop/test/testtest.txt'):
      item = line.strip('\n\r').split('\t')
      tags = jieba.analyse.extract_tags(item[0])
      for t in tags:
            word_lst.append(t)

word_dict = {}
for item in word_lst:
   if item not in word_dict:
     word_dict[item] = 1
   else:
     word_dict[item] += 1   

word_dict=pd.Series(word_dict)
word_dict.to_csv('/Users/qingmo/Desktop/test/dd.csv')


