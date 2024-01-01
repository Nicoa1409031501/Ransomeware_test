from azure.storage.blob import BlobServiceClient

def cloud_storage_object_discovery():
    connection_string = "<your_connection_string>"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client_list = blob_service_client.list_containers()  # 列舉容器
    for container_client in container_client_list:
        container_name = container_client['name']
        # 列舉容器中的物件
        blob_list = blob_service_client.get_container_client(container_name).list_blobs()
        for blob in blob_list:
            blob_name = blob.name
            print(f"Container: {container_name}, Object: {blob_name}")

cloud_storage_object_discovery()