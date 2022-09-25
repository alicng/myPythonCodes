import requests
r=requests.get('https://www.boredapi.com/api/activity')
content = r.json()
print(content)
