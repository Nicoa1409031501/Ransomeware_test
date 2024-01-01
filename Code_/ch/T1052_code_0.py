import os
import subprocess

# 實現方式1: 使用os.system執行指令
def exfiltration_over_physical_medium_1(data_path, destination_path):
    cmd = f"cp {data_path} {destination_path}"
    os.system(cmd)

# 實現方式2: 使用subprocess.call執行指令列表
def exfiltration_over_physical_medium_2(data_path, destination_path):
    cmd = ["cp", data_path, destination_path]
    subprocess.call(cmd)

# 實現方式3: 使用subprocess.run執行指令列表並捕獲輸出
def exfiltration_over_physical_medium_3(data_path, destination_path):
    cmd = ["cp", data_path, destination_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

# 使用示例
data_path = "/path/to/data"
destination_path = "/path/to/destination"
exfiltration_over_physical_medium_1(data_path, destination_path)
exfiltration_over_physical_medium_2(data_path, destination_path)
exfiltration_over_physical_medium_3(data_path, destination_path)