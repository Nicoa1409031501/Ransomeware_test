# 使用Python檔案操作來修改startup items
import plistlib

def modify_startup_items():
    plist_file_path = "/Library/StartupItems/MyStartupItem/StartupParameters.plist"  # 更改為要修改的plist檔案路徑
    script_path = "/path/to/script.sh"  # 更改為要執行的腳本路徑

    try:
        with open(plist_file_path, "rb") as plist_file:
            plist_data = plistlib.load(plist_file)

        plist_data["program"] = script_path

        with open(plist_file_path, "wb") as plist_file:
            plistlib.dump(plist_data, plist_file)

        print("Startup item modified successfully.")
    except Exception as e:
        print("Error modifying startup item:", str(e))

modify_startup_items()