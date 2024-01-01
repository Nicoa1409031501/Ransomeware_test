import subprocess

def container_discovery():
    # Run docker command to list containers
    output = subprocess.check_output(["docker", "ps", "--format", "'{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}'"])
    
    # Parse and print container information
    for line in output.decode().split("\n"):
        if line:
            container_id, container_name, container_image, container_status = line.strip().split("\t")
            print("Container ID: ", container_id)
            print("Container Name: ", container_name)
            print("Container Image: ", container_image)
            print("Container Status: ", container_status)
            print("-----------------------------------")

container_discovery()