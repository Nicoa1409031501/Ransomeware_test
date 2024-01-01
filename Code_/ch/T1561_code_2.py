import subprocess

def disk_wipe(device_path):
    subprocess.run(["dd", "if=/dev/zero", "of=" + device_path, "bs=1M"])