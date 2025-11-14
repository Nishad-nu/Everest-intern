import requests
import json
from collections import Counter
url = "https://dummy-json.mock.beeceptor.com/users"
responce = requests.get (url)
data = responce.json()
with open("data.json","w") as f:
    json.dump(data,f)
print("json.data saved to data.json")

print(type(data))
#method - 1
country_count = {}
for i in data:
    country = i.get("country")
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1
print(country_count)

#method - 2
country_list = [ i.get("country") for i in data if i.get("country")]
country_count = Counter(country_list)
print(dict(country_count))
