import requests

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
            return {"lat": data[0]["lat"], "lon": data[0]["lon"]}
        else:
            print(f"No results found for location: {location}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None
