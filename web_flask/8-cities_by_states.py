#!/usr/bin/python3
"""Module using flask to get routes"""

from flask import Flask, render_template
from models import *
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """GET information of route /cities_by_states (Objects State)"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def storage_close(self):
    '''Close current session'''
    storage.close()

"""Init"""
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
