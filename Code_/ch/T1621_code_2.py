from twilio.rest import Client

def send_mfa_sms(account_sid, auth_token, from_number, to_number):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Your MFA verification code is xxxxxx',
        from_=from_number,
        to=to_number
    )
    return message.sid