from flask import Flask, request, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/api/databases', methods=['GET'])
def get_databases():
    return jsonify({'hello': 'Hello'})


@app.route('/api/databases/<database_id>', methods=['GET'])
def get_database(database_id):
    return jsonify({'db': database_id})


@app.route('/api/databases', methods=['POST'])
def post_database():
    return jsonify(request.json)


@app.route('/api/databases/<database_id>', methods=['DELETE'])
def delete_database():
    return jsonify({'delete': 'mypost'})


if __name__ == '__main__':
    app.run(debug=True)
