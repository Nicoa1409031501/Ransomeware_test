import hashlib

password = "password123"
hash_value = hashlib.sha256(password.encode()).hexdigest()

print(hash_value)  # 輸出密碼的SHA-256雜湊值