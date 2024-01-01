import paramiko

def execute_command_in_container(container_hostname, container_username, container_password, command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(container_hostname, username=container_username, password=container_password)
  
    stdin, stdout, stderr = ssh_client.exec_command(f"docker exec {container_id} {command}")
    result = stdout.read().decode("utf-8")
  
    ssh_client.close()
    return result

# 使用範例
container_hostname = "<container_hostname>"
container_username = "<container_username>"
container_password = "<container_password>"
command = "<command>"
result = execute_command_in_container(container_hostname, container_username, container_password, command)
print(result)