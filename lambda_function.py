import json
import os

def lambda_handler(event, context):
    my_secret = os.getenv("MY_SECRET")
    body = event['body']
    body['my_secret'] = my_secret
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
