import subprocess

def get_installed_software():
    try:
        result = subprocess.check_output('wmic product get name,version', shell=True)
        software_list = result.decode('utf-8').split('\n')[1:-1]
        return software_list
    except subprocess.CalledProcessError:
        return None

installed_software = get_installed_software()
for software in installed_software:
    print(software)