import subprocess
import shutil

def automated_collection(target_directory, criteria, destination_directory):
    collected_files = []
    command = f"find {target_directory} -name '*{criteria}*' -type f -exec cp {{}} {destination_directory} \;"
    subprocess.run(command, shell=True)
    for root, dirs, files in os.walk(destination_directory):
        for file in files:
            collected_files.append(os.path.join(root, file))
    return collected_files

# 使用範例
target_directory = '/path/to/target/directory'
criteria = '.txt'
destination_directory = '/path/to/destination/directory'
collected_files = automated_collection(target_directory, criteria, destination_directory)
print(collected_files)