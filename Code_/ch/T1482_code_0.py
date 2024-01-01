import win32net
import win32netcon

def enumerate_domain_trusts():
    domain = 'target_domain'  # 目標網域名稱
    level = 1  # 網域訊息的層級

    try:
        regions, total, resume_handle = win32net.NetEnumerateTrustedDomains(domain, level)
        for region in regions:
            print(f"Trust Domain: {region['name']}")
    except Exception as e:
        print(f"Error: {e}")

enumerate_domain_trusts()