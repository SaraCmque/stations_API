import pytest
import os
import requests

# Define global constants for base URL and specific endpoints
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/estaciones/")
ENDPOINT_POST_URL = f"{BASE_URL}estaciones/"
ENDPOINT_CLOSEST_URL_TEMPLATE = f"{BASE_URL}estaciones/cercana/{{station_id}}/"

@pytest.fixture
def sample_station_data():
    """
    Fixture to provide a sample station data dictionary.
    """
    return {
        "name": "Test Station",
        "location": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    }

@pytest.mark.asyncio
async def test_create_station(sample_station_data):
    """
    Test the `/estaciones/` POST endpoint to ensure that a new station can be created successfully.
    """
    response = requests.post(ENDPOINT_POST_URL, json=sample_station_data)
    
    # Check if response status code is 201 (Created)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    # Verify the response data contains the correct fields and values
    station = response.json()
    assert station["name"] == sample_station_data["name"], "Station name does not match"
    assert "id" in station, "Station ID not found in response"
    assert "location" in station, "Location data missing in response"
    assert station["location"]["latitude"] == sample_station_data["location"]["latitude"], "Latitude mismatch"
    assert station["location"]["longitude"] == sample_station_data["location"]["longitude"], "Longitude mismatch"

@pytest.mark.asyncio
async def test_list_stations():
    """
    Test the `/estaciones/` GET endpoint to verify retrieval of all stations.
    """
    response = requests.get(ENDPOINT_POST_URL)
    
    # Check if response status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Ensure the response is a list and each station has required fields
    stations = response.json()
    assert isinstance(stations, list), "Expected list of stations"
    for station in stations:
        assert "id" in station, "Station ID missing in list"
        assert "name" in station, "Station name missing in list"
        assert "location" in station, "Location data missing in list"
        assert "latitude" in station["location"], "Latitude missing in location data"
        assert "longitude" in station["location"], "Longitude missing in location data"

@pytest.mark.asyncio
async def test_get_closest_station():
    """
    Test the `/estaciones/cercana/{station_id}/` GET endpoint to verify retrieval of the closest station.
    """
    station_data = [
        {"name": "Station A", "location": {"latitude": 40.7128, "longitude": -74.0060}},
        {"name": "Station B", "location": {"latitude": 40.73061, "longitude": -73.935242}}
    ]
    
    # Create two stations to ensure data is available for testing
    for station in station_data:
        response = requests.post(ENDPOINT_POST_URL, json=station)
        assert response.status_code == 201, f"Failed to create station {station['name']}"
    
    # Retrieve the closest station to the station with ID 1
    response = requests.get(ENDPOINT_CLOSEST_URL_TEMPLATE.format(station_id=1))
    
    # Check if response status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Validate that the closest station response includes expected fields
    closest_station = response.json()
    assert "id" in closest_station, "ID missing in closest station response"
    assert "name" in closest_station, "Name missing in closest station response"
    assert "location" in closest_station, "Location missing in closest station response"
    assert "latitude" in closest_station["location"], "Latitude missing in location data of closest station"
    assert "longitude" in closest_station["location"], "Longitude missing in location data of closest station"
