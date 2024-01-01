import ctypes
import win32con
import win32api
from ctypes import wintypes

def elevate_token(user):
    # 複製目標用戶的token
    token = win32security.LogonUser(
        user, 
        "", 
        "", 
        win32con.LOGON32_LOGON_INTERACTIVE, 
        win32con.LOGON32_PROVIDER_DEFAULT
    )
    duplicate_token = win32security.DuplicateTokenEx(
        token, 
        win32security.SecurityImpersonation, 
        win32con.TOKEN_ALL_ACCESS, 
        win32security.TokenPrimary
    )
    # 變更當前進程的安全上下文
    win32security.ImpersonateLoggedOnUser(duplicate_token)
    return True