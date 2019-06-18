#!/usr/bin/env python


import os
import json
import argparse
import datetime


try:
  import requests
  can_send = True
except:
  can_send = False


def send_post(endpoint, data={}):
  if not can_send:
    print("Python module requests is not available")
    return None

  response = requests.post(endpoint, headers={"Content-Type": "application/json"}, data=data)

  if not response.status_code in [ 200, 201 ]:
    return None
  print(response.json())
  return True


def gen_json_data(**kwargs):
  d = lambda key: kwargs.get(key, "")
  # String values cannot be empty (AWS requirement)
  json_data = """
  {{
    "token": "{token}",
    "data": {{
      "metadata": {{ "created_at": "{created_at}" }},
      "initiator": {{ "email": "{ie}", "first_name": "{ifn}", "last_name": "{iln}" }},
      "participant": {{ "email": "{pe}", "first_name": "{pfn}", "last_name": "{pln}", "ref_id": "{prefid}" }},
      "exam": {{ "name": "{exam_name}", "allocated_time": "1h", "status": "assigned", "started_at": "{created_at}", "ended_at": "{created_at}", "tasks": [] }},
      "deployment": {{ "aws": {{ "stack_name": "teststack", "instances": [] }} }}
    }}
  }}
  """.format(
    token = d('token'),
    created_at = datetime.datetime.now(),
    ie = d('initiator_email'), ifn = d('initiator_first_name'), iln = d('initiator_last_name'),
    pe = d('participant_email'), pfn = d('participant_first_name'), pln = d('participant_last_name'),
    prefid = d('participant_reference'),
    exam_name = d('exam'),
  )
  return json_data


def menu_parse():
  parser = argparse.ArgumentParser()
  parser.add_argument('--initiator-first-name', '-ifn', help='Initiator first name' )
  parser.add_argument('--initiator-last-name', '-iln', help='Initiator last name' )
  parser.add_argument('--initiator-email', '-ie', required=True, help='Initiator email' )

  parser.add_argument('--participant-first-name', '-pfn', help='Participant first name' )
  parser.add_argument('--participant-last-name', '-pln', help='Participant last name' )
  parser.add_argument('--participant-email', '-pe', required=True, help='Participant email' )
  parser.add_argument('--participant-reference', '-pr', help='Participant\'s reference' )

  parser.add_argument('--exam', '-e', required=True, help='Exam name' )
  parser.add_argument('--token', '-t', required=True, help='Session token' )
  parser.add_argument('--action', '-a', default='none', help='Action. Either none (default) or send - to send the data to the endpoint' )
  parser.add_argument('--endpoint', '-ep', default=None, help='Endpoint where to send data when --action=send')

  args = parser.parse_args()
  input_vars = vars(args)
  output = gen_json_data(**input_vars)

  if args.action == 'none':
    print(json.dumps(json.loads(output)))
  elif args.action == 'send':
    if args.endpoint is not None:
      send_post(args.endpoint, output)
    else:
      print("Endpoint must be provided")
      exit(1)

  pass


if __name__ == "__main__":
  menu_parse()


