import random
import string

def gather_victim_identity_information():
    # Gather employee names
    employee_names = ['John Doe', 'Jane Smith', 'Michael Johnson']
    
    # Gather email addresses
    email_addresses = ['john.doe@example.com', 'jane.smith@example.com', 'michael.johnson@example.com']
    
    # Gather credentials
    credentials = []
    for i in range(3): # Change the range if you need more credentials
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        credentials.append((username, password))
    
    return employee_names, email_addresses, credentials

employee_names, email_addresses, credentials = gather_victim_identity_information()

print(employee_names)
print(email_addresses)
print(credentials)