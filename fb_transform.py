import json, boto3, io, os
def handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(os.environ['CUSTOMER_TABLE'])
    for change in message['changes']:
        if isinstance(change['value'], list):
            for val in change['value']:
                if 'id' in val:
                    del val['id']
                rm_list, add_dict = [], {}
                for key, value in val.items():
                    if isinstance(value, dict):
                        for k, v in value.items():
                            if k != 'id':
                                add_dict[k] = v
                        rm_list.append(key)
                for key in rm_list:
                    del val[key]
                val.update(add_dict)
                table.put_item(
                    Item = dict(
                        id=message['id'],
                        field=change['field'],
                        **val
                    )
                )
        else:
            if isinstance(change['value'], dict):
                for key, value in change['value'].items():
                    change[key] = value
                del change['value']
    
                        
            table.put_item(
                Item = dict(
                    id=message['id'],
                    **change
                )
            )
    return None