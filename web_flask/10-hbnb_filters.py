#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb_filters')
def hbnb_filters():
    """ Display a HTML page with filters """
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def teardown(exception):
    """ Closes the current SQLAlchemy session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

