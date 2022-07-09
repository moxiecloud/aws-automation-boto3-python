# create a standard sqs queue
# for a standard sqs queue
#

import boto3

# Get the service resource
#sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
#queue = sqs.create_queue(QueueName='Messages', Attributes={'DelaySeconds': '5'})

# Can now access identifiers and attributes
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

sqs_client = boto3.client("sqs", region_name="us-east-1")

response = sqs_client.create_queue(
    QueueName="Messages",
    Attributes={
        "DelaySeconds": "0",
        "VisibilityTimeout": "60",  # 60 seconds
    }
)
print(response)
