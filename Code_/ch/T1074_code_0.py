import os

def data_staging_local(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 這裡可以加入將資料複製到指定目錄的程式碼
    # 例如：os.system("cp /path/to/source/file " + directory)

def data_staging_central(directory, source_directories):
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 這裡可以加入將多台系統上的資料複製到指定目錄的程式碼
    # 例如：for source_directory in source_directories:
    #           os.system("cp -r " + source_directory + "/. " + directory)