#开始讲模板了
from flask import Flask, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run()