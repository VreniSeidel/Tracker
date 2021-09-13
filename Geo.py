import requests
import ipaddress

class Geo():
    def __init__(self):
        self.ip = ipaddress.IPv4Address("192.168.1.1")
        self.response = requests.get(f"https://geolocation-db.com/json/{self.ip}&position=true").json()


    """Check public or private ip address"""
    def check_public_private(self):
        if self.ip.is_private:
            print("Private")
        else:
            print("Public")


    """Information about ip address"""
    def information_ip(self):
        print(self.response)
