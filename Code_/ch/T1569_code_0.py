import subprocess

# 執行Windows service control manager
subprocess.run(["sc.exe", "command", "payload"])