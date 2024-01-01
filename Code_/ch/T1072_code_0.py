import os

def deploy_software(command):
    os.system(command)
   
# 使用範例
deploy_software("msiexec /i setup.msi /qn")
deploy_software("powershell.exe -ExecutionPolicy Bypass -File deploy.ps1")