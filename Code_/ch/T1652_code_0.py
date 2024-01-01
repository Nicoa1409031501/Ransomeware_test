import win32com.client

def enumerate_device_drivers():
    wmi = win32com.client.GetObject("winmgmts:")
    drivers = wmi.InstancesOf("Win32_PnPSignedDriver")

    for driver in drivers:
        print(f"Device Name: {driver.DeviceName}")
        print(f"Manufacturer: {driver.Manufacturer}\n")

enumerate_device_drivers()