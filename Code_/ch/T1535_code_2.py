from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials

def create_unused_cloud_instance_gcp(project_id, zone, instance_name, machine_type, image_project, image_family):
    credentials = GoogleCredentials.get_application_default()
    compute_service = build('compute', 'v1', credentials=credentials)
    
    config = {
        'name': instance_name,
        'machineType': f"zones/{zone}/machineTypes/{machine_type}",
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImageFamily': image_family,
                    'sourceImageProject': image_project
                }
            }
        ]
    }
    
    result = compute_service.instances().insert(project=project_id, zone=zone, body=config).execute()
    return result