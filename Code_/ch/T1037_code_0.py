# 使用Python檔案操作來修改HKCU\Environment\UserInitMprLogonScript Registry key
import winreg

def modify_registry_key():
    reg_key = winreg.HKEY_CURRENT_USER
    reg_path = r"Environment"
    reg_subkey = "UserInitMprLogonScript"
    reg_value = "C:\\path\\to\\script.bat"  # 更改為要執行的腳本路徑

    try:
        with winreg.OpenKey(reg_key, reg_path, 0, winreg.KEY_WRITE) as hKey:
            winreg.SetValueEx(hKey, reg_subkey, 0, winreg.REG_SZ, reg_value)
            print("Registry key modified successfully.")
    except Exception as e:
        print("Error modifying registry key:", str(e))

modify_registry_key()