import subprocess

def remote_shell():
    while True:
        command = input("Enter command or 'exit' to quit: ")
        if command == 'exit':
            break
        result = subprocess.getoutput(command)
        print(result)

remote_shell()