import subprocess

def service_discovery_sc(output_file):
    with open(output_file, 'w') as file:
        subprocess.run(['sc', 'query'], capture_output=file, text=True)