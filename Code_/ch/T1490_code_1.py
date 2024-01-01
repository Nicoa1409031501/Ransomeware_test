import subprocess

def inhibit_system_recovery(service_name):
    subprocess.run(["net", "stop", service_name], shell=True)

# 使用範例
inhibit_system_recovery("BITS")