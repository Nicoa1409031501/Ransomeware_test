import boto3

def exec_command_aws(cmd, instance_id):
    ssm = boto3.client('ssm')
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [cmd]}
    )
    command_id = response['Command']['CommandId']
    return command_id