
def handler(event, context):
    # Dummy verification lambda, just replies 200 OK every time.
    # Will need to pull the verification token and challenge string
    #  out of event['queryStringParameters'] and verify the first, return
    #  the second.
    response = {
        'statusCode': 200,
        'body': '',
        'headers': {
            'Content-Type': '*/*'
        }
    }
    return response