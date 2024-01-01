import macpy

# 使用macpy套件與XPC service daemon進行互動
xpc_connection = macpy.xpc_create_connection("com.apple.xpc.some_service")
result = macpy.xpc_send_message(xpc_connection, "SomeMessage")
print(result)