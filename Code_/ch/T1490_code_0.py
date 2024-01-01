import os

def inhibit_system_recovery(service_name):
    os.system(f"net stop {service_name}")

# 使用範例
inhibit_system_recovery("BITS")