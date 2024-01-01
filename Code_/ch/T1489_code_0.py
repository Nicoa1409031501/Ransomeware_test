import subprocess

def stop_service(service_name):
    subprocess.run(['net', 'stop', service_name])

# 停止服務
stop_service('service_name')