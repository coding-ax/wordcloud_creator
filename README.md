#### 在线词云图生成器

1. 前端基于React / React Router /React Router Config /Antd /HighCharts
2. 后端采用flask jieba分词 wordcloud库 requests lxml等爬虫库

### 概述：
本项目采用两种词云图片生成方式：前端通过highcharts生成/后端通过wordcloud生成

### 启动：

启动后端，请确保环境位于python3下：

首先cd到back_end文件目录下

安装库:

```shel
pip install -r requestments.txt
```

（慢的话请自行换源）

安装完毕后：

通过：

```shel
python app.py
```

启动服务器

前端已经打包成静态文件：在后端static目录下

前端开发模式：

cd front_end/react-win-cloud-search

安装依赖：

```shell
npm install
//or
yarn
```

启动：

```shell
npm run start
```

打包
```shell
npm run build
```

#### 预览地址：

http://47.102.212.191:10010/static/index.html#

 
