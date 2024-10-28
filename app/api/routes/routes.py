from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.models.models import StationCreate, StationResponse
from app.api.methods.methods import create_station, get_stations, get_closest_station
from app.api.config.database import get_db

router = APIRouter()

@router.post("/estaciones/", response_model=StationResponse, status_code=201)
def create_station_endpoint(station: StationCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new station.

    Args:
        station (StationCreate): Station data.
        db (Session, optional): Database session dependency.

    Returns:
        StationResponse: The created station data.
    """
    new_station = create_station(db=db, station_data=station)
    return new_station

@router.get("/estaciones/", response_model=List[StationResponse])
def list_stations_endpoint(db: Session = Depends(get_db)):
    """
    Endpoint to list all stations.

    Args:
        db (Session, optional): Database session dependency.

    Returns:
        List[StationResponse]: A list of all stations.
    """
    stations = get_stations(db=db)
    return stations

@router.get("/estaciones/cercana/{station_id}/", response_model=StationResponse)
def get_closest_station_endpoint(station_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to get the closest station to the specified station ID.

    Args:
        station_id (int): ID of the reference station.
        db (Session, optional): Database session dependency.

    Returns:
        StationResponse: The closest station data.
    
    Raises:
        HTTPException: If the reference station is not found or there are no other stations.
    """
    closest_station = get_closest_station(db=db, station_id=station_id)
    if closest_station is None:
        raise HTTPException(status_code=404, detail="Station not found or no nearby stations available.")
    return closest_station
