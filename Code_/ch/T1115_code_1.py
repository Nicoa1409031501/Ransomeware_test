import ctypes

clipboard_data = ctypes.windll.user32.GetClipboardData()
print(clipboard_data)