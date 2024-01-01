import ctypes

def system_shutdown():
    ctypes.windll.shell32.ShutdownBlockReasonCreate(None, "Preparing for system shutdown")
    ctypes.windll.user32.ExitWindowsEx(0x00000008, 0x00000001)
    
def system_reboot():
    ctypes.windll.shell32.ShutdownBlockReasonCreate(None, "Preparing for system reboot")
    ctypes.windll.user32.ExitWindowsEx(0x00000002, 0x00000001)