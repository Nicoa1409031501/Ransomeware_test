import pygetwindow

def get_open_windows():
    windows = pygetwindow.getAllTitles()
    return windows

# 測試程式
open_windows = get_open_windows()
for window in open_windows:
    print(window)