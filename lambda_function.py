import json
import os

def lambda_handler(event, context):
    open_ai_key = os.getenv("OPEN_AI_KEY")
    correct_password = os.getenv("WEB_PASSWORD")

    # Parse the request body (assuming it's JSON)
    try:
        body = json.loads(event.get("body", "{}"))  # Safely get and parse the body
        input_password = body.get("Password", "")  # Get the "Password" field
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid JSON"})
        }

    # Compare passwords
    if input_password == correct_password:
        return {
            "statusCode": 200,
            "body": json.dumps({"api_key": open_ai_key})
        }
    else:
        return {
            "statusCode": 403,
            "body": json.dumps({"message": "fail"})
        }
