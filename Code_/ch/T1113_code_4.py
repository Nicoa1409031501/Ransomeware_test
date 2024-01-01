from PIL import ImageGrab
import requests
import io

# 擷取整個螢幕
image = ImageGrab.grab()

# 將圖片轉換為二進制數據流
image_data = io.BytesIO()
image.save(image_data, format='PNG')
image_data.seek(0)

# 傳送圖片到遠端伺服器
response = requests.post('http://example.com/upload', files={'image': image_data})

# 檢查傳送是否成功
if response.status_code == 200:
    print('Screenshot uploaded successfully')
else:
    print('Screenshot upload failed')