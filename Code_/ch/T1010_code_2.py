import psutil

def get_open_windows():
    pids = psutil.pids()
    window_list = []
    for pid in pids:
        try:
            process = psutil.Process(pid)
            if process.name() == "explorer.exe":
                window_handles = process.num_handles()
                if window_handles != 0:
                    window_list.append(process.name())
        except (psutil.Error, psutil.NoSuchProcess):
            continue
    return window_list

# 測試程式
open_windows = get_open_windows()
for window in open_windows:
    print(window)