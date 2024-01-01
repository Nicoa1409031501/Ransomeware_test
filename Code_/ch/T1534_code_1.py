import win32com.client as win32

def send_internal_spearphishing_email(from_email, to_email, subject, body):
    outlook_app = win32.Dispatch('Outlook.Application')
    mail_item = outlook_app.CreateItem(0)
    mail_item.Subject = subject
    mail_item.Body = body
    mail_item.To = to_email
    mail_item.Send()
    print('Internal spearphishing email sent successfully.')

# 使用方法
send_internal_spearphishing_email('from@example.com', 'to@example.com', 'Important Notice', 'Please update your account password by clicking on the link: http://example.com')