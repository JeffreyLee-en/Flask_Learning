import json

from flask import Flask, request, render_template, url_for

import settings
from werkzeug.utils import redirect

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    if n1 > 0 and n2 > 0:
        r = n1 + n2
        return '运算结果是'+str(r)
    return '输入错误'


@app.route('/', endpoint='index')    #endpoint就是起个别名
def index():
    return render_template('index.html')



@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            user = {'username':username,'password':password}
            users.append(user)
            #  return '注册成功 <a href = "/">返回首页</a> '                            #重定向
            url = url_for('index')  #路径反解析
            return redirect(url)   #有两次响应，第一次：302+location     第二次：访问location地址
        else:
            return '两次密码不一致'

    return render_template('register.html')


@app.route('/show')
def show():
    #users[] ----->str      json字符串
    j_str = json.dumps(users)
    return j_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)