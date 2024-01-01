import os

def user_open_file(file_path):
    os.startfile(file_path)

# 使用方式
user_open_file("C:/path/to/malicious_file.exe")