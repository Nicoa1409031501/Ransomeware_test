import socket

def check_remote_service(target_ip, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.close()
        print("Connected to remote service at {}:{}".format(target_ip, target_port))
        return True
    except Exception as e:
        print("Connection failed to {}:{}. Error: {}".format(target_ip, target_port, str(e)))
        return False