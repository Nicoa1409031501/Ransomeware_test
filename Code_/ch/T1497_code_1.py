# 使用 sys.platform 偵測系統資訊
import sys

def check_virtualization_sys_platform():
    platforms = ['win32', 'linux2', 'darwin']
    if sys.platform in platforms:
        return False
    else:
        return True

result = check_virtualization_sys_platform()
print(f"虛擬化檢測結果: {result}")