import subprocess

# 方法3: 使用命令行指令來重命名檔案
def rename_file(filepath, new_filename):
    # 執行命令行指令
    subprocess.call(["mv", filepath, new_filename])

# 測試
rename_file("/path/to/malware.exe", "legit.exe")