import wmi

def enumerate_device_drivers():
    c = wmi.WMI()
    drivers = c.Win32_PnPSignedDriver()

    for driver in drivers:
        print(f"Device Name: {driver.DeviceName}")
        print(f"Manufacturer: {driver.Manufacturer}\n")

enumerate_device_drivers()