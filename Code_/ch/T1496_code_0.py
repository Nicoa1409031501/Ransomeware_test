import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    if cpu_usage > 80:  # 假設超過80%的 CPU 使用率視為資源被占用
        return True
    else:
        return False

def resource_hijacking_detection():
    if check_cpu_usage():
        print("Resource hijacking detected!")
    else:
        print("No resource hijacking detected.")
        
resource_hijacking_detection()