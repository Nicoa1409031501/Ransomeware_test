import winreg

def query_registry(path, key):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(reg_key, key)
        winreg.CloseKey(reg_key)
        return value
    except Exception as e:
        print("Error:", e)

# 使用範例
result = query_registry("Software\Microsoft\Office\Excel", "Version")
print("Registry value:", result)