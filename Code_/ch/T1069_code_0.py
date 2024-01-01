import subprocess

def local_group_discovery():
    command = "net localgroup"
    result = subprocess.run(command, capture_output=True, shell=True)
    output = result.stdout.decode('utf-8')
    print(output)

local_group_discovery()