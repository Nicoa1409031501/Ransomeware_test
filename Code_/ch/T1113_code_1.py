from PIL import ImageGrab

# 擷取整個螢幕
image = ImageGrab.grab()

# 儲存擷取的圖片
image.save("screenshot.png")