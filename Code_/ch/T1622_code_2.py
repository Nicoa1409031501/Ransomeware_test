import ptrace.debugger

def check_debugger():
    try:
        # 檢查是否為Debugger
        ptrace.debugger.child().has_debugger_attached()
        print("Debugger detected!")
    except Exception as e:
        print(f"Debugger not detected.")

check_debugger()