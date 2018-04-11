import json

data = {"time": "12", "changes": {"field": "Life Event", "id": "44444444_444444444", "value": "This is an Example Status."}}
if data['changes']['field'] == 'Life Event':
	print(json.dumps({'changes': data['changes']}))
else:
	print(json.dumps(data))