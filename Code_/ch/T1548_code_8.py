import paramiko

def abuse_elevation_control9():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('hostname', username='username', password='password', look_for_keys=False)
    stdin, stdout, stderr = ssh_client.exec_command('command_to_execute')
    output = stdout.read().decode()

abuse_elevation_control9()