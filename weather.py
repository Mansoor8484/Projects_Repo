import requests, json # imports a library used for making http request

API_KEY = "3d36d5505d7bb6a70a34234790517ea0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
filename = "weather.json"
city = input("enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}" #constructs a url for the API request. It adds the APIkey and the city name as query parameters to the base url
response = requests.get(requests_url) #sends a get request to the created url and storesd the response in response

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = (data['main']['temp'] -273.5) *2 + 30
    print(f"degrees in Farenheit: {round(temperature)}")
    with open(filename, 'w') as f:
        json.dump(data, f)
else:
    print(f"an error occured {response.status_code}")