import psutil

def get_process_owners():
    owners = {}
    for proc in psutil.process_iter(['name', 'username']):
        if proc.info['username'] in owners:
            owners[proc.info['username']].append(proc.info['name'])
        else:
            owners[proc.info['username']] = [proc.info['name']]
    return owners