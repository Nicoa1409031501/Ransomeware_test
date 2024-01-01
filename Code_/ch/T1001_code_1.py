import secrets

def add_junk_data(data, junk_ratio):
    junk_data = secrets.token_hex(int(len(data) * junk_ratio))
    return junk_data + data + junk_data

command = "example_command"
junk_data_ratio = 0.2
obfuscated_command = add_junk_data(command, junk_data_ratio)
print(obfuscated_command)