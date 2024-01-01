import win32net

# 使用NetScheduleJobAdd函式創建一個BITS job
win32net.NetScheduleJobAdd(None, {
    "ServerName": None,
    "TriggerType": 0,  # 立即觸發
    "Command": "C:\\path\\to\\file.bat",  # 欲執行的檔案路徑
    "StartTime": 0,  # 開始時間（立即）
    "MinutesDuration": 0,  # 執行時間（無限）
    "Flags": 1  # 隱藏視窗
})

# 使用NetScheduleJobDel函式刪除BITS job
win32net.NetScheduleJobDel(None, "JobName")