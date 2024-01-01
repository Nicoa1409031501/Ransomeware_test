import subprocess

def disable_reboot():
    subprocess.run(["powercfg", "/hibernate", "off"])

disable_reboot()