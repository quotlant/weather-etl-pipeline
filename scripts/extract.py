import requests









def get_weather():
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":-1.2833,
        "longitude":36.8167,
        "current": "temperature_2m",
        
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    return data
    
if __name__ == "__main__":
        weather = get_weather()
        print(weather)
       