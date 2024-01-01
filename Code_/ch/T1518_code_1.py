import psutil

def get_installed_software():
    software_list = []
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name']
            if process_name != "" and process_name not in software_list:
                software_list.append(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return software_list

installed_software = get_installed_software()
for software in installed_software:
    print(software)