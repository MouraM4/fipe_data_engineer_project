import json


def handler_response(message, status_code):

    return_message = {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True
            },
    }

    return return_message