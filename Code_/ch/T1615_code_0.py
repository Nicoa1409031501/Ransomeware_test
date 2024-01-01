import os
import re

def find_group_policy():
    group_policy_paths = []
    domain_path = "<DOMAIN>\\SYSVOL\\<DOMAIN>\\Policies\\"

    for root, dirs, files in os.walk(domain_path):
        for file in files:
            if re.match(r"^[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}$", file):
                group_policy_paths.append(os.path.join(root, file))

    return group_policy_paths

# 測試程式碼
group_policy_paths = find_group_policy()
for path in group_policy_paths:
    print(path)