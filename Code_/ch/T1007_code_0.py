import subprocess

def service_discovery_sc():
    result = subprocess.run(['sc', 'query'], capture_output=True, text=True)
    output = result.stdout
    return output