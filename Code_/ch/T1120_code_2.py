import infi.devicemanager

def peripheral_device_discovery():
    devices = infi.devicemanager.DeviceManager().disk_drives
    device_names = []
    for device in devices:
        device_names.append(device.description)
    return device_names

devices = peripheral_device_discovery()
for device in devices:
    print(device)