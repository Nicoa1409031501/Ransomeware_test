import shutil

def backup_file(file_path, backup_dir):
    shutil.copy2(file_path, backup_dir)  # 複製文件至備份目錄

file_path = 'client_binary.exe'  # 要備份的二進制文件路徑
backup_dir = 'backup'  # 備份目錄路徑
backup_file(file_path, backup_dir)