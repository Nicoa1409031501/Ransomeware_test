import ctypes

def get_open_windows():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    
    def enum_window_callback(hwnd, window_list):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                title = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, title, length + 1)
                window_list.append(title.value)
        return True
    
    window_list = []
    EnumWindows(EnumWindowsProc(enum_window_callback), ctypes.byref(window_list))
    return window_list

# 測試程式
open_windows = get_open_windows()
for window in open_windows:
    print(window)