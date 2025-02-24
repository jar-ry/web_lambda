import json
import os

def lambda_handler(event, context):
    open_ai_key = os.getenv("OPEN_AI_KEY")
    correct_password = os.getenv("WEB_PASSWORD")

    # Parse the request body (assuming it's JSON)
    try:
        body = json.loads(event.get("body", "{}"))  # Parse request body
        input_password = body.get("Password", "")  # Extract password
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, POST"
            },
            "body": json.dumps({"message": "Invalid JSON"})
        }

    # Validate password
    if input_password == correct_password:
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, POST"
            },
            "body": json.dumps({"api_key": open_ai_key})
        }
    else:
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, POST"
            },
            "body": json.dumps({"message": "fail"})
        }
