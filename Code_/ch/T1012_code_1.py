import _winreg

def query_registry(path, key):
    try:
        reg_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path)
        value, _ = _winreg.QueryValueEx(reg_key, key)
        _winreg.CloseKey(reg_key)
        return value
    except Exception as e:
        print("Error:", e)

# 使用範例
result = query_registry("Software\Microsoft\Office\Excel", "Version")
print("Registry value:", result)