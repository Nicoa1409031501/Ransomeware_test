import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_fake_email(from_name, from_email, to_email, subject, message):
    # 郵件內容
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = formataddr((from_name, from_email))
    msg['To'] = to_email

    # 偽造郵件發送
    with smtplib.SMTP('your_smtp_server', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('your_username', 'your_password')
        smtp.send_message(msg)
        smtp.quit()

# 使用方法
send_fake_email("CEO John", "ceo@example.com", "employee@example.com", "Urgent Request", "Please transfer $10,000 to the following account...")