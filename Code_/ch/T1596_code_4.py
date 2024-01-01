import whois

def search_dns_data(domain):
    # Step 1: 使用python-whois套件查詢域名的WHOIS資料
    w = whois.query(domain)

    # Step 2: 輸出WHOIS資料
    print(w)

search_dns_data("example.com")