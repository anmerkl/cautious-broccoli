import os, json, boto3, logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
VERIFY_TOKEN = 'Access_Token'
clv = 0
def handler(event, context):
    if event['httpMethod'] == 'POST':
        response = {
            'statusCode': 200,
            'body': '',
            'headers': {
                'Content-Type': '*/*'
            }
        }
        webhook = json.loads(event['body'])
        sns = boto3.client('sns')
        for entry in webhook['entry']:
            for change in entry['changes']:
                if 'id' in change:
                    del change['id']
                elif 'event' in change: clv += 2
                else: clv += 1
            sns.publish(
                TopicArn=os.environ['SNS_TOPIC_ARN'],
                Message=json.dumps(dict(changes=entry['changes'], id=entry['id'], object=webhook['object'],lifetime = clv))
            )
        return response



    elif event['httpMethod'] == 'GET':
        if event['queryStringParameters']:
            queryParams = event['queryStringParameters']
            rVerifyToken = queryParams['hub.verify_token']
            if rVerifyToken == VERIFY_TOKEN:
                challenge = queryParams['hub.challenge']
                response = {
                  'body': int(challenge),
                  'statusCode': 200
                }
                return response
            else:
                response = {
                    'body': 'Error, wrong validation token: ' + rVerifyToken,
                    'statusCode': 422
                    
                }
                return response
        else:
            response = {
                'body': 'Verification Failed'
            }
            return response