'use strict';

#var USER_TOKEN = "EAACuOJLUNcoBAL8PoBGXgDVrKvv05oPsvclS0YDavfozZAl86WcHkYTM5kcalUQkt3ZBoPwjfcr07Rryf8bFfzqnjZB71erjR4gSK2tswNPOGbNmT7HrhCUe0PDvRQx864sMl9849jk8gN7C0pJff9Hx9QgYTIZD";
var VERIFY_TOKEN = "Access_Token";

def handler (event, context):
 
  if(event['queryStringParameters']){
    queryParams = event['queryStringParameters'];
 
    rVerifyToken = queryParams['hub.verify_token']
 
    if (rVerifyToken === VERIFY_TOKEN) {
      challenge = queryParams['hub.challenge']
      
      response = {
        "body": parseInt(challenge),
        "statusCode": 200
      }
      return response
    }else{
       response = {
        "body": 'Error, wrong validation token ' + rVerifyToken,
        "statusCode": 422
      }
      return response
    }
  }
  else:
    response = {
        "body": "varifification Failed "
     };
    return response
  
  
