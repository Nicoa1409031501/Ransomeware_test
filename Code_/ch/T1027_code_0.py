import zlib
from cryptography.fernet import Fernet

def obfuscate_file(file_path):
    # 讀取原始檔案
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # 加密檔案內容
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_content = f.encrypt(file_content)

    # 壓縮加密後的檔案
    compressed_content = zlib.compress(encrypted_content)

    # 將壓縮後的檔案寫入新檔案中
    obfuscated_file_path = file_path + ".obfuscated"
    with open(obfuscated_file_path, 'wb') as obfuscated_file:
        obfuscated_file.write(compressed_content)

    return obfuscated_file_path