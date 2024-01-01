import subprocess

clipboard_data = subprocess.check_output(['xclip', '-selection', 'clipboard', '-o']).decode('utf-8')
print(clipboard_data)