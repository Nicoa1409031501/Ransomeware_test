import ctypes

def exploit_vulnerability():
    # 使用ctypes呼叫具有漏洞的動態連結庫
    ctypes.cdll.LoadLibrary("vulnerable_library.so")

exploit_vulnerability()