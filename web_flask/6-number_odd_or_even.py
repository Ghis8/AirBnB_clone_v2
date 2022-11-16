#!/usr/bin/python3
"""Module using flask to get routes"""

from flask import Flask, render_template
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


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """GET Route /python and <text> to print"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/python', strict_slashes=False)
def python_default():
    """route /python with print to default"""
    return 'Python is cool'


@app.route('/number/<int:number>', strict_slashes=False)
def number(number):
    """route /number is exec if <number> is integer"""
    return '{} is a number'.format(number)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route /number_template that redirect a html and print a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """Route /number_odd_or_even with dinamics tags html"""
    context = {
        'n': n,
    }
    return render_template('6-number_odd_or_even.html', **context)

"""Init"""
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
