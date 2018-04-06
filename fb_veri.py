VERIFY_TOKEN = "Access_Token"

def handler (event, context):
    #print(event.keys())
    if event["queryStringParameters"]:
        queryParams = event['queryStringParameters']
        rVerifyToken =  queryParams['hub.verify_token']
        if rVerifyToken == VERIFY_TOKEN:
            challenge = queryParams['hub.challenge']
            response = {
              "body": int(challenge),
              "statusCode": 200
              }
            return response
        else:
            response = {
                "body": 'Error, wrong validation token ' + rVerifyToken,
                "statusCode": 422
                
            }
            return response
    else:
        response = {
            "body": "varifification Failed "
        }
        return response