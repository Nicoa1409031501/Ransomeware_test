import string
import random

def add_junk_data(data, junk_ratio):
    junk_data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(int(len(data) * junk_ratio)))
    return junk_data + data + junk_data

command = "example_command"
junk_data_ratio = 0.2
obfuscated_command = add_junk_data(command, junk_data_ratio)
print(obfuscated_command)