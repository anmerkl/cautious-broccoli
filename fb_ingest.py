import os, json, boto3
def handler(event, context):
    response = {
        'statusCode': 200,
        'body': '',
        'headers': {
            'Content-Type': '*/*'
        }
    }
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=json.dumps({'queryString': event['queryStringParameters'], 'body': event['body']})
    )
    return response