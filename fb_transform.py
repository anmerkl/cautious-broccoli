import json, boto3, io
def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    company = message['body']['company']
    company = company.lower()
    position = message['body']['position']
    position = position.lower()
    scale = 1
    if position == 'intern':
        clv = 1 * scale
    elif position == 'senior developer':
        clv = 3 * scale
    elif position == 'developer':
        clv = 2 * scale
    elif position == 'manager':
        clv = 4 * scale
    elif position == 'executive':
        clv = 5 * scale
    else:
        clv = 1 * scale

    if company == 'umass':
        clv *= 1
    elif company == 'liberty mutual':
        clv *= 5
    elif company == 'google':
        clv *= 4
    elif company == 'apple':
        clv *= 2
    elif company == 'microsoft':
        clv *= 3
    else:
        clv *= 1

    message = clv

    s3 = boto3.client('s3')
    s3.upload_fileobj(io.BytesIO(json.dumps(message).encode()), 'meaningless-bucket-2', 'api_message.txt')
    return None