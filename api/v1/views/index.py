#!/usr/bin/python3
''' API status'''

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''

    return jsonify(status='OK')

@app_views.route("/stats", strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)