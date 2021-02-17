# import resources
import json # import the json utility package since we will be working with a JSON object
import boto3 # import the AWS SDK (for Python the package name is boto3)
from time import gmtime, strftime, localtime # import packages to help us with dates and date formatting
import random

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('recordBadShotDoc')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S", localtime() ) #gmtime())

def lambda_handler(event, context):
    # TODO implement
    disc = ['putter', 'midrange', 'fairway driver', 'distance driver'];
    angle = ['hyzer', 'flat', 'anhyzer'] ;
    throw = ['backhand', 'forehand'];

    d_rdm = random.choice(disc);
    a_rdm = random.choice(angle);
    t_rdm = random.choice(throw);

    prescription = 'I recommend throwing a ' + d_rdm + ' on ' + a_rdm + ' with a ' + t_rdm + '.'
    now_id = str(now) + '  [{:03}]'.format(random.randrange(1, 10**3))

    # write to the DynamoDB table
    response = table.put_item(
        Item={
            'id': now_id,
            'disc': d_rdm,
            'angle': a_rdm,
            'throw': t_rdm,
        }
    )

    # return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps(prescription),
    }
