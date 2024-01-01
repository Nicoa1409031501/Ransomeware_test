import os
import sys

def check_debugger():
    try:
        # 檢查是否為Debugger
        if sys.gettrace() is not None:
            print("Debugger detected!")
        else:
            print("Debugger not detected.")
    except Exception as e:
        print(f"Error: {e}")

check_debugger()