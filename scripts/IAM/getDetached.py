import boto3
import pprint
import sys
​
pp = pprint.PrettyPrinter(width=20, compact=True)
​
iam = boto3.client('iam')
​
marker = None
count = 0
while True:
    if marker:
        response_iterator = iam.list_policies(
            MaxItems=100,
            Marker=marker
        )
    else:
        response_iterator = iam.list_policies(
            MaxItems=100
        )
    print("Next Page : {} ")    
    pp.pprint(response_iterator['IsTruncated'])
    for policy in response_iterator['Policies']:
        pp.pprint(policy['PolicyName'])
        count += 1
​
    try:
        marker = response_iterator['Marker']
        pp.pprint(marker)
​
    except KeyError:
        print(count)        
        sys.exit()