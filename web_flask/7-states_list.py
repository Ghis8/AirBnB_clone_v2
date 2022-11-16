#!/usr/bin/python3
"""Module using flask to get routes"""

from flask import Flask, render_template
from models import *
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """GET information of route /states_list (Objects State)"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


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
