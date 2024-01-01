import sh

def deploy_software(command):
    sh.Command(command)()
   
# 使用範例
deploy_software("msiexec /i setup.msi /qn")
deploy_software("powershell.exe -ExecutionPolicy Bypass -File deploy.ps1")