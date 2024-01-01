import ctypes

def query_registry(path, key):
    try:
        reg_key = ctypes.windll.advapi32.RegOpenKeyExW(ctypes.c_uint(0x80000002), path, 0, ctypes.c_uint(0x20019), ctypes.byref(handle))
        value, _ = ctypes.windll.advapi32.RegQueryValueExW(handle, key)
        ctypes.windll.advapi32.RegCloseKey(reg_key)
        return value
    except Exception as e:
        print("Error:", e)

# 使用範例
result = query_registry("Software\Microsoft\Office\Excel", "Version")
print("Registry value:", result)