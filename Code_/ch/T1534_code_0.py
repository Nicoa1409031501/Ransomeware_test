import smtplib
from email.mime.text import MIMEText

def send_internal_spearphishing_email(from_email, to_email, subject, body):
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    username = 'your_username'
    password = 'your_password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
        print('Internal spearphishing email sent successfully.')
    except Exception as e:
        print('Failed to send internal spearphishing email:', str(e))

# 使用方法
send_internal_spearphishing_email('from@example.com', 'to@example.com', 'Important Notice', 'Please update your account password by clicking on the link: http://example.com')