import requests

response = requests.get("http://httpbin.org")

print(response.text)
