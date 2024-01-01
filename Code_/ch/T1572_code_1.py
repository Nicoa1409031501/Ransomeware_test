import random

def random_tunnel():
    protocols = ['HTTP', 'DNS', 'ICMP']
    selected_protocol = random.choice(protocols)
    
    # 在這裡進行隧道化的內容，使用selected_protocol
    
    print('使用的隧道協定：', selected_protocol)