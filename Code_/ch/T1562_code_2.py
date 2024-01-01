import shutil

def modify_file(file_path):
    # 修改檔案內容
    with open(file_path, "w") as f:
        f.write("Modified content")

    # 刪除檔案
    # shutil.rmtree(file_path)

# 使用範例
modify_file("C:\\Program Files\\Antivirus\\config.ini")
modify_file("C:\\Windows\\System32\\firewall.dll")