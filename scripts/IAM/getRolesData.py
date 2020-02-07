import boto3
import json
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)
# Create IAM client
iam = boto3.client('iam')
response = iam.list_roles()
# list all roles
def getRoles():
    role_data = []
    for role in response['Roles']:
        role_list = {}
        role_name = role['RoleName']
        role_list['role'] = role
        role_managed_policy = getRoleManagedPolicies(role_name)
        role_inline_policy = getRoleInlinePolicies(role_name)
        role_list['managed_role_policies'] = role_managed_policy
        role_list['inline_role_policies'] = role_inline_policy
        role_data.append(role_list)
    pp.pprint(role_data)
# managed Policies in a role
def getRoleManagedPolicies(role_name):
    managed = iam.list_attached_role_policies(RoleName=role_name)
    for attached_policies in managed['AttachedPolicies']:
        managed_data = getPolicyDetails(attached_policies)
        return managed_data
#get Policy Details
def getPolicyDetails(policy):
    policy_version = {}
    policy_data = iam.get_policy(PolicyArn = policy['PolicyArn'])    
    policy_de = iam.get_policy_version(PolicyArn = policy['PolicyArn'], VersionId = policy_data['Policy']['DefaultVersionId'])
    policy_version['policy_data'] = policy_data
    policy_version['policy_details'] = policy_de
    return policy_version
# inline Policies in a role
def getRoleInlinePolicies(role_name):
    inline_policy = []
    inline = iam.list_role_policies(RoleName=role_name)
    for policy in inline['PolicyNames']:
        inline_data = iam.get_role_policy(RoleName=role_name,PolicyName=policy)
        inline_policy.append(inline_data)
    return inline_policy    
getRoles()