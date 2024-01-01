import subprocess

def deploy_software(command):
    subprocess.call(command, shell=True)
   
# 使用範例
deploy_software("msiexec /i setup.msi /qn")
deploy_software("powershell.exe -ExecutionPolicy Bypass -File deploy.ps1")