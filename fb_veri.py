
def handler(event, context):
    # Dummy verification lambda, just replies 200 OK every time
    response = {
        'statusCode': 200,
        'body': '',
        'headers': {
            'Content-Type': '*/*'
        }
    }
    return response