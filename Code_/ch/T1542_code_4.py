import subprocess

def read_firmware_info(output_file):
    output = subprocess.check_output(['dmidecode', '-t', 'bios'])
    with open(output_file, 'w') as f:
        f.write(output.decode())

output_file = 'firmware_info.txt'
read_firmware_info(output_file)