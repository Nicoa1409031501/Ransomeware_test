import dns.resolver
from random import choice

# 1. 使用dnspython套件進行DNS解析，從多個IP地址中隨機選擇一個
def resolve_dns_fast_flux(domain):
    answers = dns.resolver.resolve(domain, 'A')
    ips = [str(rdata) for rdata in answers]
    return choice(ips)

# 2. 使用dnspython套件進行DNS解析，獲取域名的TTL值
def get_dns_ttl(domain):
    answers = dns.resolver.resolve(domain, 'A')
    ttl = answers.rrset.ttl
    return ttl