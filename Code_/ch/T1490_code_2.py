import wmi

def inhibit_system_recovery(service_name):
    c = wmi.WMI()
    service = c.Win32_Service(Name=service_name)
    for s in service:
        s.StopService()

# 使用範例
inhibit_system_recovery("BITS")