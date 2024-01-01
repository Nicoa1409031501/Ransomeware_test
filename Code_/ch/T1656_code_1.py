from faker import Faker

fake = Faker()

def generate_fake_info():
    name = fake.name()
    phone = fake.phone_number()
    address = fake.address()
    email = fake.email()
    
    return name, phone, address, email

# 使用方法
fake_name, fake_phone, fake_address, fake_email = generate_fake_info()
print(fake_name, fake_phone, fake_address, fake_email)