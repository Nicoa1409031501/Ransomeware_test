from azure.storage.blob import BlobServiceClient

def get_data_from_cloud(connection_string, container_name, blob_name):
    # 連接到 Azure Storage
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # 取得 Blob Container 物件
    container_client = blob_service_client.get_container_client(container_name)

    # 取得 Blob 物件
    blob_client = container_client.get_blob_client(blob_name)

    # 讀取 Blob 內容
    data = blob_client.download_blob().readall().decode('utf-8')

    return data