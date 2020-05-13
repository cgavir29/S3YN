from flask import Blueprint, request, jsonify
from models.user import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.check_credentials(email, password)
    if not user:
        return jsonify({'msg': 'Incorrect email or password'}), 404

    return jsonify({'user': user})


@user_routes.route('/register', methods=['POST'])
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
