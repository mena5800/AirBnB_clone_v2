#!/usr/bin/python3
"""this module to try to run flask app"""

# import proper modules flask
from flask import Flask
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
    return escape(text)


if __name__ == "__main__":
    app.run(port=port, host=host)
