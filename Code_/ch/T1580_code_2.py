from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient

def discover_azure_infrastructure():
    credential = DefaultAzureCredential()
    subscription_id = 'your-subscription-id'
    
    compute_client = ComputeManagementClient(credential, subscription_id)
    storage_client = StorageManagementClient(credential, subscription_id)
    
    # 處理虛擬機器
    vm_list = compute_client.virtual_machines.list_all()
    for vm in vm_list:
        print('Instance ID:', vm.id)
        print('Instance Type:', vm.hardware_profile.vm_size)
        # 其他屬性...
        print('---')
    
    # 處理存儲服務
    storage_accounts = storage_client.storage_accounts.list()
    for account in storage_accounts:
        print('Storage Account Name:', account.name)
        # 其他屬性...
        print('---')

discover_azure_infrastructure()