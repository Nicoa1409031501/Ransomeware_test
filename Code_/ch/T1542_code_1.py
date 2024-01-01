import subprocess

def read_firmware_info():
    output = subprocess.check_output(['dmidecode', '-t', 'bios'])
    return output.decode()

print(read_firmware_info())