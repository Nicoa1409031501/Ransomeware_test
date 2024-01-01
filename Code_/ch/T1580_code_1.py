from google.cloud import compute_v1, storage

def discover_gcp_infrastructure():
    compute_client = compute_v1.InstancesClient()
    storage_client = storage.Client()

    # 處理虛擬機器
    zones = compute_client.aggregated_list_instances(project='your-project-id')
    for zone in zones:
        for instance in zones[zone].items:
            print('Instance Name:', instance.name)
            print('Instance Type:', instance.machine_type)
            # 其他屬性...
            print('---')

    # 處理存儲服務
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        print('Bucket Name:', bucket.name)
        # 其他屬性...
        print('---')

discover_gcp_infrastructure()