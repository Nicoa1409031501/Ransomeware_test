import subprocess

def network_share_discovery():
    result = subprocess.run(['net', 'share'], capture_output=True)
    output = result.stdout.decode().split('\n')[4:-2]

    shared_folders = []
    for line in output:
        shares = line.strip().split()
        shared_folders.append(shares[0])

    return shared_folders

result = network_share_discovery()
print(result)