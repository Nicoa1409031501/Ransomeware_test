import datetime

def is_scheduled_time():
    current_time = datetime.datetime.now().time()
    scheduled_time = datetime.time(8, 0)  # 指定的時間為早上8點
    
    if current_time == scheduled_time:
        return True
    else:
        return False