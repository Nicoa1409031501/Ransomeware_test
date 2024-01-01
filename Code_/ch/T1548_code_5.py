import boto3

def abuse_elevation_control6():
    sts_client = boto3.client('sts')
    response = sts_client.get_session_token()
    print(response['Credentials'])

abuse_elevation_control6()