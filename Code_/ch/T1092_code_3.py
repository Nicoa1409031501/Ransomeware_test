import subprocess

def execute_command(command):
    # 執行指令
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 將結果寫入文件
    with open("result.txt", "w") as file:
        file.write(result.stdout)

# 使用範例
execute_command("ls -l")