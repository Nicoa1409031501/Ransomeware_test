import random
import string
import hashlib

def gather_victim_identity_information():
    # Same as the previous examples
    employee_names = ['John Doe', 'Jane Smith', 'Michael Johnson']
    email_addresses = ['john.doe@example.com', 'jane.smith@example.com', 'michael.johnson@example.com']
    
    credentials = []
    for i in range(3):
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        credentials.append((username, hashed_password))
    
    return employee_names, email_addresses, credentials

employee_names, email_addresses, credentials = gather_victim_identity_information()

print(employee_names)
print(email_addresses)
print(credentials)