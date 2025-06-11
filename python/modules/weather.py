import requests

#the api key and the city i want to fetch data from
api_key = "864cdca0d337e674cbf8b87d4540f8c1"
city = "Nairobi"

# This is the url for API weather fetching
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"

weather = requests.get(url)

print(weather.json())