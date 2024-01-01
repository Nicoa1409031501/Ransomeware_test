import subprocess

def get_system_info():
    cmd = 'wmic os get Caption, Version, CSName, Architecture'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    # 可以將output寫入檔案或進行其他處理
    print(output.decode())

get_system_info()