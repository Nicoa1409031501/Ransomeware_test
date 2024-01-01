import os

# 顯示所有檔案（包括隱藏檔案）
os.system("dir /a")

# 隱藏檔案（將test.txt設為隱藏檔案）
os.system("attrib +h test.txt")

# 再次顯示檔案（確認test.txt是否已隱藏）
os.system("dir /a")