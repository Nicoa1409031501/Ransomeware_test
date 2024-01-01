import shutil

def search_shared_drive(path, local_dir):
    # 將網絡共享目錄下的文件拷貝到本地目錄中
    shutil.copytree(path, local_dir, dirs_exist_ok=True)

# 使用範例
shared_drive_path = r"\\server\share"    # 輸入網絡共享目錄的路徑
local_dir = r"C:\local\directory"        # 輸入本地目錄的路徑
search_shared_drive(shared_drive_path, local_dir)