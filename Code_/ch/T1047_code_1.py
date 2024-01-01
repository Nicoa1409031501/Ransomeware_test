import win32com.client

# 連線到本地電腦的WMI服務
wmi_connection = win32com.client.GetObject('winmgmts:')

# 執行WMI命令
wmi_result = wmi_connection.ExecQuery("SELECT * FROM Win32_Process")
for process in wmi_result:
    print(process.Name)