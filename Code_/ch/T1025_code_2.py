import os
import fnmatch

# 從指定的路徑中搜尋指定的檔案
def search_files(path, target_files):
    found_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            for pattern in target_files:
                if fnmatch.fnmatch(file, pattern):
                    found_files.append(os.path.join(root, file))
                    break
    return found_files

# 指定要搜尋的路徑
search_path = "C:\\"
# 指定要搜尋的檔案
target_files = ["*.doc", "*.xls", "*.pdf"]

# 搜尋檔案
result = search_files(search_path, target_files)

# 印出搜尋結果
for file in result:
    print(file)