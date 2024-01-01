# 安裝套件：pip install ldap3

from ldap3 import Server, Connection, ALL_ATTRIBUTES

# 方法二：使用ldap3套件，修改GPOs

# 定義LDAP伺服器的相關資訊，<DOMAIN>請替換為實際的網域名稱
server = Server('<DOMAIN>')
base_dn = 'DC=<DOMAIN>,DC=local'

# 修改GPO的設定
# 這裡是一個示範，實際上應根據需要修改對應的GPO設定
def modify_gpo_settings():
    with Connection(server, auto_bind=True) as conn:
        conn.search(base_dn, '(objectClass=groupPolicyContainer)', attributes=ALL_ATTRIBUTES)
        gpo_entries = conn.entries
        # 取得GPO的dn，這裡隨機選擇一個GPO
        gpo_dn = gpo_entries[0].entry_dn
        # 修改GPO設定，這裡將gPCMachineExtensionNames屬性改為['{35378EAC-683F-11D2-A89A-00C04FBBCFA2}']
        conn.modify(gpo_dn, {'gPCMachineExtensionNames': [(['{35378EAC-683F-11D2-A89A-00C04FBBCFA2}'],)])})

modify_gpo_settings()