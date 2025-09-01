from dotenv import load_dotenv
import os
from api_requests import get_coordinates, get_air_pollution  # Import the function from the new module

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    print("Hello from github-copilot-air-pollution-app!")
    location = input("Enter a location: ")
    coordinates = get_coordinates(location, API_KEY)
    if coordinates:
        print(f"Coordinates for {location}: {coordinates}")
        air_pollution_data = get_air_pollution(coordinates["lat"], coordinates["lon"], API_KEY)
        if air_pollution_data:
            print(f"Air pollution data for {location}: {air_pollution_data}")
        else:
            print("Failed to fetch air pollution data.")
    else:
        print("Failed to fetch coordinates.")

# Example usage
if __name__ == "__main__":
    main()