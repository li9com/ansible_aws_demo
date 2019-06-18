from __future__ import print_function
import boto3
import json
import decimal
from os import environ


dyndb_table = environ.get("dynamodb_table", "Exams")


def get_db_record(token):
  dynamodb = boto3.resource("dynamodb", region_name=environ.get('aws_region', 'us-east-1'))
  table = dynamodb.Table(dyndb_table)

  token = token
  response = { "data": "there is no any data"}
  if type(token) is str:

    response = table.get_item ( Key={ "token": token } )
    print("GetItem succeded")
    print(json.dumps(response, indent=4))
  return response

def item_get(event, context):
    token = event.get('queryStringParameters', {}).get('token', None)
    return {
        "statusCode": 200 if token else 404,
        "headers": {},
        "isBase64Encoded": "false",
        "body": json.dumps(get_db_record(token=token)) if token else '{"status": "No token provided"}'
    }


