import subprocess

def schedule_malicious_code_task_scheduler(task_name, command):
    subprocess.run(['schtasks', '/create', '/tn', task_name, '/tr', command, '/sc', 'DAILY'])

schedule_malicious_code_task_scheduler('malicious_task', 'echo "Hello World"')