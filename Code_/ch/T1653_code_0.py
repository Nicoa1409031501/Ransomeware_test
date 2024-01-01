import os

def disable_hibernate():
    os.system("powercfg /hibernate off")

disable_hibernate()