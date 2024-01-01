import os

def get_system_info():
    cmd = 'wmic os get Caption, Version, CSName, Architecture'
    output = os.popen(cmd).read()
    # 可以將output寫入檔案或進行其他處理
    print(output)

get_system_info()