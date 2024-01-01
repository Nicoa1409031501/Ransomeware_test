import os

def copy_file(source, destination):
    try:
        with open(source, 'rb') as src_file:
            with open(destination, 'wb') as dest_file:
                dest_file.write(src_file.read())
        print("檔案複製成功！")
    except Exception as e:
        print("檔案複製失敗：" + str(e))

# 使用範例
copy_file("source.txt", "destination.txt")