import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    if cpu_usage > 80:  # 假設超過80%的 CPU 使用率視為資源被占用
        return True
    else:
        return False

def resource_hijacking_detection():
    if check_cpu_usage():
        with open('resource_hijacking_log.txt', 'a') as f:  # 將偵測結果輸出至檔案
            f.write("Resource hijacking detected!\n")
    else:
        with open('resource_hijacking_log.txt', 'a') as f:  # 將偵測結果輸出至檔案
            f.write("No resource hijacking detected.\n")
        
resource_hijacking_detection()