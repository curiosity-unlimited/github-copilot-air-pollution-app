"""Utility functions for the application."""
import os
from dotenv import load_dotenv

def load_api_key():
    """
    Load the API key from .env file.
    
    Returns:
        str: The API key for OpenWeatherMap
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        raise ValueError("API_KEY not found in .env file")
    
    return api_key
