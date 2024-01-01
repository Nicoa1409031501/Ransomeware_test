import subprocess

def read_firmware_info():
    output = subprocess.check_output(['fwupdmgr', 'get-devices'])
    return output.decode()

print(read_firmware_info())