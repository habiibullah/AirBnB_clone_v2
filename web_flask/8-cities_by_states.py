#!/usr/bin/python3

""" cities_by_states: display HTML, state and cities info from storage; """

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def app_context(exception=None):
	"""after each request remove current SQLAlchemy session"""
	storage.close()


@app.route('/cities_by_states')
def html_cities_state():
	"""enumerate all states"""
	html_state = storage.all(State)
	return render_template('8-cities_by_states.html', html_state=html_state)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
	
