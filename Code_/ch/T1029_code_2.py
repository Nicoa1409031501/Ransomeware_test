import schedule
import time

def exfiltration():
    # 執行資料外洩的處理
    
def schedule_exfiltration():
    schedule.every().day.at("08:00").do(exfiltration)  # 每天早上8點執行資料外洩
    
    while True:
        schedule.run_pending()
        time.sleep(1)