import boto3
import pprint
pp = pprint.PrettyPrinter(width=20, compact=True)

iam = boto3.client('iam')

#Get all users
response = iam.list_users()

def GetUsers(args):
    user_list = []
    for users in args['Users']:
        user_list.append(users)
    return user_list

a = GetUsers(response)
pp.pprint(a)