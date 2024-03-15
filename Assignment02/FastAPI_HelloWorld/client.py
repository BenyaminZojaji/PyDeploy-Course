from requests import get

response = get("http://127.0.0.1:8000/test")

print(response.text)
