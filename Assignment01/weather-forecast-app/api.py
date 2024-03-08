import requests
import json

class Weather_api:
    URL = "https://goweather.herokuapp.com/weather/"
    def __init__(self, city):
        self.url = self.URL + city
        self.payload = {}
        self.headers = {}
        self.response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        self.data = json.loads(self.response.text)
        
        
    def get_fullData(self):
        return self.data
    
    def get_weather(self):
        self.data['description'] = (''.join(self.data['description'].split(' '))).lower()
        return {'temp': self.data['temperature'], 'wind': self.data['wind'], 'desc': self.data['description']}
    
    def get_day1forecast(self):
        return self.data['forecast'][0]
    
    def get_day2forecast(self):
        return self.data['forecast'][1]
    
    def get_day3forecast(self):
        return self.data['forecast'][2]
    