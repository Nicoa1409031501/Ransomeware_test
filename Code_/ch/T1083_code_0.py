import os

def file_and_directory_discovery():
    # 列出當前目錄下的所有文件和目錄
    files_and_directories = os.listdir('.')
    for item in files_and_directories:
        print(item)

    # 遞歸列出當前目錄及其子目錄下的所有文件和目錄
    for root, directories, files in os.walk('.'):
        for file in files:
            print(os.path.join(root, file))

file_and_directory_discovery()