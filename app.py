import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('observe')
def lambda_handler(event, context):
    # TODO implement
    {'version': '0',
     'id': '7b231e7c-23c8-e915-9a92-396851ca313e',
      'detail-type': 'EC2 Instance State-change Notification',
       'source': 'aws.ec2',
        'account': '065526474072', 
        'time': '2026-02-06T15:44:15Z',
         'region': 'ap-south-1',
          'resources': ['arn:aws:ec2:ap-south-1:065526474072:instance/i-0dcd39082871c5737']
          , 'detail': {'instance-id': 'i-0dcd39082871c5737', 
          'state': 'running'}
    }
    f={}
    f['Event time']=event.get('time')
    f['Event source']=event.get('source')
    f['Event name']=event.get('detail').get('state')
    f['Event region']=event.get('region')
    f['Instance Id']=event.get('detail').get('instance-id')

    print(event)
    print(context)
    table.put_item(Item=f)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
