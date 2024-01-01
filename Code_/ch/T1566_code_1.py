import smtplib
from email.mime.multipart import MIMEMultipart

def send_spearphishing_link():
    from_email = "sender@example.com"
    to_email = "recipient@example.com"
    subject = "Important Information"
    body = "Please click the following link to access the information: https://maliciouswebsite.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "password")
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

send_spearphishing_link()