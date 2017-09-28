import os
import boto3
import json
from datetime import datetime
import uuid


def lambda_handler(event, context):
    print("Starting Lambda Function")
    
    table_name = os.environ['TABLE_TABLE_NAME']
    table = boto3.resource('dynamodb').Table(table_name)
    
    eventBody = json.loads(event['body'])
    
    if 'device' in evenBody and 'lat' in eventBody and 'lon' in eventBody:
      uid = uuid.uuid4().hex
      
      item = {
          'uuid': uid,
          'device': eventBody['device'],
          'latitude': eventBody['lat'],
          'longitude': eventBody['lon']
      }
    
      table.put_item(Item=item)
    
      response = {
          "isBase64Encoded": "false",
          "statusCode": 200,
          "body": json.dumps(item)
      }
    else:
      response = {
          "isBase64Encoded": "false",
          "statusCode": 400,
          "body": "{\"errorMessage\": \"Invalid or missing parameters.\"}"
      }
    return response