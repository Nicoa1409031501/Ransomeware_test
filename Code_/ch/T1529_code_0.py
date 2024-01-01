import os

def system_shutdown():
    os.system("shutdown /s /t 0")
    
def system_reboot():
    os.system("shutdown /r /t 0")