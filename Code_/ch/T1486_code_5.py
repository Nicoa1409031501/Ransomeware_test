key = get_random_bytes(16)  # 生成加密金鑰
   data = "This is the data to be encrypted".encode()  # 要加密的原始資料
   encrypted_data = encrypt_data(data, key)  # 加密後的資料
   print(encrypted_data)