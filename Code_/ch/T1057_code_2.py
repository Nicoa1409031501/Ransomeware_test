import wmi

def get_running_processes():
    c = wmi.WMI()
    processes = []
    for process in c.Win32_Process():
        processes.append({'pid': process.ProcessId, 'name': process.Name})
    return processes

running_processes = get_running_processes()
print(running_processes)