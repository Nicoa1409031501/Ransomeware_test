import socket

def exfiltrate_data(data, chunk_size):
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    for chunk in chunks:
        # 這裡實際上要將chunk送出到指定的伺服器，這裡只是做例子，僅印出chunk
        print(chunk)

# 測試程式碼
data = "This is some sensitive data."
chunk_size = 10
exfiltrate_data(data, chunk_size)