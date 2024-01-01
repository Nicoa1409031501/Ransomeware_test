import clr
clr.AddReference("System.DirectoryServices.AccountManagement")

from System.DirectoryServices.AccountManagement import *

# 創建域帳戶的函式
def create_domain_account(username, password):
    context = PrincipalContext(ContextType.Domain)
    user = UserPrincipal(context)
    user.SamAccountName = username
    user.SetPassword(password)
    user.Enabled = True
    user.Save()

# 呼叫函式來創建域帳戶
create_domain_account("test_user", "password123")