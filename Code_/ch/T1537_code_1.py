from google.cloud import storage

def transfer_data_to_cloud_account(source_bucket, destination_bucket, object_name, source_credentials_path, destination_credentials_path):
    # 創建源和目標 Google Cloud Storage 實例
    source_client = storage.Client.from_service_account_json(source_credentials_path)
    destination_client = storage.Client.from_service_account_json(destination_credentials_path)
    
    # 從源儲存桶下載物件
    source_bucket = source_client.get_bucket(source_bucket)
    source_blob = source_bucket.blob(object_name)
    source_blob.download_to_filename('/tmp/temp_file')
    
    # 上傳物件到目標儲存桶
    destination_bucket = destination_client.get_bucket(destination_bucket)
    destination_blob = destination_bucket.blob(object_name)
    destination_blob.upload_from_filename('/tmp/temp_file')
    
    # 刪除暫存檔案
    os.remove('/tmp/temp_file')

# 使用範例
transfer_data_to_cloud_account('source_bucket', 'destination_bucket', 'object_name', 'source_credentials_path.json', 'destination_credentials_path.json')