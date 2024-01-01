import os

# 方法1: 修改檔案名稱
def change_filename(filepath, new_filename):
    # 從路徑中取得檔案名稱
    filename = os.path.basename(filepath)
    # 取得檔案的目錄路徑
    directory = os.path.dirname(filepath)
    # 組合新的檔案路徑
    new_filepath = os.path.join(directory, new_filename)
    # 移動檔案到新路徑
    os.rename(filepath, new_filepath)

# 測試
change_filename("/path/to/malware.exe", "legit.exe")