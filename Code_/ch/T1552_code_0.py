import os

def search_files(path, keyword):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword in file:
                results.append(os.path.join(root, file))
    return results

# 使用方式：
results = search_files('/', 'password')
print(results)