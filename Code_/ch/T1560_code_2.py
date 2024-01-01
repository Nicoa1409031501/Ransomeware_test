import shutil
import os
from cryptography.fernet import Fernet

def compress_and_encrypt_files(file_paths, output_path, password):
    # 新建資料夾
    temp_folder = 'temp_folder'
    os.makedirs(temp_folder)
    
    # 複製檔案到暫存資料夾
    for file_path in file_paths:
        shutil.copy2(file_path, temp_folder)
        
    # 壓縮暫存資料夾
    shutil.make_archive(output_path, 'zip', temp_folder)
    
    # 加密壓縮後的檔案
    encrypt_file(output_path + '.zip', password)
    
    # 刪除暫存資料夾
    shutil.rmtree(temp_folder)
    

def encrypt_file(file_path, password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted_data = cipher_suite.encrypt(file.read())

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # 刪除未加密的壓縮檔案
    os.remove(file_path)


# 使用範例
compress_and_encrypt_files(['file1.txt', 'file2.txt'], 'archive', b'password123')