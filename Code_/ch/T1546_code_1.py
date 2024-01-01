import shutil

# 創建螢幕保護程式的程式路徑
screensaver_program = "C:\\path\\to\\malicious.scr"

def create_screensaver():
    # 將執行檔複製到系統資料夾中
    shutil.copy2("C:\\path\\to\\malicious.exe", screensaver_program)

    # 設定 screensaver 的相關設定

# 使用範例
create_screensaver()