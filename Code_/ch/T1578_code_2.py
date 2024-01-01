from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# 創建虛擬機器
def createCloudInstance(provider_name, access_id, secret_key, instance_name, image_id, size, location):
    driver = get_driver(Provider(provider_name))
    conn = driver(access_id, secret_key)

    images = conn.list_images()
    sizes = conn.list_sizes()

    image = [img for img in images if img.id == image_id][0]
    size = [siz for siz in sizes if siz.id == size][0]

    node = conn.create_node(name=instance_name, image=image, size=size, location=location)
    print("Instance created:", node.name)

# 刪除虛擬機器
def deleteCloudInstance(provider_name, access_id, secret_key, instance_id):
    driver = get_driver(Provider(provider_name))
    conn = driver(access_id, secret_key)

    nodes = conn.list_nodes()
    node = [nd for nd in nodes if nd.id == instance_id][0]

    conn.destroy_node(node)
    print("Instance deleted:", instance_id)

# 修改虛擬機器配置
def modifyCloudInstance(provider_name, access_id, secret_key, instance_id, size):
    driver = get_driver(Provider(provider_name))
    conn = driver(access_id, secret_key)

    sizes = conn.list_sizes()
    size = [siz for siz in sizes if siz.id == size][0]

    nodes = conn.list_nodes()
    node = [nd for nd in nodes if nd.id == instance_id][0]

    conn.ex_resize_instance(node, size)
    print("Instance modified:", instance_id)