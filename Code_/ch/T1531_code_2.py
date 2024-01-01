import ctypes

def remove_account_access():
    # 1. 讓使用者輸入要刪除或鎖定的帳號名稱
    target_account = input("請輸入要刪除或鎖定的帳號名稱：")
    
    # 2. 刪除或鎖定帳號
    ctypes.windll.advapi32.NetUserSetInfo(None, target_account, 0, {'usri1_flags': 0x02})  
    print(f"已成功鎖定帳號：{target_account}")
    
    # 3. 登出系統
    ctypes.windll.user32.ExitWindowsEx(0x08, 0)  

remove_account_access()