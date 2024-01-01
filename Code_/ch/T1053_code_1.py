import subprocess

def schedule_malicious_code_cron(cron_expression, command):
    subprocess.run(['echo', command, '|', 'crontab', '-'])

schedule_malicious_code_cron('0 8 * * *', 'echo "Hello World"')