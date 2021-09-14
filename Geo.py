import requests
import ipaddress

class Geo():
    def __init__(self):

        try:

            self.ip = ipaddress.IPv4Address("74.195.1.128")
            self.response = requests.get(f"https://geolocation-db.com/json/{self.ip}&position=true").json()
            self.result_type_ip = self.check_public_private()

        except(ConnectionError):
            print("Check your internet connection")


    """Check public or private ip address"""
    def check_public_private(self):
        if self.ip.is_private:
            return "Private"
        return "Public"


    """{
        'country_code': 'Not found', 
        'country_name': 'Not found', 
        'city': 'Not found', 
        'postal': 'Not found', 
        'latitude': 'Not found', 
        'longitude': 'Not found', 
        'IPv4': 'Not found', 
        'state': 'Not found'
    }"""
    """Information about ip address"""
    def information_ip(self):
        print(f"Country code: {self.response['country_code']}")
        print(f"Country name: {self.response['country_name']}")
        print(f"City: {self.response['city']}")
        print(f"Postal: {self.response['postal']}")
        print(f"Latitude: {self.response['latitude']}")
        print(f"Longitude: {self.response['longitude']}")
        print(f"IPv4: {self.response['IPv4']}")
        print(f"State: {self.response['state']}")
