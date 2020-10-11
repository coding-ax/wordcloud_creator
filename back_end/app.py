from flask import Flask, request, jsonify
from flask_cors import CORS
import GetSpider
import WinCloudCreate
import CutWord
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return '<h1 style="color:red;text-align:center">当你看到这句话的时候，说明这个服务正在运行</h1>'


@app.route('/getPic', methods=['GET'])
def get_key_word():
    keyword = request.args.get('keyword')
    dqs = request.args.get('dqs') or ""
    salary = request.args.get('salary') or ""
    count = int(request.args.get('count') or 1)
    print(keyword, dqs, salary)
    txt_name = dqs + salary + keyword
    if os.path.isfile('./static/imgs/%s.png' % txt_name):
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'url': '/static/imgs/%s.png' % txt_name
        })
    if os.path.isfile('./static/imgs/%s.txt' % txt_name):
        with open('./static/imgs/%s.txt' % txt_name) as fp:
            word = fp.read()
        word = CutWord.get_cut_word(word)
        WinCloudCreate.createWinCloudPic(file='./static/imgs/%s.png' % txt_name,
                                         keyword=word,
                                         font_path='./fonts/SanJiXiangXingJianTi-2.ttf',
                                         img_path='./static/imgs/back.png')
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'url': '/static/imgs/%s.png' % txt_name
        })
    try:
        # 首先进行数据爬取
        # 进行分词
        word = CutWord.get_cut_word(
            GetSpider.save_file(keyword=keyword, count=count, dqs=dqs,
                                salary=salary,
                                txt_name=txt_name,
                                out_dir_path='./files')
        )
        WinCloudCreate.createWinCloudPic(file='./static/imgs/%s.png' % txt_name,
                                         keyword=word,
                                         font_path='./fonts/SanJiXiangXingJianTi-2.ttf',
                                         img_path='./static/imgs/back.png')
        return jsonify({
            'status': 200,
            'url': '/static/imgs/%s.png' % txt_name,
            'msg': '查询成功'
        })
    except Exception as e:
        print(e)
        return jsonify({
            'status': 500,
            'url': '',
            'msg': '查询失败'
        })


@app.route('/getDict')
def getDict():
    keyword = request.args.get('keyword')
    dqs = request.args.get('dqs') or ""
    salary = request.args.get('salary') or ""
    count = int(request.args.get('count') or 1)
    print(keyword, dqs, salary)
    txt_name = dqs + salary + keyword
    if os.path.isfile('./files/%s.txt' % txt_name):
        with open(file='./files/%s.txt' % txt_name, encoding='utf8') as fp:
            word = fp.read()
        word = CutWord.get_cut_counter(word)
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'word': word
        })
    try:
        # 首先进行数据爬取
        # 进行分词
        word = CutWord.get_cut_word(
            GetSpider.save_file(keyword=keyword, count=count, dqs=dqs,
                                salary=salary,
                                txt_name=txt_name,
                                out_dir_path='./files')
        )
        word = CutWord.get_cut_counter(word)
        return jsonify({
            'status': 200,
            'word': word,
            'msg': '查询成功'
        })
    except Exception as e:
        print(e)
        return jsonify({
            'status': 500,
            'word': '',
            'msg': '查询失败'
        })


@app.route("/getTF")
def tf_tdf_ans():
    keyword = request.args.get('keyword')
    dqs = request.args.get('dqs') or ""
    salary = request.args.get('salary') or ""
    count = int(request.args.get('count') or 1)
    print(keyword, dqs, salary)
    txt_name = dqs + salary + keyword
    if os.path.isfile('./files/%s.txt' % txt_name):
        with open(file='./files/%s.txt' % txt_name, encoding='utf8') as fp:
            word = fp.read()
        word = CutWord.TF_IDF_analyse_word(word)
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'word': word
        })
    try:
        # 首先进行数据爬取
        # 进行分词
        word = CutWord.get_cut_word(
            GetSpider.save_file(keyword=keyword, count=count, dqs=dqs,
                                salary=salary,
                                txt_name=txt_name,
                                out_dir_path='./files')
        )
        word = CutWord.TF_IDF_analyse_word(word)
        return jsonify({
            'status': 200,
            'word': word,
            'msg': '查询成功'
        })
    except Exception as e:
        print(e)
        return jsonify({
            'status': 500,
            'url': '',
            'msg': '查询失败'
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
