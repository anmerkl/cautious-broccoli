import json, boto3, io


def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    positions = {"intern": 1, "developer": 2, "senior developer": 3, "manager": 4, "executive": 5}
    companies = {"umass": 1, "apple": 2, "microsoft": 3, "google": 4, "liberty mutual": 5}
    
    company = message['body']['company'].lower()
    position = message['body']['position'].lower()
    
    clv = 1
    if position in positions:
        clv *= positions[position]
    
    if company in companies:
        clv *= companies[company]
    
    str = "We recommend: "
	if clv < 10:
		str += "the basic insurance plan"
	elif clv < 20:
		str += "the standard insurance plan"
	else:
		str += "the premium insurance plan"
    
    str += " (based on your CLV of {})".format(clv)

    s3 = boto3.client('s3')
    s3.upload_fileobj(io.BytesIO(json.dumps(str).encode()), 'linkedinsignin', message['body']['first'] + message['body']['last'] + '.txt')
    return None
