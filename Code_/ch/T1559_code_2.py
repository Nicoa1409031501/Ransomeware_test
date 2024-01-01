import win32ui

# 使用win32ui套件建立DDE連接並執行命令
dde = win32ui.CreateObject("DDE.DDEClient")
dde.Connect("ServiceName", "TopicName")
result = dde.Exec("SomeCommand")
print(result)