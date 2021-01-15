from flask import Flask
from day3 import settings

#Flask类
#__name__        --获取当前文件名
#实现了WSGI的应用，充当了核心对象

app = Flask(__name__)

#添加配置文件
app.config.from_object(settings)

#app.config:    配置，字典
#太乱了，一般配置文件解耦，也就是把他放在另一个文件里
#app.config['ENV'] = 'development'
#app.config['DEBUG'] = True




#装饰器
#route是路由
#访问该路由url下的函数

@app.route('/')      #路由
def index():         #视图函数       mtv中的view
    return 'hahahah'

#WSGI :Python Web Server Gateway Interface  Web服务器网关接口
#是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口
#flask 内置服务器

#host：默认只能本机访问，要让其他IP访问，必须设置为0.0.0.0，外网可以访问
#port：可以更改端口号，一个端口对应一个应用程序
#debug：是否启用调试模式 True:只要代码改变，服务器会重新加载最新代码 ，开发环境development ------一般在配置文件写
#环境：   production      development        testing
#                     False   默认

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)

