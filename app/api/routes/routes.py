from fastapi import APIRouter, HTTPException
from typing import List
from app.api.models.models import StationCreate, StationResponse, Location
from app.api.methods.methods import create_station, get_stations, get_closest_station

router = APIRouter()

@router.post("/estaciones/", response_model=StationResponse, status_code=201)
async def create_station_endpoint(station: StationCreate):
    """
    Endpoint to create a new station.

    Args:
        station (StationCreate): Station data.

    Returns:
        StationResponse: The created station data.
    """
    new_station = await create_station(station_data=station)
    return new_station

@router.get("/estaciones/", response_model=List[StationResponse])
async def list_stations_endpoint():
    """
    Endpoint to list all stations.

    Returns:
        List[StationResponse]: A list of all stations.
    """
    stations = await get_stations()
    return stations

@router.get("/estaciones/cercana/{station_id}/", response_model=StationResponse)
async def get_closest_station_endpoint(station_id: int):
    """
    Endpoint to get the closest station to the specified station ID.

    Args:
        station_id (int): ID of the reference station.

    Returns:
        StationResponse: The closest station data.
    
    Raises:
        HTTPException: If the reference station is not found or there are no other stations.
    """
    closest_station = await get_closest_station(station_id=station_id)
    if closest_station is None:
        raise HTTPException(status_code=404, detail="Station not found or no nearby stations available.")

    return StationResponse(
        id=closest_station.id,
        name=closest_station.name,
        location=Location(
            latitude=closest_station.latitude,
            longitude=closest_station.longitude
        )
    )
