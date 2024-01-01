import subprocess

def stop_service(service_name):
    process = subprocess.Popen(['net', 'stop', service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

# 停止服務
stop_service('service_name')