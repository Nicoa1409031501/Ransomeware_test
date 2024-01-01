import subprocess

def abuse_elevation_control1():
    subprocess.call(['sudo', 'command_to_execute'])

abuse_elevation_control1()