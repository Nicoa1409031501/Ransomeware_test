import datetime

def get_system_time():
    system_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return system_time

print(get_system_time())