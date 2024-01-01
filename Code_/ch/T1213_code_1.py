import requests
import pandas as pd

def download_sharepoint_files(url, save_directory):
    response = requests.get(url)
    with open(save_directory, 'wb') as file:
        file.write(response.content)

def parse_sharepoint_files(file_path):
    df = pd.read_excel(file_path)  # 根據實際檔案格式進行解析
    valuable_info = df['valuable_info_column'].tolist()  # 根據實際欄位名稱篩選有價值的資訊
    return valuable_info

# 使用範例：下載SharePoint文件並進行解析
sharepoint_url = 'https://example.com/sharepoint'
save_path = './sharepoint_file.xlsx'
download_sharepoint_files(sharepoint_url, save_path)
info_list = parse_sharepoint_files(save_path)
print(info_list)