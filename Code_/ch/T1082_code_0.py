import subprocess

def get_system_info():
    result = subprocess.run(['wmic', 'os', 'get', 'Caption, Version, CSName, Architecture'], capture_output=True, text=True)
    output = result.stdout
    # 可以將output寫入檔案或進行其他處理
    print(output)

get_system_info()