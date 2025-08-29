from dotenv import load_dotenv
import os
from api_requests import get_coordinates  # Import the function from the new module

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

def main():
    print("Hello from github-copilot-air-pollution-app!")

# Example usage
if __name__ == "__main__":
    main()
    location = input("Enter a location: ")
    coordinates = get_coordinates(location, API_KEY)
    if coordinates:
        print(f"Coordinates for {location}: {coordinates}")