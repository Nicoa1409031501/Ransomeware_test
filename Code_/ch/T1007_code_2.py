import subprocess

def service_discovery_net():
    result = subprocess.run(['net', 'start'], capture_output=True, text=True)
    output = result.stdout
    return output