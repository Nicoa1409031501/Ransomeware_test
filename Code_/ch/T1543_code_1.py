import plistlib

def create_modify_system_process(file_path, label, program, run_at_load):
    # 讀取plist檔案
    with open(file_path, 'rb') as f:
        plist_data = plistlib.load(f)
    
    # 修改相對應的參數
    plist_data['Label'] = label
    plist_data['Program'] = program
    plist_data['RunAtLoad'] = run_at_load
    
    # 將修改後的內容寫回檔案
    with open(file_path, 'wb') as f:
        plistlib.dump(plist_data, f)

# 使用方式
create_modify_system_process('/System/Library/LaunchDaemons/com.apple.periodic-monthly.plist', 'custom-label', '/usr/local/bin/custom-program', True)