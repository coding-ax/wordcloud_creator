#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 0:25
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import jieba
from collections import Counter
import jieba.analyse

# 设置停用词
stopWordList = r"1234567890,./!@#$%^&*()-=+_ \t\n"


# 返回生成词云可用的分词
def get_cut_word(word: str) -> str:
    res = jieba.cut(word, cut_all=True)
    ans = []
    for item in res:
        if item not in stopWordList:
            ans.append(item)
    return "/".join(ans)


# 返回分词列表
def get_cut_word_list(word: str) -> list:
    res = jieba.cut(word)
    ans = []
    for item in res:
        if item not in stopWordList:
            ans.append(item)
    return ans


# 返回词语出现数量
def get_cut_counter(word: list) -> dict:
    return Counter(get_cut_word_list(word))


# TF_IDF返回词频
def TF_IDF_analyse_word(word: str) -> dict:
    # keywords = jieba.analyse.extract_tags(word, topK=5, withWeight=True, ,
    #                                           allowPOS=('n', 'ns', 'nz', 'nt', 'an', 'nw', 'vn'))
    keywords = jieba.analyse.extract_tags(word, topK=50, withWeight=True)
    keywords = dict(keywords)
    return keywords