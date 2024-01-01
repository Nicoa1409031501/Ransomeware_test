import subprocess

def load_payload():
    subprocess.Popen(['payload.exe'], shell=True)

load_payload()