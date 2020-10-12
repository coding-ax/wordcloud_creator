#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 22:27
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm'
# 爬虫相关
import requests
# 解析
from lxml import etree
# ua随机
import random
import os

user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)']


def get_all_links(key: str, count: int = 3, salary: str = "", dqs: str = "") -> dict:
    """
    :param key: 搜索的关键词
    :param salary: 薪资区域
    :param dqs:地区
    :param count: 要爬取的页数
    :return: 一个充满详情页的列表 key  count的字典
    """
    # 定义最后结果数组
    res = []
    for i in range(count):
        # 随机UA
        user_agent = random.choice(user_agents)
        session = requests.Session()
        headers = {
            'User-Agent': user_agent
        }
        response = session.get(
            url='https://www.liepin.com/zhaopin/?key=%s&curPage=%s&dqs=%s&salary=%s' % (key, i, dqs, salary),
            headers=headers)
        html = response.text
        # 解析开始
        # 使用lxml解析
        tree = etree.HTML(html)
        # 拿到etree
        h3s = tree.xpath('//div[contains(@class,"job-info")]/h3')
        for h3 in h3s:
            if len(h3.xpath('./a/@href')) == 0:
                continue
            temp = {
                'title': str(h3.xpath('./a/text()')[0]).strip(),
                'href': str(h3.xpath('./a/@href')[0])
            }
            res.append(temp)
    return {
        'key': key,
        'count': count,
        'data': res
    }


def get_detail_data(url: str) -> dict:
    """
    :param url: 要爬取的详情页面url
    :return:  返回JSON对象
    """
    # 随机ua设置
    user_agent = random.choice(user_agents)

    # 建立关键词用于清洗数据
    describution_word = ['专业要求', '岗位要求', '任职资格', '职位要求', '任职要求', '一些要求']

    # 建立爬取
    session = requests.Session()
    headers = {
        'User-Agent': user_agent
    }
    response = session.get(url=url, headers=headers)
    html = response.text

    # 开始解析
    tree = etree.HTML(html)
    description = list(tree.xpath(
        '//div[contains(@class,"job-description")]/div[contains(@class,"content") and contains(@class,"content-word") ]//text()'))
    desc = ''
    for des in description:
        desc = desc + str(des.strip())

    # 数据清洗
    isFind = False
    for item in describution_word:
        if item in desc:
            idx = desc.find(item)
            desc = desc[idx + 5:]
            isFind = True
            break
    if not isFind:
        desc = ''
    #print(desc)
    # 返回要求
    return {
        'url': url,
        'desc': desc
    }


def save_file(keyword: str, count: int, dqs: str, salary: str, txt_name: str, out_dir_path: str) -> str:
    """
    保存爬取到的文字内容到txt，进行数据持久化
    :param keyword: 关键词
    :param count: 爬取的页数
    :param dqs: 地点
    :param salary: 薪资
    :param out_dir_path: 文件路径
    :return:
    """
    res = ''
    # 检测文件夹存在
    if not os.path.exists(out_dir_path):
        os.mkdir(out_dir_path)
    with open(out_dir_path + '/%s.txt' % txt_name, 'w+', encoding='utf8') as fp:
        try:
            # 进行详情提取
            all_links = get_all_links(key=keyword, count=count, dqs=dqs, salary=salary)
           # print(all_links)
            for data in all_links['data']:
                try:
                    # 进行解析
                    print('正在爬取%s:%s' % (data['title'], data['href']))
                    current = get_detail_data(data['href'])
                    fp.write(current['desc'])
                    res = res + current['desc']
                except Exception as e1:
                    print(e1)
                    continue
            print("爬取完成")
        except Exception as e:
            print(e)
    return res


if __name__ == "__main__":
    get_detail_data(
        'https://www.liepin.com/job/1924502631.shtml?imscid=R000000075&siTag=596nxAVoLb717rCoE4uPCg%7EDf_ytIWx_TSnbjuaKbsjLQ&d_sfrom=search_prime&d_ckId=0614228f32d7993dd7519bb385a6017d&d_curPage=0&d_pageSize=40&d_headId=0614228f32d7993dd7519bb385a6017d&d_posi=0')
