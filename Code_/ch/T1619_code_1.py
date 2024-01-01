from google.cloud import storage

def cloud_storage_object_discovery():
    client = storage.Client()
    buckets = client.list_buckets()  # 列舉存儲桶
    for bucket in buckets:
        bucket_name = bucket.name
        # 列舉存儲桶中的物件
        objects = client.list_blobs(bucket_name)
        for obj in objects:
            object_name = obj.name
            print(f"Bucket: {bucket_name}, Object: {object_name}")

cloud_storage_object_discovery()