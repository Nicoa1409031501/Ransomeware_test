from ctypes import wintypes, windll

def create_process_with_token(token):
    startupinfo = wintypes.STARTUPINFO()
    process_information = wintypes.PROCESS_INFORMATION()
    
    # 創建進程，使用指定的Token
    windll.advapi32.CreateProcessWithTokenW(
        token, 
        0, 
        None, 
        None, 
        0, 
        None, 
        None, 
        byref(startupinfo), 
        byref(process_information)
    )
    return True