import boto3

def establish_cloud_account(access_key, secret_key):
    # 建立雲服務提供商的帳號
    client = boto3.client(
        'iam',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    # 創建雲服務提供商帳號後，進一步建立帳號的資料和執行相關操作
    # ...

# 使用範例
establish_cloud_account("example_access_key", "example_secret_key")