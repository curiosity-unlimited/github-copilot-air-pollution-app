from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    print("Hello from github-copilot-air-pollution-app!")

def get_coordinates(location):
    """
    Fetches the longitude and latitude for a given location using OpenWeather's Geocoding API.

    Args:
        location (str): The name of the location (e.g., city, state, country).

    Returns:
        dict: A dictionary containing 'lat' and 'lon' if successful, or None if an error occurs.
    """
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": location,
        "appid": API_KEY,
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

# Example usage
if __name__ == "__main__":
    main()
    location = input("Enter a location: ")
    coordinates = get_coordinates(location)
    if coordinates:
        print(f"Coordinates for {location}: {coordinates}")
