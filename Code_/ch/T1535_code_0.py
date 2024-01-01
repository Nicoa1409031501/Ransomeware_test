import boto3

def create_unused_cloud_instance_aws(region, instance_type, image_id, key_name):
    ec2_client = boto3.client('ec2', region_name=region)
    response = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name
    )
    return response