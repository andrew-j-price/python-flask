#!/usr/bin/python
from flask import Flask
import optparse
import socket
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world! from '+socket.gethostname()+'\n'


if __name__ == '__main__':
    parser = optparse.OptionParser(usage='python app.py -p ')
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port is None:
        print 'Missing required argument: -p/--port'
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
