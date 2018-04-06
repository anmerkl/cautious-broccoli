import json, boto3, io, os
def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    s3 = boto3.client('s3')
    s3.upload_fileobj(io.BytesIO(json.dumps(message).encode()), os.environ['S3_BUCKET'], 'api_message.txt')
    return None