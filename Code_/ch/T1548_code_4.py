import boto3

def abuse_elevation_control5():
    sts_client = boto3.client('sts')
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::123456789012:role/MyRole',
        RoleSessionName='MySession'
    )
    print(response['Credentials'])

abuse_elevation_control5()