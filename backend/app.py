from flask import Flask, request, jsonify
from mongoengine import *

app = Flask(__name__)
app.url_map.strict_slashes = False

DB_URI = 'mongodb+srv://s3yn:s3yn@pi2-j348a.mongodb.net/test?retryWrites=true&w=majority'
connect(host=DB_URI)


class Credential(Document):
    name = StringField(max_length=100, required=True)
    url = StringField(max_length=255, required=True)
    username = StringField(max_length=100, required=True)
    password = StringField(max_length=200, required=True)


@app.route('/api/credentials', methods=['GET'])
def get_credentials():
    credentials = Credential.objects()
    return credentials.to_json()


@app.route('/api/credentials/<credential_id>', methods=['GET'])
def get_credential(credential_id):
    credential = Credential.objects(id=credential_id)
    if not credential:
        return jsonify({'msg': 'Credential not found'})

    return credential.to_json()


@app.route('/api/credentials', methods=['POST'])
def post_credential():
    credential = Credential(
        name=request.json.get('name'),
        url=request.json.get('url'),
        username=request.json.get('username'),
        password=request.json.get('password')
    )
    credential.save()
    return credential.to_json()


@app.route('/api/credentials/<credential_id>', methods=['DELETE'])
def delete_credential(credential_id):
    credential = Credential.objects(id=credential_id)
    if not credential:
        return jsonify({'msg': 'Credential not found'})

    credential.delete()
    return jsonify({'msg': 'Credential deleted'})


if __name__ == '__main__':
    app.run(debug=True)
