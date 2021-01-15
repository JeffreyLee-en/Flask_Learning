#app.py  与模板的结合使用

from flask import Flask, render_template, request

import settings

app = Flask(__name__)
app.config.from_object(settings)
@app.route('/register')
def register():
    r = render_template('register.html')           #找到模板殷勤 Jinjia2 ，找到模板文件夹中的文件，然后转成字符串   #默认去模板文件夹中找文件，为什么？
    # print(r)
    return r

@app.route('/register2', methods = ['GET','POST'])    #post一定要加methods
def register2(): # 获取页面提交的内容
    r = render_template('register.html')
    print(request.full_path)   # /register2?username=dfsd&address=sdfsd
    print(request.path)      # /register2
    print(request.args)
    print(request.args.get('username'))   #GET请求，post请求取不到
    # print(request.form)
    # print(request.form.get('username'))      #post请求取值
    return r


if __name__ == '__main__':
    print(app.url_map)      #路由规则表
    app.run(host='0.0.0.0', port=8080)