import requests

def get_weather(city,units='metric',api_key='ddc102448cf7b70ac2db20664ab6ea9e'):
    url= f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&unit={units}'
    r = requests.get(url)
    content = r.json()
    #with open('data.txt', 'a') as file:
    for dicty in content['list']:
        return (f"{dicty['dt_txt']}, {dicty['main'] ['temp']}, {dicty['weather'][0]['description']}\n") 
    #return content
print(get_weather(city='Phoenix'))