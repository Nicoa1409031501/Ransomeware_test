from twilio.rest import Client

def send_spearphishing_voice():
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='This is an urgent message. Please provide your login credentials immediately.',
        from_='+1234567890',  # Twilio號碼
        to='+0987654321'  # 收件者號碼
    )

    print(message.sid)

send_spearphishing_voice()