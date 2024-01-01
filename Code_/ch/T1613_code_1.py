import os
from kubernetes import client, config

def container_discovery():
    # Load kubeconfig file
    config.load_kube_config(os.path.join(os.getenv("HOME"), '.kube', 'config'))
    
    # Create Kubernetes API client
    v1 = client.CoreV1Api()
    
    # List pods in all namespaces
    pods = v1.list_pod_for_all_namespaces().items
    
    # Print pod information
    for pod in pods:
        print("Pod Name: ", pod.metadata.name)
        print("Pod Namespace: ", pod.metadata.namespace)
        print("Pod Status: ", pod.status.phase)
        print("-----------------------------------")

container_discovery()