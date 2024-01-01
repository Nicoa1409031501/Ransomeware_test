import os

def enumerate_logs():
    log_files = ["system.log", "service.log"] # 假設系統和服務日誌文件的名稱
    for log_file in log_files:
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                data = file.read()
                # 攻擊者可以根據需求從日誌文件中獲取有用的數據
                # 例如檢查用戶身份驗證記錄、軟件信息或受感染主機等等
                print(f"Enumerating {log_file}:")
                print(data)
        else:
            print(f"{log_file} does not exist.")

enumerate_logs()