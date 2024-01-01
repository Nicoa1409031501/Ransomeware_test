import os
import yaml

def detect_exploitable_vulnerabilities(directory):
    vulnerabilities = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.yaml'):
                with open(file_path, 'r') as f:
                    try:
                        data = yaml.safe_load(f)
                        if 'vulnerabilities' in data:
                            vulnerabilities.extend(data['vulnerabilities'])
                    except yaml.YAMLError as e:
                        print(f"Error parsing {file_path}: {str(e)}")
    
    return vulnerabilities

# 指定需要檢測漏洞的目錄
directory = '/path/to/client_applications'

# 執行檢測並列出潛在的可利用漏洞
exploitable_vulnerabilities = detect_exploitable_vulnerabilities(directory)
for vulnerability in exploitable_vulnerabilities:
    print(vulnerability)