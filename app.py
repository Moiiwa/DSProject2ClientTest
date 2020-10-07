from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/init/', methods=['POST'])
def init_f():
    pass

@app.route('/create/', methods=['POST'])
def create():
    pass

@app.route('/read/', methods=['GET'])
def read():
    file = open('static/pic.png','rb')
    content = file.read()
    return content

@app.route('/write/', methods=['POST'])
def write():
    pass

@app.route('/delete/', methods=['POST'])
def delete():
    pass

@app.route('/info/', methods=['GET'])
def info():
    pass

@app.route('/copy/', methods=['POST'])
def copy():
    pass

@app.route('/move/', methods=['POST'])
def move():
    pass

@app.route('/open_dir/', methods=['POST'])
def open_dir():
    pass

@app.route('/read_dir/', methods=['GET'])
def read_dir():
    pass

@app.route('/make_dir/', methods=['POST'])
def make_dir():
    pass

@app.route('/delete_dir/', methods=['POST'])
def init():
    pass

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =1337)
