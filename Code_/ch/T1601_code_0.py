import os

# 方法一：修改存儲的系統映像檔案
def modify_system_image(file_path):
    # 讀取檔案
    with open(file_path, 'r') as file:
        system_image = file.read()
    
    # 修改系統映像檔案
    modified_image = system_image.replace('old_feature', 'new_feature')
    
    # 寫入修改後的檔案
    with open(file_path, 'w') as file:
        file.write(modified_image)

# 使用範例
modify_system_image('system_image.txt')