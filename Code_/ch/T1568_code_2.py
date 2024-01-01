import dns.resolver
from random import choice

# 1. 使用dnspython套件進行DNS解析，從多個可能的域名中隨機選擇一個
def resolve_dga_domain(dga_domains):
    domain = choice(dga_domains)
    return domain

# 2. 使用dnspython套件進行DNS解析，獲取域名的IP地址
def resolve_dns_ip(domain):
    answers = dns.resolver.resolve(domain, 'A')
    ip = str(answers[0])
    return ip