#!/usr/bin/python3
"""this module to try to run flask app"""

# import proper modules flask
from flask import Flask, render_template
from markupsafe import escape

port = 5000
host = "0.0.0.0"
# init flask app
app = Flask(__name__)
# init main route


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_string(text):
    return escape(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def show_python_is(text="is cool"):
    return "python " + escape(text.replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def show_number(num):
    return escape(num) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def send_html(n):
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def send_html_even_odd(n):
    type = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, type=type)

if __name__ == "__main__":
    app.run(port=port, host=host)
