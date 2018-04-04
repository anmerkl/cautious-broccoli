import requests
import random
import datetime
import json
import sys

i = int(sys.argv[1])
counter = 0

while counter<i:
    objType = ""
    obj = random.randint(1, 4)
    if(obj == 1):
        objType = "user"
    elif(obj == 2):
        objType = "page"
    elif(obj == 3):
        objType = "permissions"
    else:
        objType = "payments"

    id = ""
    counter = 0
    while(counter < 17):
        id += chr(random.randint(48, 57))
        counter+=1

    uid = id

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()

    changes = ["", 2]
    changes[0] = 'field'
    changes[1] = "test2"

    JSON = {}
    JSON['entry'] = []
    JSON['entry'].append({
        'time': time,
        'changes': changes,
        'id': id,
        'uid': id
    })
    JSON['object'] = objType

    requests.post('https://4trzhd70v2.execute-api.us-east-2.amazonaws.com/Prod/PushEvent', json = JSON)
    counter+=1
