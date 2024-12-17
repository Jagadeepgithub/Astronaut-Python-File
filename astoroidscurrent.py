import requests
responce=requests.get("http://api.open-notify.org/astros.json")
json=responce.json()
print("People in space currentle are:")
for person in json['people']:
    print(person['name'])