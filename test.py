import requests
import json

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#print(response)
#print(response.json()['items'])
for data in response.json()['items']:
    print(data['title'])
    print(data['owner']['display_name'])
    print(data['link'])
    print('-------------------------------------')