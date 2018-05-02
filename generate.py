import random
import requests
import datetime
import asyncio
import sys
import string

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

def rand_text():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(3, 16)))

def gen_change():
    change = {}
    field = random.choice(['status', 'work', 'education', 'location', 'activities', 'about'])
    if field == 'status' or field == 'about':
        change['value'] = rand_text()
    elif field == 'education':
        change['value'] = [
            {
                'school': {
                    'id': random.randint(0, 65536),
                    'name': rand_text()
                },
                'type': random.choice(['High School', 'College']),
                'id': random.randint(0, 65536)
            }
        ]
    elif field == 'work':
        change['value'] = [
            {
                'employer': {
                    'id': random.randint(0, 65536),
                    'name': rand_text()
                },
                'id': random.randint(0, 65536)
            }
        ]
    elif field == 'location':
        change['value'] = {'page': random.randint(0, 65536)}
        change['verb'] = random.choice(['add', 'edit', 'delete', 'follow', 'remove', 'update'])
    elif field == 'activities':
        change['value'] = {'page': random.randint(0, 65536)}
        change['verb'] = random.choice(['add', 'edit', 'delete', 'follow', 'remove', 'update'])
    change['field'] = field
    return change



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
    changes = [
        gen_change() for _ in range(random.randint(1, 6))
    ]

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
