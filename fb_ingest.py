import os, json, boto3
VERIFY_TOKEN = 'Access_Token'
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
        if webhook['changes'] == 'status':
            Msg=json.dumps({'changes': webhook})
        else:
            Msg= "No relevant information"
        sns = boto3.client('sns')
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message = msg
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