from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from anomaly_detection.feature_extractor import FeatureExtractor
from anomaly_detection.log_parser import LogParser
from anomaly_detection.clustering import Clustering

# Models
from models.user import User
from models.result import Result
from models.system import System
# from models.cluster import Cluster

# Routes
from routes.users import user_routes

import config

import os

ALLOWED_EXTENSIONS = {'txt', 'csv', 'log'}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['MONGODB_HOST'] = config.DB_URI

app.register_blueprint(user_routes)

db = MongoEngine(app)
CORS(app)


@app.route('/systems')
def get_systems():
    try:
        systems = System.objects.only('name')

        return jsonify({'systems': systems})
    except:
        return jsonify({'msg': 'Internal server error'}), 500


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/files')
def get_files(user_id):
    try:
        files = []

        systems = os.listdir(f'{config.UPLOADS_FOLDER}/{user_id}')
        for system in systems:
            files.append({
                'system': system,
                'logs': os.listdir(f'{config.UPLOADS_FOLDER}/{user_id}/{system}')
            })

        return jsonify({'files': files})
    except FileNotFoundError:
        return jsonify({'msg': "You haven't uploaded any files yet."}), 404


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/systems/<system_name>/files', methods=['POST'])
def save_file(user_id, system_name):
    if 'file' not in request.files:
        return jsonify({'msg': 'Something bad happened...'}), 400

    user_folder = f'{config.UPLOADS_FOLDER}/{user_id}'
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    system_folder = f'{user_folder}/{system_name}'
    if not os.path.exists(system_folder):
        os.makedirs(system_folder)

    file = request.files['file']
    file.save(os.path.join(f'{system_folder}/{file.filename}'))

    return jsonify({'msg': 'File uploaded.'})


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/systems/<system_name>/files/<filename>')
def get_file(user_id, system_name, filename):
    try:
        with open(f'{config.UPLOADS_FOLDER}/{user_id}/{system_name}/{filename}') as file:
            lines = []

            for idx, line in enumerate(file):
                if idx < 10:
                    lines.append(line)

        return jsonify({'lines': lines})
    except:
        return jsonify({'msg': 'We were unable to find that file'}), 404


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/systems/<system_name>/files/<filename>/preprocess')
def preprocess(user_id, system_name, filename):

    parser = LogParser(
        f'{config.UPLOADS_FOLDER}/{user_id}/{system_name}/{filename}')
    events, _ = parser.parse()

    system = System.objects(name=system_name).first()
    system_events_name = [event.name for event in system.events]
    # f'{system_name/filename}'
    setEvents = set(events)
    setSystemEventsName = set(system_events_name)

    registeredEvents = list(setEvents.intersection(setSystemEventsName))
    unregisteredEvents = list(setEvents - setSystemEventsName)

    return jsonify({
        'registeredEvents': registeredEvents,
        'unregisteredEvents': unregisteredEvents
    })


# --------------------------------------------------------------------------------
@app.route('/users/<user_id>/systems/<system_name>/files/<filename>/detect', methods=['POST'])
def detect(user_id, system_name, filename):
    events = request.json.get('events')
    # Save events to the corresponding System document if not there previously.

    parser = LogParser(
        f'{config.UPLOADS_FOLDER}/{user_id}/{system_name}/{filename}')
    _, log_sequences = parser.parse()

    extractor = FeatureExtractor(log_sequences, events)
    log_sequences = extractor.extract()

    clustering = Clustering(log_sequences, events)
    log_sequences, clusters = clustering.cluster()

    # Save clusters to the log's Result document.

    return jsonify({'clusters': clusters})


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
