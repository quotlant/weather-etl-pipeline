from extract import get_weather
from transform import transform_weather
from load import load_weather



def main():
    weather = get_weather(-1.2833, 36.8167)
    transformed_weather = transform_weather(weather)
    load_weather(transformed_weather)
    
    

if __name__ == "__main__":
    main()
    