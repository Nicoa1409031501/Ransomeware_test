import time

def get_system_time():
    system_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return system_time

print(get_system_time())