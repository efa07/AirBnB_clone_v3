#!/usr/bin/python3
''' API status'''

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''

    return jsonify(status='OK')