import subprocess

def copy_file(source, destination):
    try:
        subprocess.run(["cp", source, destination])
        print("檔案複製成功！")
    except Exception as e:
        print("檔案複製失敗：" + str(e))

# 使用範例
copy_file("source.txt", "destination.txt")