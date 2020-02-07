import boto3
import pprint

client = boto3.client('iam')

AllRoles = client.list_roles()


def getRoles(args):
    role = []
    for roles in args['Roles']:
        role.append(roles['RoleName'])
    return role

a = (getRoles(AllRoles)
print(a)