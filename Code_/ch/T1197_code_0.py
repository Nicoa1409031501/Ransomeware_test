import subprocess

# 使用BITSAdmin指令創建一個BITS job
subprocess.run(["bitsadmin", "/create", "myjob"])

# 將指定檔案加入到BITS job中
subprocess.run(["bitsadmin", "/addfile", "myjob", "C:\\path\\to\\file.txt"])

# 啟動或恢復BITS job
subprocess.run(["bitsadmin", "/resume", "myjob"])

# 暫停BITS job
subprocess.run(["bitsadmin", "/suspend", "myjob"])

# 刪除BITS job
subprocess.run(["bitsadmin", "/cancel", "myjob"])