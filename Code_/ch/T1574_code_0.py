import os

def hijack_execution_flow(command):
    os.system(command)

# 使用方法
hijack_execution_flow("calc.exe")