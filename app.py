# """
# Belongs to Branch 2
# Simple "Hello, World" application using Flask
# """

# from flask import Flask


# app = Flask(__name__)


# @app.route("/")
# def homepage():
#     return render_template("homepage.html")


# @mbta_helper.route("/hello/")
# @mbta_helper.route("/hello/<name>")
# def hello(name=None):
#     if name:
#         name = name.upper()
#     return render_template("hello.html", name=name)


from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
