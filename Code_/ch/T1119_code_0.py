import os
import shutil

def automated_collection(target_directory, criteria, destination_directory):
    collected_files = []
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            if criteria in file:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_directory, file)
                shutil.copy2(source_path, destination_path)
                collected_files.append(destination_path)
    return collected_files

# 使用範例
target_directory = '/path/to/target/directory'
criteria = '.txt'
destination_directory = '/path/to/destination/directory'
collected_files = automated_collection(target_directory, criteria, destination_directory)
print(collected_files)