import requests

def send_spearphishing_via_service():
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer API_KEY"
    }
    payload = {
        "personalizations": [
            {
              "to": [
                {
                  "email": "recipient@example.com"
                }
              ],
              "subject": "Important Announcement"
            }
        ],
        "from": {
            "email": "sender@example.com"
        },
        "content": [
            {
              "type": "text/plain",
              "value": "Please pay attention to the attached document."
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

send_spearphishing_via_service()