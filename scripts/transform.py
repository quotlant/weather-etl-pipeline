from extract import get_weather



def transform_weather(weather_data):
    """
    Transforms the weather data into a more readable format.
    """
    current = weather_data["current"]
    
    transformed_data = {
        
       "time": current["time"],
       "latitude": weather_data["latitude"],
       "longitude":weather_data["longitude"],
       "temperature_2m": current["temperature_2m"],
       "relative_humidity_2m": current["relative_humidity_2m"],
       "is_day": current["is_day"],
       "precipitation": current["precipitation"],
       "rain": current["rain"],
       "showers": current["showers"],
       "wind_speed_10m": current["wind_speed_10m"],
       "wind_direction_10m": current["wind_direction_10m"],
       "wind_gusts_10m": current["wind_gusts_10m"],
       
       
       
       
        }
    
    return transformed_data



if __name__ == "__main__":
    weather = get_weather(-1.2833, 36.8167)
    transformed = transform_weather(weather)
    print(transformed)