#!/usr/bin/python3
''' State module'''

from api.v1.views import app_views
from flask import Flask, abort, request, jsonify
from models.state import State
from os import name


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def toGet():
    '''getting thing'''
    objects = storage.all('State')
    lista = []
    for state in objects.values():
        lista.append(state.to_dict())
    return jsonify(lista)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def toGetid(state_id):
    '''Updates a State object id'''
    objects = storage.get('State', state_id)
    if objects is None:
        abort(404)
    return jsonify(objects.to_dict()), 'OK'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def posting():
    '''Creates a State'''
    response = request.get_json()
    if response is None:
        abort(400, {'error': 'Not a JSON'})
    if 'name' not in response:
        abort(400, {'error': 'Missing name'})
    stateObject = State(name=response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def putinV(state_id):
    '''vladimir'''
    response = request.get_json()
    if response is None:
        abort(400, {'error': 'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key, value in response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key, value)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting(state_id):
    ''' to delete an object'''
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), '200'