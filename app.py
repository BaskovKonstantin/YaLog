from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    if not request.json or not 'level' in request.json or not 'message' in request.json:
        abort(400)
    print('log')
    print(request.json)

    сommand = f"yc logging write \
  --group-name=logger \
  --message='{str(request.json['message'])}' \
  --timestamp='{str(datetime.datetime.now())}' \
  --level={str(request.json['level'])} \
  --json-payload='1'"
    print(сommand)
    os.system(сommand)
    return jsonify(), 201

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
