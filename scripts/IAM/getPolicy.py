import boto3
import json
import pprint
pp = pprint.PrettyPrinter(width=20, compact=True)
# Create IAM client
iam = boto3.client('iam')
users = iam.list_users()

def getUserList(users):
    user_data = {}
    for key in users['Users']:
        user_data['user'] = key['UserName']
        #print(key['UserName'])
        user_policy = getPolicyListPerUser(key)    
        inline_data = getUserInlinePolicy(key)
        group_list = getListOfUserGroups(key)
        group_policy = getListGroupPolicies(group_list)
        user_data['managed_policy'] = user_policy
        user_data['inline_policy'] = inline_data
        user_data['group_list'] = group_list
        user_data['group_policies'] = group_policy
        pp.pprint(user_data)    



#get User Attached Policies
def getPolicyListPerUser(user):
    policy_detail = []
    listofpolicies =  iam.list_attached_user_policies(UserName=user['UserName'])
    for policy in listofpolicies['AttachedPolicies']:
        policy_detail.append(getPolicyDetails(policy))    
    return policy_detail



#get Policy Details
def getPolicyDetails(policy):
    policy_version = {}
    policy_data = iam.get_policy(PolicyArn = policy['PolicyArn'])    
    policy_de = iam.get_policy_version(PolicyArn = policy['PolicyArn'], VersionId = policy_data['Policy']['DefaultVersionId'])
    policy_version['policy_data'] = policy_data
    policy_version['policy_details'] = policy_de
    return policy_version



#get usr Inline Policy
def getUserInlinePolicy(user):
    inlinePolicy = []
    response = iam.list_user_policies(UserName=user['UserName'])
    for policy in response['PolicyNames']:
        inline = iam.get_user_policy(UserName=user['UserName'],PolicyName=policy)
        inlinePolicy.append(inline)
    return inlinePolicy



#get User Group List
def getListOfUserGroups(user):
    groups = []
    List_of_Groups =  iam.list_groups_for_user(UserName=user['UserName'])
    for key in List_of_Groups['Groups']:
        groups.append(key)
    return groups

#get Group Policies
def getListGroupPolicies(group_name):
    policy = {}
    for group in group_name:
        list_inline = getInlineGroupPolicy(group['GroupName'])
        list_managed = getManagedGroupPolicy(group['GroupName'])
        policy['group_inline'] = list_inline
        policy['group_managed'] = list_managed
    return policy    


#get Inline Group Policies
def getInlineGroupPolicy(group):
    inlinePolicy = []
    group_inline_policy = iam.list_group_policies(GroupName=group)
    for policy in group_inline_policy['PolicyNames']:
        inline = iam.get_group_policy(GroupName=group,PolicyName=policy)
        inlinePolicy.append(inline)
    return inlinePolicy


#get Managed Group Policies
def getManagedGroupPolicy(group):
    policy_detail = []
    listofpolicies =  iam.list_attached_group_policies(GroupName=group)
    for policy in listofpolicies['AttachedPolicies']:
        policy_detail.append(getPolicyDetails(policy))    
    return policy_detail
    

getUserList(users)