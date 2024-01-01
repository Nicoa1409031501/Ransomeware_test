import paramiko

def abuse_elevation_control8():
    private_key = paramiko.RSAKey.from_private_key_file('private_key_file')
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('hostname', username='username', pkey=private_key)
    stdin, stdout, stderr = ssh_client.exec_command('command_to_execute')
    output = stdout.read().decode()

abuse_elevation_control8()