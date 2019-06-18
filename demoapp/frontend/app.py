#!/usr/bin/env python

import json
from flask import Flask
from flask import request

from backend_client import get_item, add_item

app = Flask(__name__)


@app.route('/api/v1/exam', methods=[ 'GET', 'POST', 'UPDATE', 'DELETE' ])
def handle_request():
  response = dict()

  if request.method == 'GET':
    token = request.args.get('token', '')
    response = get_item(token)

  elif request.method == 'POST':
    data = request.args.get('data', {})
    response = add_item(data)

  print(response)
  return json.dumps(response)


