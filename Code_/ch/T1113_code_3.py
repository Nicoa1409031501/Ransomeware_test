from PIL import ImageGrab
import time

# 設定擷取的時間間隔 (單位: 秒)
interval = 10

while True:
    # 擷取整個螢幕
    image = ImageGrab.grab()
    
    # 儲存擷取的圖片，以時間戳記做為檔名
    filename = time.strftime("%Y%m%d%H%M%S") + ".png"
    image.save(filename)
    
    # 等待指定的時間間隔
    time.sleep(interval)