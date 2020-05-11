from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from anomaly_detection.feature_extractor import FeatureExtractor
from anomaly_detection.log_parser import LogParser
from anomaly_detection.clustering import Clustering

from models.user import User
from models.result import Result
from models.cluster import Cluster

import auth
import config

import os

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

# --------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------
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

# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/files/<filename>', methods=['GET'])
def show_file(user_id, filename):
    try:
        with open(f'{UPLOADS_FOLDER}/{user_id}/{filename}') as log_file:
            lines = []

            for idx, line in enumerate(log_file):
                if idx < 10:
                    lines.append(line)

        return jsonify({'lines': lines})
    except:
        return jsonify({'msg': 'We were unable to find that file'}), 404

# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/files/<filename>/detect', methods=['GET'])
def preprocess(user_id, filename):
    parser = LogParser(f'{UPLOADS_FOLDER}/{user_id}/{filename}')
    events, log_sequences = parser.parse()

    extractor = FeatureExtractor(log_sequences, events)
    log_sequences = extractor.extract()

    clustering = Clustering(log_sequences, events)
    log_sequences, clusters = clustering.cluster()

    return jsonify({
        'events': events,
        'clusters': clusters
    })

# --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
