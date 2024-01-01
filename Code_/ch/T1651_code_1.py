from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

def exec_command_azure(cmd, vm_resource_id):
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential)
    compute_client = ComputeManagementClient(credential)
    
    vm_instance = compute_client.virtual_machines.get(vm_resource_id)
    
    extension = {
        "commandToExecute": cmd
    }
    
    compute_client.virtual_machine_extensions.begin_create_or_update(
        vm_resource_id,
        'RunCommandExtension',
        {
            "location": vm_instance.location,
            "publisher": "Microsoft.Azure.Extensions",
            "type": "RunCommand",
            "typeHandlerVersion": "2.0",
            "autoUpgradeMinorVersion": True,
            "settings": extension,
            "protectedSettings": {},
        }
    ).result()