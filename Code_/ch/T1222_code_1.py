import subprocess

# 修改文件權限
def modify_file_permissions(file_path, permissions):
    subprocess.call(["chmod", oct(permissions), file_path])

# 修改目錄權限
def modify_directory_permissions(directory_path, permissions):
    subprocess.call(["chmod", oct(permissions), directory_path])

# 使用範例
file_path = "/path/to/file"
directory_path = "/path/to/directory"
permissions = 0o777  # 權限值

modify_file_permissions(file_path, permissions)
modify_directory_permissions(directory_path, permissions)