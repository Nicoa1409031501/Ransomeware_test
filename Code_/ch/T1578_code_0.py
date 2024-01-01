# 使用boto3套件
import boto3

# 創建虛擬機器
def createInstance(instance_name, image_id, instance_type, key_name, security_group_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        MinCount=1,
        MaxCount=1
    )
    print("Instance created:", instance[0].id)

# 刪除虛擬機器
def deleteInstance(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.terminate()
    print("Instance deleted:", instance_id)

# 修改虛擬機器配置
def modifyInstance(instance_id, instance_type):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.stop()
    instance.modify_attribute(InstanceType={'Value': instance_type})
    instance.start()
    print("Instance modified:", instance_id)

# 使用google-cloud-sdk套件
from google.cloud import compute_v1

# 創建云實例
def createCloudInstance(project_id, zone, instance_name, machine_type, disk_size, image_project, image_family):
    compute_client = compute_v1.InstancesClient()
    project = f"projects/{project_id}"
    zone = f"zones/{zone}"
    instance_name = f"{project}/instances/{instance_name}"

    config = {
        'name': instance_name,
        'machine_type': f"{project}/machineTypes/{machine_type}",
        'disks': [
            {
                'boot': True,
                'auto_delete': True,
                'initialize_params': {
                    'source_image_family': image_family,
                    'source_image_project': image_project,
                    'disk_size_gb': disk_size,
                },
            }
        ],
        'network_interfaces': [
            {
                'network': f"{project}/networks/default",
            }
        ],
    }

    instance = compute_client.insert(project=project, zone=zone, instance_resource=config)
    print("Instance created:", instance.name)

# 刪除云實例
def deleteCloudInstance(project_id, zone, instance_name):
    compute_client = compute_v1.InstancesClient()
    project = f"projects/{project_id}"
    zone = f"zones/{zone}"
    instance_name = f"{project}/instances/{instance_name}"

    compute_client.delete(project=project, zone=zone, instance=instance_name)
    print("Instance deleted:", instance_name)

# 修改云實例配置
def modifyCloudInstance(project_id, zone, instance_name, machine_type):
    compute_client = compute_v1.InstancesClient()
    project = f"projects/{project_id}"
    zone = f"zones/{zone}"
    instance_name = f"{project}/instances/{instance_name}"

    instance = compute_client.get(project=project, zone=zone, instance=instance_name)
    instance.machine_type = f"{project}/machineTypes/{machine_type}"
    update_mask = {
        'paths': ['machine_type']
    }
    operation = compute_client.update(project=project, zone=zone, instance=instance_name, instance_resource=instance, update_mask=update_mask)

    print("Instance modified:", instance.name)