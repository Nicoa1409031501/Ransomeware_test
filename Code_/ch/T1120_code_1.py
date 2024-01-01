import wmi

def peripheral_device_discovery():
    c = wmi.WMI()
    devices = c.Win32_PnPEntity()
    device_names = []
    for device in devices:
        device_names.append(device.Caption)
    return device_names

devices = peripheral_device_discovery()
for device in devices:
    print(device)