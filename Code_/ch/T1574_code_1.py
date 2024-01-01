import subprocess

def hijack_execution_flow(cmd_args):
    subprocess.run(cmd_args)

# 使用方法
hijack_execution_flow(["calc.exe"])