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
	
	info = {}
	info['first'] = 'Dev'
	info['last'] = 'Account'
	info['position'] = 'Senior Developer'
	info['company'] = 'Microsoft'
	
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=json.dumps({'queryString': event['queryStringParameters'], 'body': parse(event['body'])})
    )
    return response
