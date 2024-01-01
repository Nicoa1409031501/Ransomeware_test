import subprocess

def execute_script(script_path):
    subprocess.call(["cscript", script_path])

# 使用方法
execute_script("pubprn.vbs")