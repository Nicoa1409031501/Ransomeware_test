import ctypes

kernel32 = ctypes.WinDLL('kernel32')

# 使用Native API中的GetTickCount函數獲取系統運行時間
tick_count = kernel32.GetTickCount()
print(f'System has been running for {tick_count} milliseconds')