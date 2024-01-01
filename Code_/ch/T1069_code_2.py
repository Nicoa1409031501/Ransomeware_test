import cloud

def cloud_group_discovery():
    # 透過 cloud 模組存取雲端的API，進行組和權限設定查詢
    groups = cloud.get_groups()
    permissions = cloud.get_permissions()

    for group in groups:
        print(f"Group: {group}")

    for user, permission in permissions:
        print(f"User: {user}, Permission: {permission}")

cloud_group_discovery()