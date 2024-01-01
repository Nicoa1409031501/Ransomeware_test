from ldap3 import Server, Connection, ALL

def domain_group_discovery():
    server = Server('ldap://your_domain_controller')
    conn = Connection(server, user='your_username', password='your_password')
    conn.bind()

    conn.search(search_base='OU=Groups,DC=your_domain,DC=com',
                search_filter='(objectClass=group)',
                attributes=['cn', 'member'])

    for entry in conn.entries:
        print(f"Group: {entry.cn}, Members: {entry.member}")

    conn.unbind()

domain_group_discovery()