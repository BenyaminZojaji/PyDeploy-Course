import requests

url = "https://fruityvice.com/api/fruit/banana"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
