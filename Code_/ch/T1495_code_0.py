import binascii

def firmware_corruption(file_path):
    with open(file_path, 'rb') as f:
        firmware_data = f.read()
        
    corrupted_data = binascii.unhexlify('deadbeef')
    
    with open(file_path, 'wb') as f:
        f.write(corrupted_data)
    
    print("Firmware corrupted successfully.")