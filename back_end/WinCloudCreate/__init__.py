#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 0:49
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
# 数学绘图库
import matplotlib.pyplot as plt
# 词云
from wordcloud import WordCloud
# 导入图像处理库
import PIL.Image as image
# 导入数据处理库
import numpy as np


def createWinCloudPic(file: str, keyword: str, font_path: str, img_path: str):
    print("正在生成词云图")
    # 生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
    # 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
    # 自定义图片生成词云
    img = np.array(image.open(img_path))
    wc = WordCloud(font_path=font_path,
                   background_color='white',
                   width=980,
                   height=540,
                   max_font_size=200,
                   mask=img,
                   max_words=2000)  # ,min_font_size=10)#,mode='RGBA',colormap='pink')
    wc.generate(keyword)
    wc.to_file(file)  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
    print("生成完成")
    # 4、显示图片
    # plt.figure("%s词云图" % file.split('/')[-1][:-4])  # 指定所绘图名称
    # plt.imshow(wc)  # 以图片的形式显示词云
    # plt.axis("off")  # 关闭图像坐标系
    # plt.show()
