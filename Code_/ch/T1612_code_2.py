import subprocess

def build_image_from_local_command(dockerfile_path):
    command = f'docker build -t custom_image -f {dockerfile_path} .'
    subprocess.run(command, shell=True)