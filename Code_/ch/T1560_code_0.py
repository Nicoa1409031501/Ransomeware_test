import zipfile
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def compress_and_encrypt_files(file_paths, output_path, password):
    # 壓縮檔案
    with zipfile.ZipFile(output_path, 'w') as zip_file:
        for file_path in file_paths:
            zip_file.write(file_path)

    # 加密壓縮後的檔案
    encrypt_file(output_path, password)


def encrypt_file(file_path, password):
    chunk_size = 64 * 1024
    cipher = AES.new(get_random_bytes(16), AES.MODE_CBC)
    iv = cipher.iv

    with open(file_path, 'rb') as file:
        with open(file_path + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(iv)

            while True:
                chunk = file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                encrypted_file.write(cipher.encrypt(chunk))

    # 刪除未加密的壓縮檔案
    os.remove(file_path)


# 使用範例
compress_and_encrypt_files(['file1.txt', 'file2.txt'], 'archive.zip', 'password123')