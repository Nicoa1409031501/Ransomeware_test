import os

def execute_script(script_path):
    os.system("cscript " + script_path)

# 使用方法
execute_script("pubprn.vbs")