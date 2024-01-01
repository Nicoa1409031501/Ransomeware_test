# 使用Python的popen套件來執行命令，需要安裝popen套件
from subprocess import Popen

# 在目標系統上執行要引入的硬體設備的命令
Popen("command_to_introduce_hardware_device", shell=True)