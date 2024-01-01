import platform

def check_debugger():
    try:
        # 檢查是否為Debugger
        if platform.system() == 'Windows' and platform.python_compiler().startswith('MSC v.'):
            print("Debugger detected!")
        else:
            print("Debugger not detected.")
    except Exception as e:
        print(f"Error: {e}")

check_debugger()