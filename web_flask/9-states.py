#!/usr/bin/python3
"""Module using flask to get routes"""

from http.client import FOUND
from flask import Flask, render_template
from models import *
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """GET all information of route /states (Objects State)"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=False)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Route /states with filter <id> (Objects State)"""
    states = storage.all(State)
    for state in states.values():
        if state.id == str(id):
            return render_template('9-states.html', states=state)
    return render_template('9-states.html', no_found=True)


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
