from lab3.wtiproj03_ETL import pivot_movie_all_genres
from flask import Flask, request, jsonify, make_response
import json
import random

api = Flask(__name__)
api.config['JSON_SORT_KEYS'] = False

data_frame, all_genres = pivot_movie_all_genres()
data_frame = data_frame.fillna(0)


@api.route('/rating', methods=['GET', 'POST', 'DELETE'])
def app():
    if request.method == 'POST':
        value = request.form
        global data_frame
        data_frame = data_frame.append(value, ignore_index=True)
        return json.dumps(value)


@api.route('/ratings', methods=['GET', 'DELETE'])
def ratings():
    global data_frame
    if request.method == 'GET':
        if data_frame.empty:
            return jsonify('empty')
        else:
            json_files = json.loads(data_frame.to_json(orient='records'))
            return make_response(jsonify(json_files), 200)
    if request.method == 'DELETE':
        data_frame = data_frame.iloc[0:0]
        if data_frame.empty:
            return make_response("removed", 200)


@api.route('/ratings/<id>', methods=['GET'])
def get_user(id):
    if data_frame.empty:
        return jsonify('empty')
    else:
        user = {}
        for x in all_genres:
            user[x] = random.uniform(0, 5)
        user['userID'] = id
        return jsonify(user)


@api.route('/ratings/all', methods=['GET'])
def all_users():
    if data_frame.empty:
        return jsonify('empty')
    else:
        users = {}
        for x in all_genres:
            users[x] = random.uniform(0, 5)
        return jsonify(users)


if __name__ == '__main__':
    api.run()