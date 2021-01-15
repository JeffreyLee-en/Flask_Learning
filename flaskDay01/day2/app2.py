from flask import Flask, Response, make_response, request

from day3 import settings

app = Flask(__name__)
app.config.from_object(settings)

#看视图函数
#返回值是response对象
#其他类型的返回，都是把字符串也做了一个response的封装，最终转换的还是response对象
@app.route('/index')
def index():
    return Response('大家想好中午吃什么了吗？')

@app.route('/index2')
def index2():
    return 'sorry', 200          #这个样子的元组，不是写成（）元组
                                 #一般来说，就还是封装成response，200是状态码

@app.route('/index3')
def index3():
    content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
<h1>欢迎来到京东购物</h1>
<div>
    <ul>
        <li>hello</li>
        <li>abc</li>
    </ul>
</div>
</body>
</html>
'''
    response = make_response(content)           ##定制响应头
    response.headers['mytest'] = '123abc'
    return response


@app.route('/index4')
def index4():
    print(request.headers)
    return 'hahahahah'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)