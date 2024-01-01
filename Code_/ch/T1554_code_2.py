import os
import time

def watch_file(file_path):
    initial_modify_time = os.path.getmtime(file_path)  # 初始修改時間

    while True:
        current_modify_time = os.path.getmtime(file_path)  # 當前修改時間
        if current_modify_time != initial_modify_time:
            print("File has been modified!")
            # 在這裡執行應對措施，例如發送警報或執行修復操作
            break
        
        time.sleep(1)  # 每秒檢查一次