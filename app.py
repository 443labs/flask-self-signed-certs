import datetime
import json
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def default():
    data = {
        'method': request.method,
        'local-time': datetime.datetime.now().astimezone().isoformat(),
        'hostname': socket.gethostname()
    }

    if request.method == 'POST':
        data = request.get_json() or data # default to our sample payload if no data was presented

    print('Responding with JSON...', json.dumps(data, indent=2, sort_keys=True))
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context='adhoc', debug=True)