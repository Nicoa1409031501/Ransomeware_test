import glob

def file_and_directory_discovery():
    # 查找當前目錄下的所有文件
    files = glob.glob('*')
    for file in files:
        print(file)

    # 查找指定目錄及其子目錄下的所有.txt文件
    txt_files = glob.glob('dir/**/*.txt', recursive=True)
    for txt_file in txt_files:
        print(txt_file)

file_and_directory_discovery()