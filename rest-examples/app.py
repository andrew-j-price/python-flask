#!/usr/bin/python
from flask import Flask, json, jsonify, Response, request, url_for
import optparse
import socket
import sys

app = Flask(__name__)


@app.route('/')
def api_root():
    return socket.gethostname()


# Utilizes: url_for
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


# Utilizes: url_for
@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


# Utilizes: import request
@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


# Utilizes: import request
@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


# Utilizes: import json
@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return request.data
    elif request.headers['Content-Type'] == 'application/json':
        return json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"


# Utilizes: Response
@app.route('/health', methods=['GET'])
def api_health():
    data = {
        'API': 'Healthy'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


# Utilizes: jsonify
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


# Utilizes: jsonify
@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {'1': 'john', '2': 'steve', '3': 'bill'}
    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()


if __name__ == '__main__':
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
