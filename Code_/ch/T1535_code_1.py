from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials

def create_unused_cloud_instance_azure(subscription_id, resource_group, region, vm_name, vm_size, image_uri):
    credentials = ServicePrincipalCredentials(
        client_id='<Azure AD client ID>',
        secret='<Azure AD client secret>',
        tenant='<Azure AD tenant ID>'
    )
    compute_client = ComputeManagementClient(credentials, subscription_id)
    
    params = {
        'location': region,
        'hardware_profile': {
            'vm_size': vm_size
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'Canonical',
                'offer': 'UbuntuServer',
                'sku': '16.04-LTS',
                'version': 'latest'
            }
        },
        'os_profile': {
            'computer_name': vm_name,
            'admin_username': 'adminuser',
            'admin_password': 'adminpassword'
        }
    }
    
    result = compute_client.virtual_machines.create_or_update(resource_group, vm_name, params)
    return result