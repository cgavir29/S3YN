from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

from models.result import Result
from models.user import User

import auth
import config


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = config.MONGODB_SETTINGS
app.url_map.strict_slashes = False


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.check_credentials(email, password)
    if not user:
        return jsonify({'msg': 'Incorrect credentials'})

    return user.to_json()

    # user = User.objects(email=email)
    # if not user:
    #    return jsonify({'msg' : 'User not found'})

    # if not auth.check_encrypted_password(password, user.password):
    #     return jsonify({'msg' : 'Password incorrect'})

    # return user.to_json()


@app.route('/register', methods=['POST'])
def register():
    user = User(
        name=request.json.get('name'),
        email=request.json.get('email'),
        password=auth.encrypt_password(request.json.get('password'))
    )

    user.save()


if __name__ == '__main__':
    app.run(debug=True)
