import wmi

def network_share_discovery():
    c = wmi.WMI()

    shared_folders = []
    for share in c.Win32_Share():
        shared_folders.append(share.Name)

    return shared_folders

result = network_share_discovery()
print(result)