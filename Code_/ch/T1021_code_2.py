hostname = '遠端主機的IP地址或主機名稱'
username = '遠端帳號'
password = '遠端帳號的密碼'
command = '要執行的遠端命令'

output = run_ssh_command(hostname, username, password, command)
print(output)