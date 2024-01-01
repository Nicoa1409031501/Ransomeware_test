import os

# 插入數據
with open('data.txt', 'a') as file:
    file.write('New Data\n')

# 刪除數據
with open('data.txt', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if line.strip() != 'Data to delete':
            file.write(line)
    file.truncate()

# 操作數據
with open('data.txt', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if line.strip() == 'Data to modify':
            file.write('Modified data\n')
        else:
            file.write(line)
    file.truncate()