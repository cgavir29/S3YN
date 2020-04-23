from flask import Flask, flash, request, redirect, url_for, jsonify
from anomaly_detection.feature_extractor import FeatureExtractor
from anomaly_detection.log_parser import LogParser
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from models.result import Result
from models.user import User

import auth
import config

import requests
import os
import sys

UPLOADS_FOLDER = './uploaded_files'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'log'}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['MONGODB_HOST'] = config.DB_URI
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER

db = MongoEngine(app)
CORS(app)


# --------------------------------------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.check_credentials(email, password)
    if not user:
        return jsonify({'msg': 'Incorrect email or password'}), 404

    return jsonify({'user': user})


@app.route('/register', methods=['POST'])
def register():
    try:
        user = User(
            name=request.json.get('name'),
            email=request.json.get('email'),
            password=auth.encrypt_password(request.json.get('password'))
        )
        user.save()
    except:
        return jsonify({'msg': 'Email already taken'}), 500

    return jsonify({'user': user})


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/files', methods=['GET'])
def get_files(user_id):
    try:
        logs = os.listdir(f'{UPLOADS_FOLDER}/{user_id}')

        return jsonify({'logs': logs})
    except FileNotFoundError:
        return jsonify({'msg': "You haven't uploaded any logs yet."}), 404


@app.route('/users/<user_id>/files', methods=['POST'])
def uploaded_file(user_id):
    if 'file' not in request.files:
        return jsonify({'msg': 'Something bad happened...'}), 400

    user_folder = f'{UPLOADS_FOLDER}/{user_id}'
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    file = request.files['file']
    file.save(os.path.join(f'{user_folder}/{file.filename}'))

    return jsonify({'msg': 'File uploaded.'})


@app.route('/users/<user_id>/files/<filename>', methods=['GET'])
def show_file(user_id, filename):

    lines = []

    with open('./uploaded_files/' + str(user_id) + '_' + str(filename), 'r') as log_file:
        for line in log_file.readlines():
            lines.append(line)

    return jsonify(lines)


@app.route('/users/<user_id>/files/<filename>/preprocess', methods=['GET'])
def preprocess(user_id, filename):
    parser = LogParser(f'{UPLOADS_FOLDER}/{user_id}/{filename}')
    events, blk_events = parser.parse()

    extractor = FeatureExtractor(events, blk_events)
    features_vector = extractor.extract()

    return jsonify({'events': events, 'features': features_vector})


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
