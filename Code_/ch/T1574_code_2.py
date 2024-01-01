import ctypes

def hijack_execution_flow(command):
    ctypes.windll.kernel32.WinExec(command, 1)

# 使用方法
hijack_execution_flow("calc.exe")