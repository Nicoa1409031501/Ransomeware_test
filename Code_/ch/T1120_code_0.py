import subprocess

def peripheral_device_discovery():
    result = subprocess.check_output("wmic path Win32_PnPEntity get caption", shell=True)
    devices = result.decode().split('\n')[1:-1]
    return devices

devices = peripheral_device_discovery()
for device in devices:
    print(device)