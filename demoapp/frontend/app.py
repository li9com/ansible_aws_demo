#!/usr/bin/env python

import json
from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime

from forms import AddItemForm, GetItemForm

from backend_client import get_item, add_item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-secret-value'

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


@app.route("/", methods=[ 'GET', ])
def page_welcome():
  return render_template('main.html.j2', title='Welcome page')


@app.route("/add", methods=[ 'GET', ])
def page_add():
  form = AddItemForm()
  return render_template('subpage-add.html.j2', title='Add record', form=form)


@app.route("/get", methods=[ 'GET', ])
def page_get():
  form = GetItemForm()
  return render_template('subpage-get.html.j2', title='Get record', form=form)


@app.route("/get-post", methods=[ 'POST', ])
def page_get_handler():
  form = GetItemForm()
  data = "No data found or something went wrong"
  if form.validate_on_submit():
    token = form.token.data
    backend_response = get_item(token=token)
    if backend_response.get('Item', False):
      data = json.dumps(backend_response.get('Item'))
  return render_template('subpage-display-record.html.j2', title='Display record ' + token, data=data)


@app.route("/add-post", methods=[ 'POST', ])
def page_add_handler():
  form = AddItemForm()
  if form.validate_on_submit():
    data = {
      "token": form.token.data,
      "data": {
        "metadata": datetime.now().strftime("%m/%d/%Y %H:%M:%S")
      },
      "initiator": {
        "email": form.initiator_email.data
      },
      "participant": {
        "email": form.participant_email.data,
        "ref_id": form.participant_refid.data
      },
      "exam": {
        "name": form.exam_name.data,
        "status": "assigned"
      }
    }
    backend_response = add_item(data=json.dumps(data))
    print(backend_response)
    msg = ""
    if backend_response:
      msg = """
        Exam "{exam}" successfully added for "{name}".
      """.format(
        exam = form.exam_name.data,
        name = form.participant_email.data
      )
    else:
      msg = """
        Exam "{exam}" has not been added for "{name}" due to some reason.
      """.format(
        exam = form.exam_name.data,
        name = form.participant_email.data
      )

    return render_template(
      'subpage-add-post.html.j2',
      title='Assigning exam result',
      message=msg
    )
  else:
    return render_template(
      'subpage-add-post.html.j2',
      title='Assigning exam result (failed)',
      message="The record has not been added"
    )

