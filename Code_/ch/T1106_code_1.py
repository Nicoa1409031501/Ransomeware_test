import ctypes

ntdll = ctypes.WinDLL('ntdll')

# 使用Native API中的NtDeleteFile函數刪除指定文件
ntdll.NtDeleteFile(ctypes.c_wchar_p('C:\\path\\to\\file.txt'))