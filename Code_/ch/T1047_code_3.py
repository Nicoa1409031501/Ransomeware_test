import wmi

def execute_wmi_query(wmi_query):
    wmi_connection = wmi.WMI()
    wmi_result = wmi_connection.query(wmi_query)
    for result in wmi_result:
        print(result)

# 執行WMI命令
execute_wmi_query("SELECT * FROM Win32_Process")