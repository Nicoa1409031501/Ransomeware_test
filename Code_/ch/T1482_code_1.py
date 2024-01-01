from ldap3 import Server, Connection, SUBTREE, ALL

def enumerate_domain_trusts():
    server_address = 'ldap://domain_controller_address'  # 目標網域控制器的位置
    username = 'username'  # 帳號
    password = 'password'  # 密碼
    base_dn = 'DC=target_domain,DC=com'  # 網域的根節點

    try:
        server = Server(server_address, get_info=ALL)
        conn = Connection(server, user=username, password=password)
        conn.bind()

        conn.search(base_dn, '(objectClass=trustedDomain)', SUBTREE)
        for entry in conn.entries:
            print(f"Trust Domain: {entry.name.value}")

        conn.unbind()
    except Exception as e:
        print(f"Error: {e}")

enumerate_domain_trusts()