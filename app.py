from flask import Flask
app = Flask(__name__)

@app.route('/page2')
def page2():
    return '<h1>Hello, World!</h1>'

@app.route('/')
def hello_world():
    return 'Hello, World!'
