# AccuWeather Weather Information Retriever

## Overview
This Python script allows users to retrieve current weather conditions and daily forecast information for a specified city using the AccuWeather API.

## Features
- City location search
- Current weather conditions retrieval
- Daily forecast information
- Temperature and weather text display
- Supports both Celsius and Fahrenheit measurements

## Prerequisites
- Python 3.7+
- `requests` library
- `pandas` library (optional)
- AccuWeather Developer Account and API Key

## Installation

### Dependencies
Install the required Python libraries:
```bash
pip install requests pandas
```

### AccuWeather API Key
1. Create an account at [AccuWeather Developer Portal](https://developer.accuweather.com/)
2. Generate an API key
3. Replace the `API_KEY` in the script with your personal key

## Usage

### Running the Script
```bash
python weather_script.py
```

1. When prompted, enter the name of the city
2. The script will display:
   - Current temperature
   - Current weather conditions
   - Minimum and maximum temperatures
   - Day and night weather conditions

## Functions
- `city_search()`: Finds the location key for a given city
- `get_current_conditions()`: Retrieves current weather conditions
- `get_daily_forecast()`: Fetches daily weather forecast

## Error Handling
- Checks API response status
- Handles city not found scenarios
- Provides error messages for failed API calls

## Limitations
- Requires active internet connection
- Limited by AccuWeather API request quotas
- Relies on first search result for city matching

## Security Notes
- Keep your API key confidential
- Do not commit API keys to version control
- Consider using environment variables for API key storage

## Potential Improvements
- Add support for multiple-day forecasts
- Implement temperature unit conversion
- Create more robust error handling
- Add caching mechanism for API responses

## Dependencies
- `requests`: HTTP library for API calls
- `pandas`: Data manipulation (optional)

## Contributing
Contributions, bug reports, and feature requests are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
