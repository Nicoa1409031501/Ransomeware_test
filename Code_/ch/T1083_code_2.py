import os
import re

def file_and_directory_discovery():
    # 列出當前目錄下的所有以.txt為結尾的文件
    files = [file for file in os.listdir('.') if re.match(r'.+\.txt$', file)]
    for file in files:
        print(file)

    # 列出當前目錄及其子目錄下的所有以.tmp或.bak為結尾的文件和目錄
    for root, directories, files in os.walk('.'):
        items = [item for item in directories + files if re.match(r'.+\.(tmp|bak)$', item)]
        for item in items:
            print(os.path.join(root, item))

file_and_directory_discovery()