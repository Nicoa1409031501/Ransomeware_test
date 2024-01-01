from impacket.dcerpc.v5.dtypes import NULL
from impacket.dcerpc.v5 import transport

def enumerate_domain_trusts():
    target = 'target_domain_controller'  # 目標網域控制器
    username = 'username'  # 帳號
    password = 'password'  # 密碼

    try:
        rpctransport = transport.DCERPCTransportFactory(f'ncacn_ip_tcp:{target}')
        rpctransport.set_credentials(username, password)
        rpctransport.set_kerberos(True)

        dce = rpctransport.get_dce_rpc()
        dce.connect()
        dce.bind('\samr-interface', NULL)
        
        resp = dce.call('NetEnumerateTrustedDomains', NULL)
        for trusted_domain in resp['Buffer']['TrustedDomainList']['Domains']:
            print(f"Trust Domain: {trusted_domain['Name'].decode('utf-16le')}")

        dce.disconnect()
    except Exception as e:
        print(f"Error: {e}")

enumerate_domain_trusts()