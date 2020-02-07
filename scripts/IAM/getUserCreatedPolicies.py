import boto3
import pprint
pp = pprint.PrettyPrinter(width=20, compact=True)

iam = boto3.client('iam')

policies = iam.list_policies(
    Scope='Local',
    OnlyAttached=False
)

pp.pprint(policies)