from passlib.hash import sha256_crypt

password = "password123"
hash_value = sha256_crypt.hash(password)

print(hash_value)  # 輸出密碼的SHA-256雜湊值