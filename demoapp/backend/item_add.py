from __future__ import print_function
import boto3
import json
import decimal
from os import environ
import json


dyndb_table = environ.get("dynamodb_table", "Exams")


def add_db_record(data):
  dynamodb = boto3.resource("dynamodb", region_name=environ.get('aws_region', 'us-east-1'))
  table = dynamodb.Table(dyndb_table)

  item = json.loads(data)
  response = table.put_item( Item=item )
  return response


def item_add(event, context):
  response = add_db_record(event.get('body', {}))
  result = {
    "statusCode": 200,
    "headers": {
      "Content-type": "application/json"
    },
    "isBase64Encoded": "false",
    "body": json.dumps(response)
  }
  return result

