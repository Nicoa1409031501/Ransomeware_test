import subprocess

def execute_payload(payload_path):
    subprocess.Popen(payload_path, shell=True)

execute_payload('/path/to/payload.exe')