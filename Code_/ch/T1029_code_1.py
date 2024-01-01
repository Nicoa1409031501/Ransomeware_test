import time

def is_scheduled_time():
    current_time = time.time()
    interval = 60 * 60  # 指定的間隔時間為1小時
    
    if current_time % interval == 0:
        return True
    else:
        return False