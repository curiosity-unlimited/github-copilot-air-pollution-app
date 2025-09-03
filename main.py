from api_requests import get_geocoding_data, get_air_pollution_data

def display_air_quality_info(aqi):
    """Display air quality information based on AQI value."""
    aqi_descriptions = {
        1: "Good - Air quality is satisfactory, and air pollution poses little or no risk.",
        2: "Fair - Air quality is acceptable. However, there may be a risk for some people.",
        3: "Moderate - Members of sensitive groups may experience health effects.",
        4: "Poor - Everyone may begin to experience health effects.",
        5: "Very Poor - Health warnings of emergency conditions. The entire population is likely to be affected."
    }
    
    return aqi_descriptions.get(aqi, "Unknown AQI level")

def format_components(components):
    """Format air pollution components for display."""
    component_names = {
        "co": "Carbon Monoxide (CO)",
        "no": "Nitrogen Monoxide (NO)",
        "no2": "Nitrogen Dioxide (NO2)",
        "o3": "Ozone (O3)",
        "so2": "Sulphur Dioxide (SO2)",
        "pm2_5": "Fine Particles (PM2.5)",
        "pm10": "Coarse Particles (PM10)",
        "nh3": "Ammonia (NH3)"
    }
    
    formatted = []
    for code, value in components.items():
        name = component_names.get(code, code)
        formatted.append(f"{name}: {value} μg/m³")
    
    return "\n".join(formatted)

def main():
    print("=== Air Pollution Data Viewer ===")
    print("Enter a location to get current air pollution data.")
    print("(Example: London, UK or New York, NY, US)")
    
    while True:
        location = input("\nEnter location (or 'exit' to quit): ")
        
        if location.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get geocoding data (lat/lon) for the location
        geo_data = get_geocoding_data(location)
        
        if not geo_data:
            print("Location not found. Please try again with a different location.")
            continue
        
        location_name = f"{geo_data['name']}"
        if geo_data.get('state'):
            location_name += f", {geo_data['state']}"
        location_name += f", {geo_data['country']}"
        
        print(f"\nFetching air pollution data for {location_name}...")
        
        # Get air pollution data using the latitude and longitude
        pollution_data = get_air_pollution_data(geo_data['lat'], geo_data['lon'])
        
        if not pollution_data:
            print("Failed to retrieve air pollution data. Please try again.")
            continue
        
        # Display the results
        aqi = pollution_data['aqi']
        components = pollution_data['components']
        
        print("\n=== Air Pollution Report ===")
        print(f"Location: {location_name}")
        print(f"Coordinates: Lat {geo_data['lat']}, Lon {geo_data['lon']}")
        print(f"Air Quality Index (AQI): {aqi}")
        print(display_air_quality_info(aqi))
        print("\nDetailed Components:")
        print(format_components(components))
        print("=" * 30)


if __name__ == "__main__":
    main()
