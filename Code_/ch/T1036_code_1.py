import shutil

# 方法2: 移動檔案到不同目錄並重命名
def move_and_rename_file(filepath, new_directory, new_filename):
    # 組合新的檔案路徑
    new_filepath = os.path.join(new_directory, new_filename)
    # 移動檔案到新路徑
    shutil.move(filepath, new_filepath)

# 測試
move_and_rename_file("/path/to/malware.exe", "/new_directory", "legit.exe")