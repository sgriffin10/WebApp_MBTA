"""
Belongs to Branch 2
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

