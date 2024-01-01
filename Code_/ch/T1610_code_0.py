import docker

def deploy_container(image_name):
    client = docker.from_env()
    container = client.containers.run(image_name, detach=True)
    return container.id

# 使用範例
container_id = deploy_container('ubuntu:latest')
print('Deployed container ID:', container_id)