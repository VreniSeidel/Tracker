import requests
import ipaddress

class Geo():
    def __init__(self):

            self.ip = ipaddress.IPv4Address("74.195.1.128")
            self.url = f"https://geolocation-db.com/json/{self.ip}&position=true"
            self.response = []
            self.country_code = None
            self.country_name = None
            self.city = None
            self.postal = None
            self.latitude = None
            self.longtitude = None
            self.ipv4 = None
            self.state = None
            self.information = []
            self.result_type_ip = self.check_public_private()
            if self.__is_online():
                self.__init_information()


    """Init function for data"""
    def __init_information(self):
        self.response = requests.get(self.url).json()
        self.result_type_ip = self.check_public_private()
        self.country_code = self.response['country_code']
        self.country_name = self.response['country_name']
        self.city = self.response['city']
        self.postal = self.response['postal']
        self.latitude = self.response['latitude']
        self.longtitude = self.response['longitude']
        self.ipv4 = self.response['IPv4']
        self.state = self.response['state']
        self.information = [self.country_code, self.country_name, self.city, self.postal, self.latitude, self.longtitude, self.ipv4, self.state]


    """Check if internet"""
    def __is_online(self):
        try:
            requests.get(self.url)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
        return False


    """Check public or private ip address"""
    def check_public_private(self):
        if self.ip.is_private:
            return "Private"
        return "Public"


    """Information about ip address"""
    def information_ip_address(self):
        text = ["Country code", "Country name", "City", "Postal", "Latitude", "Longitude", "IPv4", "State"]

        with open('info.txt', 'w') as f:
            for line in range(len(self.information)):
                f.write(f"{text[line]}: {self.information[line]}")
                f.write(f"\n")