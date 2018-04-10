import json, boto3, io, os
def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    dynamo = boto3.resource('dynamodb')
    table = dynamo.table(os.environ['CUSTOMER_TABLE'])
    for entry in message['entry']:
        table.put_item(
            Item={
                'id': entry['id'],
                'latest_change': json.dumps(entry['changes'])
            }
        )
    return None