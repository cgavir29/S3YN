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
from models.event import Event
from models.cluster import Cluster

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
@app.route('/users/<user_id>/systems/<system_name>/files/<filename>/detect', methods=['POST'])
def detect(user_id, system_name, filename):
    parser = LogParser(
        f'{config.UPLOADS_FOLDER}/{user_id}/{system_name}/{filename}')
    events, log_sequences = parser.parse()

    extractor = FeatureExtractor(log_sequences, events)
    log_sequences = extractor.extract()

    clustering = Clustering(log_sequences, events)
    log_sequences, clusters = clustering.cluster()
    print(clusters)

    # document_clusters = []
    # for cluster in clusters:
    #     document_clusters.append(
    #         Cluster(
    #             centroid=cluster.get('centroid'),
    #             num_possible_abnormal_events=cluster.get(
    #                 'num_possible_abnormal_events'),
    #             possible_abnormal_events=cluster.get(
    #                 'possible_abnormal_events')
    #         )
    #     )

    # document_events = []
    # document_names = []
    # for name, status in events.items():
    #     document_events.append(Event(name=name, status=status))
    #     document_names.append(name)

    # system = System.objects(name=system_name).first()

    # system_events_name = [event.name for event in system.events]

    # setEvents = set(document_names)
    # setSystemEventsName = set(system_events_name)

    # unregisteredEvents = list(setEvents - setSystemEventsName)

    # agregar los unregisteredEvents al system en el atributo de events

    # falta merterle a result los clusters, si se junta el preprocess y detect
    # ir al modelo de result y pner el campo cluster required true

    # {
    #     'posible_abnormal_events': 1,
    #     'event(juanchito * pepito)': ['blk343545', 'blk565478']
    # }

    # result = Result(
    #     user_id=user_id,
    #     path=f'{system_name}/{filename}',
    #     events=document_events

    # )

    # verificar el json document_events
    return jsonify({
        'events': events,
        'clusters': clusters
    })


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
