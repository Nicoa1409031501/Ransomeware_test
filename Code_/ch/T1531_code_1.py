import subprocess

def remove_account_access():
    # 1. 讓使用者輸入要刪除或鎖定的帳號名稱
    target_account = input("請輸入要刪除或鎖定的帳號名稱：")
    
    # 2. 刪除或鎖定帳號
    subprocess.run(["net", "user", target_account, "/active:no"])
    print(f"已成功鎖定帳號：{target_account}")
    
    # 3. 登出系統
    subprocess.run(["shutdown", "/l"])

remove_account_access()