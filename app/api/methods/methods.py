from sqlalchemy.orm import Session
from app.api.models.sqlalchemy_models import Station
from app.api.models.models import StationCreate, StationResponse, Location
from sqlalchemy import func
from typing import List

def create_station(db: Session, station_data: StationCreate) -> StationResponse:
    """
    Creates a new station in the database.

    Args:
        db (Session): Database session.
        station_data (StationCreate): Data of the station to create.

    Returns:
        Station: The created station object.
    """
    new_station = Station(
        name=station_data.name,
        latitude=station_data.location.latitude,
        longitude=station_data.location.longitude
    )
    db.add(new_station)
    db.commit()
    db.refresh(new_station)

    return StationResponse(
        id=new_station.id,
        name=new_station.name,
        location=Location(latitude=new_station.latitude, longitude=new_station.longitude)
    )

def get_stations(db: Session) -> List[StationResponse]:
    """
    Retrieves all stations from the database.

    Args:
        db (Session): Database session.

    Returns:
        List[Station]: A list of station objects.
    """
    stations = db.query(Station).all()
    return [
        StationResponse(
            id=station.id,
            name=station.name,
            location=Location(latitude=station.latitude, longitude=station.longitude)
        )
        for station in stations
    ]

def get_station_by_id(db: Session, station_id: int):
    """
    Retrieves a station by its ID.

    Args:
        db (Session): Database session.
        station_id (int): ID of the station to retrieve.

    Returns:
        Station or None: The station object if found, else None.
    """
    return db.query(Station).filter(Station.id == station_id).first()

def get_closest_station(db: Session, station_id: int):
    """
    Finds the closest station to a given station ID.

    Args:
        db (Session): Database session.
        station_id (int): ID of the reference station.

    Returns:
        Station or None: The closest station object, or None if the reference station doesn't exist.
    """
    base_station = get_station_by_id(db, station_id)
    if not base_station:
        return None

    closest = db.query(
        Station,
        (func.pow(Station.latitude - base_station.latitude, 2) +
         func.pow(Station.longitude - base_station.longitude, 2)).label("distance")
    ).filter(Station.id != station_id).order_by("distance").first()

    return closest[0] if closest else None  # closest is a tuple (Station, distance)
