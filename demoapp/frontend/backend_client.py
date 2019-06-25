#!/usr/bin/env python

import os
import json
import requests as R

endpoints_file = "endpoints.json"

aws_region = os.environ.get("BACKEND_AWS_REGION", "us-east-1")


class BackendClient:

  good_response_codes = [ 200, 201, ]
  def __init__(self):

    with open(endpoints_file, 'r') as ep:
      self.endpoints = json.load(ep)


  def endpoint(self, action):
    ep = self.endpoints.get(action, None)
    print("Backend endpoint", ep)
    return ep


  def makeAPICall(self, **kwargs):
    action = kwargs.get("action", None)
    result = dict()
    request = None
    headers = {
      'Content-Type': 'application/json'
    }
    payload = {}
    if action == 'get_item':
      print("Accepted parameter", kwargs.get('token', ''))
      url = self.endpoint(action) + '?token=' + kwargs.get('token','')
      print("Calling URL: ", url)
      response = R.get(
        url
      )
      print(response)
      if response.status_code in self.good_response_codes:
        result = response.json()
        return result
      else:
        return False

    elif action == 'add_item':
      payload['data'] = kwargs.get('data', {})
      print("Passed data", kwargs.get('data', {}))
      response = R.post(
        self.endpoint(action),
        headers = headers,
        data = kwargs.get('data', {})
      )

      if response.status_code in self.good_response_codes:
        result = response.json()
        if result.get('ResponseMetadata', {}).get('HTTPStatusCode', 0) in [ 200, ]:
          return True
      else:
        print("Somethng went wrong")
        print(response.text)
        return False
      pass
    elif action == 'del_item':
      pass
    elif action == 'mod_item':
      pass

    print("A call is done")
    return result

def get_item(token): return BackendClient().makeAPICall(action='get_item', token=token)
def add_item(data): return BackendClient().makeAPICall(action='add_item', data=data)


if __name__ == "__main__":

  bc = BackendClient();
  print("""
    Endpoints:
      GET {get}
      ADD {post}
      DEL {dele}
      MOD {mod}
  """.format(
    get = bc.endpoint('get_item'),
    post = bc.endpoint('add_item'),
    dele = bc.endpoint('del_item'),
    mod  = bc.endpoint('mod_item'),
  ))
