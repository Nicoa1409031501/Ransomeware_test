import os

def data_destruction(file_path):
    with open(file_path, 'w') as f:
        pass
    os.unlink(file_path)