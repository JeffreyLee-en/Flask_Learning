from flask import Flask

from day3 import settings

app = Flask(__name__)
#添加配置文件
app.config.from_object(settings)


#定义一个字典

data = {'a': '北京', 'b': '上海', 'c': '深圳'}

@app.route('/')      #路由
def hellow_world():         #视图函数       mtv中的view
    return 'hahahah'

def index():
    return 'hahahha'
app.add_url_rule('/index',view_func = index)


#变量规则
@app.route('/getcity/<key>')   #key是变量名
def get_city(key):
    print(type(key))
    return data.get(key)

@app.route('/add/<int:num>')
def add(num):
    result = num + 5
    return  str(result)

@app.route('/add1/<float:money>')
def add1(money):
    return str(money)

@app.route('/index/<path:p>')   #用的不多
def get_path(p):
    print('--------->', type(p))
    print(p)
    return p

@app.route('/test/<uuid:id>')   #用的很少，必须用uuid格式的
def test(id):
    print('---------->',type(id))
    return 'ssssss'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)