# """
# Belongs to Branch 2
# Simple "Hello, World" application using Flask
# """

# from flask import Flask


# app = Flask(__name__)


from flask import Flask, escape, url_for, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
# 
# 
# @app.route("/hello/")
# def hello_human(name=None):
#     if name:
#         name = name.upper()
#     return render_template("hello.html", name=name)

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/mbta_helper", methods= ["GET", "POST"]) #binds a function to a specified URL
def find_neareststop_and_accessibility():
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    if request.method == "POST":
        place_name = request.form["place"]
        # wheelchair_boarding = str(request.form["wheelchair_boarding"]) 
        # print(place_name)
        stop, wheelchair_boarding = find_stop_near(place_name)

        return render_template(
            "input_results.html", stop=stop, wheelchair_boarding=wheelchair_boarding
        )
    else:
        return render_template ("input_form.html", error=True)
    return render_template("input_form.html", error=None)

 
    # return '{}\'s mbta_helper'.format(escape(username))


with app.test_request_context():   
    # print(url_for('homepage'))
    print(url_for('find_neareststop_and_accessibility'))
