from azure.storage.blob import BlobServiceClient

def transfer_data_to_cloud_account(source_connection_string, destination_connection_string, source_container_name, destination_container_name, blob_name):
    # 創建源和目標 BlobServiceClient 實例
    source_client = BlobServiceClient.from_connection_string(source_connection_string)
    destination_client = BlobServiceClient.from_connection_string(destination_connection_string)
    
    # 從源容器下載 Blob
    source_container = source_client.get_container_client(source_container_name)
    source_blob = source_container.download_blob(blob_name)
    source_blob.download_to_path('/tmp/temp_file')
    
    # 上傳 Blob 到目標容器
    destination_container = destination_client.get_container_client(destination_container_name)
    destination_blob = destination_container.upload_blob(blob_name, open('/tmp/temp_file', 'rb'))
    
    # 刪除暫存檔案
    os.remove('/tmp/temp_file')

# 使用範例
transfer_data_to_cloud_account('source_connection_string', 'destination_connection_string', 'source_container_name', 'destination_container_name', 'blob_name')