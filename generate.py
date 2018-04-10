import random
import requests
import datetime
import asyncio
import sys

"""
Asynchronously sends POST requests with randomly generated data to the API gateway 
in json format. Provide one command line argument to tell the script how many
requests to send.
"""

count = int(sys.argv[1])

async def main():
    loop = asyncio.get_event_loop()

    futures = [
        loop.run_in_executor(
            None,
            generate
        )
        for i in range (count)
    ]

def generate():
    obj = random.randint(1, 4)
    if (obj == 1):
        objType = "user"
    elif (obj == 2):
        objType = "page"
    elif (obj == 3):
        objType = "permissions"
    else:
        objType = "payments"

    id = ""
    counter = 0
    while (counter < 17):
        id += chr(random.randint(48, 57))
        counter += 1

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

    requests.post('https://4trzhd70v2.execute-api.us-east-2.amazonaws.com/Prod/', json=JSON)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
