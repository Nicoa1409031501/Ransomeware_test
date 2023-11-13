import pygetwindow as gw

# 獲得當前活動窗口
active_window = gw.getWindowsWithTitle('')[0]

# 獲得窗口的標題
window_title = active_window.title

print(f"當前活動窗口的標題: {window_title}")
print(gw.getWindowsWithTitle(''))
