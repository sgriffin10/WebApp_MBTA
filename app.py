"""
Belongs to Branch 2
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)



