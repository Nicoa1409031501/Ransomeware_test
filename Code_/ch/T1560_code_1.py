import py7zr
from cryptography.fernet import Fernet

def compress_and_encrypt_files(file_paths, output_path, password):
    # 壓縮檔案
    with py7zr.SevenZipFile(output_path, 'w', password=password) as archive:
        for file_path in file_paths:
            archive.write(file_path)

    # 加密壓縮後的檔案
    encrypt_file(output_path, password)


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
compress_and_encrypt_files(['file1.txt', 'file2.txt'], 'archive.7z', b'password123')