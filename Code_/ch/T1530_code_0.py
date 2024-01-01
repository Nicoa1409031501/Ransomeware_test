import os
from google.cloud import storage

def get_data_from_cloud(bucket_name, file_name):
    # 設定認證憑證
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/credentials.json"

    # 連接到 Google Cloud Storage
    client = storage.Client()

    # 取得 bucket 物件
    bucket = client.get_bucket(bucket_name)

    # 取得檔案物件
    blob = bucket.blob(file_name)

    # 讀取檔案內容
    data = blob.download_as_text()

    return data