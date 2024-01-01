import imaplib
import smtplib
import email

def establish_email_account(username, password):
    # 連接郵件伺服器
    imap_server = imaplib.IMAP4("mail.example.com")
    smtp_server = smtplib.SMTP("smtp.example.com")

    # 登入郵件帳號
    imap_server.login(username, password)
    smtp_server.login(username, password)

    # 在郵件伺服器上建立新帳號
    imap_server.create("new_account@example.com") 

    # 在建立的新帳號中發送和接收郵件等操作
    # ...

    # 關閉連線
    imap_server.logout()
    smtp_server.quit()

# 使用範例
establish_email_account("example_username", "example_password")