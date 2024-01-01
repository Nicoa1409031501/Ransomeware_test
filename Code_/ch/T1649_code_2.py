from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# 讀取合法證書的私鑰
with open("private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# 製作自己的偽造證書
cert_builder = x509.CertificateBuilder().subject_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"www.example.com")
])).issuer_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"www.example.com")
])).serial_number(x509.random_serial_number()).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).public_key(private_key.public_key()).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"www.example.com")]),
    critical=False,
    # 以這個擴展名來模仿原本的合法證書
).sign(private_key, hashes.SHA256())

# 輸出偽造證書到檔案
with open("fake_cert.pem", "wb") as f:
    f.write(cert_builder.public_bytes(serialization.Encoding.PEM))

print("偽造證書已生成")