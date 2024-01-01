import docker

def build_image_from_remote(dockerfile_path):
    client = docker.from_env()
    build_result = client.images.build(path=dockerfile_path)
    return build_result