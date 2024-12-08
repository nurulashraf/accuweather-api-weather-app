import requests
import pandas as pd
from datetime import datetime
from IPython.display import display

# Insert your API key here
API_KEY =""

def city_search(api_key, q):
    end_point = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        'apikey': api_key,
        'q': q
    }
    response = requests.get(end_point, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_current_conditions(api_key, location_key):
    end_point = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
    params = {
        'apikey': api_key,
    }
    response = requests.get(end_point, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_daily_forecast(api_key, location_key):
    end_point = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}"
    params = {
        'apikey': api_key,
    }
    response = requests.get(end_point, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    api_key = "rXvw1YLkzEuEMX1X4RbryS1E3yX1O8MT"
    city = input("Enter a city name: ")

    # Search for the city
    city_data = city_search(api_key, city)
    if not city_data:
        print("City not found.")
        return

    # Get the location key of the first result
    location_key = city_data[0]['Key']
    city_name = city_data[0]['LocalizedName']

    # Get current conditions
    current_conditions = get_current_conditions(api_key, location_key)
    if not current_conditions:
        print("Unable to fetch current conditions.")
        return

    # Get daily forecast
    daily_forecast = get_daily_forecast(api_key, location_key)
    if not daily_forecast:
        print("Unable to fetch daily forecast.")
        return

    # Display the information
    print(f"\nWeather information for {city_name}:")
    print(f"Current temperature: {current_conditions[0]['Temperature']['Metric']['Value']}°C")
    print(f"Current conditions: {current_conditions[0]['WeatherText']}")

    print("\nToday's forecast:")
    print(f"Min temperature: {daily_forecast['DailyForecasts'][0]['Temperature']['Minimum']['Value']}°F")
    print(f"Max temperature: {daily_forecast['DailyForecasts'][0]['Temperature']['Maximum']['Value']}°F")
    print(f"Day conditions: {daily_forecast['DailyForecasts'][0]['Day']['IconPhrase']}")
    print(f"Night conditions: {daily_forecast['DailyForecasts'][0]['Night']['IconPhrase']}")

if __name__ == "__main__":
    main()