#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """Display a HTML page like 8-index.html"""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    cities = sorted(storage.all("City").values(), key=lambda city: city.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all("Place").values(), key=lambda place: place.name)
    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

