# 使用 wmi套件 偵測系統資訊
import wmi

def check_virtualization_wmi():
    try:
        c = wmi.WMI()
        # 判斷系統使用的虛擬化技術是否存在
        for os in c.Win32_OperatingSystem():
            if os.Name.lower().find("virtualbox") != -1:
                return True
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

result = check_virtualization_wmi()
print(f"虛擬化檢測結果: {result}")