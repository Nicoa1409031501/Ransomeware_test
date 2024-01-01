import subprocess

def read_uefi_info(output_file):
    output = subprocess.check_output(['UEFITool', '-V'])
    with open(output_file, 'w') as f:
        f.write(output.decode())

output_file = 'uefi_info.txt'
read_uefi_info(output_file)