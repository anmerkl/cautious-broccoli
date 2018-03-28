import json, boto3, io
def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    message['body'] += "!"
    s3 = boto3.client('s3')
    s3.upload_fileobj(io.BytesIO(json.dumps(message).encode()), 'meaningless-bucket-2', 'api_message.txt')
    return None