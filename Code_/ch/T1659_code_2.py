import requests
from burp import IBurpExtender, IHttpListener

def content_injection():
    #將在Burp Suite的Proxy標籤中偵聽到的HTTP請求攔截下來
    class BurpListener(IHttpListener):

        def processHttpMessage(self, toolFlag, messageIsRequest, currentRequest):
            #如果攔截到的是HTTP請求
            if messageIsRequest:
                httpService = currentRequest.getHttpService()
                host = httpService.getHost()
                port = httpService.getPort()
                request = str(currentRequest.getRequest())
                
                #篡改HTTP請求的內容
                request = request.replace("\r\n\r\n", "\r\n\r\nEvilContent")
                
                #重新送回篡改後的請求
                newRequest = self._callbacks.makeHttpRequest(host, port, False, request)
                
                currentRequest.setRequest(newRequest)
                print("Sent modified request")
    
    #建立Burp Suite的API連線
    from burp import callbacks
    callbacks = callbacks()
    callbacks.registerExtension(BurpListener())

    #監聽Burp Suite的Proxy標籤中攔截到的請求
    while True:
        pass

content_injection()