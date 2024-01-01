import os

def stop_service(service_name):
    os.system('net stop ' + service_name)

# 停止服務
stop_service('service_name')