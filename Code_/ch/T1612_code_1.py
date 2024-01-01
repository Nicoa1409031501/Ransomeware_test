import docker

def build_image_from_local(dockerfile_path):
    client = docker.from_env()
    with open(dockerfile_path, 'r') as dockerfile:
        build_result = client.images.build(fileobj=dockerfile)
    return build_result