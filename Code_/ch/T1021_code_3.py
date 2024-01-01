import paramiko

def run_ssh_command_with_key(hostname, username, private_key_path, command):
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, pkey=private_key)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output