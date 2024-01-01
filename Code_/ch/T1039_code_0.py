import os

def search_shared_drive(path, file_extension):
    files = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_extension):
                files.append(os.path.join(root, filename))
    return files

# 使用範例
shared_drive_path = r"\\server\share"    # 輸入網絡共享目錄的路徑
file_extension = ".txt"                  # 輸入感興趣的文件擴展名
found_files = search_shared_drive(shared_drive_path, file_extension)
for file in found_files:
    print(file)