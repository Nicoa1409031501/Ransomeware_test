# 使用Python內建的base64模組進行資料編碼
import base64

# 編碼
def encode_data(data):
    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return encoded_data

# 解碼
def decode_data(encoded_data):
    decoded_data = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
    return decoded_data

# 測試
data = "Hello, World!"
encoded_data = encode_data(data)
decoded_data = decode_data(encoded_data)

print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)