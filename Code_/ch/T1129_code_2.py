import ctypes

def execute_payload(payload_path):
    ctypes.windll.kernel32.LoadLibraryA(payload_path)

execute_payload('C:\\path\\to\\payload.dll')