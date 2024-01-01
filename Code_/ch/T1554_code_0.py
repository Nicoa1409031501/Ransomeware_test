import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        md5_hash = hashlib.md5(content).hexdigest()
        sha1_hash = hashlib.sha1(content).hexdigest()
        sha256_hash = hashlib.sha256(content).hexdigest()
        
    return md5_hash, sha1_hash, sha256_hash

file_path = 'client_binary.exe'  # 要計算哈希值的二進制文件路徑
md5_hash, sha1_hash, sha256_hash = calculate_hash(file_path)

# 將哈希值保存到日誌文件 (可選)
with open('hash_log.txt', 'a') as f:
    f.write(f"File: {file_path}\n")
    f.write(f"MD5 Hash: {md5_hash}\n")
    f.write(f"SHA1 Hash: {sha1_hash}\n")
    f.write(f"SHA256 Hash: {sha256_hash}\n\n")