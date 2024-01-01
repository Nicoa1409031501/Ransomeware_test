import subprocess

def execute_command_in_container(container_id, command):
    full_command = f"docker exec {container_id} {command}"
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    return result.stdout

# 使用範例
container_id = "<container_id>"
command = "<command>"
result = execute_command_in_container(container_id, command)
print(result)