import csv
import win32com.client

def enumerate_device_drivers_csv(filename):
    wmi = win32com.client.GetObject("winmgmts:")
    drivers = wmi.InstancesOf("Win32_PnPSignedDriver")

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Device Name", "Manufacturer"])

        for driver in drivers:
            writer.writerow([driver.DeviceName, driver.Manufacturer])

enumerate_device_drivers_csv("device_drivers.csv")