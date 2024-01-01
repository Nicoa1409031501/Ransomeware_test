import win32com.client

def get_installed_software():
    software_list = []
    wmi = win32com.client.GetObject("winmgmts:")
    colItems = wmi.ExecQuery("SELECT * FROM Win32_Product")
    for item in colItems:
        software_list.append(item.Name)
    return software_list

installed_software = get_installed_software()
for software in installed_software:
    print(software)