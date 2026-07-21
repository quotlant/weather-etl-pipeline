import requests



def get_weather(latitude, longitude):
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude":longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "rain", "showers", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        
    }
    
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
    return data

#this     
if __name__ == "__main__":
    weather = get_weather(latitude, longitude)
    print(weather)
       