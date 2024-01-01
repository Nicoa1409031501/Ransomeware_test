import ctypes
   
   kernel32 = ctypes.WinDLL('kernel32')
   
   def hook_api(api_name):
       api_address = kernel32.GetProcAddress(kernel32.GetModuleHandle("kernel32"), api_name)
       hook_code = b'\xc3'  # RET opcode
       ctypes.windll.kernel32.VirtualProtect(api_address, 1, 0x40, ctypes.byref(ctypes.c_ulong()))
       ctypes.memmove(api_address, hook_code, 1)