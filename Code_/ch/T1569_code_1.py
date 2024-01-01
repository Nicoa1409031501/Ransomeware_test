import subprocess

# 執行launchctl
subprocess.run(["launchctl", "command", "payload"], capture_output=True, text=True)