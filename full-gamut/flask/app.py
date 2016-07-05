#!/usr/bin/python
from flask import Flask
from flask import g
from flask import jsonify
from flask import request
from flask import Response
import json
import MySQLdb
import optparse
import socket
import sys

app = Flask(__name__)


@app.before_request
def db_connect():
    g.conn = MySQLdb.connect(host='mariadb',
                             user='root',
                             passwd='Password123',
                             db='api')
    g.cursor = g.conn.cursor()


@app.after_request
def db_disconnect(response):
    g.cursor.close()
    g.conn.close()
    return response


def query_db(query, args=(), one=False):
    g.cursor.execute(query, args)
    rv = [dict((g.cursor.description[idx][0], value)
        for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv


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


@app.route("/names", methods=['GET'])
def names_get():
    result = query_db("SELECT * FROM names")
    data = json.dumps(result)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


@app.route("/names", methods=['POST'])
def names_add():
    req_json = request.get_json()
    g.cursor.execute("INSERT INTO names (firstname, lastname) VALUES (%s,%s)", (req_json['firstname'], req_json['lastname']))
    g.conn.commit()
    resp = Response("Updated", status=201, mimetype='application/json')
    return resp


@app.errorhandler(404)
def not_found(error=None):
    return '404\n'


@app.route('/names/<int:post_id>', methods=['DELETE'])
def names_delete(post_id):
    g.cursor.execute("DELETE FROM names WHERE id = %s", str(post_id))
    g.conn.commit()
    resp = Response("Deleted", status=202, mimetype='application/json')
    return resp


if __name__ == "__main__":
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=True)
