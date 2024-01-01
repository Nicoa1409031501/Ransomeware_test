import subprocess

def read_uefi_info():
    output = subprocess.check_output(['UEFITool', '-V'])
    return output.decode()

print(read_uefi_info())