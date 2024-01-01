import mmap

# 方法三：使用mmap修改系統映像檔案
def modify_system_image(file_path):
    # 開啟文件
    with open(file_path, 'r+') as file:
        # 創建mmap物件
        mm = mmap.mmap(file.fileno(), 0)
        
        # 搜尋舊特徵
        old_feature = b'old_feature'
        new_feature = b'new_feature'
        if mm.find(old_feature) != -1:
            # 修改內容
            mm.replace(old_feature, new_feature)
        
        # 關閉mmap物件
        mm.close()

# 使用範例
modify_system_image('system_image.txt')