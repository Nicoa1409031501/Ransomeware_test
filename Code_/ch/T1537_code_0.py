import boto3

def transfer_data_to_cloud_account(access_key, secret_key, source_bucket, destination_bucket, object_key):
    # 創建源和目標 S3 實例
    source_s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    destination_s3 = boto3.resource('s3')
    
    # 從源 S3 下載物件
    source_object = source_s3.Object(source_bucket, object_key)
    source_object.download_file('/tmp/temp_file')
    
    # 上傳物件到目標 S3
    destination_object = destination_s3.Object(destination_bucket, object_key)
    destination_object.upload_file('/tmp/temp_file')
    
    # 刪除暫存檔案
    os.remove('/tmp/temp_file')

# 使用範例
transfer_data_to_cloud_account('source_access_key', 'source_secret_key', 'source_bucket', 'destination_bucket', 'object_key')