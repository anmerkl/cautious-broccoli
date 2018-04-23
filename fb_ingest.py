import os, json, boto3, re


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

    fname = re.search(r'firstName=([A-Z][a-z]*)&', event['body'])
    info['first'] = fname.group(1)

    lname = re.search(r'&lastName=([A-Z][a-z]*)&', event['body'])
    info['last'] = lname.group(1)

    pos = re.search(r'&headline=(.*)\+at', event['body'])
    info['position'] = "N/A" if pos.group(1) == "N%2FA" else pos.group(1)

    comp = re.search(r'\+at\+(.*)&id=', event['body'])
    info['company'] = "N/A" if comp.group(1) == "N%2FA" else comp.group(1)
	
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=json.dumps({'queryString': event['queryStringParameters'], 'body': info })
    )
    return response
