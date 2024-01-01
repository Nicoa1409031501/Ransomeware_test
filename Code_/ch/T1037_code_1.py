# 使用Python調用subprocess模組來運行默認登錄腳本
import subprocess

def run_logon_script():
    logon_script_path = r"C:\path\to\script.bat"  # 更改為要執行的腳本路徑

    try:
        subprocess.run(logon_script_path, shell=True)
        print("Logon script executed successfully.")
    except Exception as e:
        print("Error executing logon script:", str(e))

run_logon_script()