import subprocess

def system_shutdown():
    subprocess.call(["shutdown", "/s", "/t", "0"])
    
def system_reboot():
    subprocess.call(["shutdown", "/r", "/t", "0"])