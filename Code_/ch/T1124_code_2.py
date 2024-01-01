import subprocess

def get_system_time():
    cmd = "date /t"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    system_time = output.decode().strip()
    return system_time

print(get_system_time())