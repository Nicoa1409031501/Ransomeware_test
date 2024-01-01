import subprocess

def search_bash_history(keyword):
    command = "cat ~/.bash_history | grep " + keyword
    output = subprocess.check_output(command, shell=True)
    return output.decode().split('\n')

# 使用方式：
results = search_bash_history('password')
print(results)