from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from models.result import Result
from models.user import User

import auth
import config

import requests
import os
import sys
sys.path.insert(1, '../anomaly_detection')

from log_parser import LogParser
from feature_extractor import FeatureExtractor

UPLOAD_FOLDER = './uploaded_files'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'log'}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['MONGODB_HOST'] = config.DB_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = MongoEngine(app)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.check_credentials(email, password)
    if not user:
        return jsonify({'msg': 'Incorrect credentials'}), 404

    return jsonify({'user': user.to_json()})

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

    return user.to_json()

@app.route('/users/<user_id>/files', methods=['POST'])
def uploaded_file(user_id):    
    
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
        
    file = request.files['file']
        
    if file.filename == '': 
        flash('No selected file')
        return redirect(request.url)
        
    user_id = request.json.get('user_id')    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], user_id + '_' +file.filename))

    return jsonify({'response': 'File uploaded.'})   

@app.route('/users/<user_id>/files/<file_name>', methods=['GET'])
def show_file(user_id, file_name):
    
    lines = []

    with open('./uploaded_files/' + str(user_id) + '_' + str(file_name), 'r') as log_file:
        for line in log_file.readlines(): lines.append(line)
    
    return jsonify(lines)

@app.route('/users/<user_id>/files/<file_name>/preprocess', methods=['GET'])
def preprocess(user_id, file_name):
    
    parser = LogParser('./uploaded_files/' + str(user_id) + '_' + str(file_name))
    events, blk_events = parser.parse()

    extractor = FeatureExtractor(events, blk_events)
    features_vector = extractor.extract()

    return jsonify({'events': events, 'features': features_vector}) 

if __name__ == '__main__':
    app.run(debug=True)
