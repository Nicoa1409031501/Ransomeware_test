import docker

def execute_command_in_container(container_id, command):
    client = docker.from_env()
    container = client.containers.get(container_id)
    exec_result = container.exec_run(command)
    return exec_result.output.decode('utf-8')

# 使用範例
container_id = "<container_id>"
command = "<command>"
result = execute_command_in_container(container_id, command)
print(result)