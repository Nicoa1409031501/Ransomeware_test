import boto3

def cloud_storage_object_discovery():
    s3 = boto3.client('s3')
    response = s3.list_buckets()  # 列舉存儲桶
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        # 列舉存儲桶中的物件
        objects = s3.list_objects(Bucket=bucket_name)
        for obj in objects['Contents']:
            object_name = obj['Key']
            print(f"Bucket: {bucket_name}, Object: {object_name}")

cloud_storage_object_discovery()