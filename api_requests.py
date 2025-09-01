import requests
from utils import validate_coordinates

def get_coordinates(location, api_key):
    """
    Fetches the longitude and latitude for a given location using OpenWeather's Geocoding API.

    Args:
        location (str): The name of the location (e.g., city, state, country).
        api_key (str): The API key for OpenWeather.

    Returns:
        dict: A dictionary containing 'lat' and 'lon' if successful, or None if an error occurs.
    """
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": location,
        "appid": api_key,
        "limit": 1
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            lat, lon = data[0]["lat"], data[0]["lon"]
            if validate_coordinates(lat, lon):
                return {"lat": lat, "lon": lon}
            else:
                print(f"Invalid coordinates received for location: {location}")
                return None
        else:
            print(f"No results found for location: {location}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None

def get_air_pollution(lat, lon, api_key):
    """
    Fetches air pollution data for a given latitude and longitude using OpenWeather's Air Pollution API.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        api_key (str): The API key for OpenWeather.

    Returns:
        dict: A dictionary containing air pollution data if successful, or None if an error occurs.
    """
    base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching air pollution data: {e}")
        return None
