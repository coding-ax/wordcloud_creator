#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 0:25
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
import jieba


def get_cut_word(word: str) -> str:
    res = jieba.cut(word)
    return "/".join(res)
