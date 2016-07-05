#!/usr/bin/python
from flask import Flask, json, Response
import optparse
import socket
import sys

app = Flask(__name__)


@app.route('/')
def api_root():
    return socket.gethostname()+'\n'


@app.route('/health', methods=['GET'])
def api_health():
    payload = {
        'API': 'Healthy'
    }
    data = json.dumps(payload)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


@app.errorhandler(404)
def not_found(error=None):
    return '404\n'


if __name__ == '__main__':
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
