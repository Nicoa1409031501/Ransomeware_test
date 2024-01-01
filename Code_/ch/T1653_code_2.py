import win32api

def disable_shutdown():
    win32api.SetSuspendState(0, 0, 0)
    win32api.SetSystemPowerState(False, False)

disable_shutdown()