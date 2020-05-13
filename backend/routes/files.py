# import os
# import config
# from flask import Blueprint, request, jsonify

# user_routes = Blueprint('user_routes', __name__)

# @app.route('/users/<user_id>/files', methods=['GET'])
# def get_files(user_id):
#     try:
#         logs = os.listdir(f'{config.UPLOADS_FOLDER}/{user_id}')

#         return jsonify({'logs': logs})
#     except FileNotFoundError:
#         return jsonify({'msg': "You haven't uploaded any logs yet."}), 404

# # --------------------------------------------------------------------------------
# @app.route('/users/<user_id>/files', methods=['POST'])
# def uploaded_file(user_id):
#     if 'file' not in request.files:
#         return jsonify({'msg': 'Something bad happened...'}), 400

#     user_folder = f'{config.UPLOADS_FOLDER}/{user_id}'
#     if not os.path.exists(user_folder):
#         os.makedirs(user_folder)

#     file = request.files['file']
#     file.save(os.path.join(f'{user_folder}/{file.filename}'))

#     return jsonify({'msg': 'File uploaded.'})

# # --------------------------------------------------------------------------------


# @app.route('/users/<user_id>/files/<filename>', methods=['GET'])
# def show_file(user_id, filename):
#     try:
#         with open(f'{config.UPLOADS_FOLDER}/{user_id}/{filename}') as log_file:
#             lines = []

#             for idx, line in enumerate(log_file):
#                 if idx < 10:
#                     lines.append(line)

#         return jsonify({'lines': lines})
#     except:
#         return jsonify({'msg': 'We were unable to find that file'}), 404
