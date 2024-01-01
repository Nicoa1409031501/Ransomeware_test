import pyperclip

def exfiltration_over_physical_medium(data):
    pyperclip.copy(data)
    print("Data copied to clipboard. Please manually paste it to the destination device.")

# 使用示例
data = "Sensitive data"
exfiltration_over_physical_medium(data)