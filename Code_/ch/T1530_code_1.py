import boto3

def get_data_from_cloud(bucket_name, file_name):
    # 連接到 AWS S3
    s3 = boto3.client('s3')

    # 讀取檔案內容
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = response['Body'].read().decode('utf-8')

    return data