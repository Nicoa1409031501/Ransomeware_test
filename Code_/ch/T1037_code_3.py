# 使用Python檔案操作來修改RC scripts
import os

def modify_rc_scripts():
    rc_script_path = "/etc/rc.local"  # 更改為要修改的RC script路徑
    script_to_add = "bash /path/to/script.sh"  # 更改為要執行的腳本路徑

    try:
        with open(rc_script_path, "a") as rc_file:
            rc_file.write(script_to_add)
            print("RC script modified successfully.")
    except Exception as e:
        print("Error modifying RC script:", str(e))

modify_rc_scripts()