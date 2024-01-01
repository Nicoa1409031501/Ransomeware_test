import smtplib

def send_smtp():
    target_email = "c2server@example.com"  # C2 server的郵件地址
    payload = "Subject: Hello\n\nHello, C2 server!"  # 要傳送的郵件內容

    smtp_server = "smtp.example.com"  # SMTP伺服器地址
    smtp_port = 587  # SMTP伺服器連接埠

    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
    smtp_obj.starttls()
    smtp_obj.login("your_email@example.com", "your_password")  # 你的郵件帳號和密碼
    smtp_obj.sendmail("your_email@example.com", target_email, payload)
    smtp_obj.quit()

send_smtp()