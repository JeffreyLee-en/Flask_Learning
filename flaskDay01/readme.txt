路由的请求和相应：
浏览器地址栏输入的部分：    http://192.168.1.5:8000/index     --------->服务器 -------->app ------>有没有这个路由
-------->有就会执行路由匹配的函数 --- ----->执行函数就会有返回值 ------> response ------>客户端的浏览器


请求：request
http协议：
request  请求

请求行  :  请求地址：http://192.168.1.5:8000/index
          请求方法是什么   get    post  ----一般浏览器点开的get都是
请求头  :
:authority: wgo.mmstat.com
:method: GET
:path: /turing.plan.1?content_type=activity&content_id=164245&lygImp=1&turing_bucket=7&scm=1049.lyg_turing_-1_182.164245.164245-THJH_283828&impid=9r8iZeyJyFG
:scheme: https
accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: cna=OaqGGDQrBWYCAd6ACWXkAyQf; sca=33002926; tbsa=0965d5ac3365d4d98ade7366_1610595385_2; atpsida=481200a13230254a930423f2_1610595385_2
referer: https://www.taobao.com/
sec-fetch-dest: image
sec-fetch-mode: no-cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36


请求体  :  post里面才有

response  响应
响应行：状态码 200：OK    404:not found   ,500      ,    302 -----状态码有哪些？
响应头
响应体  :就是代码return的东西

-------------------------------------------------------------------------------------------------------------------------

day02

一.路由
192.168.1.10:8080

#路由自上向下搜索，有了就进入了
#route 和 add_url_rule的关系

@app.route('/index')
def index()
    return ''

URL : http://192.168.1.10:8080/index

route:
    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator

这个装饰器其实就是讲rule字符串跟视图函数进行了绑定，通过add_url_rule()实现绑定

def index():
    return 'hahahha'
app.add_url_rule('/index',view_func = index)


2.路由的变量规则

string         *（缺省值） 接受任何不包含斜杠的文本
int            * 接受正整数
float           接受正浮点数
path            类似 string ，但可以包含斜杠
uuid            接受 UUID 字符串

@app.route('/add/<int:num>')       #默认字符串
def add(num):                      #参数必须有
    result = num + 5
    return  str(result)

唯一的 URL / 重定向行为
@app.route('/projects/')     #浏览器做重定向
def projects():
    return 'The project page'

@app.route('/about')    #一般这么写
def about():
    return 'The about page'


二.视图
返回值
1.response


2.request

request.path
request.full_path

重点
request.args   --->get请求        http://192.168.3.56:8080/register2?username=ll&address=1123
request.form   --->post请求       在请求体中

3.response
视图函数返回值
1>str
2>dict
3>response对象
4>make_response()
5>redirect()          ----重定向
6>render_template()   ----渲染模板


三.模板{网页}
模板的语法


