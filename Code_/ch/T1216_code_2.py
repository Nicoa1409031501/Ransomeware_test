import ctypes

def execute_script(script_path):
    ctypes.windll.WScript.Shell.Run("cmd /c cscript " + script_path)

# 使用方法
execute_script("pubprn.vbs")