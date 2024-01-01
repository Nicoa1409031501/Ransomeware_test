# 使用Python檔案操作來修改/Library/Preferences/com.apple.loginwindow.plist檔案
import plistlib

def modify_login_hook():
    plist_file_path = r"/Library/Preferences/com.apple.loginwindow.plist"  # 輸入您的檔案路徑
    script_path = r"/path/to/script.sh"  # 更改為要執行的腳本路徑

    try:
        with open(plist_file_path, "rb") as plist_file:
            plist_data = plistlib.load(plist_file)

        plist_data["LoginHook"] = script_path

        with open(plist_file_path, "wb") as plist_file:
            plistlib.dump(plist_data, plist_file)

        print("Login hook modified successfully.")
    except Exception as e:
        print("Error modifying login hook:", str(e))

modify_login_hook()