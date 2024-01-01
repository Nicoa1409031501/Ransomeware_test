from PIL import ImageGrab

# 設定擷取的區域 (左上角 x, y, 右下角 x, y)
region = (100, 100, 500, 500)

# 擷取指定區域
image = ImageGrab.grab(region)

# 儲存擷取的圖片
image.save("screenshot.png")