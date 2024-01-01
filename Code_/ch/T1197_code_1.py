import win32com.client

# 創建一個BITS job
bits = win32com.client.Dispatch("Bits.Ibits")

job = bits.CreateJob()

# 將指定檔案加入到BITS job中
job.AddFile("C:\\path\\to\\file.txt")

# 啟動或恢復BITS job
job.Resume()

# 暫停BITS job
job.Suspend()

# 刪除BITS job
job.Cancel()