import psutil

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append({'pid': proc.info['pid'], 'name': proc.info['name']})
    return processes

running_processes = get_running_processes()
print(running_processes)