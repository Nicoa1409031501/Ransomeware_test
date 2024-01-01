from azure.identity import DefaultAzureCredential
from azure.mgmt.intune import IntuneResourceManagementClient
from azure.mgmt.intune.models import BuiltinRoleIdentifier, GroupAssignment

def exec_command_intune(cmd, device_id):
    credential = DefaultAzureCredential()
    intune_client = IntuneResourceManagementClient(credential)
    
    role_assignment = intune_client.role_assignments.create(
        builtin_role_identifier=BuiltinRoleIdentifier.SERVICE_CONFIGURATION_OPERATOR,
        scope=device_id,
    )
    
    group_assignment = GroupAssignment(
        role_assignment_id=role_assignment.id,
        source_type="microsoft.graph.device",
        assignment_target=device_id
    )
    
    intune_client.group_assignments.create(group_assignment)
    
    result = intune_client.script.run(
        group_assignment_id=group_assignment.id,
        script_contents=cmd,
        frequency="once",
        started_by=UserPrincipalName(),
    )
    
    return result.id