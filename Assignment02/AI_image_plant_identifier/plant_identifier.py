import json
import requests


class Plant_identifier:
    def __init__(self, PlantNet_API_KEY, imgPath):
        self.url = "https://my-api.plantnet.org/v2/identify/all"
        self.payload = {
            "api-key": PlantNet_API_KEY
        }

        self.headers = {}
        self.file = imgPath
        self.files = {
            'images': open(f'{self.file}','rb')
        }
        self.response = requests.post(self.url, params=self.payload, headers=self.headers, files=self.files)

    def get_responseCode(self):
        return self.response.status_code

    def get_plantName(self):
        return self.response.json()['results'][0]['species']['commonNames'][0]
    