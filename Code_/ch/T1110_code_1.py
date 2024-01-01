import hashlib

def crack_password(password_hash):
    with open('common_passwords.txt', 'r') as f:  # 假設存在一個包含常見密碼的檔案
        common_passwords = f.read().splitlines()
        
    for password in common_passwords:
        hashed_password = hashlib.md5(password.encode()).hexdigest()  # 使用MD5哈希函數
        if hashed_password == password_hash:
            return password
    
    return None

password_hash = '5f4dcc3b5aa765d61d8327deb882cf99'  # 使用MD5編碼的密碼
password = crack_password(password_hash)
if password:
    print(f"Password found: {password}")
else:
    print("Password not found")