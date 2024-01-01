import subprocess

def get_running_processes():
    output = subprocess.check_output('tasklist', universal_newlines=True)
    processes = []
    for line in output.strip().split('\n')[3:]:
        parts = line.split()
        pid = int(parts[1])
        name = parts[0]
        processes.append({'pid': pid, 'name': name})
    return processes

running_processes = get_running_processes()
print(running_processes)