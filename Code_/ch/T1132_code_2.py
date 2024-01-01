# 使用Python內建的codecs模組進行資料編碼
import codecs

# 編碼
def encode_data(data):
    encoded_data = codecs.encode(data.encode('utf-8'), 'hex').decode('utf-8')
    return encoded_data

# 解碼
def decode_data(encoded_data):
    decoded_data = codecs.decode(encoded_data.encode('utf-8'), 'hex').decode('utf-8')
    return decoded_data

# 測試
data = "Hello, World!"
encoded_data = encode_data(data)
decoded_data = decode_data(encoded_data)

print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)