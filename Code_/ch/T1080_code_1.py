import shutil

def t1080_exec(payload_path, target_path):
    # 複製惡意程式碼到目標檔案所在的共享資料夾
    shutil.copy2(payload_path, target_path)

    print("惡意程式碼已複製到檔案:", target_path)

# 測試
t1080_exec('payload.exe', '\\\\network\\shared\\file.txt')