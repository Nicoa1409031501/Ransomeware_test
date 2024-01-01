import random
import string
import secrets

def gather_victim_identity_information():
    # Same as the previous example
    employee_names = ['John Doe', 'Jane Smith', 'Michael Johnson']
    email_addresses = ['john.doe@example.com', 'jane.smith@example.com', 'michael.johnson@example.com']
    
    credentials = []
    for i in range(3):
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = secrets.token_hex(6)
        credentials.append((username, password))
    
    return employee_names, email_addresses, credentials

employee_names, email_addresses, credentials = gather_victim_identity_information()

print(employee_names)
print(email_addresses)
print(credentials)