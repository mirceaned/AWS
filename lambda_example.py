# vim: set fileencoding=utf-8 :

from __future__ import absolute_import

import datetime
import re
import boto3


def get_boto3_client(service):
    return boto3.client(service, 'us-west-2')


def lambda_handler(event, context):
    iam_client = get_boto3_client('iam')
    Marker = ''

    while True:
        try:
            if Marker:
                response = iam_client.list_roles(Marker=Marker)
            elif Marker == '':
                response = iam_client.list_roles()
            else:
                break

            roles = response.get('Roles', [])
            for role in roles:
                if _should_be_deleted(role):
                    _delete_role(role)
            Marker = response.get('Marker')

        except Exception as e:
            print 'exception: ' + str(e)


def _should_be_deleted(role):
    role_name = role['RoleName']
    role_create_date = role['CreateDate']

    match_project_role = re.match('^([a-zA-Z0-9-]+)_([a-zA-Z0-9]+)$', role_name)
    
    if match_project_role:
        print 'role is ' + role_name    
        user_name = match_project_role.group(1)
        print 'user name is ' + user_name    
        if not _is_user_in_db(user_name):
            return True
    
    return False


def _is_user_in_db(user_name):
    dynamodb_client = get_boto3_client('dynamodb')

    existingProject = dynamodb_client.query(
        TableName='Users',
        Select='COUNT',
        ExpressionAttributeValues={':user_name': {'S': user_name}},
        KeyConditionExpression='UserName = :user_name'
    )

    if not existingProject['Count']:
        print 'user ' + user_name + ' not found in db'
        return False

    return True


def _delete_role(role):
    role_name = role['RoleName']
    iam_client = get_boto3_client('iam')
    
    response = iam_client.list_role_policies(RoleName=role_name)
    if response['PolicyNames']:
        for policy_name in response['PolicyNames']:
            print 'deleting policy name ' + policy_name
            iam_client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)

    iam_client.delete_role(RoleName=role_name)
    print 'deleted role ' + role_name
