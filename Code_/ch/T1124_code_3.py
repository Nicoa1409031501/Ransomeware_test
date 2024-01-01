import time

def write_system_time_to_file(filename):
    system_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filename, "w") as file:
        file.write(system_time)

write_system_time_to_file("system_time.txt")