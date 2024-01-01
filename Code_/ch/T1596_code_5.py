from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

def search_public_certificate_data(certificate_file):
    # Step 1: 讀取憑證檔案
    with open(certificate_file, "rb") as f:
        cert_data = f.read()

    # Step 2: 解析憑證資料
    cert = load_pem_x509_certificate(cert_data, default_backend())

    # Step 3: 取得憑證資訊
    subject_name = cert.subject

    # Step 4: 輸出結果
    print(subject_name)

search_public_certificate_data("certificate.pem")