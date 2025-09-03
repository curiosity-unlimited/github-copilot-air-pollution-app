"""API request functions for OpenWeatherMap."""
import requests
from utils import load_api_key, validate_coordinates

def get_geocoding_data(location):
    """
    Get geocoding data for a location using OpenWeatherMap's Geocoding API.
    
    Args:
        location (str): The location to search for (city name, state, country)
    
    Returns:
        dict: The first geocoding result containing latitude and longitude
        None: If no results found or an error occurs
    """
    api_key = load_api_key()
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    
    params = {
        "q": location,
        "limit": 1,  # Get only the first result
        "appid": api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        
        if data and len(data) > 0:
            lat = data[0].get("lat")
            lon = data[0].get("lon")
            
            # Validate coordinates from the API response
            validate_coordinates(lat, lon)
            
            return {
                "name": data[0].get("name", "Unknown"),
                "country": data[0].get("country", "Unknown"),
                "lat": lat,
                "lon": lon,
                "state": data[0].get("state", "")
            }
        return None
    
    except ValueError as e:
        # Handle coordinate validation errors
        print(f"Coordinate validation error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geocoding data: {e}")
        return None

def get_air_pollution_data(lat, lon):
    """
    Get air pollution data for a location using OpenWeatherMap's Air Pollution API.
    
    Args:
        lat (float): Latitude of the location
        lon (float): Longitude of the location
    
    Returns:
        dict: Air pollution data including AQI and components
        None: If an error occurs
    """
    try:
        # Validate coordinates before making the API request
        validate_coordinates(lat, lon)
        
        api_key = load_api_key()
        base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
        
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data and "list" in data and len(data["list"]) > 0:
            air_data = data["list"][0]
            return {
                "aqi": air_data.get("main", {}).get("aqi"),
                "components": air_data.get("components", {})
            }
        return None
    
    except ValueError as e:
        # Handle coordinate validation errors
        print(f"Coordinate validation error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching air pollution data: {e}")
        return None
