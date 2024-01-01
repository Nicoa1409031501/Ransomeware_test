from krb5 import * #import python-krb5套件

def use_tgs_ticket(ticket):
    # 使用TGS票據
    krb_context = krb5.Context()
    krb_context.default_realm = get_default_realm()
    tgt = krb5_ticket.Ticket()
    tgt.from_asn1(ticket.as_asn1())
    tgt_client = tgt.client
    tgt_server = tgt.server
    ap_req = krb_context.mk_rep(tgt, tgt_client, tgt_server)
    
    # 返回使用結果
    return ap_req