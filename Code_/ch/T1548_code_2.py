import ctypes

def abuse_elevation_control3():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "command_to_execute", None, None, 1)

abuse_elevation_control3()