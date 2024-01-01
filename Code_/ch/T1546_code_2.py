import win32com.client

def create_wmi_event_subscription():
    wmi = win32com.client.GetObject("winmgmts:root\\subscription")

    # 設定事件訂閱的細節，例如篩選器、提供者、消費者等等...

    # 執行 WMI 事件訂閱
    subscription = wmi.ExecNotificationQuery("SELECT * FROM __InstanceCreationEvent WHERE TargetInstance ISA 'Win32_Process'")

    for event in subscription:
        # 在此加入執行惡意程式的程式碼
        pass

# 使用範例
create_wmi_event_subscription()