import glob
import shutil

def automated_collection(target_directory, criteria, destination_directory):
    collected_files = []
    file_paths = glob.glob(os.path.join(target_directory, f"*{criteria}*"))
    for file_path in file_paths:
        destination_path = os.path.join(destination_directory, os.path.basename(file_path))
        shutil.copy2(file_path, destination_path)
        collected_files.append(destination_path)
    return collected_files

# 使用範例
target_directory = '/path/to/target/directory'
criteria = '.txt'
destination_directory = '/path/to/destination/directory'
collected_files = automated_collection(target_directory, criteria, destination_directory)
print(collected_files)