from PIL import Image

def obfuscate_data_in_image(data, image_path):
    # 打開圖片
    image = Image.open(image_path)

    # 將資料隱藏到圖片中
    data = data.encode('utf-8')  # 將資料轉換為bytes格式，以便隱藏
    image.putdata(list(data))

    # 儲存混淆後的圖片
    obfuscated_image_path = image_path + ".obfuscated"
    image.save(obfuscated_image_path)

    return obfuscated_image_path