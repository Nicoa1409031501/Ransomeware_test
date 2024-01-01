# 使用mitmproxy套件
from mitmproxy import io, http

# 繼承mitmproxy的AddOn類別
class InterceptAddOn:
    def __init__(self):
        self.flow_count = 0
    
    # 偵測每個HTTP請求
    def request(self, flow: http.HTTPFlow) -> None:
        # 篡改session cookie的值
        flow.request.cookies['sessionid'] = 'modified_session_id'
        
        # 增加流量計數
        self.flow_count += 1
        
        # 印出請求資訊
        print(f"Flow #{self.flow_count}: {flow.request.url}")
    
    # 偵測每個HTTP回應
    def response(self, flow: http.HTTPFlow) -> None:
        # 印出回應資訊
        print(f"Flow #{self.flow_count}: {flow.response.status_code}")
    

# 啟動mitmproxy
addons = [InterceptAddOn()]
io.run(io.FlowReader(open("flows.txt", "rb")), addons=addons)