from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

from models.result import Result
from models.user import User

import auth
import config


app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['MONGODB_HOST'] = config.DB_URI
db = MongoEngine(app)


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.check_credentials(email, password)
    if not user:
        return jsonify({'msg': 'Incorrect credentials'}), 404

    return user.to_json()


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


if __name__ == '__main__':
    app.run(debug=True)
