from flask import render_template
from SLL.index import index



@index.route('/')
def index():
    return render_template('index.html')