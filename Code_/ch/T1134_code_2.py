import win32security
from win32api import SetTokenInformation

def impersonate_user(username, password):
    token = win32security.LogonUser(
        username,
        None,
        password,
        win32security.LOGON32_LOGON_INTERACTIVE,
        win32security.LOGON32_PROVIDER_DEFAULT
    )
    # 設置Token以便在系統上下文中運行線程
    SetTokenInformation(win32api.GetCurrentThread(), win32security.TokenImpersonation, token)
    return True