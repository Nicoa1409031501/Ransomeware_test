import hmac
import hashlib

password = "password123"
key = b"secret_key"
hash_value = hmac.new(key, password.encode(), hashlib.sha256).hexdigest()

print(hash_value)  # 輸出密碼的SHA-256 HMAC 雜湊值