"""Utility functions for the application."""
import os
from typing import Optional, Union, NoReturn, Tuple, Dict, List, Any, cast
from dotenv import load_dotenv

def load_api_key() -> str:
    """
    Load the API key from .env file.
    
    Returns:
        str: The API key for OpenWeatherMap
        
    Raises:
        ValueError: If API_KEY is not found in the .env file
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        raise ValueError("API_KEY not found in .env file")
    
    return api_key

def validate_coordinates(lat: Union[int, float], lon: Union[int, float]) -> bool:
    """
    Validate that latitude and longitude values are within valid ranges.
    
    Args:
        lat: Latitude value to validate (-90 to 90)
        lon: Longitude value to validate (-180 to 180)
    
    Returns:
        bool: True if coordinates are valid
        
    Raises:
        ValueError: If coordinates are outside valid ranges
    """
    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        raise ValueError("Coordinates must be numeric values")
        
    if lat < -90 or lat > 90:
        raise ValueError(f"Latitude {lat} is out of range (-90 to 90)")
        
    if lon < -180 or lon > 180:
        raise ValueError(f"Longitude {lon} is out of range (-180 to 180)")
        
    return True
