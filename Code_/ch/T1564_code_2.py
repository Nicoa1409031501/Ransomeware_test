import os

# 顯示所有檔案（包括隱藏檔案）
for file in os.listdir():
    print(file)

# 隱藏檔案（將test.txt設為隱藏檔案）
os.rename("test.txt", ".test.txt")

# 再次顯示檔案（確認test.txt是否已隱藏）
for file in os.listdir():
    print(file)