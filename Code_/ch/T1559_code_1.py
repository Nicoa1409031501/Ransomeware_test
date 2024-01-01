import win32com.client

# 使用pywin32套件執行COM物件
obj = win32com.client.Dispatch("SomeCOMObject")
result = obj.SomeMethod()
print(result)