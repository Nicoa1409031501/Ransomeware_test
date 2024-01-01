import winreg

def search_registry(key, keyword):
    results = []
    reg_key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, key)
    try:
        i = 0
        while True:
            name, value, _ = winreg.EnumValue(reg_key, i)
            if keyword in name or keyword in value:
                results.append(value)
            i += 1
    except OSError:
        pass
    return results

# 使用方式：
results = search_registry('Software\Microsoft', 'password')
print(results)