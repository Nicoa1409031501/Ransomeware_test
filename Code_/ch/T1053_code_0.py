import subprocess

def run_malicious_code_at(date, time, command):
    subprocess.run(['at', time, date], input=bytes(command, encoding='utf-8'))

run_malicious_code_at('2022-01-01', '08:00', 'echo "Hello World"')