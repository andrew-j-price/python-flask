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
    g.conn = MySQLdb.connect(host='mariadb', db='api',
                             user='root', passwd='Password123')
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


@app.route("/health", methods=['GET'])
def api_health():
    result = query_db("SELECT API FROM health")
    data = json.dumps(result)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


@app.route("/minions", methods=['GET'])
def minions_get():
    result = query_db("SELECT * FROM minions")
    data = json.dumps(result)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


@app.route("/minions", methods=['POST'])
def minions_add():
    req_json = request.get_json()
    g.cursor.execute("INSERT INTO minions (firstname, lastname) VALUES (%s,%s)", (req_json['firstname'], req_json['lastname']))
    g.conn.commit()
    resp = Response("Updated", status=201, mimetype='application/json')
    return resp


@app.route('/minions/<int:post_id>', methods=['DELETE'])
def minions_delete(post_id):
    g.cursor.execute("DELETE FROM minions WHERE id = %s", str(post_id))
    g.conn.commit()
    resp = Response("Accepted", status=202, mimetype='application/json')
    return resp


@app.route("/users", methods=['GET'])
def users_get():
    result = query_db("SELECT * FROM users")
    data = json.dumps(result)
    resp = Response(data, status=200, mimetype='application/json')
    return resp


@app.route("/users", methods=['POST'])
def users_add():
    req_json = request.get_json()
    g.cursor.execute("INSERT INTO users (name, city, state, country) VALUES (%s,%s,%s,%s)", (req_json['name'], req_json['city'], req_json['state'], req_json['country']))
    g.conn.commit()
    resp = Response("Updated", status=201, mimetype='application/json')
    return resp


@app.route('/users/<int:post_id>', methods=['DELETE'])
def users_delete(post_id):
    g.cursor.execute("DELETE FROM users WHERE id = %s", str(post_id))
    g.conn.commit()
    resp = Response("Accepted", status=202, mimetype='application/json')
    return resp


@app.errorhandler(404)
def not_found(error=None):
    return '404\n'


if __name__ == "__main__":
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=True)
