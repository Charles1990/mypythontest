import jieba
import numpy as np 
import pandas as pd 
import xlrd

def gettext():
    txt = open("/Users/qingmo/Desktop/test/testenglish.txt","r",errors='ignore').read()
    txt = txt.lower()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’':
        txt = txt.replace(ch,"")
    return txt

txt = gettext()
words = txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)


items=pd.DataFrame(items)
items.to_csv('/Users/qingmo/Desktop/test/ddcc.csv')
