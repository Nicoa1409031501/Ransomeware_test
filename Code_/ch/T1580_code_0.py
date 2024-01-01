import boto3

def discover_aws_infrastructure():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    
    # 處理虛擬機器
    instances = response['Reservations']
    for instance in instances:
        print('Instance ID:', instance['Instances'][0]['InstanceId'])
        print('Instance Type:', instance['Instances'][0]['InstanceType'])
        # 其他屬性...
        print('---')
    
    # 處理存儲服務
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    
    buckets = response['Buckets']
    for bucket in buckets:
        print('Bucket Name:', bucket['Name'])
        # 其他屬性...
        print('---')

discover_aws_infrastructure()