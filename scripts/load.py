import psycopg2
import os
from dotenv import load_dotenv
from extract import get_weather
from transform import transform_weather



load_dotenv()

def load_weather(weather_data):
    """
    load transformed weather data into postgreSQL
    """
    connection = None
    cursor = None 
    
    try:
        connection = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port= os.getenv("DB_PORT")
    )
    
        cursor = connection.cursor()
    
        

        #insert into weather
        cursor.execute(
            
            """
            INSERT INTO weather (
            time,

            latitude,

            longitude,

            temperature_2m,

            relative_humidity_2m,

            is_day,

            precipitation,

            rain,

            showers,

            wind_speed_10m,

            wind_direction_10m,

            wind_gusts_10m

        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """,
        (
        weather_data["time"],

        weather_data["latitude"],

        weather_data["longitude"],

        weather_data["temperature_2m"],

        weather_data["relative_humidity_2m"],

        weather_data["is_day"],

        weather_data["precipitation"],

        weather_data["rain"],

        weather_data["showers"],

        weather_data["wind_speed_10m"],

        weather_data["wind_direction_10m"],

        weather_data["wind_gusts_10m"]    
        )
        
        )
        
        connection.commit()
        
        print("weather loaded successfully!")
        
    
    except Exception as e:
        
        if connection:
              connection.rollback()
        
      
        print(f"error loading weather data: {e}")
        
        
    
    
    
    
    
    finally:
        
        if cursor:
            cursor.close()
            
            
        if connection:
            connection.close()
    
    
if __name__ == "__main__":
    weather = get_weather(-1.2833, 36.8167)
    transformed_weather = transform_weather(weather)
    load_weather(transformed_weather)




