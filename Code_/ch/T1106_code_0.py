import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

# 使用Native API中的MessageBoxA函數顯示彈出對話框
user32.MessageBoxA(None, 'Hello, World!', 'Message', 0)