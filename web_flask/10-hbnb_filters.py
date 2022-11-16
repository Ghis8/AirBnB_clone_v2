#!/usr/bin/python3
"""Module using flask to get routes"""

from http.client import FOUND
from flask import Flask, render_template
from models import *
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """GET information of route /hbnb_filters (Objects State)"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


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
