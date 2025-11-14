import requests
from pymongo import MongoClient
import json
client = MongoClient("localhost", 27017)
db = client["Mydatabase"]
collection = db["mydatabase"]


data = {
    "username": "nishat",
    "email": "nishat@gmail.com",
    "phonenumber": "9876543210",
    "password": "abc123",
}
response = requests.post("http://localhost:8000/data", data)
print(response.json)
