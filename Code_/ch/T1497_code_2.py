# 使用 psutil 套件 偵測系統資訊
import psutil

def check_virtualization_psutil():
    try:
        for proc in psutil.process_iter():
            if 'qemu-ga' in proc.name() or 'VBoxService' in proc.name():
                return True
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

result = check_virtualization_psutil()
print(f"虛擬化檢測結果: {result}")