import subprocess

def service_discovery_tasklist():
    result = subprocess.run(['tasklist', '/svc'], capture_output=True, text=True)
    output = result.stdout
    return output