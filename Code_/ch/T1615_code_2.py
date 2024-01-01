import shutil

def find_group_policy():
    group_policy_paths = []
    domain_path = "<DOMAIN>\\SYSVOL\\<DOMAIN>\\Policies\\"
    
    for root, dirs, files in os.walk(domain_path):
        for dir in dirs:
            if len(dir.split('\\')) == 8:
                group_policy_paths.append(os.path.join(root, dir))

    return group_policy_paths

# 測試程式碼
group_policy_paths = find_group_policy()
for path in group_policy_paths:
    print(path)