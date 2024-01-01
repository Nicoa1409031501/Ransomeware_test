import glob

def find_group_policy():
    group_policy_paths = []
    domain_path = "<DOMAIN>\\SYSVOL\\<DOMAIN>\\Policies\\"
    pattern = domain_path + "**/*"

    for file in glob.glob(pattern, recursive=True):
        if len(file.split('\\')) == 8:
            group_policy_paths.append(file)

    return group_policy_paths

# 測試程式碼
group_policy_paths = find_group_policy()
for path in group_policy_paths:
    print(path)