#
# Scenario: Our DevOps engineering team often uses a development lab to test releases of our application.
# The Managers are complaining about the rising cost of our development lab and need to save money
# by stopping our (for this example) 3 ec2 instances after all engineers are clocked out.
#
# **Create a Python script that you can run that will stop all instances.**
#
# Boto3 session is an object to create a connection to your AWS service and
# manage the connection state throughout your program life cycle.
# You can create Boto3 session using your AWS credentials Access key id and secret access key.
# The boto3 library is an AWS SDK for Python. It provides object-oriented API services and low-level
# services to the AWS services. It allows users to create, and manage AWS services.
#

# AWS Python SDK
import boto3

# All API services are available in the Boto3 Client. Maps 1:1 with the AWS service API.
# The client provides methods to connect with AWS services similar to the AWS API service.
#
# Create a low-level client for the ec2 service
ec2_client = boto3.client('ec2')

# Use the describe_instances method to get a list of all running instances
response = ec2_client.describe_instances()

# take list with all the running instances, find the Reservations section and grab all the
# elements
# data = response["Reservations"]

# initialize list
ec2_list=[]

# "for" loop to process the content under the Reservations list and stored in the data variable.
# Will extract the Instance Name and Instance ID that will be sent to the stop instance method.
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        ec2_list.append(instance_id)

# list of instances that are running will be stopped by the stop_instances boto3 method.
ec2_client.stop_instances(InstanceIds=ec2_list)

print("all EC2 instances stopped")
