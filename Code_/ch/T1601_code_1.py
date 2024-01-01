import subprocess

# 方法二：修改運行時的系統映像
def modify_runtime_image():
    # 使用subprocess呼叫操作系統的命令
    subprocess.run(['sed', '-i', 's/old_feature/new_feature/g', '/path/to/system_image'])

# 使用範例
modify_runtime_image()