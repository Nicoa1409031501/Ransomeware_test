# 使用aws-cli
import subprocess

# 創建虛擬機器
def createInstance(instance_name, image_id, instance_type, key_name, security_group_id):
    subprocess.run(['aws', 'ec2', 'run-instances',
                    '--image-id', image_id,
                    '--instance-type', instance_type,
                    '--key-name', key_name,
                    '--security-group-ids', security_group_id,
                    '--tag-specifications', 'ResourceType=instance,Tags=[{Key=Name,Value='+instance_name+'}]']
    )
    print("Instance created")

# 刪除虛擬機器
def deleteInstance(instance_id):
    subprocess.run(['aws', 'ec2', 'terminate-instances', '--instance-ids', instance_id])
    print("Instance deleted")

# 修改虛擬機器配置
def modifyInstance(instance_id, instance_type):
    subprocess.run(['aws', 'ec2', 'stop-instances', '--instance-ids', instance_id])
    subprocess.run(['aws', 'ec2', 'modify-instance-attribute',
                    '--instance-id', instance_id,
                    '--instance-type', instance_type]
    )
    subprocess.run(['aws', 'ec2', 'start-instances', '--instance-ids', instance_id])
    print("Instance modified")

# 使用gcloud
# 創建云實例
def createCloudInstance(project, zone, instance_name, machine_type, disk_size, image_project, image_family):
    subprocess.run(['gcloud', 'compute', 'instances', 'create', instance_name,
                    '--project', project,
                    '--image-family', image_family, 
                    '--image-project', image_project, 
                    '--boot-disk-size', disk_size, 
                    '--machine-type', machine_type,
                    '--zone', zone]
    )
    print("Instance created")

# 刪除云實例
def deleteCloudInstance(project, zone, instance_name):
    subprocess.run(['gcloud', 'compute', 'instances', 'delete', instance_name,
                    '--project', project, 
                    '--zone', zone, 
                    '--quiet']
    )
    print("Instance deleted")

# 修改云實例配置
def modifyCloudInstance(project, zone, instance_name, machine_type):
    subprocess.run(['gcloud', 'compute', 'instances', 'stop', instance_name,
                    '--project', project, 
                    '--zone', zone]
    )
    subprocess.run(['gcloud', 'compute', 'instances', 'set-machine-type', instance_name,
                    '--project', project, 
                    '--machine-type', machine_type, 
                    '--zone', zone]
    )
    subprocess.run(['gcloud', 'compute', 'instances', 'start', instance_name,
                    '--project', project, 
                    '--zone', zone]
    )
    print("Instance modified")