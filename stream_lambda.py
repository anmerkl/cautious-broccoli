import sagemaker, boto3, os, logging
from botocore.exceptions import ClientError
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
MODEL_BUCKET = os.environ['']
def handler(event, context):
    if not 'Records' in event:
        return 'Error!'
    update = {}
    for record in event['Records']:
        update[record['dynamodb']['NewImage']['id']['S']] = record['dynamodb']['NewImage']['clv']['S']
    ses = boto3.client('ses')
    try:
        resp = ses.send_mail(
            Destination={'ToAddresses': ['schickosky@umass.edu',]},
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': update
                    }
                }
            },
            Source='Sender Name <sender@example.com>'
        )
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
    else:
        logger.info(resp['ResponseMetadata']['RequestID'])

    s3 = boto3.client('s3')
    model_bucket = s3.Bucket(MODEL_BUCKET)
    role = sagemaker.get_execution_role()
    # Do a thing.
