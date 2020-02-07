import boto3
import pprint
import sys
pp = pprint.PrettyPrinter(width=20, compact=True)
iam = boto3.client('iam')
def getAllPolicies():
    marker = None
    count = 0
    allPolicies = []
    while True:
        
        if marker:
            response_iterator = iam.list_policies(
                Scope='AWS',
                OnlyAttached=False,
                MaxItems=100,
                Marker=marker
            )
        else:
            response_iterator = iam.list_policies(
                Scope='AWS',
                OnlyAttached=False,
                MaxItems=100
            )
    
    
        for policy in response_iterator['Policies']:
            allPolicies.append(policy['PolicyName'])
            count += 1
    
        try:
            marker = response_iterator['Marker']
            
        except KeyError:
            print(count)
            break       
            # sys.exit()
        
    return allPolicies

def getAttachPolicies():
    marker = None
    count = 0
    attachPolicies = []

    while True:

        if marker:
            response_iterator = iam.list_policies(
                Scope='AWS',
                OnlyAttached=True,
                MaxItems=100,
                Marker=marker
            )
        else:
            response_iterator = iam.list_policies(
                Scope='AWS',

                OnlyAttached=True,
                MaxItems=100
            )

        for policy in response_iterator['Policies']:
            attachPolicies.append(policy['PolicyName'])
            count += 1

        try:
            marker = response_iterator['Marker']
            
        except KeyError:
            print(count) 
            break      
            # sys.exit()
            
    return attachPolicies

all = set(getAllPolicies())
attach = set(getAttachPolicies())

detached_policies = all.difference(attach)
pp.pprint("-------NO._OF_DETACHED_POLICIES-------")
pp.pprint(len(detached_policies))
pp.pprint("-------DETACHED_ POLICIES-------")
pp.pprint(detached_policies)