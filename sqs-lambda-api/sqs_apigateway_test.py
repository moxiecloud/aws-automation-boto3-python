# project scenario
# create an SQS queue using boto3 python script
#
# create API Gateway trigger that runs the lambda_function created
# use browser to confirm message renders on browser
# use the API Gateway endpoint URL, copy/paste in browser
#
# The lambda function should write to the SQS Messages queue and I should
# see an entry when I check CloudWatch
#
# I used the AWS Management Console to perform the following tasks:
# 1. created a custom Lambda role
# 2. created a policy that gives the Lambda role execution permissions
#    with full access to the SQS, CloudWatch, and Lambda services so that
#    could perform the needed tasks
# 3. created a lambda function with 2 triggers (SQS and API Gateway)
# 4. tested the lambda function in the AWS management console lambda code environment
#

import boto3
import json
from datetime import datetime

#create variables
message = ""

#create boto3 SQS object
sqs = boto3.client('sqs')
queue = sqs.get_queue_url(QueueName='Messages')

#create lambda handler
def lambda_handler(event, context):
    print("lambda triggered")

    #create message
    message = "The Lambda function executed at: "+str(datetime.now().isoformat())

    #send message
    response = sqs.send_message(
        QueueUrl=queue['QueueUrl'],
        MessageBody=message,
        )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

    # Delete SQS message
    message.delete()
    print("Deleted message:", message.message_id)
