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
    print(keyword)
    if os.path.isfile('./static/imgs/%s.png' % keyword):
        return jsonify({
            'status': 200,
            'msg': '查询成功',
            'url': '/static/imgs/%s.png' % keyword
        })
    try:
        # 首先进行数据爬取
        # 进行分词
        word = CutWord.get_cut_word(GetSpider.save_file(keyword, 1, out_dir_path='./files'))
        WinCloudCreate.createWinCloudPic('./static/imgs/%s.png' % keyword, word,
                                         font_path='./fonts/SanJiXiangXingJianTi-2.ttf',
                                         img_path='./static/imgs/back.png')
    except Exception as e:
        print(e)
        return jsonify({
            'status': 500,
            'url': '',
            'msg': '查询失败'
        })

    return jsonify({
        'status': 200,
        'url': '/static/imgs/%s.png' % keyword,
        'msg': '查询成功'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
