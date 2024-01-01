import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    
    if cpu_usage > 80:  # 假設超過80%的 CPU 使用率視為資源被占用
        return True
    else:
        return False

def resource_hijacking_detection():
    if check_cpu_usage():
        # 發送警報郵件
        send_email('admin@example.com', 'Resource hijacking detected!')
        
def send_email(receiver, content):
    # 使用 email 模組來發送郵件
    import smtplib
    from email.mime.text import MIMEText
    
    msg = MIMEText(content)
    msg['Subject'] = 'Resource hijacking alert'
    msg['From'] = 'noreply@example.com'
    msg['To'] = receiver
    
    with smtplib.SMTP('smtp.example.com', 25) as smtp:
        smtp.send_message(msg)
        
resource_hijacking_detection()