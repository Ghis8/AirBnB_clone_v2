#!/usr/bin/python3
"""Module using flask to get routes"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """GET Route /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """GET Route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """GET Route /c and <text> to print"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)

"""Init"""
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
