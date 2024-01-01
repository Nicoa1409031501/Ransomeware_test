# 使用Python內建的binascii模組進行資料編碼
import binascii

# 編碼
def encode_data(data):
    encoded_data = binascii.b2a_hex(data.encode('utf-8')).decode('utf-8')
    return encoded_data

# 解碼
def decode_data(encoded_data):
    decoded_data = binascii.a2b_hex(encoded_data.encode('utf-8')).decode('utf-8')
    return decoded_data

# 測試
data = "Hello, World!"
encoded_data = encode_data(data)
decoded_data = decode_data(encoded_data)

print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)