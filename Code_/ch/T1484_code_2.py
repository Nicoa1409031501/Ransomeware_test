# 安裝套件：pip install pywinrm

from winrm.protocol import Protocol

# 方法三：使用pywinrm套件，執行PowerShell指令，修改GPOs

# 定義目標遠端伺服器的IP地址、帳戶名稱和密碼
target_ip = '<Remote_Server_IP>'
username = '<Username>'
password = '<Password>'

# 修改GPO的設定
# 這裡是一個示範，實際上應根據需要修改對應的GPO設定
def modify_gpo_settings():
    # 建立與遠端伺服器的連線
    p = Protocol(endpoint=f"http://{target_ip}:5985/wsman", transport='ntlm', username=username, password=password)
    shell_id = p.open_shell()
    # 定義要執行的PowerShell指令
    script = '''
    # 將gPCMachineExtensionNames屬性改為['{35378EAC-683F-11D2-A89A-00C04FBBCFA2}']
    Set-GPRegistryValue -Name "GPO_Name" -Key "HKLM\Software\Policies\Microsoft\Windows\...",...
    '''
    # 執行PowerShell指令
    stdout, stderr, return_code = p.run_command(shell_id, script)
    p.cleanup_command(shell_id)

modify_gpo_settings()