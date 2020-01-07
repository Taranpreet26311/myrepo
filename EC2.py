
import boto3

client = boto3.client('ec2')

#describe an instance
response = client.describe_instances(
    InstanceIds=[
        'i-096a53d7e47f220ae'
    ]
)
print(response)

