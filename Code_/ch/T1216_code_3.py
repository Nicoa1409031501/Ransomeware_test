def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

# 使用方法
write_file("pubprn.vbs", "Your VBScript code here")