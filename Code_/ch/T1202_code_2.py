import ctypes

def run_command(command):
    ctypes.windll.shell32.ShellExecuteW(None, "open", "cmd.exe", "/c " + command, None, 1)

# 使用ctypes.windll.shell32.ShellExecuteW()執行指定的命令
run_command("notepad.exe")