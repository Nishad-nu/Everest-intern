import requests
import json
url = "https://dummy-json.mock.beeceptor.com/users"
responce = requests.get (url)
data = responce.json()
with open("data.json","w") as f:
    json.dump(data,f)
print("json.data saved to data.json")

