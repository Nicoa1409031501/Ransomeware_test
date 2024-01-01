import shutil

# 實現方式1: 使用shutil.copy
def exfiltration_over_physical_medium_1(data_path, destination_path):
    shutil.copy(data_path, destination_path)

# 實現方式2: 使用shutil.copy2
def exfiltration_over_physical_medium_2(data_path, destination_path):
    shutil.copy2(data_path, destination_path)

# 實現方式3: 使用shutil.move
def exfiltration_over_physical_medium_3(data_path, destination_path):
    shutil.move(data_path, destination_path)

# 使用示例
data_path = "/path/to/data"
destination_path = "/path/to/destination"
exfiltration_over_physical_medium_1(data_path, destination_path)
exfiltration_over_physical_medium_2(data_path, destination_path)
exfiltration_over_physical_medium_3(data_path, destination_path)