import boto3
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)


iam = boto3.client('iam')

#Get roles
roles = iam.list_roles()
#pp.pprint(roles)

def getRoles(roles):
    r_data  = {}
    for key in roles['Roles']:
        r_data['Role'] = key['RoleName']
        data_roles = getRoleData(key)
        managed_roles= getManagedPolicyData(key)
        inline_roles= getRoleInlinePolicies(key)
        r_data['Role_information']= data_roles
        r_data['Managed_Role']= managed_roles
        r_data['Inline_role']=inline_roles
        pp.pprint(r_data)
        

#Get data about roles
def getRoleData(role):
    role_info = iam.get_role(RoleName=role['RoleName'])
    return role_info

#Get managed policies
def getManagedPolicyData(role):
    managed_role = []
    managed_info= iam.list_attached_role_policies(RoleName=role['RoleName'])
    for i in managed_info['AttachedPolicies']:
        #managed_role.append(i)
        p_data= getPolicyDetails(i)
        managed_role.append(p_data)
    return managed_role

def getPolicyDetails(policy):
    policy_version = {}
    policy_data = iam.get_policy(PolicyArn = policy['PolicyArn'])    
    policy_de = iam.get_policy_version(PolicyArn = policy['PolicyArn'], VersionId = policy_data['Policy']['DefaultVersionId'])
    policy_version['policy_data'] = policy_data
    policy_version['policy_details'] = policy_de
    return policy_version

#Get inline roles
def getRoleInlinePolicies(role):
    inline_role_data = []
    inline_info =  iam.list_role_policies(RoleName=role['RoleName'])
    for i in inline_info['PolicyNames']:
        inline_role_data.append(i)
    return inline_role_data


getRoles(roles)

