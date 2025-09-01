def validate_coordinates(lat, lon):
    """
    Validates that the latitude and longitude are within reasonable ranges.

    Args:
        lat (float): Latitude value to validate (-90 to 90).
        lon (float): Longitude value to validate (-180 to 180).

    Returns:
        bool: True if both latitude and longitude are valid, False otherwise.
    """
    if -90 <= lat <= 90 and -180 <= lon <= 180:
        return True
    return False
