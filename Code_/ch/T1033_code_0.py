import os
import subprocess

def get_current_user():
    return os.getlogin()

def get_logged_in_users():
    output = subprocess.check_output('net user', shell=True)
    users = []
    for line in output.decode().split('\n'):
        if line.strip().startswith('User name'):
            users.append(line.strip().split()[3])
    return users