import docker

def container_discovery():
    client = docker.from_env()
    containers = client.containers.list()
    
    # Print container information
    for container in containers:
        print("Container ID: ", container.id)
        print("Container Name: ", container.name)
        print("Container Image: ", container.image)
        print("Container Status: ", container.status)
        print("-----------------------------------")

container_discovery()